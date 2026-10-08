# Skills Audit (v3 → v4)

Nguyên tắc áp dụng cho Technical Skills của bản v4:
1. **Chỉ giữ skill có giá trị rõ ràng với vị trí.** Work Experience là nơi chứng minh kinh nghiệm; Skills chỉ tóm tắt những năng lực quan trọng nhất.
2. **Tách technology khỏi domain và responsibility.** Các mục như "interest accrual", "repayment", "ETL pipeline design", "parallel processing", "multi-tenancy", "event-driven services", "automated simulation testing" không còn nằm trong Skills mà được mô tả trong Work Experience.
3. **Không lặp lại.** Không để PostgreSQL và Amazon RDS cùng xuất hiện, không ghi EKS trong cả nhóm Kubernetes lẫn nhóm AWS, không ghi REST ở nhiều nhóm.
4. **Không liệt kê skill chưa có bằng chứng** nếu nó không quan trọng với vị trí. Ví dụ RabbitMQ, Consul, HashiCorp Vault chỉ có trong danh sách Skills của CV gốc mà không có kinh nghiệm đi kèm, nên bị loại ở hầu hết các bản.
5. **Mục tiêu:** 4–6 nhóm, khoảng 12–20 mục, đọc xong trong vài giây.

## Tổng quan

| CV | v3 | v4 | Nhóm v4 |
|---|---|---|---|
| Backend Engineer | 31 mục / 6 nhóm | 20 / 5 | Languages · APIs · Databases & Messaging · Service Infrastructure · Observability |
| Cloud Engineer | 27 / 8 | 19 / 5 | Cloud Platforms · AWS Services · Kubernetes · IaC & Monitoring · Identity & Access |
| Data Engineer | 34 / 8 | 20 / 5 | Languages · Data Processing · AWS · Storage & Streaming · Infrastructure & Monitoring |
| DevOps Engineer | 36 / 7 | 20 / 6 | Containers & Orchestration · Cloud · IaC & CI/CD · Observability · Security & Networking · Scripting |
| FinTech Backend | 35 / 7 | 19 / 5 | Languages · Core Banking · Backend & Data · Cloud · Security |
| Golang Backend | 33 / 7 | 19 / 5 | Languages · Backend · Data & Messaging · Infrastructure · Observability |
| Java Backend | 33 / 7 | 17 / 5 | Languages · Frameworks & APIs · Data & Messaging · Security · Infrastructure |
| Platform Engineer | 34 / 7 | 20 / 6 | Kubernetes Platform · Platform Services · Infrastructure & Delivery · Cloud · Observability · Languages |
| Python Backend | 29 / 7 | 16 / 5 | Languages · Backend · Databases & Messaging · Cloud · Core Banking |
| Software Engineer | 34 / 6 | 20 / 5 | Languages · Backend · Data · Cloud & Infrastructure · Monitoring & Delivery |

## Chi tiết theo từng CV

### Data Engineer
**Giữ:** Python, SQL, Golang · ETL pipelines, batch processing, data migration · S3, Athena, Lambda, ECS, RDS · PostgreSQL, OpenSearch, Elasticsearch, ClickHouse, Kafka · Terraform, AWS SAM, CloudWatch, DataDog

| Bị loại | Lý do |
|---|---|
| data ingestion, data transformation, parallel processing, search indexing, "Elasticsearch to OpenSearch migration", "account data migration" | Đây là trách nhiệm, đã mô tả trong Vietlink và Galaxy |
| MongoDB, Redis | Chỉ dùng trong dự án backend DattingQ, không phải trọng tâm data |
| RabbitMQ | Chỉ có trong Skills gốc, không có kinh nghiệm |
| Docker, Kubernetes | Không quan trọng với hồ sơ Data Engineer này |
| Prometheus, Grafana, OpenTelemetry, ELK | Observability của dự án, không phải data tooling |

Ghi chú: "Data Processing" vẫn giữ ở mức khái niệm (ETL, batch, migration) vì đây là cách nhà tuyển dụng data lọc CV.

### DevOps Engineer
**Giữ:** Kubernetes, Cluster API, Docker · AWS (EKS, ECS, Lambda, RDS), OpenStack · Terraform, AWS SAM, Jenkins, ArgoCD · Prometheus, Grafana, CloudWatch, DataDog · Kong Gateway, Keycloak · Golang, Python

| Bị loại | Lý do |
|---|---|
| Amazon EKS và Amazon ECS ở nhóm Orchestration | Đã có trong nhóm Cloud |
| ECR, ELB, S3 | Dịch vụ phụ; vẫn được nêu trong Experience |
| "CI/CD pipeline design (build, test, deploy)" | Là trách nhiệm, đã có trong Experience |
| Git | Mặc định với mọi kỹ sư |
| OpenTelemetry, ELK | Giảm bớt số công cụ monitoring |
| HashiCorp Vault, Consul | Không có kinh nghiệm đi kèm |

⚠ Jenkins và ArgoCD được giữ vì CV gốc liệt kê và nhà tuyển dụng DevOps cần thấy tên công cụ CI/CD. Tuy vậy, Experience **chưa** ghi công cụ nào đã dùng cho pipeline ở Galaxy (xem review-needed B4).

### Cloud Engineer
**Giữ:** AWS, OpenStack · EKS, ECS, Lambda, RDS, S3, Athena, ELB · Kubernetes, Cluster API, Docker · Terraform, AWS SAM, CloudWatch, DataDog · Keycloak, RBAC, Kong Gateway

| Bị loại | Lý do |
|---|---|
| Cluster API ở nhóm Provisioning | Bị lặp |
| ECR | Dịch vụ phụ |
| "multi-tenant isolation", phần mô tả trong ngoặc của Kong | Là mô tả, đã có trong Experience |
| HashiCorp Vault, Consul | Không có kinh nghiệm đi kèm |
| Prometheus, Grafana, OpenTelemetry | Thuộc dự án; cloud monitoring giữ CloudWatch, DataDog |
| Golang, Python | Không phải trọng tâm của vị trí Cloud |

### Platform Engineer
**Giữ:** Kubernetes, Cluster API, OpenStack, Docker · Kong Gateway, Keycloak · Terraform, AWS SAM, Jenkins, ArgoCD · AWS (EKS, ECS, Lambda, RDS) · Prometheus, Grafana, CloudWatch, DataDog · Golang, Python

| Bị loại | Lý do |
|---|---|
| Amazon EKS ở nhóm Kubernetes | Bị lặp |
| Consul, HashiCorp Vault | Không có kinh nghiệm đi kèm |
| "Test frameworks in Golang", "CI/CD pipelines" | Là trách nhiệm, đã có trong Experience |
| Git, OpenTelemetry, ELK | Không cần thiết |
| ECR, ELB, S3, Athena | Dịch vụ phụ hoặc thuộc về data |

### Golang Backend Engineer
**Giữ:** Golang, Python, SQL · gRPC, gRPC-Gateway, REST APIs, Protocol Buffers · PostgreSQL, MongoDB, Redis, Kafka · Docker, Kubernetes, AWS (ECS, Lambda, RDS) · OpenTelemetry, Prometheus, Grafana

| Bị loại | Lý do |
|---|---|
| "concurrency (goroutines, channels)", "test frameworks" | Kiến thức mặc định của Go; concurrency chưa có bằng chứng trong Experience (review-needed B1/B2) |
| RabbitMQ | Không có kinh nghiệm đi kèm |
| Amazon RDS | Lặp với PostgreSQL |
| OpenSearch, ClickHouse | Không phải trọng tâm Go backend |
| Kong Gateway, Keycloak | Thuộc tầng platform; vẫn có trong Experience VNPAY |
| EKS, S3, ECR, ELB, ELK | Không cần thiết |
| "Python (Vault Core Smart Contracts)" | Rút gọn thành "Python" |

### Python Backend Engineer
**Giữ:** Python, SQL, Golang · FastAPI, REST APIs, gRPC · PostgreSQL, Redis, Kafka · AWS (Lambda, ECS, RDS, S3, Athena), Docker · Thought Machine Vault Core

| Bị loại | Lý do |
|---|---|
| Lending, overdraft, interest accrual, penalty and late fees, repayment, settlement, scheduled events | Là nghiệp vụ; đã mô tả sâu trong Galaxy FinX |
| Simulation testing, automated test frameworks | Là trách nhiệm |
| "Python 3", "Vault Core Smart Contracts" | Gộp thành Python + Thought Machine Vault Core |
| event-driven services, Keycloak | Không phải trọng tâm Python backend |
| MongoDB, OpenSearch, EKS | Không cần thiết |

⚠ FastAPI được giữ vì CV gốc liệt kê và đây là framework được tìm nhiều nhất cho Python backend, nhưng **chưa có** dự án FastAPI nào trong Experience (xem role-matching).

### Java Backend Engineer
**Giữ:** Golang, Python, SQL, Java (working knowledge) · Spring Boot (working knowledge), REST APIs, gRPC · PostgreSQL, Redis, MongoDB, Kafka · Keycloak, RBAC · Docker, Kubernetes, AWS, CI/CD

| Thay đổi / bị loại | Lý do |
|---|---|
| Java chuyển từ vị trí đầu xuống sau các ngôn ngữ production, kèm "(working knowledge)" | Tránh khiến người đọc nghĩ đã làm Java production |
| microservices, API gateway, event-driven services, authentication and authorization, multi-tenancy | Là khái niệm, đã có trong Experience |
| Automated simulation testing, Jenkins, Git | Là trách nhiệm hoặc công cụ không cần thiết |
| Amazon RDS, OpenSearch, RabbitMQ | Lặp hoặc chưa có bằng chứng |
| Danh sách dịch vụ AWS | Rút gọn thành "AWS" |

### FinTech Backend Engineer
**Giữ:** Python, Golang, SQL · Thought Machine Vault Core, Python Smart Contracts · gRPC, REST APIs, PostgreSQL, Redis, Kafka · AWS (EKS, ECS, Lambda, RDS), Kubernetes, Docker · Keycloak, RBAC, Kong Gateway

| Bị loại | Lý do |
|---|---|
| Nhóm "Banking Products" (lending, overdraft, interest accrual…) | Là nghiệp vụ; đã mô tả trong Galaxy |
| "product simulation testing" | Là trách nhiệm |
| Nhóm "DeFi" (Solidity, Move, Ethereum, BSC, Polygon, Aptos, Sui) | Kinh nghiệm blockchain vẫn có trong EsolLabs; không cần thành skill |
| Amazon RDS, HashiCorp Vault, ECR, ELB | Lặp hoặc chưa có bằng chứng |

### Backend Engineer
**Giữ:** Golang, Python, SQL · gRPC, gRPC-Gateway, REST, FastAPI · PostgreSQL, MongoDB, Redis, OpenSearch, Kafka · Kong Gateway, Keycloak, Docker, Kubernetes, AWS · OpenTelemetry, Prometheus, Grafana

| Bị loại | Lý do |
|---|---|
| Protocol Buffers | Đã ngầm hiểu qua gRPC |
| Amazon RDS | Lặp với PostgreSQL |
| Elasticsearch | Giữ OpenSearch, hệ thống hiện tại; quá trình migration có trong Experience |
| ClickHouse | Chỉ dùng trong observability của dự án |
| RabbitMQ | Không có kinh nghiệm đi kèm |
| "event-driven services" | Là khái niệm |
| ELK, CloudWatch, DataDog | Giảm số công cụ monitoring |
| Danh sách dịch vụ AWS | Rút gọn thành "AWS" |

### Software Engineer
**Giữ:** Golang, Python, SQL, Java · gRPC, REST APIs, Kafka, PostgreSQL, Redis · ETL pipelines, OpenSearch · AWS, OpenStack, Kubernetes, Docker, Terraform · Prometheus, Grafana, CloudWatch, CI/CD

| Bị loại | Lý do |
|---|---|
| Solidity, Move | Không liên quan đến vị trí; blockchain vẫn có trong EsolLabs |
| Nhóm "Domain" (core banking, utilities data, fintech cloud, blockchain) | Đã thể hiện qua các công ty |
| microservices, event-driven services | Là khái niệm |
| MongoDB, ClickHouse, Amazon Athena, Cluster API, OpenTelemetry, DataDog | Rút gọn để bản tổng quát dễ đọc |

## Skill chỉ có trong danh sách Skills của CV gốc (không có kinh nghiệm đi kèm)

| Skill | v4 |
|---|---|
| Java, Spring Boot | Chỉ có ở bản Java (ghi "working knowledge") và bản Software (Java) |
| FastAPI | Bản Python và Backend |
| Jenkins, ArgoCD | Bản DevOps và Platform |
| PostgreSQL | Nhiều bản. Experience ghi "RDS"; engine chưa xác nhận (review-needed) |
| RabbitMQ, Consul, HashiCorp Vault, Postman, Git | **Đã bỏ khỏi mọi bản** |
