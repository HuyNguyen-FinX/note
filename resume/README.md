# Resume Variants: Nguyen Gia Huy

10 CV được định vị theo 10 hướng nghề nghiệp khác nhau. Mỗi bản có functional job title, Work Experience và Technical Skills riêng. Tất cả viết bằng LaTeX, dùng chung một template, xuất ra PDF A4 1 trang, ATS-friendly.

## Cấu trúc

```text
resume/
├── original/                      # CV gốc (main.tex) + PDF để đối chiếu
├── analysis/
│   ├── profile-analysis.md        # phân tích kinh nghiệm và bằng chứng
│   ├── role-matching.md           # mức độ phù hợp với từng vị trí, kỹ năng còn thiếu
│   ├── cv-differentiation-report.md  # audit v1, chỉ số khác biệt v2, title, đánh giá hiring manager
│   └── review-needed.md           # chi tiết kỹ thuật cần bạn xác minh
├── templates/resume-template.tex  # layout, font, thông tin cá nhân, timeline, học vấn
├── latex/                         # 1 file .tex cho mỗi vị trí
├── pdf/                           # Nguyen_Gia_Huy_<Role>.pdf
├── scripts/
│   ├── build-all.sh               # build và kiểm tra toàn bộ
│   └── check-differentiation.py   # đo mức khác biệt Work Experience giữa các CV
└── README.md
```

| Source | PDF | Trọng tâm |
|---|---|---|
| `backend-engineer.tex` | `Nguyen_Gia_Huy_Backend_Engineer.pdf` | Tích hợp, API, data store, gateway & identity |
| `software-engineer.tex` | `Nguyen_Gia_Huy_Software_Engineer.pdf` | End-to-end: product, testing, data, delivery |
| `python-backend.tex` | `Nguyen_Gia_Huy_Python_Backend_Engineer.pdf` | Python Smart Contracts, vòng đời lãi và repayment |
| `golang-backend.tex` | `Nguyen_Gia_Huy_Golang_Backend_Engineer.pdf` | 2 hệ thống Go (5x, 20x), gRPC project |
| `java-backend.tex` | `Nguyen_Gia_Huy_Java_Backend_Engineer.pdf` | Kỹ năng backend chuyển giao sang Java/Spring Boot |
| `data-engineer.tex` | `Nguyen_Gia_Huy_Data_Engineer.pdf` | Vietlink ETL, migration, ingestion |
| `devops-engineer.tex` | `Nguyen_Gia_Huy_DevOps_Engineer.pdf` | Cluster lifecycle, CI/CD, IaC, monitoring |
| `cloud-engineer.tex` | `Nguyen_Gia_Huy_Cloud_Engineer.pdf` | Dịch vụ AWS + OpenStack, tenant isolation |
| `platform-engineer.tex` | `Nguyen_Gia_Huy_Platform_Engineer.pdf` | Nền tảng dùng chung, internal tooling |
| `fintech-backend.tex` | `Nguyen_Gia_Huy_FinTech_Backend_Engineer.pdf` | Core banking (Vault Core) |

## Build

```bash
cd resume
./scripts/build-all.sh                    # build tất cả
./scripts/build-all.sh data-engineer      # build 1 hoặc vài bản (tên file .tex, bỏ đuôi)
ENGINE=docker ./scripts/build-all.sh      # ép dùng engine cụ thể
PDF_PREFIX="Nguyen_Gia_Huy" ./scripts/build-all.sh   # đổi tiền tố tên file PDF
```

- Engine được chọn tự động theo thứ tự `latexmk` → `xelatex` → `tectonic` → `docker`. Template dùng `fontspec`, nên cần XeLaTeX hoặc LuaLaTeX.
- Cài nhanh trên macOS: `brew install tectonic poppler`.
- Tên PDF = `<PDF_PREFIX>_<pdf-name>.pdf`, trong đó `pdf-name` lấy từ dòng đầu của mỗi file `.tex`, ví dụ `% pdf-name: Data_Engineer`.
- Tên file mặc định viết không dấu ("Nguyen") để tránh lỗi font hoặc encoding trên một số cổng ATS và email. Muốn có dấu thì chạy `PDF_PREFIX="Nguyễn_Gia_Huy" ./scripts/build-all.sh`.
- Sau khi build, script tự kiểm tra: số trang, khả năng trích xuất text (ATS), ligature, đủ tên/email/công ty, và overfull box.

Đo mức khác biệt giữa các CV sau khi chỉnh sửa:

```bash
python3 scripts/check-differentiation.py latex
```

Mục tiêu: mọi cặp CV ≥ 60%. Hiện tại thấp nhất 65%, trung bình 87%.

## Chỉnh sửa

### Thông tin dùng chung: `templates/resume-template.tex`
- Thông tin cá nhân: `\cvname`, `\cvemail`, `\cvphone`, `\cvlinkedin`.
- Công ty, thời gian, chức danh chính thức: `\jobGalaxyFinX`, `\jobVietlink`, `\jobVNPAY`, `\jobEsolLabs`.
- Dự án: `\projDattingQ`, `\projMeetQ`. Học vấn: `\cveducation`. Cỡ chữ: `\cvfontsize` (mặc định 10pt).

### Functional job title
Có ba cách gọi header công ty. Chức danh chính thức luôn hiện kèm:

```latex
\jobVietlink                                % Software Engineer
\jobVietlink[Data Engineer]                 % Data Engineer (Software Engineer)
\jobVietlink*[Data Platform Infrastructure] % Software Engineer – Data Platform Infrastructure
\jobVNPAY[Platform Engineer][Mô tả khác]    % tham số thứ 2 (tuỳ chọn) thay dòng mô tả công ty
```

- Dùng dạng `[Role]` khi phần lớn công việc ở công ty đó đúng với role.
- Dùng dạng `*[Focus]` khi chỉ một phần công việc liên quan.

### Nội dung từng CV: `latex/<role>.tex`
Mỗi file gồm: `\cvheader{...}`, `\cvsummary{...}`, `cvskills`, các header công ty kèm `itemize`, các project và `\cveducation`. Số bullet và thứ tự section có thể khác nhau giữa các bản.

### Duyệt các chi tiết mở rộng
`analysis/review-needed.md` có hai phần:
- **Phần A:** những gì đã có trong CV nhưng được suy ra từ cơ chế của công nghệ. Hãy kiểm tra lại.
- **Phần B:** bullet viết sẵn cho những chi tiết **chưa** xác minh, ví dụ kiến trúc controller/worker của hệ thống migration, ngôn ngữ của các ETL job, orchestration. Chỉ dán vào CV sau khi bạn xác nhận đúng và có thể giải thích khi phỏng vấn.

### Nếu CV tràn sang trang 2
1. Bỏ bullet ít liên quan nhất với vị trí.
2. Rút gọn những bullet có dòng cuối chỉ 1–2 chữ.
3. Gộp các bullet của dự án.
4. Cuối cùng mới giảm cỡ chữ: đặt `\renewcommand{\cvfontsize}{\fontsize{9.5pt}{11pt}\selectfont}` trước `\cvheader`.

## Quy tắc nội dung
- Không thêm công nghệ, số liệu hay thành tích chưa xác minh. Chỉ dùng chi tiết suy ra từ cơ chế vốn có của công nghệ, và liệt kê chúng trong `review-needed.md`.
- Không biến hệ thống viết bằng Golang/Python thành kinh nghiệm Java.
- Java/Spring Boot, FastAPI, RabbitMQ, Jenkins, ArgoCD, Consul, HashiCorp Vault hiện chỉ là skill được liệt kê.
- "nearly three years" đúng tại 10/2026. Hãy cập nhật khi thời gian trôi qua.
