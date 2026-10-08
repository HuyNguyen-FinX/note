# CV Differentiation Report

Ngày: 2026-10-08. Phạm vi: 10 CV trong `latex/`, PDF tương ứng trong `pdf/Nguyen_Gia_Huy_*.pdf`.

## 1. Phase 1: Audit bộ CV cũ (v1)

### Phát hiện
| Vấn đề | Chi tiết |
|---|---|
| Work Experience gần như giống nhau | Cả 10 CV dùng cùng 17 bullet gốc, chỉ đổi thứ tự hoặc đổi vài từ. Mức khác biệt trung bình giữa các cặp chỉ **30%**, thấp nhất **7%** (Backend vs Golang) và **8%** (Cloud vs Platform, Java vs Python, FinTech vs Java) |
| Job title không định vị | Mọi CV đều ghi y hệt "Software Engineer" / "Middle Software Engineer, Core Banking" cho mọi công ty |
| Tỷ trọng công ty cố định | Mỗi CV đều có 3–5 bullet cho Galaxy và 3–4 bullet cho VNPAY, bất kể vị trí ứng tuyển |
| Thiếu technical depth | Bullet dạng "Built ETL pipelines on AWS (…)" chỉ liệt kê công nghệ, không nói kiến trúc hay vai trò của từng thành phần |
| Kinh nghiệm bị đặt sai trọng tâm | Bản Data dành 4 bullet cho Galaxy dù Vietlink mới là kinh nghiệm data chính; bản DevOps vẫn mô tả Lending/Overdraft; bản Golang để Kong/Keycloak chiếm chỗ của hệ thống Go |
| Bị đánh giá thấp | Vai trò "platform" của VNPAY (gateway và identity dùng chung); tooling nội bộ ở Galaxy (test framework); khía cạnh ingestion của EsolLabs |

### Cách đo
`scripts/check-differentiation.py`: một bullet Work Experience của CV A được tính là **trùng** với CV B nếu bullet giống nhất trong B có độ tương đồng chuỗi từ ≥ 0.6 (difflib, đã bỏ stopword). Mức khác biệt của A so với B = 1 − (số bullet trùng / tổng số bullet của A). Thay từ đồng nghĩa trong cùng cấu trúc câu vẫn bị tính là trùng.

## 2. Phase 2–3: Kết quả sau khi viết lại (v2)

| Chỉ số | v1 | v2 |
|---|---|---|
| Khác biệt trung bình giữa các cặp | 30% | **87%** |
| Cặp thấp nhất | 7% | **65%** |
| Số cặp dưới 60% | 45/45 | **0/45** |

Ma trận v2 (hàng = CV được đo, cột = CV so sánh):

```
                  backen cloud- data-e devops fintec golang java-b platfo python softwa
backend-engineer    --     100%    73%    73%    73%   100%   100%    91%    82%   100%
cloud-engineer      100%   --      92%    67%    75%    92%    92%    83%    83%    75%
data-engineer        70%   100%   --      90%    70%    80%    90%    70%    90%    80%
devops-engineer      77%    69%    92%   --      77%   100%   100%    69%   100%    77%
fintech-backend      77%    77%    77%    77%   --      85%    92%    85%    85%    92%
golang-backend      100%    90%    80%   100%    80%   --     100%    90%   100%    80%
java-backend        100%    89%    89%   100%    89%   100%   --     100%   100%    89%
platform-engineer    90%    80%    70%    60%    80%    90%   100%   --     100%    90%
python-backend       78%    78%    89%   100%    78%   100%   100%   100%   --     100%
software-engineer   100%    82%    82%    73%    91%    82%    91%    91%   100%   --
```

### Các cặp gần nhau nhất và lý do chấp nhận được
| Cặp | Mức khác biệt | Phần trùng | Vì sao chấp nhận |
|---|---|---|---|
| DevOps vs Platform | 65% | Cluster API / 50+ clusters | Cùng dựa trên một sự kiện thật. DevOps kể về **vận hành lifecycle**, Platform kể về **năng lực nền tảng cung cấp cho người dùng**. Bullet Galaxy và Vietlink của hai bản hoàn toàn khác nhau |
| Cloud vs DevOps | 68% | Keycloak, Kong, 80% automation | Bản Cloud xoay quanh dịch vụ cloud và cô lập tenant; bản DevOps xoay quanh CI/CD và lifecycle |
| Data vs Platform | 70% | Terraform/SAM + monitoring ở Vietlink | Đây là sự kiện duy nhất về hạ tầng data |
| Backend vs Data | 71% | OpenSearch migration | Bản Backend kể về backend search; bản Data kể về indexing workload |

## 3. Functional job titles

Chức danh chính thức luôn hiển thị (trong ngoặc, hoặc đứng trước dấu "–") để khớp khi background check.

| CV | Galaxy FinX | Vietlink | VNPAY | EsolLabs |
|---|---|---|---|---|
| Backend | Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Backend & Data Services | Software Engineer – API Gateway & Identity | Blockchain Developer – Event-Driven Backend |
| Software | Middle Software Engineer, Core Banking | Software Engineer | Software Engineer | Blockchain Developer |
| Python | Python Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Data Processing | Software Engineer | Blockchain Developer |
| Golang | Golang Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Backend & Data Services | Software Engineer | Blockchain Developer |
| Java | Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Backend & Data Services | Software Engineer – Microservices & Identity | Blockchain Developer |
| Data | Middle Software Engineer – Core Banking Data Migration | **Data Engineer (Software Engineer)** | Software Engineer | Blockchain Developer – On-chain Data Ingestion |
| DevOps | Middle Software Engineer – Cloud Infrastructure & Automation | Software Engineer – Data Platform Infrastructure | **Cloud Platform Engineer (Software Engineer)** | Blockchain Developer |
| Cloud | Middle Software Engineer – AWS Cloud Infrastructure | Software Engineer – AWS Data Platform | **Cloud Engineer, OpenStack & Kubernetes (Software Engineer)** | Blockchain Developer |
| Platform | Middle Software Engineer – Internal Tooling & Delivery Platform | Software Engineer – Data Platform | **Platform Engineer (Software Engineer)** | Blockchain Developer |
| FinTech | Middle Software Engineer, Core Banking | Software Engineer | Software Engineer – Fintech Cloud Platform | Blockchain Developer – DeFi & Transaction Systems |

Quy tắc chọn title:
- Dạng **"Role (Official)"** chỉ dùng khi phần lớn công việc ở công ty đó đúng với role: Vietlink → Data Engineer; VNPAY → Platform/Cloud.
- Dạng **"Official – Focus"** dùng khi chỉ một phần công việc liên quan.
- Bản Software Engineer giữ nguyên title chính thức.

## 4. Tỷ trọng bullet theo công ty

| CV | Galaxy FinX | Vietlink | VNPAY | EsolLabs | Projects | Trọng tâm |
|---|---|---|---|---|---|---|
| backend-engineer | 4 | 3 | 2 | 2 | 3 | Tích hợp, API, data store |
| cloud-engineer | 3 | 3 | **5** | 1 | 1 | AWS + OpenStack |
| data-engineer | 2 | **5** | 1 | 2 | 2 | Vietlink ETL |
| devops-engineer | 4 | 3 | **5** | 1 | 2 | VNPAY lifecycle + CI/CD |
| fintech-backend | **6** | 1 | 3 | 3 | 1 | Vault Core |
| golang-backend | 3 | 2 | 1 | 1 | **3** | 2 hệ thống Go + dự án gRPC |
| java-backend | 4 | 2 | 2 | 1 | 2 | Kỹ năng chuyển giao được |
| platform-engineer | 3 | 2 | **4** | 1 | 1 | Nền tảng dùng chung |
| python-backend | **5** | 2 | 1 | 1 | 3 | Python Smart Contracts |
| software-engineer | 4 | 3 | 3 | 1 | 2 | End-to-end, cân bằng |

Khác biệt cấu trúc giữa các bản:
- Bản Golang dùng section **"Key Project"** với 3 bullet sâu về gRPC.
- Bản Software dùng nhãn **Product / Testing / Data / Delivery** cho bullet Galaxy.
- Bản Python đặt MeetQ (tích hợp AI) lên trước DattingQ.
- Bản FinTech có nhóm skill **Banking Products** và **DeFi**.
- Bản Java tách rõ "working knowledge" và "production" trong mục Languages.

## 5. Phase 5: Đánh giá của Technical Hiring Manager

Thang: ★ yếu → ★★★★★ rất mạnh. "Credibility" = mức tin cậy khi đối chiếu với phỏng vấn kỹ thuật.

| CV | Role alignment | Credibility | Depth | ATS | Nhận xét |
|---|---|---|---|---|---|
| FinTech Backend | ★★★★★ | ★★★★★ | ★★★★ | ★★★★★ | Mạnh nhất. Vault Core là kinh nghiệm hiếm; 6 bullet Galaxy kể đủ lifecycle sản phẩm. Thiếu: quy mô (số tài khoản, số giao dịch) |
| Platform | ★★★★ | ★★★★ | ★★★★ | ★★★★ | VNPAY được kể đúng góc platform; Galaxy được kể dưới góc tooling. Thiếu: chỉ số developer experience, IDP hoặc self-service |
| DevOps | ★★★★ | ★★★★ | ★★★★ | ★★★★★ | VNPAY 5 bullet sâu, có cert DevOps on AWS. Thiếu: công cụ CI/CD cụ thể (B4), Helm, SLO |
| Backend | ★★★★ | ★★★★ | ★★★★ | ★★★★ | Tập trung tích hợp, data store và gateway, khác rõ với bản Software. Thiếu: chi tiết thiết kế API và giao dịch (B1, B3) |
| Golang | ★★★★ | ★★★★ | ★★★ | ★★★★ | Hai hệ thống Go có số liệu rất tốt, nhưng Galaxy chỉ có 3 bullet vì thiếu chi tiết triển khai. Xác nhận B1/B2 sẽ đưa lên ★★★★★ |
| Cloud | ★★★★ | ★★★★ | ★★★ | ★★★★ | Có cả AWS và OpenStack. Thiếu: VPC, IAM, networking, cost (chưa có bằng chứng) |
| Data | ★★★★ | ★★★★ | ★★★ | ★★★★ | Vietlink 5 bullet đúng chất data engineering. Thiếu: orchestration, data volume, format, data quality (B5). Không có Spark/Airflow |
| Software | ★★★★ | ★★★★★ | ★★★ | ★★★★ | Rộng, có số liệu ở mọi công ty. Phù hợp JD general |
| Python | ★★★ | ★★★★ | ★★★★ | ★★★★ | Đào sâu Vault Core contract, nhưng Python chỉ có ở 1 hệ thống. Xác nhận ngôn ngữ ETL Vietlink (B5) sẽ cải thiện rõ |
| Java | ★★ | ★★★★★ | ★★★ | ★★★ | Trung thực: không gán Golang/Python thành Java. Phù hợp JD "Java **or** Go" hoặc ngân hàng tuyển chuyển stack. Cần một dự án Spring Boot thật (B8) |

## 6. Kiểm tra kỹ thuật (Phase 4)

| Hạng mục | Kết quả |
|---|---|
| Compile 10/10 | Đạt (tectonic/XeTeX), không có lỗi hay overfull box |
| Số trang | 10/10 bản 1 trang A4 |
| Cỡ chữ | Tăng từ 9.5pt lên **10pt** (leading 11.6pt) mà vẫn giữ 1 trang |
| Text extraction (pdftotext) | Không có ligature, không có ký tự lỗi, không ngắt từ bằng gạch nối |
| Tên, liên hệ, học vấn, chứng chỉ | Khớp ở 10/10 |
| Công ty, mốc thời gian, chức danh chính thức | Khớp ở 10/10 (chức danh chính thức có mặt ở dòng title của từng công ty) |
| Metric | Không có con số nào ngoài các metric của CV gốc |
| Kiểm tra trực quan | Đã render và xem từng trang; các dòng cuối chỉ có 1 chữ đã được xử lý |
| Tên file PDF | `Nguyen_Gia_Huy_<Role>.pdf` |
