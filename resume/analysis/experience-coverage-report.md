# Experience Coverage Report

Sinh tự động bởi `scripts/coverage-report.py` từ các tag trong `latex/*.tex`, đối chiếu với `analysis/experience-inventory.md`. Chạy lại script sau mỗi lần sửa CV.

- **Sự kiện** = 20 thành tích/trách nhiệm trong CV gốc (G1–G5, V1–V4, P1–P4, E1–E3, D1–D2, M1–M2).
- **Aspects** = các chi tiết bên trong mỗi sự kiện (công nghệ, số liệu, phạm vi).
- **Metric** = 12 con số đã xác nhận (5x, 20x, 150%, 50+, 20+, 100+, 80%, 15+, 5+, 1.5K, 80–100 ms, 99.95%).

## Tổng quan

| CV | Sự kiện | Aspects | Metric | Galaxy | Vietlink | VNPAY | EsolLabs | Projects |
|---|---|---|---|---|---|---|---|---|
| backend-engineer | 20/20 | 113/114 (99%) | 12/12 | 6 | 4 | 4 | 3 | 3 |
| cloud-engineer | 18/20 | 96/114 (84%) | 11/12 | 5 | 5 | 6 | 2 | 1 |
| data-engineer | 20/20 | 114/114 (100%) | 12/12 | 5 | 7 | 4 | 3 | 4 |
| devops-engineer | 18/20 | 106/114 (92%) | 12/12 | 5 | 5 | 6 | 2 | 2 |
| fintech-backend | 18/20 | 103/114 (90%) | 12/12 | 8 | 4 | 4 | 3 | 1 |
| golang-backend | 20/20 | 107/114 (93%) | 12/12 | 5 | 4 | 4 | 2 | 4 |
| java-backend | 20/20 | 107/114 (93%) | 12/12 | 6 | 4 | 4 | 2 | 3 |
| platform-engineer | 18/20 | 101/114 (88%) | 12/12 | 5 | 5 | 5 | 2 | 2 |
| python-backend | 20/20 | 104/114 (91%) | 12/12 | 7 | 4 | 4 | 2 | 3 |
| software-engineer | 20/20 | 107/114 (93%) | 12/12 | 4 | 4 | 3 | 1 | 3 |

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
| Bullet theo công ty | Galaxy 6 · Vietlink 4 · VNPAY 4 · EsolLabs 3 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 113/114 aspects (99%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G1×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A2×1, A3×1, A8×1, A18×1, A20×1 |

**Trình bày:** Galaxy mở đầu bằng integration; tách interest/fees và repayment/settlement.

**Không đưa vào và lý do:** MeetQ gộp còn 1 bullet.

Aspects chưa xuất hiện: M2 MeetQ translation pipeline: accuracy & coherence

### cloud-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | VNPAY / Galaxy FinX + Vietlink / EsolLabs |
| Bullet theo công ty | Galaxy 5 · Vietlink 5 · VNPAY 6 · EsolLabs 2 · Projects 1 |
| Sự kiện giữ lại | 18/20 sự kiện, 96/114 aspects (84%) |
| Metric giữ lại | 11/12 |
| Sự kiện được mở rộng thành nhiều bullet | G3×2, P1×3, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A5×2, A6×1, A7×1, A9×1, A10×1, A18×1 |

**Trình bày:** VNPAY 6 bullet theo góc kiến trúc private cloud và tenant isolation. Galaxy kể vai trò từng dịch vụ AWS.

**Không đưa vào và lý do:** MeetQ bị bỏ; DattingQ chỉ giữ 1 bullet về failover và monitoring.

Aspects chưa xuất hiện: E3 Multi-chain integration: Ethereum, BSC, Polygon, Aptos, Sui; D1 DattingQ backend: gRPC-Gateway, Kafka, MongoDB, Redis, 80-100 ms; M1 MeetQ platform: LiveKit, OpenAI, transcription, voice translation, summarization; M2 MeetQ translation pipeline: pipeline design, context handling, accuracy & coherence

### data-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | Vietlink / Galaxy FinX / VNPAY, EsolLabs |
| Bullet theo công ty | Galaxy 5 · Vietlink 7 · VNPAY 4 · EsolLabs 3 · Projects 4 |
| Sự kiện giữ lại | 20/20 sự kiện, 114/114 aspects (100%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | V1×3, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A6×1, A15×1, A20×1 |

**Trình bày:** Vietlink 7 bullet (kiến trúc ETL, vai trò từng dịch vụ AWS, transformation, tối ưu 150%, OpenSearch, IaC, monitoring). Galaxy kể theo góc data migration.

**Không đưa vào và lý do:** Không bỏ sự kiện nào.

### devops-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | VNPAY / Galaxy FinX / Vietlink, EsolLabs |
| Bullet theo công ty | Galaxy 5 · Vietlink 5 · VNPAY 6 · EsolLabs 2 · Projects 2 |
| Sự kiện giữ lại | 18/20 sự kiện, 106/114 aspects (92%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G3×2, P1×3, V1×2, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A5×2, A10×1, A18×1 |

**Trình bày:** VNPAY 6 bullet (OpenStack, lifecycle với Cluster API, zero-downtime upgrade, automation 80%, Kong, Keycloak). Galaxy tách deploy và CI/CD.

**Không đưa vào và lý do:** MeetQ bị bỏ vì không liên quan DevOps.

Aspects chưa xuất hiện: M1 MeetQ platform: LiveKit, OpenAI, transcription, voice translation, summarization; M2 MeetQ translation pipeline: pipeline design, context handling, accuracy & coherence

### fintech-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / VNPAY + EsolLabs / Vietlink |
| Bullet theo công ty | Galaxy 8 · Vietlink 4 · VNPAY 4 · EsolLabs 3 · Projects 1 |
| Sự kiện giữ lại | 18/20 sự kiện, 103/114 aspects (90%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G1×4 |
| Diễn giải cần xác nhận (review-needed Phần A) | A1×1, A3×1, A4×1, A10×1 |

**Trình bày:** Galaxy 8 bullet theo vòng đời sản phẩm (sản phẩm, interest accrual, penalty/late fee, repayment/settlement, integration, migration, testing, deploy).

**Không đưa vào và lý do:** MeetQ bị bỏ vì không liên quan FinTech.

Aspects chưa xuất hiện: V3 Elasticsearch -> OpenSearch: stability, consistency, query performance; M1 MeetQ platform: LiveKit, OpenAI, transcription, voice translation, summarization; M2 MeetQ translation pipeline: pipeline design, context handling, accuracy & coherence

### golang-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / Vietlink / VNPAY, EsolLabs |
| Bullet theo công ty | Galaxy 5 · Vietlink 4 · VNPAY 4 · EsolLabs 2 · Projects 4 |
| Sự kiện giữ lại | 20/20 sự kiện, 107/114 aspects (93%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | D1×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A3×1, A6×1, A8×1, A18×1 |

**Trình bày:** Galaxy có 2 hệ thống Go đứng đầu; DattingQ là Key Project với 3 bullet (API layer, messaging/storage, reliability).

**Không đưa vào và lý do:** MeetQ chỉ giữ 1 bullet (M2b, M2c bỏ). Chi tiết concurrency của Go chưa được nhận (review-needed B1/B2).

Aspects chưa xuất hiện: E3 Multi-chain integration: Ethereum, BSC, Polygon, Aptos, Sui; M2 MeetQ translation pipeline: context handling, accuracy & coherence

### java-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / VNPAY + Vietlink / EsolLabs |
| Bullet theo công ty | Galaxy 6 · Vietlink 4 · VNPAY 4 · EsolLabs 2 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 107/114 aspects (93%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G1×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A4×1, A6×1, A8×1, A9×1 |

**Trình bày:** Galaxy tách transaction logic và repayment/settlement; VNPAY kể theo góc API gateway và identity.

**Không đưa vào và lý do:** MeetQ gộp còn 1 bullet. Không hệ thống Golang/Python nào được trình bày thành Java.

Aspects chưa xuất hiện: E3 Multi-chain integration: Ethereum, BSC, Polygon, Aptos, Sui; M2 MeetQ translation pipeline: context handling, accuracy & coherence

### platform-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | VNPAY / Galaxy FinX / Vietlink, EsolLabs |
| Bullet theo công ty | Galaxy 5 · Vietlink 5 · VNPAY 5 · EsolLabs 2 · Projects 2 |
| Sự kiện giữ lại | 18/20 sự kiện, 101/114 aspects (88%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | P1×2, V4×2 |
| Diễn giải cần xác nhận (review-needed Phần A) | A9×1, A10×1, A11×1 |

**Trình bày:** VNPAY kể như nền tảng (Kubernetes platform, gateway và identity dùng chung). Galaxy kể theo góc tooling và delivery.

**Không đưa vào và lý do:** MeetQ bị bỏ vì không liên quan Platform.

Aspects chưa xuất hiện: E3 Multi-chain integration: Ethereum, BSC, Polygon, Aptos, Sui; M1 MeetQ platform: LiveKit, OpenAI, transcription, voice translation, summarization; M2 MeetQ translation pipeline: pipeline design, context handling, accuracy & coherence

### python-backend

| | |
|---|---|
| Primary / Secondary / Supporting | Galaxy FinX / Vietlink / VNPAY, EsolLabs |
| Bullet theo công ty | Galaxy 7 · Vietlink 4 · VNPAY 4 · EsolLabs 2 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 104/114 aspects (91%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | G1×3 |
| Diễn giải cần xác nhận (review-needed Phần A) | A1×1, A2×1, A3×1, A4×1, A6×1 |

**Trình bày:** G1 tách 3 bullet (sản phẩm, interest + penalty/late fee, repayment + settlement). MeetQ đặt lên đầu Projects.

**Không đưa vào và lý do:** Không bỏ sự kiện nào. Python chỉ được gán cho Vault Core Smart Contracts.

Aspects chưa xuất hiện: E3 Multi-chain integration: Ethereum, BSC, Polygon, Aptos, Sui; D2 DattingQ reliability: OpenTelemetry, Prometheus, Grafana, ELK, ClickHouse

### software-engineer

| | |
|---|---|
| Primary / Secondary / Supporting | Cân bằng / Cả bốn công ty / - |
| Bullet theo công ty | Galaxy 4 · Vietlink 4 · VNPAY 3 · EsolLabs 1 · Projects 3 |
| Sự kiện giữ lại | 20/20 sự kiện, 107/114 aspects (93%) |
| Metric giữ lại | 12/12 |
| Sự kiện được mở rộng thành nhiều bullet | - |
| Diễn giải cần xác nhận (review-needed Phần A) | - |

**Trình bày:** Mỗi công ty 1–4 bullet theo kết quả; các thành tích liên quan được gộp (ví dụ Kong và Keycloak thành một bullet về access control).

**Không đưa vào và lý do:** MeetQ chỉ giữ 1 bullet.

Aspects chưa xuất hiện: E3 Multi-chain integration: Ethereum, BSC, Polygon, Aptos, Sui; M2 MeetQ translation pipeline: context handling, accuracy & coherence
