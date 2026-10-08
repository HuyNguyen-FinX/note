# Resume Content Review (v3 → v4)

Mục tiêu của v4: biên tập lại cả 10 CV cho **tự nhiên, chọn lọc và thực tế hơn**, thay vì thêm nội dung.
Thứ tự ưu tiên: Natural English > Technical Credibility > Relevant Skills > Meaningful Experience > Visual Consistency.

Bản v3 được giữ nguyên trong `archive/v3-2026-10-08/` (gồm `latex/`, `pdf/`, `templates/`) để so sánh.

---

## Phase 1: Content Audit (bản v3)

| Vấn đề | Mức độ ở v3 |
|---|---|
| Summary quá dài | 73–106 từ, 3–5 câu; cố nhắc mọi công ty, công nghệ và metric |
| Technical Skills quá nhiều | 27–36 mục trong 6–8 nhóm |
| Skill là nghiệp vụ hoặc trách nhiệm | "interest accrual, repayment, settlement, scheduled events", "ETL pipeline design", "parallel processing", "multi-tenancy", "automated simulation testing", "event-driven services" |
| Skill lặp | PostgreSQL + Amazon RDS; EKS ở cả nhóm Kubernetes lẫn AWS; REST/JSON ở nhiều nhóm; Cluster API ở 2 nhóm |
| Skill không liên quan | Solidity, Move và danh sách chain ở bản Software/FinTech; RabbitMQ, Kubernetes, Prometheus… ở bản Data |
| Skill không có bằng chứng | RabbitMQ, Consul, HashiCorp Vault, Git, Postman |
| Bullet tách vụn, trùng ý | Ví dụ ở bản Golang, account migration bị tách thành 3 bullet: "Designed and built…", "Deployed the migration processing on AWS…", "Reduced…". CI/CD tách thành "Built the CI/CD pipeline" và "Automated build, test, deployment" |
| Subsection không cần thiết | 9/10 bản chia nhóm bullet (ví dụ "Data Pipeline Architecture", "Batch Processing Optimization"), làm nội dung bị chia vụn |
| Câu gượng hoặc giống AI viết | "Consistently turns bottlenecks into measured wins"; "Platform engineer who builds the shared foundations other engineers ship on"; "Moved account data faster: built…"; "Gave the platform CloudWatch and DataDog monitoring…"; "Took about 80% of data center provisioning … off manual processes"; "Kept the services deployable and observable"; "Worked inside a 100+ service microservices ecosystem…"; "Secured tenant boundaries…"; "Ran the platform's Kubernetes runtime"; "Turned cluster creation into a platform capability"; "Delivered multi-tenant identity as a platform service"; "Made transaction handling consistent across every chain"; "Carried the search platform through its move…" |

## Phase 2: Rewrite

### 1. Professional Summary
Mọi summary được viết lại: 40–51 từ, tối đa 3 câu, không dùng marketing phrase, không cố nhắc mọi công ty hay metric.

| CV | Summary v4 |
|---|---|
| Data | Data Engineer with hands-on experience building and operating ETL pipelines on AWS. Worked on ingestion, transformation, and batch processing for a large-scale utility platform using Lambda, ECS, S3, Athena, and RDS, and migrated its search workloads to OpenSearch. Currently builds account data migration tooling for a core banking platform. |
| DevOps | DevOps Engineer focused on Kubernetes operations, infrastructure automation, and CI/CD. Operated an OpenStack private cloud with 50+ production Kubernetes clusters at VNPAY, and most recently deployed a core banking platform on AWS EKS and built its delivery pipeline. Works mainly with Terraform, AWS, and production monitoring. |
| Cloud | Cloud Engineer with experience on both AWS and OpenStack. Designed and operated VNPAY Cloud's private cloud, which runs 50+ production Kubernetes clusters for fintech and enterprise customers. On AWS, has deployed core banking and data workloads on EKS, ECS, Lambda, RDS, S3, and Athena, with infrastructure managed in Terraform. |
| Platform | Platform Engineer working on Kubernetes platforms, shared services, and internal tooling. At VNPAY Cloud, built and operated a multi-tenant Kubernetes platform on OpenStack and Cluster API, together with its API gateway and identity services. At a digital bank, built the testing framework and AWS delivery pipeline for the core banking platform. |
| Golang | Backend engineer working mainly in Golang. Built an account migration system and a simulation testing framework for a core banking platform, and has developed gRPC services backed by Kafka, MongoDB, and Redis. Interested in performance, reliability, and clean service design. |
| Python | Python Backend Engineer working on core banking at Vikki Digital Bank, developing the Lending and Overdraft products as Python Smart Contracts on Thought Machine Vault Core. Previously built ETL pipelines on AWS for a large-scale utility platform. Most of the work involves financial logic, data processing, and backend integrations. |
| Java | Backend engineer with production experience in Golang and Python and working knowledge of Java and Spring Boot. Has worked on core banking transaction logic, service integrations, multi-tenant authentication, and microservices behind an API gateway, all of which carry over to Spring-based backends. |
| FinTech | Backend engineer at Vikki Digital Bank, working on the Lending and Overdraft products built on Thought Machine Vault Core. Experience covers interest and fee calculation, repayment and settlement, account migration, and integration with surrounding banking systems. Previously worked on multi-tenant security for VNPAY's fintech cloud platform. |
| Backend | Backend Engineer working with Golang and Python on financial and data-heavy systems. Currently builds core banking features at Vikki Digital Bank, including lending and overdraft logic, account migration, and integrations with external services. Most interested in service design, data consistency, and performance. |
| Software | Software Engineer with experience across backend development, data pipelines, and cloud infrastructure. Currently works on core banking at Vikki Digital Bank. Before that, built ETL pipelines on AWS for KDDI's au Denki platform and operated a private Kubernetes cloud at VNPAY. |

Ghi chú về độ trung thực: summary bản Data **không** ghi Python là ngôn ngữ của các pipeline, vì CV gốc chưa xác nhận (review-needed B5). Python chỉ xuất hiện trong Skills.

### 2. Technical Skills
Mỗi bản còn 4–6 nhóm, 16–20 mục, chỉ gồm technology. Chi tiết từng skill bị loại và lý do nằm trong `skills-audit.md`.

### 3. Work Experience
- **Gộp bullet trùng ý:** mỗi deliverable thành 1 bullet "làm gì, bằng gì, kết quả gì". Ví dụ account migration (hệ thống + nơi chạy + kết quả) giờ là 1 bullet; deploy + CI/CD gộp hoặc tách tuỳ vị trí.
- **Chỉ tách khi là thành tích độc lập:** ví dụ tính lãi/phí và repayment/settlement (bản FinTech, Python, Backend, Java); zero-downtime upgrade và provisioning (bản DevOps, Cloud); IaC và monitoring (bản Cloud, Data).
- **Bỏ toàn bộ subsection** (`\cvgroup`). Với 5–8 bullet mỗi công ty, danh sách liền mạch dễ đọc hơn.
- **Số bullet Work Experience mỗi CV:** v3 có 21–29, v4 có 12–19 (Software ít nhất với 12, vì là bản tổng quát). Không bullet nào bị bỏ chỉ để tiết kiệm chỗ; phần giảm đến từ việc gộp ý trùng.
- **Viết lại câu gượng** bằng động từ đơn giản (Built, Developed, Implemented, Migrated, Improved, Automated, Integrated, Operated). Không còn các cụm đã liệt kê ở Phase 1 (đã grep kiểm tra).
- **Phân bổ theo vị trí vẫn giữ:** Data lấy Vietlink làm chính (7 bullet); DevOps, Cloud, Platform lấy VNPAY (5–6); Golang, Python, Java, FinTech, Backend lấy Galaxy (5–8); Software cân bằng.

### 4. Layout
- **Font:** 10pt lên **10.5pt**, leading 13pt. Lề 1.55 cm lên **1.8 cm**. Tăng khoảng cách giữa bullet và section. Phần dư nhờ summary và skills ngắn hơn được dùng cho độ dễ đọc, không dùng để nhồi nội dung.
- **Lỗi template đã sửa:** `\needspace` (bản xấp xỉ) báo thiếu chỗ sai khi dùng cùng `\raggedbottom`, đẩy cả khối công ty sang trang sau và để trống 10 dòng ở trang 1. Đã chuyển sang `\Needspace` (tính chính xác).
- **Học vấn:** tách tên trường và bằng thành 2 dòng; ở lề mới, 2 phần này bị dính chữ ("(HCMUS)B.Sc.").

## Phase 3: Review (Technical Hiring Manager)

Thang 1–5.

| CV | Natural English | Human tone | Role relevance | Skill relevance | Credibility | Depth | Concise | Readable | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| Data | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | Vietlink 7 bullet đọc như data engineer. Cần thêm orchestration và volume (B5, B9) |
| DevOps | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | Jenkins/ArgoCD chưa gắn với kinh nghiệm cụ thể (B4) |
| Cloud | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | Thiếu networking/IAM của AWS (chưa có bằng chứng) |
| Platform | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | Kể đúng góc nền tảng mà không dùng ngôn từ marketing |
| Golang | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | Galaxy có 5 bullet; chiều sâu Go phụ thuộc B1/B2 |
| Python | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | Python chỉ có ở Vault Core; FastAPI chưa có bằng chứng |
| Java | 5 | 5 | 3 | 4 | 5 | 3 | 5 | 5 | Trung thực về stack; vị trí phù hợp vẫn thấp nhất |
| FinTech | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | Mạnh nhất; trang 2 ngắn (EsolLabs + Projects + Education) |
| Backend | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | |
| Software | 5 | 5 | 4 | 5 | 5 | 3 | 5 | 5 | Ngắn và cân bằng; có gộp vài thành tích liên quan |

## Phase 4: Build

| Kiểm tra | Kết quả |
|---|---|
| Compile | 10/10, không có lỗi hay warning (`./scripts/build-all.sh`) |
| Số trang | 10/10 bản 2 trang. Trang 2 lấp 31–54% so với trang 1 |
| Ngắt trang | Không có section header hay header công ty nằm cuối trang; mọi chỗ ngắt đều rơi vào ranh giới công ty hoặc giữa các bullet (≥ 2 bullet mỗi bên) |
| Dòng cuối chỉ có 1 chữ | 0 |
| Text extraction | Không ligature, không ngắt từ bằng gạch nối; đủ tên, liên hệ, học vấn, 4 công ty, chức danh chính thức, ngày tháng |
| Metric | Không có con số nào ngoài các metric gốc |
| Câu gượng của v3 | 0 (đã grep) |

## Đánh đổi cần biết

1. **Mức khác biệt giữa các CV giảm từ 81% (v3) xuống 73%** (thấp nhất 54%, DevOps vs Platform). Khi viết bằng câu đơn giản, cùng một sự kiện (ví dụ "automated about 80% of data center provisioning") chỉ có vài cách diễn đạt tự nhiên. Tôi đã viết lại các bullet ở công ty supporting theo trọng tâm từng vị trí, nhưng không ép câu chữ khác nhau bằng cách nói gượng. Sự khác biệt chính giờ nằm ở: công ty nào là trọng tâm, số bullet, bullet nào được giữ, summary và skills.
2. **CV ngắn hơn (khoảng 1,3–1,5 trang nội dung).** Đây là hệ quả của việc gộp bullet trùng ý, không phải do cắt thành tích (coverage vẫn 18–20/20 sự kiện, 11–12/12 metric). Tôi không thêm bullet để kéo dài.
3. **MeetQ bị bỏ ở bản DevOps, Cloud, Platform, FinTech** vì không liên quan. Đây là thay đổi có chủ đích, đã ghi trong `experience-coverage-report.md`.
