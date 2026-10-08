# Experience Inventory

Danh mục **toàn bộ** nội dung đã được xác nhận trong CV gốc (`original/original_cv.tex` = `main.tex`). Đây là nguồn sự thật duy nhất cho 10 CV.

Mỗi sự kiện có ID dạng `<Fact><aspect>`, ví dụ `V1b` = Vietlink, ETL pipelines, dùng AWS Lambda. Mỗi bullet trong `latex/*.tex` được gắn ID bằng comment LaTeX (ví dụ `% @V1abg !A14`), nên `scripts/coverage-report.py` tính được chính xác CV nào giữ, mở rộng hay bỏ sự kiện nào.

- `@…` = sự kiện từ inventory này.
- `!A…` = diễn giải cần bạn xác nhận (xem `review-needed.md`, Phần A).

---

## Galaxy FinX (Vikki Digital Bank): Middle Software Engineer, Core Banking, 03/2026 – Present
Bối cảnh: core banking platform của Vikki Digital Bank, xây trên Thought Machine Vault Core.

| ID | Sự kiện | Aspects |
|---|---|---|
| **G1** | Developed and maintained Lending and Overdraft products on Vault Core using Python Smart Contracts | a Lending · b Overdraft · c interest accrual · d penalty & late-fee calculation · e repayment · f settlement · g Python Smart Contracts · h ongoing maintenance |
| **G2** | Rebuilt the simulation testing framework entirely in Golang | a Golang rewrite · b replaced legacy Gauge-based framework · c 24 min → just over 50 s (**20x**) |
| **G3** | Deployed a new Vault Core version on AWS and built its CI/CD | a new Vault Core version deployed · b EKS · c RDS · d ECR · e ELB · f CI/CD pipeline (automated build, test, deploy) |
| **G4** | Built an account migration system | a Golang · b AWS ECS · c AWS Lambda · d AWS RDS · e 2.5 h → 27 min (**5x**) |
| **G5** | Integrated Vault Core with external backend services | a external backend services · b core banking operations · c transaction workflows |

## Vietlink (KDDI Agile Development Center Group): Software Engineer, 04/2025 – 03/2026
Bối cảnh: au Denki (auでんき), large-scale electric utility platform serving millions of users.

| ID | Sự kiện | Aspects |
|---|---|---|
| **V1** | Designed, developed, and operated ETL data pipelines on AWS | a design/develop/operate · b Lambda · c ECS · d RDS · e S3 · f Athena · g transforming & processing large-scale utility data · h downstream analytics · i operational workloads |
| **V2** | Optimized batch-oriented data processing workflows | a batch-oriented workflows · b pipeline redesign · c parallel execution · d more efficient data access patterns · e throughput **+150%** |
| **V3** | Migrated the search and analytics platform from Elasticsearch to OpenSearch | a migration · b redesigned data ingestion flows · c redesigned indexing flows · d stability · e consistency · f query performance |
| **V4** | Built and maintained data-platform infrastructure and monitoring | a Terraform · b AWS SAM · c build & maintain data-platform infra · d CloudWatch · e DataDog · f pipeline health · g failures · h operational anomaly detection |

## VNPAY: Software Engineer, 04/2024 – 04/2025
Bối cảnh: VNPAY Cloud, cloud platform for fintech and enterprise customers.

| ID | Sự kiện | Aspects |
|---|---|---|
| **P1** | Designed and operated a private cloud platform | a design & operate · b OpenStack · c Cluster API · d automated provisioning · e scaling · f zero-downtime upgrades · g **50+** production Kubernetes clusters |
| **P2** | Implemented multi-tenant authentication and authorization | a authentication · b authorization · c Keycloak · d RBAC · e tenant isolation · f **20+** customer organizations |
| **P3** | Integrated and operated Kong Gateway | a Kong integrated & operated · b microservices ecosystem of **100+** services · c service-level access control · d network-level access control |
| **P4** | Automated data center provisioning | a about **80%** of DC provisioning · b infrastructure configuration processes · c reduced manual operational effort |

## EsolLabs: Blockchain Developer, 06/2023 – 09/2023
Bối cảnh: Innovaz Market Factory, cross-chain NFT and token platform.

| ID | Sự kiện | Aspects |
|---|---|---|
| **E1** | Developed and reviewed smart contracts | a **15+** contracts developed · b code review · c DeFi · d NFT · e Solidity · f Move |
| **E2** | Built event-driven backend services | a event-driven · b capture · c process · d synchronize on-chain events · e off-chain databases · f APIs |
| **E3** | Integrated backend services with multiple chains | a **5+** networks · b Ethereum · c BSC · d Polygon · e Aptos · f Sui · g consistent transaction handling · h data integrity |

## Selected Projects (không có ngày tháng trong CV gốc)

| ID | Sự kiện | Aspects |
|---|---|---|
| **D1** | DattingQ (dating platform), Software Engineer: built the backend | a gRPC-Gateway · b Kafka · c MongoDB · d Redis · e up to **1.5K requests/second** · f **80–100 ms** API latency |
| **D2** | DattingQ: multi-cluster failover and observability | a multi-cluster failover · b OpenTelemetry · c Prometheus · d Grafana · e ELK · f ClickHouse · g **99.95%** uptime |
| **M1** | MeetQ (AI-powered online meeting platform), Software Engineer: real-time meeting platform | a LiveKit · b OpenAI models · c live transcription · d voice translation · e meeting summarization |
| **M2** | MeetQ: translation pipeline | a designed real-time translation pipeline · b optimized conversational context handling · c translation accuracy & coherence |

## Skills chỉ xuất hiện trong mục Skills của CV gốc (không có bullet kinh nghiệm)
Java, Spring Boot, FastAPI, PostgreSQL, RabbitMQ, Consul, HashiCorp Vault, Jenkins, ArgoCD, Postman, Git, Docker.
→ Được phép xuất hiện trong Technical Skills, **không** được viết thành thành tích.

## Học vấn và chứng chỉ
- University of Science, Ho Chi Minh City (HCMUS): B.Sc. Information Technology, Knowledge Engineering
- DevOps on AWS Specialization: Coursera

## Nội dung bị ẩn trong CV gốc (đang bị comment trong `main.tex`)
**Freelance: Blockchain Developer, 09/2023 – 03/2024**, gồm:
- Solidity smart contracts cho token, NFT, marketplace, on-chain transaction workflows
- Tích hợp contract với Web3 apps và backend: wallet connectivity, contract interactions, transaction handling, blockchain data sync
- APIs và off-chain components bằng Python và Node.js, làm việc với khách hàng từ khâu làm rõ yêu cầu đến testing và deployment

→ **Không đưa vào** 10 CV vì bạn đã chủ động ẩn mục này. Nếu muốn dùng, nó lấp được khoảng trống 09/2023–04/2024, đưa tổng kinh nghiệm lên "3+ years", và là bằng chứng cho Python/Node.js. Xem `review-needed.md`, mục C.
