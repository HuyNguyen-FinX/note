# Experience Coverage Report

Sinh tự động bởi `scripts/coverage-report.py` từ các tag trong `latex/*.tex`, đối chiếu với `analysis/experience-inventory.md`. Chạy lại script sau mỗi lần sửa CV.

- **Sự kiện** = 20 thành tích/trách nhiệm trong CV gốc (G1–G5, V1–V4, P1–P4, E1–E3, D1–D2, M1–M2).
- **Aspects** = các chi tiết bên trong mỗi sự kiện (công nghệ, số liệu, phạm vi).
- **Metric** = 12 con số đã xác nhận (5x, 20x, 150%, 50+, 20+, 100+, 80%, 15+, 5+, 1.5K, 80–100 ms, 99.95%).

## Tổng quan

| CV | Sự kiện | Aspects | Metric | Galaxy | Vietlink | VNPAY | EsolLabs | Projects |
|---|---|---|---|---|---|---|---|---|
| backend-engineer | 20/20 | 114/114 (100%) | 12/12 | 9 | 6 | 6 | 4 | 5 |
| cloud-engineer | 20/20 | 112/114 (98%) | 12/12 | 7 | 6 | 10 | 3 | 3 |
| data-engineer | 20/20 | 114/114 (100%) | 12/12 | 7 | 13 | 5 | 4 | 5 |
| devops-engineer | 20/20 | 112/114 (98%) | 12/12 | 7 | 7 | 11 | 3 | 4 |
| fintech-backend | 20/20 | 112/114 (98%) | 12/12 | 12 | 4 | 6 | 5 | 3 |
| golang-backend | 20/20 | 114/114 (100%) | 12/12 | 8 | 5 | 4 | 4 | 6 |
| java-backend | 20/20 | 113/114 (99%) | 12/12 | 9 | 5 | 6 | 3 | 4 |
| platform-engineer | 20/20 | 112/114 (98%) | 12/12 | 7 | 6 | 10 | 3 | 3 |
| python-backend | 20/20 | 114/114 (100%) | 12/12 | 10 | 5 | 5 | 3 | 5 |
| software-engineer | 20/20 | 114/114 (100%) | 12/12 | 9 | 6 | 6 | 3 | 5 |

## Nội dung không đưa vào CV nào
- **Freelance Blockchain Developer (09/2023 – 03/2024):** bạn đang comment trong `main.tex`, nên tôi tôn trọng quyết định ẩn mục này. Xem `review-needed.md`, mục C.
- **Skills chỉ có trong danh sách Skills** (Java, Spring Boot, FastAPI, RabbitMQ, Jenkins, ArgoCD, Consul, HashiCorp Vault, Postman): chỉ xuất hiện trong Technical Skills của các bản liên quan, không viết thành thành tích.
- **Postman:** bỏ khỏi mọi bản vì không thêm giá trị cho các vị trí mục tiêu.

## Chi tiết mới cần xác minh
- **Phần A** của `review-needed.md`: các diễn giải **đã có** trong CV, được đánh dấu `!A…` ở từng bullet. Số lần dùng của từng mã nằm trong bảng chi tiết bên dưới.
- **Phần B**: các chi tiết **chưa** đưa vào CV (worker/concurrency trong migration, outbox/retry/reconciliation, orchestration ETL, data volume, Helm/ArgoCD...).

## Chi tiết theo từng CV

### backend-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / Vietlink + VNPAY / EsolLabs |
| Bullet theo công ty | Galaxy 9 · Vietlink 6 · VNPAY 6 · EsolLabs 4 · Projects 5 |
| Sự kiện giữ lại | 20/20 sự kiện, 114/114 aspects (100%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D1×2, E3×2, G1×3, G2×2, G4×2, P2×2, P3×2, V3×2, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A2×1, A8×1 |

**Mở rộng:** Galaxy chia Integration & Transaction Logic / Migration Backend / Testing & Deployment. VNPAY tách gateway, access control, authentication, authorization. Vietlink tách V3 thành migration + ingestion/indexing, V4 thành IaC + monitoring.

**Không đưa vào và lý do:** Không bỏ sự kiện nào.

### cloud-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | VNPAY / Galaxy FinX + Vietlink / EsolLabs |
| Bullet theo công ty | Galaxy 7 · Vietlink 6 · VNPAY 10 · EsolLabs 3 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 112/114 aspects (98%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G3×3, P1×5, P2×2, P3×2, V1×2, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A5×3, A6×1, A7×1, A9×1, A10×1, A18×1, A19×1, A23×1 |

**Mở rộng:** VNPAY kể theo kiến trúc private cloud: P1 tách 5 bullet, P2 tách tenant isolation + RBAC, P3 tách gateway + chính sách truy cập. Galaxy G3 kể theo vai trò từng dịch vụ AWS. Vietlink V1 tách serverless/container và storage/query.

**Không đưa vào và lý do:** MeetQ chỉ giữ 1 bullet (M2b, M2c).

Aspects chưa xuất hiện: M2 MeetQ translation pipeline: context handling, accuracy & coherence

### data-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | Vietlink / Galaxy FinX / VNPAY, EsolLabs |
| Bullet theo công ty | Galaxy 7 · Vietlink 13 · VNPAY 5 · EsolLabs 4 · Projects 5 |
| Sự kiện giữ lại | 20/20 sự kiện, 114/114 aspects (100%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D1×2, E3×2, G1×2, G4×2, P1×2, V1×4, V2×3, V3×3, V4×3 |
| Diễn giải cần xác nhận (review-needed Phần A) | A2×1, A4×1, A6×1, A10×1, A14×1, A15×1, A16×1, A17×1, A18×1, A19×1, A20×1, A21×1 |

**Mở rộng:** Vietlink V1–V4 tách thành 13 bullet trong 4 nhóm (Pipeline Architecture, Batch Optimization, Search & Analytics, Reliability & Operations). Galaxy G4 tách thành 2 bullet (hệ thống + mô hình chạy ECS/Lambda/RDS); G1 tách thành tính toán và repayment/settlement. EsolLabs kể theo góc ingestion.

**Không đưa vào và lý do:** Không bỏ sự kiện nào.

### devops-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | VNPAY / Galaxy FinX / Vietlink, EsolLabs |
| Bullet theo công ty | Galaxy 7 · Vietlink 7 · VNPAY 11 · EsolLabs 3 · Projects 4 |
| Sự kiện giữ lại | 20/20 sự kiện, 112/114 aspects (98%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D2×2, G3×3, P1×5, P2×2, P3×2, P4×2, V1×2, V4×4 |
| Diễn giải cần xác nhận (review-needed Phần A) | A5×3, A7×1, A10×1, A11×1, A18×1, A22×1 |

**Mở rộng:** VNPAY P1 tách thành 5 bullet về lifecycle (OpenStack, vận hành 50+ cluster, provisioning, scaling, zero-downtime upgrade); P4 thành 2; P2 thành authentication + RBAC. Galaxy G3 tách thành deploy, hạ tầng EKS/RDS/ECR/ELB và CI/CD. Vietlink V4 tách thành Terraform, SAM, CloudWatch, DataDog.

**Không đưa vào và lý do:** MeetQ chỉ giữ 1 bullet (M2b, M2c bỏ vì ít liên quan DevOps).

Aspects chưa xuất hiện: M2 MeetQ translation pipeline: context handling, accuracy & coherence

### fintech-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / VNPAY + EsolLabs / Vietlink |
| Bullet theo công ty | Galaxy 12 · Vietlink 4 · VNPAY 6 · EsolLabs 5 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 112/114 aspects (98%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | E3×3, G1×5, G2×2, G3×2, G4×2, P1×2, P2×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A1×1, A3×1, A4×2, A10×2 |

**Mở rộng:** G1 tách 5 bullet (sản phẩm, interest accrual, penalty/late fees, repayment, settlement); G4 tách hệ thống + tác động; G2 tách framework + tốc độ; G3 tách deploy + CI/CD. EsolLabs E3 tách consistent transactions và data integrity.

**Không đưa vào và lý do:** MeetQ chỉ giữ 1 bullet (M2b, M2c).

Aspects chưa xuất hiện: M2 MeetQ translation pipeline: context handling, accuracy & coherence

### golang-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / Vietlink / VNPAY, EsolLabs |
| Bullet theo công ty | Galaxy 8 · Vietlink 5 · VNPAY 4 · EsolLabs 4 · Projects 6 |
| Sự kiện giữ lại | 20/20 sự kiện, 114/114 aspects (100%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D1×3, E3×2, G2×2, G3×2, G4×2, V3×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A2×1, A3×1, A6×1, A7×1, A8×1, A16×1, A18×1, A19×1 |

**Mở rộng:** Galaxy chia 3 nhóm: Account Migration (Go), Testing Infrastructure (Go), Integration & Delivery. DattingQ thành Key Project 4 bullet (API layer, messaging/data, hiệu năng, độ tin cậy).

**Không đưa vào và lý do:** Không bỏ sự kiện nào. Chi tiết concurrency/worker của Go **không** được nhận vì chưa xác minh (review-needed B1/B2).

### java-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / VNPAY / Vietlink, EsolLabs |
| Bullet theo công ty | Galaxy 9 · Vietlink 5 · VNPAY 6 · EsolLabs 3 · Projects 4 |
| Sự kiện giữ lại | 20/20 sự kiện, 113/114 aspects (99%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D1×2, G1×3, G2×2, G3×2, P2×2, P3×2, V3×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A3×1, A4×2, A6×1, A7×1, A8×1, A9×2 |

**Mở rộng:** Galaxy chia Transaction Processing / Integration & Data / Testing & Delivery. VNPAY 6 bullet theo góc microservices và identity (gateway, access control, authentication, authorization model).

**Không đưa vào và lý do:** MeetQ gộp còn 1 bullet. Không có hệ thống Golang/Python nào được trình bày thành Java.

Aspects chưa xuất hiện: M2 MeetQ translation pipeline: accuracy & coherence

### platform-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | VNPAY / Galaxy FinX / Vietlink, EsolLabs |
| Bullet theo công ty | Galaxy 7 · Vietlink 6 · VNPAY 10 · EsolLabs 3 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 112/114 aspects (98%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G2×2, G3×2, P1×4, P2×2, P3×2, P4×2, V4×3 |
| Diễn giải cần xác nhận (review-needed Phần A) | A5×1, A9×2, A10×1, A11×1 |

**Mở rộng:** VNPAY kể như sản phẩm nền tảng: Kubernetes platform (4), shared services gateway + identity (4), platform automation (2). Galaxy G2 tách công cụ + feedback loop; G3 tách delivery path + CI/CD.

**Không đưa vào và lý do:** MeetQ chỉ giữ 1 bullet (M2b, M2c).

Aspects chưa xuất hiện: M2 MeetQ translation pipeline: context handling, accuracy & coherence

### python-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / Vietlink / VNPAY, EsolLabs |
| Bullet theo công ty | Galaxy 10 · Vietlink 5 · VNPAY 5 · EsolLabs 3 · Projects 5 |
| Sự kiện giữ lại | 20/20 sự kiện, 114/114 aspects (100%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G1×5, G2×2, M1×2, P2×2, V1×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A1×1, A2×1, A3×2, A4×2, A6×1 |

**Mở rộng:** G1 tách thành 5 bullet (sản phẩm, interest accrual, penalty/late fees, repayment, settlement). G2 tách thành framework + tốc độ kiểm chứng contract. MeetQ lên đầu với 3 bullet.

**Không đưa vào và lý do:** Không bỏ sự kiện nào. Python chỉ được gán cho Vault Core Smart Contracts.

### software-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | Cân bằng / Cả bốn công ty / - |
| Bullet theo công ty | Galaxy 9 · Vietlink 6 · VNPAY 6 · EsolLabs 3 · Projects 5 |
| Sự kiện giữ lại | 20/20 sự kiện, 114/114 aspects (100%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D1×2, G1×2, G2×2, G3×2, G4×2, P1×2, P2×2, V1×2, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A6×1 |

**Mở rộng:** Galaxy có 9 bullet, mỗi bullet gắn nhãn theo tầng công việc (Product, Financial logic, Testing, Performance, Data, Infrastructure, Delivery, Integration). Các công ty còn lại 4–6 bullet.

**Không đưa vào và lý do:** Không bỏ sự kiện nào.
