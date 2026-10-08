# Role Matching

**Profile Match** là đánh giá định tính của người review dựa trên bằng chứng trong CV gốc. Đây **không phải** điểm ATS thật, vì điểm ATS phụ thuộc vào từng job description cụ thể.

Thang đánh giá: **Rất cao** > **Cao** > **Khá** > **Trung bình** > **Thấp**

## Tổng quan

| Target Position | File | Relevant Experience | Strongest Skills | Missing Skills | Profile Match |
|---|---|---|---|---|---|
| Core Banking / FinTech Backend *(bổ sung)* | `fintech-backend` | Galaxy FinX (toàn bộ), VNPAY Cloud (fintech), EsolLabs (transaction integrity) | Thought Machine Vault Core, lending/overdraft logic, simulation testing, Golang, AWS | Payments/card/ISO 8583, reconciliation, PCI-DSS, Java (nhiều core banking dùng Java) | **Rất cao** |
| Backend Engineer | `backend-engineer` | Galaxy (business logic, migration, integration), Vietlink (OpenSearch migration), VNPAY (gateway, IAM), DattingQ | Golang, Python, gRPC, Kafka, MongoDB, Redis, AWS, số liệu hiệu năng | System design có quy mô traffic công khai (ngoài DattingQ), testing strategy, REST API design có mô tả cụ thể | **Cao** |
| Software Engineer | `software-engineer` | Toàn bộ, nhấn mạnh sự đa dạng và ownership end-to-end | Rộng: backend, data, cloud, CI/CD, domain banking | Frontend (nếu JD yêu cầu full-stack), mô tả về code review/mentoring | **Cao** |
| Golang Backend Developer | `golang-backend` | Galaxy (2 hệ thống Go có số liệu), DattingQ (gRPC-Gateway) | Golang, gRPC, Kafka, Redis, MongoDB, AWS ECS/Lambda | Kinh nghiệm Go chỉ được xác nhận rõ từ 03/2026; thiếu nói về concurrency patterns, profiling (pprof), testing trong Go | **Cao** |
| Platform Engineer | `platform-engineer` | VNPAY (50+ cluster, Kong, Keycloak), Galaxy (test tooling, CI/CD), Vietlink (IaC) | Kubernetes, Cluster API, OpenStack, Terraform, internal tooling | Internal developer platform (Backstage), GitOps có bằng chứng, Helm/Operators, SLO | **Cao** |
| DevOps Engineer | `devops-engineer` | VNPAY (vận hành K8s, automation 80%), Galaxy (EKS + CI/CD), Vietlink (Terraform, monitoring) | Kubernetes, Terraform, AWS, observability, tự động hoá | Jenkins/ArgoCD chưa có bullet cụ thể, Helm, Ansible, Linux/networking, scripting (Bash) | **Khá – Cao** |
| Cloud Engineer | `cloud-engineer` | Galaxy (EKS/RDS/ECR/ELB, ECS/Lambda), Vietlink (serverless ETL), VNPAY (OpenStack) | AWS breadth, OpenStack private cloud, multi-tenancy, IaC | AWS networking (VPC, IAM policies), cost optimization, AWS Associate/Professional cert, GCP/Azure | **Khá** |
| Data Engineer | `data-engineer` | Vietlink (ETL, +150%, OpenSearch), Galaxy (account migration), EsolLabs (ingestion) | ETL trên AWS (S3, Athena, Lambda, ECS), batch, migration, Kafka | Spark, Airflow/orchestration, dbt, data warehouse, data modeling, streaming processing (Flink/Kafka Streams) | **Khá** |
| Python Backend Developer | `python-backend` | Galaxy (Python Smart Contracts), MeetQ | Python cho logic tài chính, backend tổng quát | Python web framework có bằng chứng (FastAPI/Django), ORM, async Python, pytest | **Trung bình** |
| Java Backend Developer | `java-backend` | Kinh nghiệm backend chuyển giao được: logic giao dịch, microservices, IAM, Kafka, RDBMS | Kiến thức domain ngân hàng, microservices ở quy mô 100+ service | **Java/Spring Boot trong production**, JPA/Hibernate, Maven/Gradle, JUnit | **Thấp – Trung bình** |

## Ghi chú theo từng vị trí

### Core Banking / FinTech Backend: nên ưu tiên ứng tuyển
- Kinh nghiệm Thought Machine Vault Core rất hiếm trên thị trường. Các ngân hàng và đơn vị tích hợp dùng Vault Core (Vikki, các ngân hàng số trong khu vực, đối tác SI của Thought Machine) sẽ đánh giá cao.
- Cần bổ sung: số lượng sản phẩm hoặc tham số đã cấu hình, số test scenario, quy mô số tài khoản đã migrate (nếu được phép công bố).

### Backend Engineer / Software Engineer
- Điểm mạnh: mỗi công ty đều có ít nhất một kết quả đo được.
- Cần bổ sung: một bullet về thiết kế API hoặc data model cụ thể; quy mô (số request, số bản ghi, số tài khoản) của account migration và ETL.

### Golang Backend Developer
- Hai hệ thống Go ở Galaxy có số liệu rất tốt. Nếu xác nhận được DattingQ viết bằng Go, nên ghi "Golang" thẳng vào bullet đó.
- Cần bổ sung: cách xử lý concurrency trong migration system (worker pool, batching...), nhưng chỉ khi đúng với thực tế.

### DevOps / Cloud / Platform
- VNPAY là điểm mạnh nhất (50+ cluster, zero-downtime upgrades, 80% automation).
- Cần bổ sung: công cụ CI/CD thực tế đã dùng ở Galaxy, có dùng Helm/ArgoCD trong VNPAY không, và các chỉ số như deployment frequency, MTTR, thời gian provision cluster.
- Nên thi **AWS Solutions Architect – Associate** hoặc **CKA/CKAD** để đẩy các bản Cloud/DevOps/Platform lên mức "Cao".

### Data Engineer
- Kinh nghiệm thật khoảng 11 tháng ở Vietlink, cộng thêm migration và ingestion. Đủ cho vị trí Data Engineer mid-level thiên về AWS, chưa đủ cho JD yêu cầu Spark/Airflow.
- Cần bổ sung: khối lượng dữ liệu (GB/TB mỗi ngày, số bản ghi), tần suất batch, công cụ orchestration thực tế (Step Functions? EventBridge?) nếu có.
- Nên làm thêm một side project dùng Airflow + Spark/dbt để lấp khoảng trống.

### Python Backend Developer
- Python chỉ được xác nhận qua Vault Core Smart Contracts. Đây là Python thật nhưng không phải web backend.
- Nếu pipeline ở Vietlink hoặc MeetQ viết bằng Python, hãy cập nhật bullet: mức match sẽ lên **Khá – Cao**.
- Nên làm thêm một dự án FastAPI có test, async và SQLAlchemy, đưa lên GitHub.

### Java Backend Developer
- CV **không** gán kinh nghiệm Go/Python thành Java. Summary ghi rõ production stack là Golang/Python.
- Bản này hợp nhất với: ngân hàng hoặc công ty fintech chấp nhận ứng viên chuyển stack, hoặc vị trí ghi "Java **or** Go".
- Để cải thiện: xây một service Spring Boot (Spring Data JPA, Spring Security + Keycloak, Kafka, Testcontainers), đưa vào Selected Projects với link GitHub.

## Cải thiện chung cho mọi phiên bản

1. **Hiện lại mục Freelance (09/2023–03/2024)** nếu có thể chứng minh, để lấp khoảng trống và có thể ghi "3+ years".
2. Thêm **địa điểm** (ví dụ "Ho Chi Minh City, Vietnam") và **ngôn ngữ** (mức tiếng Anh; tiếng Nhật nếu có, vì Vietlink thuộc KDDI Agile Development Center Group) vào header: thêm biến trong khối PERSONAL INFORMATION và dòng liên hệ trong `\cvheader` của template, mọi bản sẽ tự cập nhật.
3. Thêm **năm tốt nghiệp** HCMUS.
4. Thêm **GitHub** nếu có code công khai (đặc biệt quan trọng cho các bản Java/Python).
5. Thêm **thời gian** cho DattingQ và MeetQ.
6. Mỗi lần ứng tuyển, đối chiếu JD và đổi thứ tự skills hoặc 1–2 bullet theo đúng keyword trong JD, nhưng **chỉ dùng keyword mà bạn thực sự có**.
