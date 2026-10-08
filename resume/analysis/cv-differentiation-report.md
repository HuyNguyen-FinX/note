# CV Differentiation Report (v3: CV 2 trang, đầy đủ kinh nghiệm)

Ngày: 2026-10-08. Phạm vi: 10 CV trong `latex/` → `pdf/Nguyen_Gia_Huy_*.pdf`.

## 1. Lịch sử các phiên bản

| | v1 | v2 | **v3 (hiện tại)** |
|---|---|---|---|
| Độ dài | 1 trang | 1 trang | **2 trang** (10/10) |
| Bullet Work Experience mỗi CV | 12–15 | 9–13 | **21–29** |
| Sự kiện gốc được giữ (trên 20) | 17–20 | 14–20, nhiều bản bỏ bớt | **20/20 ở mọi CV** |
| Aspects được giữ | – | – | **98–100%** |
| Metric được giữ (trên 12) | đủ | thiếu ở một số bản | **12/12 ở mọi CV** |
| Khác biệt trung bình giữa các cặp | 30% | 87% | **81%** |
| Cặp thấp nhất | 7% | 65% | **62%** |
| Số cặp dưới 60% | 45/45 | 0/45 | **0/45** |

Ở v2, mức khác biệt cao một phần là nhờ **bỏ bớt** kinh nghiệm. Sang v3, mọi CV giữ đủ 20/20 sự kiện mà vẫn đạt khác biệt ≥ 62% ở mọi cặp. Lý do:
- **Primary experience khác nhau:** mỗi CV có công ty trọng tâm riêng, viết thành 8–13 bullet chia nhóm.
- **Cùng sự kiện, khác góc nhìn:** cùng một sự kiện nhưng mỗi CV kể theo vai trò riêng. Ví dụ Kong Gateway được kể là "access layer" ở bản Cloud, "shared platform service" ở Platform, "API gateway in front of microservices" ở Java, và "integrated and operated" ở DevOps.
- **Không trùng ở công ty supporting:** bullet của các công ty supporting được viết lại cho từng CV, không copy giữa các bản.

Cách đo: `python3 scripts/check-differentiation.py latex`. Một bullet bị tính là trùng nếu giống ≥ 60% chuỗi từ (đã bỏ stopword) với một bullet bất kỳ ở CV kia. Đổi từ đồng nghĩa trong cùng cấu trúc câu vẫn bị tính là trùng.

## 2. Ma trận khác biệt v3

```
                  backen cloud- data-e devops fintec golang java-b platfo python softwa
backend-engineer    --      72%    64%    80%    72%    84%    72%    72%    84%    76%
cloud-engineer       73%   --      77%    65%    73%    92%    96%    65%    85%    85%
data-engineer        69%    79%   --      79%    72%    86%    93%    72%    83%    76%
devops-engineer      82%    68%    79%   --      82%    96%    96%    68%    86%    79%
fintech-backend      74%    74%    70%    81%   --      85%    89%    63%    78%    74%
golang-backend       81%    90%    81%    95%    81%   --     100%    76%   100%    95%
java-backend         70%    96%    91%    96%    87%   100%   --      96%    91%    83%
platform-engineer    73%    65%    65%    65%    62%    81%    96%   --      81%    81%
python-backend       83%    83%    78%    83%    74%   100%    91%    78%   --      91%
software-engineer    75%    83%    71%    75%    71%    96%    83%    79%    92%   --
```

| Cặp gần nhất | Mức | Phần trùng còn lại | Vì sao chấp nhận |
|---|---|---|---|
| FinTech vs Platform | 62% | Bullet Galaxy về deploy và CI/CD | Cùng một sự kiện. FinTech kể là "verification & delivery" của sản phẩm ngân hàng, Platform kể là "delivery path" cho các team |
| Cloud vs Platform | 65% | Cluster API, OpenStack | Cloud kể kiến trúc và hạ tầng; Platform kể năng lực nền tảng cung cấp cho người dùng |
| Backend vs Data | 66% | Account migration, OpenSearch | Data kể dưới góc dữ liệu, Backend dưới góc service |
| Cloud vs DevOps | 67% | VNPAY lifecycle | DevOps kể vận hành và tự động hoá, Cloud kể kiến trúc và phân tách tenant |

## 3. Phân bổ Primary / Secondary / Supporting

| CV | Primary (số bullet) | Secondary | Supporting | Nhóm bullet trong Primary |
|---|---|---|---|---|
| Data Engineer | **Vietlink (13)** | Galaxy (7) | VNPAY (5), EsolLabs (4) | Pipeline Architecture · Batch Optimization · Search & Analytics · Reliability & Operations |
| DevOps Engineer | **VNPAY (11)** | Galaxy (7) | Vietlink (7), EsolLabs (3) | Private Cloud & Cluster Lifecycle · Infrastructure Automation · Traffic, Identity & Multi-tenancy |
| Cloud Engineer | **VNPAY (10)** | Galaxy (7), Vietlink (6) | EsolLabs (3) | Private Cloud Architecture · Multi-tenant Identity & Access · Service Networking & Automation |
| Platform Engineer | **VNPAY (10)** | Galaxy (7) | Vietlink (6), EsolLabs (3) | Kubernetes Platform · Shared Platform Services · Platform Automation |
| Golang Backend | **Galaxy (8)** | Vietlink (5) | VNPAY (4), EsolLabs (4) + Key Project DattingQ (4) | Account Migration (Go) · Testing Infrastructure (Go) · Integration & Delivery |
| Python Backend | **Galaxy (10)** | Vietlink (5) | VNPAY (5), EsolLabs (3) | Lending & Overdraft (Python Smart Contracts) · Integration & Testing · Data & Platform |
| Java Backend | **Galaxy (9)** | VNPAY (6) | Vietlink (5), EsolLabs (3) | Transaction Processing · Integration & Data · Testing & Delivery |
| FinTech Backend | **Galaxy (12)** | VNPAY (6), EsolLabs (5) | Vietlink (4) | Lending & Overdraft · Banking Integration & Migration · Verification & Delivery |
| Backend Engineer | **Galaxy (9)** | Vietlink (6), VNPAY (6) | EsolLabs (4) | Integration & Transaction Logic · Migration Backend · Testing & Deployment |
| Software Engineer | Cân bằng: Galaxy (9) | Vietlink (6), VNPAY (6) | EsolLabs (3) | Gắn nhãn theo tầng: Product, Financial logic, Testing, Performance, Data, Infrastructure, Delivery, Integration |

Chi tiết từng sự kiện được giữ hay mở rộng nằm trong `experience-coverage-report.md`.

## 4. Functional job titles (không đổi so với v2)

| CV | Galaxy FinX | Vietlink | VNPAY | EsolLabs |
|---|---|---|---|---|
| Data | Middle Software Engineer – Core Banking Data & Migration | **Data Engineer (Software Engineer)** | Software Engineer – Cloud Platform Infrastructure | Blockchain Developer – On-chain Data Ingestion |
| DevOps | Middle Software Engineer – Cloud Infrastructure & Automation | Software Engineer – Data Platform Infrastructure | **Cloud Platform Engineer (Software Engineer)** | Blockchain Developer |
| Cloud | Middle Software Engineer – AWS Cloud Infrastructure | Software Engineer – AWS Data Platform | **Cloud Engineer, OpenStack & Kubernetes (Software Engineer)** | Blockchain Developer |
| Platform | Middle Software Engineer – Internal Tooling & Delivery Platform | Software Engineer – Data Platform | **Platform Engineer (Software Engineer)** | Blockchain Developer |
| Golang | Golang Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Backend & Data Services | Software Engineer | Blockchain Developer |
| Python | Python Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Data Processing | Software Engineer | Blockchain Developer |
| Java | Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Backend & Data Services | Software Engineer – Microservices & Identity | Blockchain Developer |
| FinTech | Middle Software Engineer, Core Banking | Software Engineer | Software Engineer – Fintech Cloud Platform | Blockchain Developer – DeFi & Transaction Systems |
| Backend | Backend Engineer, Core Banking (Middle Software Engineer) | Software Engineer – Backend & Data Services | Software Engineer – API Gateway & Identity | Blockchain Developer – Event-Driven Backend |
| Software | Middle Software Engineer, Core Banking | Software Engineer | Software Engineer | Blockchain Developer |

## 5. Layout và pagination (Phase 4)

| Hạng mục | Kết quả |
|---|---|
| Số trang | 10/10 bản 2 trang A4. Trang 2 lấp từ 38% (Software) đến 95% (DevOps) |
| Cỡ chữ và khoảng cách | 10pt, leading 12.3pt, lề 1.55 cm, khoảng cách giữa bullet 1.6pt. Không thu nhỏ chữ để nhồi nội dung |
| Section header ở cuối trang | Không có: `\needspace` giữ header section kèm ≥ 6 dòng |
| Header công ty ở cuối trang | Không có: header công ty luôn kèm tiêu đề nhóm và ≥ 2 bullet |
| Bullet bị chia đôi qua 2 trang | Không có (widow/club penalty = 10000) |
| Chỗ ngắt trang | 8/10 bản ngắt đúng ranh giới công ty hoặc nhóm. Cloud và DevOps chia nhóm đầu của VNPAY 3/2 bullet, không có bullet lẻ |
| Dòng cuối chỉ có 1 chữ | 0, nhờ ragged-right có kiểm soát (`\parfillskip`) |
| Footer từ trang 2 | "Nguyen Gia Huy \| <Role> \| Page 2 of 2" |
| Text extraction (ATS) | Không ligature, không ngắt từ bằng gạch nối, đủ tên, liên hệ, công ty, chức danh chính thức và ngày tháng |
| Số liệu | Không có con số nào ngoài các metric gốc |

Lỗi phát hiện và đã sửa trong quá trình này: trong template cũ, `\raggedright` và `\parfillskip` bị reset bên trong list, nên mọi bullet thực chất được căn đều 2 bên (gây giãn chữ khi đã tắt hyphenation). Giờ các thiết lập này được áp dụng trong từng list qua key `first=` của enumitem.

## 6. Phase 5: Đánh giá của Technical Hiring Manager

| CV | Role alignment | Depth | Credibility | Nhận xét |
|---|---|---|---|---|
| Data Engineer | ★★★★ | ★★★★ | ★★★★ | Vietlink 13 bullet, 4 nhóm rõ ràng; đọc như hồ sơ data engineer. Còn thiếu orchestration, volume, data quality (B5, B9) |
| DevOps Engineer | ★★★★ | ★★★★ | ★★★★ | VNPAY 11 bullet về lifecycle, automation, multi-tenancy. Còn thiếu công cụ CI/CD cụ thể, Helm, SLO (B4, B6) |
| Platform Engineer | ★★★★ | ★★★★ | ★★★★ | Kể đúng góc "platform as a product" và internal tooling |
| Cloud Engineer | ★★★★ | ★★★ | ★★★★ | Có cả AWS lẫn OpenStack. Thiếu VPC, IAM, networking (chưa có bằng chứng) |
| FinTech Backend | ★★★★★ | ★★★★ | ★★★★★ | Galaxy 12 bullet theo vòng đời sản phẩm ngân hàng. Thiếu quy mô (số tài khoản, số giao dịch) |
| Backend Engineer | ★★★★ | ★★★★ | ★★★★ | Tập trung tích hợp, transaction logic, gateway và identity |
| Golang Backend | ★★★★ | ★★★ | ★★★★ | Hai hệ thống Go có số liệu tốt, nhưng thiếu chi tiết concurrency. Xác nhận B1/B2 sẽ đưa lên ★★★★★ |
| Python Backend | ★★★ | ★★★★ | ★★★★ | Vault Core được đào sâu 5 bullet; Python chỉ có ở 1 hệ thống (B5 sẽ cải thiện) |
| Java Backend | ★★ | ★★★ | ★★★★★ | Trung thực về stack; cần một dự án Spring Boot thật (B8) |
| Software Engineer | ★★★★ | ★★★ | ★★★★★ | Rộng, có số liệu ở mọi công ty; ngắn nhất (trang 2 lấp 38%) |
