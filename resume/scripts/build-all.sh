#!/usr/bin/env bash
# Build every CV in latex/ into pdf/ and run basic quality checks.
#
# Usage:
#   scripts/build-all.sh                 # build all CVs
#   scripts/build-all.sh data-engineer   # build selected CVs (name without .tex)
#   ENGINE=docker scripts/build-all.sh   # force a specific engine
#
# Engine selection (first available wins, or set ENGINE=...):
#   latexmk   -> latexmk -xelatex          (TeX Live / MacTeX)
#   xelatex   -> xelatex, run twice
#   tectonic  -> tectonic -X compile       (brew install tectonic)
#   docker    -> texlive/texlive image with latexmk -xelatex
#
# Checks after each build (need poppler: brew install poppler):
#   - page count (warns when > 3 pages or the last page is under 30% full)
#   - text extraction via pdftotext (ATS readability)
#   - no ligature glyphs / replacement characters in extracted text
#   - name, e-mail and every employer present in extracted text

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/latex"
OUT="$ROOT/pdf"
BUILD="$ROOT/.build"
DOCKER_IMAGE="${DOCKER_IMAGE:-texlive/texlive:latest}"
# Output file name: <PDF_PREFIX>_<pdf-name>.pdf, where pdf-name comes from the
# "% pdf-name: Data_Engineer" line at the top of each .tex file.
PDF_PREFIX="${PDF_PREFIX:-Nguyen_Gia_Huy}"

mkdir -p "$OUT" "$BUILD"

pick_engine() {
  if [[ -n "${ENGINE:-}" ]]; then echo "$ENGINE"; return; fi
  if command -v latexmk  >/dev/null 2>&1 && command -v xelatex >/dev/null 2>&1; then echo latexmk; return; fi
  if command -v xelatex  >/dev/null 2>&1; then echo xelatex; return; fi
  if command -v tectonic >/dev/null 2>&1; then echo tectonic; return; fi
  if command -v docker   >/dev/null 2>&1; then echo docker; return; fi
  echo "ERROR: no LaTeX engine found. Install tectonic (brew install tectonic)," \
       "TeX Live/MacTeX, or Docker." >&2
  exit 1
}

ENGINE="$(pick_engine)"
echo "Engine: $ENGINE"

pdf_path() {
  local label
  label="$(sed -n 's/^% *pdf-name: *//p' "$SRC/$1.tex" | head -n 1)"
  echo "$OUT/${PDF_PREFIX}_${label:-$1}.pdf"
}

compile() {
  local name="$1" dest
  dest="$(pdf_path "$name")"
  # Sources use \input{../templates/...}, so compile from inside latex/.
  case "$ENGINE" in
    latexmk)
      (cd "$SRC" && latexmk -xelatex -interaction=nonstopmode -halt-on-error \
         -outdir="$BUILD" "$name.tex" >"$BUILD/$name.build.log" 2>&1)
      cp "$BUILD/$name.pdf" "$dest" ;;
    xelatex)
      (cd "$SRC" && for _ in 1 2; do
         xelatex -interaction=nonstopmode -halt-on-error -output-directory="$BUILD" \
           "$name.tex" >"$BUILD/$name.build.log" 2>&1
       done)
      cp "$BUILD/$name.pdf" "$dest" ;;
    tectonic)
      (cd "$SRC" && tectonic -X compile --keep-logs --outdir "$BUILD" "$name.tex" \
         >"$BUILD/$name.build.log" 2>&1)
      cp "$BUILD/$name.pdf" "$dest" ;;
    docker)
      docker run --rm -v "$ROOT":/resume -w /resume/latex "$DOCKER_IMAGE" \
        latexmk -xelatex -interaction=nonstopmode -halt-on-error \
        -outdir=/resume/.build "$name.tex" >"$BUILD/$name.build.log" 2>&1
      cp "$BUILD/$name.pdf" "$dest" ;;
    *)
      echo "Unknown ENGINE=$ENGINE" >&2; exit 1 ;;
  esac
}

check() {
  local name="$1" pdf problems=()
  pdf="$(pdf_path "$name")"
  command -v pdftotext >/dev/null 2>&1 || { echo "  (skip checks: pdftotext not installed)"; return 0; }

  local pages text
  pages="$(pdfinfo "$pdf" | awk '/^Pages:/ {print $2}')"
  text="$(pdftotext -layout "$pdf" -)"

  # Multi-page CVs: at most 3 pages, and the last page must not be nearly empty.
  [[ "$pages" -gt 3 ]] && problems+=("$pages pages (max: 3)")
  if [[ "$pages" -gt 1 ]]; then
    local first last
    first="$(pdftotext -f 1 -l 1 -layout "$pdf" - | grep -c '[^[:space:]]')"
    last="$(pdftotext -f "$pages" -l "$pages" -layout "$pdf" - | grep -c '[^[:space:]]')"
    (( last * 100 < first * 30 )) && problems+=("last page only ${last}/${first} lines filled")
  fi
  grep -qE $'ﬀ|ﬁ|ﬂ|ﬃ|ﬄ|�' <<<"$text" \
    && problems+=("ligature/replacement glyphs in extracted text")
  for must in "NGUYEN GIA HUY" "johnnynguyen882@gmail.com" "Galaxy FinX" "Vietlink" "VNPAY" "EsolLabs" "HCMUS"; do
    grep -qF "$must" <<<"$text" || problems+=("missing text: $must")
  done
  if grep -qiE 'overfull \\hbox' "$BUILD/$name.log" 2>/dev/null; then
    problems+=("overfull hbox (see .build/$name.log)")
  fi

  if ((${#problems[@]})); then
    printf '  WARN  %-22s %s\n' "$name" "$(IFS='; '; echo "${problems[*]}")"
    return 1
  fi
  printf '  OK    %-22s %s page, %s words -> pdf/%s\n' "$name" "$pages" "$(wc -w <<<"$text" | tr -d ' ')" "$(basename "$pdf")"
}

if (($#)); then targets=("$@"); else
  targets=()
  for f in "$SRC"/*.tex; do targets+=("$(basename "$f" .tex)"); done
fi

failed=0; warned=0
for name in "${targets[@]}"; do
  printf 'Building %s ... ' "$name"
  if compile "$name"; then
    echo "done"
    check "$name" || warned=$((warned + 1))
  else
    echo "FAILED (log: .build/$name.build.log)"
    tail -n 20 "$BUILD/$name.build.log" || true
    failed=$((failed + 1))
  fi
done

echo
echo "Built: $(( ${#targets[@]} - failed ))/${#targets[@]}   failed: $failed   with warnings: $warned"
((failed == 0))
