"""Cross-CV differentiation metrics.
Usage: python3 scripts/check-differentiation.py latex [--json out.json]
A Work Experience bullet in CV A counts as 'shared' with CV B when its most similar
bullet in B has a word-sequence similarity >= THRESH (difflib ratio, stopwords removed).
Differentiation(A vs B) = 1 - shared/total bullets of A.
"""
import re, sys, glob, os, json, itertools, difflib
THRESH = 0.6
STOP = set("a an the and or of for to in on with by from at as into its it that this across via while".split())
def bullets(path):
    s = open(path).read()
    s = re.sub(r"(?<!\\)%.*", "", s)  # drop LaTeX comments (fact tags)
    s = re.split(r"\\cvsection\{(?:Selected Projects|Key Project|Projects)\}", s)[0]
    s = s.split(r"\cvsection{Work Experience}")[-1]
    items = re.findall(r"\\item\s+(.*?)(?=\\item|\\end\{itemize\})", s, re.S)
    out = []
    for it in items:
        t = re.sub(r"\\textbf\{|\\mbox\{|\\emph\{|[{}]|\\%|~", " ", it)
        t = re.sub(r"\\[a-zA-Z]+", " ", t)
        w = [x for x in re.findall(r"[a-z0-9+.%/-]+", t.lower()) if x not in STOP]
        out.append(w)
    return out
def sim(a, b): return difflib.SequenceMatcher(None, a, b).ratio()
d = sys.argv[1]
cvs = {os.path.basename(p)[:-4]: bullets(p) for p in sorted(glob.glob(d + "/*.tex"))}
names = list(cvs)
mat = {}
for a, b in itertools.permutations(names, 2):
    A, B = cvs[a], cvs[b]
    shared = sum(1 for x in A if max(sim(x, y) for y in B) >= THRESH)
    mat[(a, b)] = 1 - shared / len(A)
w = max(len(n) for n in names)
print("bullets per CV:", {n: len(v) for n, v in cvs.items()})
print(" " * w, " ".join(n[:6].rjust(6) for n in names))
for a in names:
    print(a.ljust(w), " ".join(("  --  " if a == b else f"{mat[(a,b)]*100:5.0f}%") for b in names))
pairs = [(a, b, (mat[(a,b)] + mat[(b,a)]) / 2) for a, b in itertools.combinations(names, 2)]
vals = [p[2] for p in pairs]
print(f"\npairwise differentiation: min {min(vals)*100:.0f}%  mean {sum(vals)/len(vals)*100:.0f}%  max {max(vals)*100:.0f}%")
print("lowest pairs:", [(a, b, round(v*100)) for a, b, v in sorted(pairs, key=lambda p: p[2])[:5]])
if "--json" in sys.argv:
    json.dump({"names": names, "pairs": [[a, b, v] for a, b, v in pairs],
               "bullets": {n: len(v) for n, v in cvs.items()}}, open(sys.argv[sys.argv.index("--json")+1], "w"))
