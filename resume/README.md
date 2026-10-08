# Resume Variants: Nguyen Gia Huy

10 CV được định vị theo 10 hướng nghề nghiệp khác nhau. Mỗi bản có functional job title, Work Experience và Technical Skills riêng, và **giữ đủ 20/20 kinh nghiệm gốc**. Tất cả viết bằng LaTeX, dùng chung một template, xuất ra PDF A4 **2 trang**, ATS-friendly.

## Cấu trúc

```text
resume/
├── original/                      # CV gốc (main.tex) + PDF để đối chiếu
├── analysis/
│   ├── profile-analysis.md        # phân tích kinh nghiệm và bằng chứng
│   ├── role-matching.md           # mức độ phù hợp với từng vị trí, kỹ năng còn thiếu
│   ├── experience-inventory.md    # mọi sự kiện đã xác nhận trong CV gốc, có ID (G1a, V2e…)
│   ├── experience-coverage-report.md # (tự sinh) CV nào giữ, mở rộng hay bỏ sự kiện nào
│   ├── cv-differentiation-report.md  # lịch sử v1→v3, ma trận khác biệt, phân bổ, layout, đánh giá
│   └── review-needed.md           # diễn giải cần xác nhận (Phần A) và đề xuất chưa đưa vào (Phần B)
├── templates/resume-template.tex  # layout, font, thông tin cá nhân, timeline, học vấn
├── latex/                         # 1 file .tex cho mỗi vị trí
├── pdf/                           # Nguyen_Gia_Huy_<Role>.pdf
├── scripts/
│   ├── build-all.sh               # build và kiểm tra toàn bộ
│   ├── check-differentiation.py   # đo mức khác biệt Work Experience giữa các CV
│   └── coverage-report.py         # sinh analysis/experience-coverage-report.md
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
- Sau khi build, script tự kiểm tra: tối đa 3 trang, trang cuối không gần như trống (≥ 30% so với trang 1), khả năng trích xuất text (ATS), ligature, đủ tên/email/công ty, và overfull box.

Đo mức khác biệt giữa các CV sau khi chỉnh sửa:

```bash
python3 scripts/check-differentiation.py latex
```

Mục tiêu: mọi cặp CV ≥ 60%. Hiện tại thấp nhất 62%, trung bình 81%, trong khi mọi CV đều giữ đủ kinh nghiệm.

Kiểm tra mức bao phủ kinh nghiệm (và sinh lại báo cáo coverage):

```bash
python3 scripts/coverage-report.py
```

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

Kinh nghiệm primary được chia nhóm bằng `\cvgroup{Tiêu đề nhóm}`, đặt ngay trước một `itemize`.

**Tag sự kiện:** cuối mỗi bullet có comment, ví dụ `% @V1bc !A14`:
- `@V1bc` trỏ tới sự kiện trong `analysis/experience-inventory.md` (V1, aspects b và c).
- `!A14` trỏ tới diễn giải trong `analysis/review-needed.md` (Phần A).

Khi thêm hoặc sửa bullet, hãy giữ tag để `coverage-report.py` tiếp tục chính xác.

### Duyệt các chi tiết mở rộng
`analysis/review-needed.md` có hai phần:
- **Phần A:** những gì đã có trong CV nhưng được suy ra từ cơ chế của công nghệ. Hãy kiểm tra lại.
- **Phần B:** bullet viết sẵn cho những chi tiết **chưa** xác minh, ví dụ kiến trúc controller/worker của hệ thống migration, ngôn ngữ của các ETL job, orchestration. Chỉ dán vào CV sau khi bạn xác nhận đúng và có thể giải thích khi phỏng vấn.

### Phân trang
Template tự xử lý:
- Section header và header công ty không bao giờ nằm cuối trang (`\needspace`).
- Một bullet không bao giờ bị chia đôi qua 2 trang.
- Dòng cuối của bullet không bao giờ chỉ có 1 chữ.
- Footer từ trang 2 có tên, vị trí và số trang.

Nếu một nhóm bị chia trang khó đọc, đặt `\needspace{5\baselineskip}` ngay trước `\item` cần đi cùng bullet kế tiếp (xem ví dụ trong `cloud-engineer.tex`).

Ưu tiên chỉnh layout, **không** cắt nội dung để giữ số trang.

## Quy tắc nội dung
- Không thêm công nghệ, số liệu hay thành tích chưa xác minh. Chỉ dùng chi tiết suy ra từ cơ chế vốn có của công nghệ, và liệt kê chúng trong `review-needed.md`.
- Không biến hệ thống viết bằng Golang/Python thành kinh nghiệm Java.
- Java/Spring Boot, FastAPI, RabbitMQ, Jenkins, ArgoCD, Consul, HashiCorp Vault hiện chỉ là skill được liệt kê.
- "nearly three years" đúng tại 10/2026. Hãy cập nhật khi thời gian trôi qua.
