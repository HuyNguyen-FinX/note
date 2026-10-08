# Profile Analysis: Nguyen Gia Huy

Nguồn: `original/original_cv.tex` (bản sao của `main.tex`), đã compile thành `original/original_cv.pdf`.
Ngày phân tích: 2026-10-08.

Mọi nhận định dưới đây chỉ dựa trên nội dung CV gốc. Chỗ nào là suy luận sẽ được ghi rõ là **suy luận**.

---

## 1. Thông tin cá nhân (giữ nguyên ở mọi phiên bản)

| Mục | Giá trị |
|---|---|
| Họ tên | Nguyen Gia Huy |
| Email | johnnynguyen882@gmail.com |
| Điện thoại | 0948385149 |
| LinkedIn | linkedin.com/in/huy8bit |
| Học vấn | University of Science, HCMC (HCMUS): B.Sc. Information Technology, Knowledge Engineering |
| Chứng chỉ | DevOps on AWS Specialization (Coursera) |

Không có trong CV gốc: địa điểm sinh sống, năm tốt nghiệp, trình độ tiếng Anh/Nhật, GitHub.

## 2. Timeline thực tế

| Thời gian | Công ty | Chức danh | Thời lượng (đến 10/2026) |
|---|---|---|---|
| 03/2026 – Present | Galaxy FinX (Vikki Digital Bank) | Middle Software Engineer, Core Banking | khoảng 7 tháng |
| 04/2025 – 03/2026 | Vietlink (KDDI Agile Development Center Group) | Software Engineer | khoảng 11 tháng |
| 04/2024 – 04/2025 | VNPAY | Software Engineer | khoảng 12 tháng |
| 06/2023 – 09/2023 | EsolLabs | Blockchain Developer | khoảng 3–4 tháng |
| *(09/2023 – 03/2024)* | *Freelance* | *Blockchain Developer* | *đang bị comment trong source* |

- **Tổng kinh nghiệm đã xác nhận:** khoảng 2 năm 10 tháng. Vì vậy các CV ghi "nearly three years", không ghi "3+ years".
  Nếu bạn muốn hiện lại mục Freelance (09/2023–03/2024), tổng sẽ khoảng 3 năm 4 tháng và có thể ghi "3+ years".
- **Khoảng trống 09/2023 → 04/2024:** đúng bằng giai đoạn Freelance đang bị ẩn. Nhà tuyển dụng có thể hỏi về khoảng này.
- **Tháng 04/2025** xuất hiện ở cả VNPAY (kết thúc) và Vietlink (bắt đầu), tức là chuyển việc trong cùng tháng. Đây là chuyện bình thường, không phải mâu thuẫn.
- Hai dự án DattingQ và MeetQ **không có mốc thời gian**, và CV không nói rõ là dự án cá nhân, freelance hay làm cho công ty.

## 3. Tech stack theo từng công ty / dự án

| Nơi làm | Công nghệ có bằng chứng trong bullet |
|---|---|
| Galaxy FinX | Thought Machine Vault Core, Python Smart Contracts, Golang, AWS (EKS, RDS, ECR, ELB, ECS, Lambda), CI/CD (công cụ không ghi rõ), Gauge (framework cũ đã được thay thế) |
| Vietlink | AWS (Lambda, ECS, RDS, S3, Athena), Elasticsearch, OpenSearch, Terraform, AWS SAM, CloudWatch, DataDog. Ngôn ngữ của các pipeline **không ghi rõ** |
| VNPAY | OpenStack, Cluster API, Kubernetes (50+ cluster), Keycloak, RBAC, Kong Gateway |
| EsolLabs | Solidity, Move, Ethereum, BSC, Polygon, Aptos, Sui, backend event-driven (ngôn ngữ không ghi rõ) |
| DattingQ | gRPC-Gateway, Kafka, MongoDB, Redis, OpenTelemetry, Prometheus, Grafana, ELK, ClickHouse |
| MeetQ | LiveKit, OpenAI models |

## 4. Hệ thống đã xây dựng / vận hành và các thành tích có số liệu

| Hệ thống | Số liệu (nguyên văn từ CV gốc) |
|---|---|
| Sản phẩm Lending & Overdraft trên Vault Core | không có |
| Simulation testing framework (Golang) | 24 phút → hơn 50 giây (20x) |
| Account migration system (Golang, ECS, Lambda, RDS) | 2.5 giờ → 27 phút (5x) |
| Triển khai Vault Core trên AWS + CI/CD | không có |
| ETL pipelines (Vietlink) | throughput +150% |
| Migration Elasticsearch → OpenSearch | không có |
| Private cloud OpenStack + Cluster API | 50+ production K8s clusters, zero-downtime upgrades |
| Keycloak multi-tenant | 20+ customer organizations |
| Kong Gateway | 100+ services |
| Tự động hoá data center | khoảng 80% quy trình |
| Smart contracts | 15+ contracts, 5+ chains |
| DattingQ backend | 1.5K req/s, 80–100 ms, 99.95% uptime |

Ghi chú: 24 phút ≈ 1440 giây, chia cho khoảng 50–55 giây ra khoảng 26–29x. Con số "20x" trong CV gốc là ước lượng thận trọng, các bản mới giữ nguyên "20x".

## 5. Năng lực theo nhóm, kèm mức độ bằng chứng

**Mạnh** = có bullet cụ thể kèm kết quả. **Trung bình** = có bullet nhưng không có số liệu, hoặc gián tiếp. **Chỉ liệt kê** = chỉ xuất hiện trong mục Skills.

| Nhóm | Mạnh | Trung bình | Chỉ liệt kê |
|---|---|---|---|
| Backend / business logic | Vault Core lending/overdraft, account migration, DattingQ | Tích hợp Vault Core với external services, backend event-driven (EsolLabs) | Spring Boot, FastAPI |
| Ngôn ngữ | Golang (2 hệ thống tại Galaxy), Python (Vault Smart Contracts) | Solidity, Move | **Java** |
| Database / search | OpenSearch/Elasticsearch, MongoDB, Redis (DattingQ) | RDS (engine không rõ), ClickHouse (dùng cho observability) | PostgreSQL |
| Messaging | Kafka (DattingQ) | | RabbitMQ |
| Data processing | ETL trên AWS, batch +150%, migration dữ liệu tài khoản | Athena (SQL) | Spark/Airflow/dbt: **không có** |
| Cloud (AWS) | EKS, ECS, Lambda, RDS, S3, Athena, ECR, ELB | CloudWatch, SAM | |
| Private cloud / K8s | OpenStack, Cluster API, 50+ cluster | | |
| IaC / automation | Terraform, AWS SAM, tự động hoá 80% data center | | |
| CI/CD | Đã xây pipeline CI/CD cho Vault Core | | Jenkins, ArgoCD (không rõ đã dùng ở đâu) |
| Security / IAM | Keycloak multi-tenant RBAC, Kong access control | | HashiCorp Vault, Consul |
| Observability | OTel/Prometheus/Grafana/ELK (DattingQ), CloudWatch/DataDog (Vietlink) | | |
| Testing | Framework simulation test (Golang) | | |
| Domain | Core banking (rất hiếm, giá trị cao), fintech cloud, blockchain | | |

## 6. Kỹ năng có thể chuyển giao giữa nhiều vị trí

- **Cải thiện hiệu năng có số đo**: 20x, 5x, +150%. Dùng được cho mọi vị trí.
- **Golang + AWS**: phục vụ được Backend, Golang, Cloud, Platform.
- **Kubernetes ở quy mô 50+ cluster**: phục vụ DevOps, Platform, Cloud.
- **Hiểu domain tài chính** (lãi, phí phạt, repayment, settlement): phục vụ FinTech, Backend, Java (ngân hàng thường dùng Java).
- **Dữ liệu**: ETL, migration, ingestion, search. Phục vụ Data Engineer, Backend.
- **Security / multi-tenancy**: phục vụ Platform, Cloud, Backend.

## 7. Kỹ năng thiếu bằng chứng (không được nhận là đã dùng trong production)

| Kỹ năng | Cách xử lý trong các CV |
|---|---|
| Java, Spring Boot | Chỉ để trong Skills. Bản Java có summary ghi rõ "Production work has been in Golang and Python" |
| FastAPI | Chỉ để trong Skills |
| PostgreSQL | Để trong Skills. Bullet chỉ ghi "RDS" |
| RabbitMQ | Chỉ để trong Skills |
| Jenkins, ArgoCD | Chỉ để trong Skills. Bullet CI/CD không gắn với công cụ cụ thể |
| HashiCorp Vault, Consul | Chỉ để trong Skills của các bản DevOps/Cloud/Platform |
| Protocol Buffers | **Suy luận**: gRPC-Gateway bắt buộc dùng `.proto`. Chỉ thêm ở bản Golang |
| Python cho ETL / MeetQ | **Không** gán cho Python vì CV gốc không nói ngôn ngữ |
| Spark, Airflow, dbt, Redshift/Snowflake/BigQuery, Helm, Ansible, GCP/Azure, Backstage, SRE/on-call metrics | **Không** đưa vào bất kỳ CV nào |

## 8. Lỗi và rủi ro phát hiện trong CV gốc

1. **Typo trong source:** `\project 3{MeetQ ...}` khiến PDF hiện ra "**3** | MeetQ – Software Engineer", và phần mô tả bị lệch dòng. Đã sửa trong template mới.
2. **Chữ Nhật "auでんき"**: dùng `CJKutf8`. Engine XeTeX làm mất ký tự, còn nhiều ATS không đọc được CJK. Bản mới dùng tên Latin **"au Denki"**.
3. **Ligature khi trích xuất text**: PDF gốc ra "workﬂows", "eﬃcient", "signiﬁcantly" (ký tự U+FB01…). ATS có thể không khớp keyword. Template mới tắt ligature, đã kiểm tra trích xuất ra 0 dòng lỗi.
4. **Hyphenation**: CV justified có thể cắt từ thành "con-trol", "Over-draft", làm hỏng keyword. Template mới tắt hyphenation và dùng ragged-right.
5. Link chứng chỉ hiển thị chữ "Certificate", không có nghĩa với ATS. Bản mới hiển thị "DevOps on AWS Specialization | Coursera".
6. Thiếu năm tốt nghiệp, địa điểm và ngôn ngữ (xem `role-matching.md`, mục Cải thiện chung).

## 9. Những điểm cần bạn xác nhận để CV mạnh hơn

Các mục dưới đây **chưa được đưa vào CV** vì CV gốc không xác nhận:

1. Pipeline ETL ở Vietlink viết bằng ngôn ngữ gì (Python? Go?). Nếu là Python, bản Python Backend và Data Engineer sẽ mạnh hơn đáng kể.
2. Backend của MeetQ và DattingQ viết bằng ngôn ngữ gì. gRPC-Gateway gần như chắc chắn là Go, nhưng CV không ghi rõ. Dự án thuộc loại nào (cá nhân, freelance, công ty) và làm trong thời gian nào.
3. Engine của RDS là PostgreSQL hay MySQL.
4. Pipeline CI/CD ở Galaxy FinX dùng Jenkins, ArgoCD, GitHub Actions hay GitLab CI.
5. Bạn có dùng Java/Spring Boot trong dự án thực tế nào không (kể cả dự án học tập hay side project).
6. Trong môi trường Docker local có các image tên `account-migration-*/migration-controller`, `migration-worker`, `ams/outbox-publisher`, `ams/retry-scheduler`, `ams/job-reconciler`... Nếu đó là kiến trúc của hệ thống account migration thật, có thể bổ sung chi tiết (mô hình controller/worker, outbox pattern, retry và reconciliation) vào bullet. Tôi **chưa** đưa vào vì CV gốc không nói tới.
