# Review Needed: chi tiết kỹ thuật cần bạn xác minh

Nguyên tắc tôi đã áp dụng khi viết lại 10 CV:

| Loại | Ví dụ | Xử lý |
|---|---|---|
| **Sự kiện có trong CV gốc** | "2.5 hours → 27 minutes", "Kong Gateway for 100+ services" | Dùng tự do, diễn đạt lại theo từng vị trí |
| **Cơ chế vốn có của công nghệ đã nêu** (không thể làm khác đi) | Athena truy vấn dữ liệu trên S3; Cluster API nâng cấp bằng cách thay node lần lượt (rolling) | **Đã đưa vào CV.** Liệt kê ở Phần A để bạn kiểm tra |
| **Lựa chọn thiết kế, số liệu, công cụ chưa được xác nhận** | worker pool, idempotency, Step Functions, Helm | **Chưa đưa vào CV.** Liệt kê ở Phần B kèm bullet viết sẵn |

Cách dùng: đánh dấu `[x]` vào mục bạn xác nhận đúng, gửi lại cho tôi (hoặc tự dán bullet vào file `.tex` tương ứng), rồi chạy `./scripts/build-all.sh`.

---

## Phần A: Đã có trong CV, cần bạn xác nhận lại

Đây là các mô tả suy ra từ cách nền tảng vận hành, không phải từ câu chữ CV gốc. Nếu mục nào sai, hãy báo để tôi gỡ ra.

| # | Mô tả trong CV | File | Cơ sở |
|---|---|---|---|
| A1 | Interest accrual/penalty "driven by Vault Core's contract hooks and **scheduled events**" / "scheduled through Vault Core events" | python-backend, fintech-backend | Smart contract của Vault Core tính lãi định kỳ thông qua scheduled event hooks |
| A2 | "Vault Core, the bank's **core ledger**"; "wiring the core ledger into…" | python-backend, backend, golang | Vault Core là core banking ledger |
| A3 | Simulation testing framework dùng để kiểm thử **product/contract behaviour** của Vault Core ("product simulation testing", "contract behaviour is verified") | python-backend, fintech-backend, golang ("Vault Core simulation testing framework") | Simulation trong Vault Core là cơ chế chạy thử contract theo thời gian giả lập |
| A4 | Repayment/settlement là "the paths that move money and close out customer obligations"; "every calculation flows directly into customer balances" | fintech-backend, python-backend | Định nghĩa nghiệp vụ |
| A5 | Cluster API: "**declarative** provisioning, scaling, and **rolling** upgrades" | devops, cloud | Cluster API quản lý cluster theo kiểu khai báo và nâng cấp bằng cách thay machine lần lượt |
| A6 | Vietlink: Lambda = serverless, ECS = containerized batch jobs, S3 lưu dữ liệu, Athena truy vấn SQL trên S3, RDS là relational store | data, devops, cloud, golang | Vai trò mặc định của từng dịch vụ AWS |
| A7 | Vault Core trên AWS: EKS chạy platform, RDS là database, ECR chứa container images, ELB cân bằng tải | cloud, java | Vai trò mặc định của từng dịch vụ AWS |
| A8 | DattingQ: gRPC-Gateway "exposing **REST/JSON** endpoints generated from **Protocol Buffer** contracts" | golang, backend, java | gRPC-Gateway sinh reverse proxy REST từ file `.proto` |
| A9 | Kong Gateway "centralizing access control in one layer" / "shared API gateway" | platform, java | Bản chất của API gateway |
| A10 | VNPAY: clusters "for fintech and enterprise customers"; Keycloak isolating "20+ **fintech and enterprise** customer organizations" | devops, cloud, fintech | Ghép mô tả VNPAY Cloud ("for fintech and enterprise customers") với "20+ customer organizations" |
| A11 | Simulation framework "shortening the development feedback loop" | platform | Hệ quả trực tiếp của việc chạy test nhanh hơn 20x |
| A12 | Chức danh chức năng (functional title), ví dụ "Data Engineer (Software Engineer)", "Platform Engineer (Software Engineer)", "Middle Software Engineer – Cloud Infrastructure & Automation" | tất cả trừ software-engineer | Chức danh chính thức luôn hiện kèm. Hãy kiểm tra từng title có phản ánh đúng công việc của bạn không (bảng đầy đủ ở `cv-differentiation-report.md`) |
| A13 | Golang skills: "concurrency (goroutines, channels)" | golang | Kiến thức nền tảng của Go. Đây là **skill**, không phải thành tích |
| A14 | Vietlink: kết hợp Lambda và ECS "so each pipeline stage runs on the execution model that suits its workload" | data | Diễn giải lý do chọn serverless hay container cho từng stage. Hãy xác nhận mỗi stage có thực sự được chọn theo đặc điểm workload không |
| A15 | Vietlink: stage ingestion/transformation biến "raw utility data into structured, analytics-ready datasets" | data | Diễn giải từ "transforming and processing … for downstream analytics" |
| A16 | OpenSearch: "keeping indexed data consistent with its source" / "consistency of indexed data" | data, golang | Diễn giải từ "improve … consistency" |
| A17 | Terraform "keeping deployments of AWS data workloads consistent across releases" | data | Lợi ích vốn có của IaC |
| A18 | Account migration chạy "containerized workloads on ECS **with** serverless functions on Lambda", RDS là nơi lưu migration data | data, devops, cloud, golang | Ghép 3 dịch vụ trong CV gốc. **Chưa biết phần nào chạy trên ECS, phần nào trên Lambda** (xem B1) |
| A19 | Phân loại chain: EVM (Ethereum, BSC, Polygon) và Move-based (Aptos, Sui); Solidity cho EVM, Move cho Aptos/Sui | data, cloud, golang | Sự thật kỹ thuật về các chain |
| A20 | Vietlink: parallel execution "processing independent units of work concurrently to make better use of available compute" | data | Diễn giải "parallel execution". "Better use of compute" là hệ quả suy ra, **không có số đo** |
| A21 | Vietlink: data access patterns "so that reads and writes against S3 and RDS are more efficient per batch" | data | Giả định các truy cập dữ liệu nằm trên S3/RDS, vì đây là 2 nơi lưu dữ liệu duy nhất được nêu |
| A22 | DattingQ observability: "OpenTelemetry instrumentation, Prometheus and Grafana metrics, ELK logging" | devops | Vai trò mặc định của từng công cụ. Vai trò của ClickHouse không được nêu cụ thể |
| A23 | VNPAY RBAC "so that each tenant's users only reach their own organization's resources" | cloud | Định nghĩa của tenant isolation |

> Các mã A1–A23 được gắn ngay trên từng bullet trong `latex/*.tex` (comment `% … !A16`). Muốn gỡ một diễn giải, tìm mã đó trong file `.tex` và sửa lại câu tương ứng.

---

## Phần B: Đề xuất mở rộng, chưa đưa vào CV

Mỗi mục có bullet tiếng Anh viết sẵn. Chỉ đưa vào sau khi bạn xác nhận **đúng và có thể giải thích khi phỏng vấn**.

### B1. Account migration system (Galaxy FinX): ưu tiên cao

> **Bằng chứng gián tiếp:** Docker local có các image `account-migration-*/migration-controller`, `migration-worker`, `mock-core-api`, `ams/importer`, `ams/outbox-publisher`, `ams/retry-scheduler`, `ams/job-reconciler`, `ams/report-generator`, `ams/migration-api`. Nếu đây chính là hệ thống migration trong CV, đây là phần có thể nâng cấp CV mạnh nhất.

- [ ] **Kiến trúc controller/worker** (Golang, Data, Platform, Backend)
  `Designed the migration system as a controller/worker architecture in Golang: a controller on ECS partitions account batches and Lambda workers process them in parallel against RDS.`
  → Cần xác nhận: phần nào chạy trên ECS, phần nào trên Lambda; có chia batch không.
- [ ] **Outbox pattern + retry** (Backend, Golang, FinTech)
  `Used the transactional outbox pattern and a retry scheduler so migration events are published exactly once and transient core banking failures are retried safely.`
  → Cần xác nhận: có outbox thật không; đảm bảo "exactly once" hay "at least once + idempotent".
- [ ] **Reconciliation** (Data, FinTech)
  `Added a reconciliation job that compares migrated accounts against the source and reports mismatches before cut-over.`
  → Cần xác nhận: reconcile những gì (số dư, số lượng tài khoản, trạng thái).
- [ ] **Report generation** (Data, FinTech)
  `Generated per-run migration reports covering migrated, failed, and retried accounts for operations sign-off.`
- [ ] **Mock core API for testing** (Golang, Backend, Java)
  `Built a mock core banking API to test the migration pipeline end to end without touching the real core.`
- [ ] **Concurrency trong Go** (Golang)
  `Parallelized account processing with goroutine worker pools and bounded concurrency to stay within RDS and core API limits.`
- [ ] **Quy mô:** số lượng tài khoản mỗi lần migrate. Ví dụ "migrates N accounts in 27 minutes" sẽ rất mạnh.

### B2. Simulation testing framework (Galaxy FinX)
- [ ] `Ran simulation scenarios in parallel with goroutines`: nguyên nhân chính của mức tăng 20x có phải chạy song song không?
- [ ] Số lượng test scenario hoặc số sản phẩm được phủ (ví dụ "200+ scenarios across Lending and Overdraft").
- [ ] Framework có chạy trong CI/CD pipeline không? Nếu có: `Wired the framework into the CI/CD pipeline as a pre-deployment gate.`

### B3. Vault Core product logic (Galaxy FinX)
- [ ] Các hook cụ thể đã dùng (pre-posting validation, post-posting, scheduled events), để thêm vào bản Python/FinTech: `Validated postings in pre-posting hooks to block overdraft limit breaches.`
- [ ] Có xử lý **penalty interest** (lãi phạt) riêng hay chỉ là penalty fee?
- [ ] Có tham gia **product parameters/configuration** (lãi suất, kỳ hạn, hạn mức) không?
- [ ] Vault Core version (v4/v5)? Có dùng **Streaming API (Kafka)** của Vault Core để tích hợp không? Nếu có, đây là bằng chứng Kafka trong production cho bản Backend/Java/FinTech.

### B4. Vault Core deployment & CI/CD (Galaxy FinX)
- [ ] Công cụ CI/CD: Jenkins / GitHub Actions / GitLab CI / ArgoCD?
- [ ] Có dùng **Helm** hoặc Terraform cho EKS không?
- [ ] Chiến lược deploy (rolling, blue/green)?
  Bullet mẫu (DevOps): `Deployed Vault Core to EKS with Helm and Terraform, promoting releases through environments via a GitOps flow in ArgoCD.`

### B5. Vietlink ETL (Data Engineer, quan trọng nhất cho bản Data)
- [ ] **Ngôn ngữ** của Lambda/ECS jobs (Python?). Nếu là Python, nên ghi thẳng vào bản Data và Python Backend.
- [ ] **Orchestration:** Step Functions / EventBridge / cron?
  `Orchestrated pipeline stages with AWS Step Functions and EventBridge schedules.`
- [ ] **Định dạng và partitioning:** Parquet? Partition theo ngày/khu vực để Athena chạy nhanh hơn?
  `Partitioned S3 datasets by date and stored them as Parquet to cut Athena scan cost and query time.`
- [ ] **Data validation / data quality checks** có không?
- [ ] **Khối lượng dữ liệu:** GB/TB mỗi ngày, số bản ghi, tần suất batch.
- [ ] **SQL optimization** cụ thể trên RDS/Athena (index, rewrite query)?
- [ ] OpenSearch migration: có zero-downtime reindex hay dual-write không? Quy mô index?

### B6. VNPAY Cloud (DevOps / Cloud / Platform)
- [ ] Nền tảng có cung cấp **Kubernetes cluster cho khách hàng** (managed Kubernetes / Kubernetes-as-a-Service) không?
  `Delivered managed Kubernetes to fintech and enterprise tenants, provisioning isolated clusters on demand through Cluster API.`
- [ ] Tự động hoá data center bằng gì (Ansible, Terraform, scripts Go/Python)?
- [ ] Keycloak: realm-per-tenant hay một realm có nhiều group? Dùng OIDC/OAuth2 cho các service không?
- [ ] Kong: có plugin rate limiting, JWT/OIDC, mTLS không?
- [ ] Monitoring stack của VNPAY (Prometheus/Grafana?), các SLO hoặc chỉ số availability.
- [ ] Thời gian provision một cluster trước và sau khi tự động hoá.

### B7. DattingQ / MeetQ
- [ ] Backend DattingQ có viết bằng **Golang** không? gRPC-Gateway là thư viện Go nên khả năng cao là có. Nếu đúng, ghi "Golang" vào bullet của bản Golang/Backend.
- [ ] Vai trò của Redis (cache, session, rate limit?) và Kafka (event bus, feed, notification?).
- [ ] Chạy trên Kubernetes không? Multi-cluster failover dùng cơ chế gì?
- [ ] MeetQ viết bằng ngôn ngữ gì (Python/Go/Node.js)?
- [ ] Hai dự án làm trong thời gian nào; là dự án cá nhân, freelance hay của công ty?

### B9. Vietlink: chi tiết data engineering mà bản Data muốn có (chưa đưa vào CV)
- [ ] **Performance bottleneck investigation:** bạn có profile hoặc đo đạc để tìm nút thắt trước khi tối ưu không? Dùng công cụ gì?
  `Profiled the batch pipelines to locate I/O and serialization bottlenecks before redesigning them for parallel execution.`
- [ ] **Resource efficiency:** chi phí hoặc tài nguyên (vCPU, memory, Lambda duration) có giảm không? Có số liệu không?
- [ ] **Data modeling / SQL optimization:** có thiết kế schema trên RDS hoặc bảng Athena (partition, format) không?
- [ ] **Data validation:** có bước kiểm tra chất lượng dữ liệu (schema, null, duplicate) trong pipeline không?
- [ ] **Vai trò dẫn dắt:** bạn có **lead** việc migration OpenSearch hay redesign pipeline không? Nếu có, nên dùng "Led" thay cho "Migrated/Redesigned".

### B10. Galaxy FinX: financial data consistency (bản Data, FinTech)
- [ ] Hệ thống migration có **validation** trước khi ghi vào core không?
- [ ] Có **reconciliation** sau migration không (so số dư, số tài khoản)? Xem B1.
- [ ] Có **batching** và **retry** không? Xem B1.
  Bullet mẫu (Data): `Validated and reconciled migrated balances against source records, with batched processing and retries for failed accounts.`

### B8. Java
- [ ] Có dự án Java/Spring Boot nào (kể cả side project, đồ án) không? Nếu có, đưa vào Selected Projects của bản Java với link GitHub.
- [ ] Nếu chưa có: đề xuất xây 1 service Spring Boot 3 (Spring Data JPA + PostgreSQL, Spring Security + Keycloak, Kafka, Testcontainers) mô phỏng loan repayment. Sau đó bản Java sẽ có bằng chứng thật.

---

## Phần C: Thông tin cá nhân còn thiếu

- [ ] Địa điểm (ví dụ "Ho Chi Minh City, Vietnam")
- [ ] Năm tốt nghiệp HCMUS
- [ ] Trình độ tiếng Anh / tiếng Nhật
- [ ] GitHub
- [ ] Có muốn hiện lại mục Freelance (09/2023–03/2024) không. Nếu có, tổng kinh nghiệm sẽ thành "3+ years".
