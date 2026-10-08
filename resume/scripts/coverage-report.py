#!/usr/bin/env python3
"""Experience coverage report.

Every bullet in latex/*.tex carries tags in a trailing LaTeX comment:
    \\item ... % @V1abg @V2c !A6
  @<Fact><aspects>  facts from analysis/experience-inventory.md
  !A<n>             interpretations listed in analysis/review-needed.md (Part A)

This script checks, for every CV, which inventory facts/aspects and metrics are
kept, how many bullets each fact was expanded into, what is missing, and which
interpretations need review. It writes analysis/experience-coverage-report.md.

Usage: python3 scripts/coverage-report.py
"""
import glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fact -> (company, label, aspects{letter: description})
INVENTORY = {
    "G1": ("Galaxy FinX", "Lending & Overdraft on Vault Core", dict(a="Lending", b="Overdraft", c="interest accrual", d="penalty & late fees", e="repayment", f="settlement", g="Python Smart Contracts", h="maintenance")),
    "G2": ("Galaxy FinX", "Simulation testing framework", dict(a="Golang rewrite", b="replaced Gauge", c="24 min -> ~50 s (20x)")),
    "G3": ("Galaxy FinX", "Vault Core on AWS + CI/CD", dict(a="new version deployed", b="EKS", c="RDS", d="ECR", e="ELB", f="CI/CD build/test/deploy")),
    "G4": ("Galaxy FinX", "Account migration system", dict(a="Golang", b="ECS", c="Lambda", d="RDS", e="2.5 h -> 27 min (5x)")),
    "G5": ("Galaxy FinX", "Vault Core integrations", dict(a="external backend services", b="core banking operations", c="transaction workflows")),
    "V1": ("Vietlink", "ETL pipelines on AWS", dict(a="design/develop/operate", b="Lambda", c="ECS", d="RDS", e="S3", f="Athena", g="large-scale utility data", h="analytics", i="operational workloads")),
    "V2": ("Vietlink", "Batch optimization", dict(a="batch workflows", b="pipeline redesign", c="parallel execution", d="data access patterns", e="+150% throughput")),
    "V3": ("Vietlink", "Elasticsearch -> OpenSearch", dict(a="migration", b="ingestion flows", c="indexing flows", d="stability", e="consistency", f="query performance")),
    "V4": ("Vietlink", "IaC + monitoring", dict(a="Terraform", b="AWS SAM", c="build & maintain infra", d="CloudWatch", e="DataDog", f="pipeline health", g="failures", h="anomaly detection")),
    "P1": ("VNPAY", "OpenStack private cloud", dict(a="design & operate", b="OpenStack", c="Cluster API", d="provisioning", e="scaling", f="zero-downtime upgrades", g="50+ clusters")),
    "P2": ("VNPAY", "Multi-tenant auth", dict(a="authentication", b="authorization", c="Keycloak", d="RBAC", e="tenant isolation", f="20+ organizations")),
    "P3": ("VNPAY", "Kong Gateway", dict(a="integrate & operate", b="100+ services", c="service-level access", d="network-level access")),
    "P4": ("VNPAY", "Data center automation", dict(a="~80% provisioning", b="infra configuration", c="less manual effort")),
    "E1": ("EsolLabs", "Smart contracts", dict(a="15+ contracts", b="code review", c="DeFi", d="NFT", e="Solidity", f="Move")),
    "E2": ("EsolLabs", "Event-driven services", dict(a="event-driven", b="capture", c="process", d="sync on-chain events", e="off-chain databases", f="APIs")),
    "E3": ("EsolLabs", "Multi-chain integration", dict(a="5+ networks", b="Ethereum", c="BSC", d="Polygon", e="Aptos", f="Sui", g="consistent transactions", h="data integrity")),
    "D1": ("Projects", "DattingQ backend", dict(a="gRPC-Gateway", b="Kafka", c="MongoDB", d="Redis", e="1.5K req/s", f="80-100 ms")),
    "D2": ("Projects", "DattingQ reliability", dict(a="multi-cluster failover", b="OpenTelemetry", c="Prometheus", d="Grafana", e="ELK", f="ClickHouse", g="99.95% uptime")),
    "M1": ("Projects", "MeetQ platform", dict(a="LiveKit", b="OpenAI", c="transcription", d="voice translation", e="summarization")),
    "M2": ("Projects", "MeetQ translation pipeline", dict(a="pipeline design", b="context handling", c="accuracy & coherence")),
}
METRICS = ["2.5 hours", "24 minutes", "150\\%", "50+", "20+", "100+", "80\\%", "15+", "5+", "1.5K", "80--100", "99.95"]
COMPANY_MACROS = [("Galaxy FinX", r"\jobGalaxyFinX"), ("Vietlink", r"\jobVietlink"), ("VNPAY", r"\jobVNPAY"), ("EsolLabs", r"\jobEsolLabs")]

# Narrative per CV: role allocation and what was expanded or left out (and why).
NOTES = {
    "data-engineer": ("Vietlink", "Galaxy FinX", "VNPAY, EsolLabs",
        "Vietlink V1–V4 tách thành 13 bullet trong 4 nhóm (Pipeline Architecture, Batch Optimization, Search & Analytics, Reliability & Operations). Galaxy G4 tách thành 2 bullet (hệ thống + mô hình chạy ECS/Lambda/RDS); G1 tách thành tính toán và repayment/settlement. EsolLabs kể theo góc ingestion.",
        "Không bỏ sự kiện nào."),
    "devops-engineer": ("VNPAY", "Galaxy FinX", "Vietlink, EsolLabs",
        "VNPAY P1 tách thành 5 bullet về lifecycle (OpenStack, vận hành 50+ cluster, provisioning, scaling, zero-downtime upgrade); P4 thành 2; P2 thành authentication + RBAC. Galaxy G3 tách thành deploy, hạ tầng EKS/RDS/ECR/ELB và CI/CD. Vietlink V4 tách thành Terraform, SAM, CloudWatch, DataDog.",
        "MeetQ chỉ giữ 1 bullet (M2b, M2c bỏ vì ít liên quan DevOps)."),
    "cloud-engineer": ("VNPAY", "Galaxy FinX + Vietlink", "EsolLabs",
        "VNPAY kể theo kiến trúc private cloud: P1 tách 5 bullet, P2 tách tenant isolation + RBAC, P3 tách gateway + chính sách truy cập. Galaxy G3 kể theo vai trò từng dịch vụ AWS. Vietlink V1 tách serverless/container và storage/query.",
        "MeetQ chỉ giữ 1 bullet (M2b, M2c)."),
    "platform-engineer": ("VNPAY", "Galaxy FinX", "Vietlink, EsolLabs",
        "VNPAY kể như sản phẩm nền tảng: Kubernetes platform (4), shared services gateway + identity (4), platform automation (2). Galaxy G2 tách công cụ + feedback loop; G3 tách delivery path + CI/CD.",
        "MeetQ chỉ giữ 1 bullet (M2b, M2c)."),
    "golang-backend": ("Galaxy FinX", "Vietlink", "VNPAY, EsolLabs",
        "Galaxy chia 3 nhóm: Account Migration (Go), Testing Infrastructure (Go), Integration & Delivery. DattingQ thành Key Project 4 bullet (API layer, messaging/data, hiệu năng, độ tin cậy).",
        "Không bỏ sự kiện nào. Chi tiết concurrency/worker của Go **không** được nhận vì chưa xác minh (review-needed B1/B2)."),
    "python-backend": ("Galaxy FinX", "Vietlink", "VNPAY, EsolLabs",
        "G1 tách thành 5 bullet (sản phẩm, interest accrual, penalty/late fees, repayment, settlement). G2 tách thành framework + tốc độ kiểm chứng contract. MeetQ lên đầu với 3 bullet.",
        "Không bỏ sự kiện nào. Python chỉ được gán cho Vault Core Smart Contracts."),
    "java-backend": ("Galaxy FinX", "VNPAY", "Vietlink, EsolLabs",
        "Galaxy chia Transaction Processing / Integration & Data / Testing & Delivery. VNPAY 6 bullet theo góc microservices và identity (gateway, access control, authentication, authorization model).",
        "MeetQ gộp còn 1 bullet. Không có hệ thống Golang/Python nào được trình bày thành Java."),
    "fintech-backend": ("Galaxy FinX", "VNPAY + EsolLabs", "Vietlink",
        "G1 tách 5 bullet (sản phẩm, interest accrual, penalty/late fees, repayment, settlement); G4 tách hệ thống + tác động; G2 tách framework + tốc độ; G3 tách deploy + CI/CD. EsolLabs E3 tách consistent transactions và data integrity.",
        "MeetQ chỉ giữ 1 bullet (M2b, M2c)."),
    "backend-engineer": ("Galaxy FinX", "Vietlink + VNPAY", "EsolLabs",
        "Galaxy chia Integration & Transaction Logic / Migration Backend / Testing & Deployment. VNPAY tách gateway, access control, authentication, authorization. Vietlink tách V3 thành migration + ingestion/indexing, V4 thành IaC + monitoring.",
        "Không bỏ sự kiện nào."),
    "software-engineer": ("Cân bằng", "Cả bốn công ty", "-",
        "Galaxy có 9 bullet, mỗi bullet gắn nhãn theo tầng công việc (Product, Financial logic, Testing, Performance, Data, Infrastructure, Delivery, Integration). Các công ty còn lại 4–6 bullet.",
        "Không bỏ sự kiện nào."),
}


def parse(path):
    """Return list of (section, company, text, facts{F:set}, flags[]) for each bullet."""
    src = open(path).read()
    out, company, section = [], None, "experience"
    for line in src.splitlines():
        for name, macro in COMPANY_MACROS:
            if line.strip().startswith(macro):
                company = name
        if re.match(r"\\cvsection\{(Selected Projects|Key Project)\}", line.strip()):
            company, section = "Projects", "projects"
        if r"\item" not in line or "%" not in line:
            continue
        text, _, tags = line.partition("% @") if "% @" in line else line.rpartition("%")
        tags = "@" + tags if "% @" in line else tags
        facts = collections.defaultdict(set)
        for f, asp in re.findall(r"@([GVPEDM]\d)([a-z]*)", tags):
            facts[f] |= set(asp)
        flags = re.findall(r"!(A\d+)", tags)
        if facts:
            out.append((section, company, text.strip(), facts, flags))
    return out


def main():
    rows, details = [], []
    for path in sorted(glob.glob(os.path.join(ROOT, "latex", "*.tex"))):
        name = os.path.basename(path)[:-4]
        src = open(path).read()
        bullets = parse(path)
        covered = collections.defaultdict(set)
        per_fact = collections.Counter()
        per_company = collections.Counter()
        flags = collections.Counter()
        for _, comp, _, facts, fl in bullets:
            per_company[comp] += 1
            for f, asp in facts.items():
                covered[f] |= asp
                per_fact[f] += 1
            flags.update(fl)
        total_aspects = sum(len(v[2]) for v in INVENTORY.values())
        got_aspects = sum(len(covered[f] & set(INVENTORY[f][2])) for f in INVENTORY)
        facts_kept = sum(1 for f in INVENTORY if covered[f])
        metrics_kept = [m for m in METRICS if m in src]
        missing = []
        for f, (_, label, asp) in INVENTORY.items():
            lost = [asp[a] for a in asp if a not in covered[f]]
            if lost:
                missing.append(f"{f} {label}: " + ", ".join(lost))
        rows.append((name, facts_kept, got_aspects, total_aspects, len(metrics_kept), per_company))
        primary, secondary, supporting, expanded, excluded = NOTES.get(name, ("", "", "", "", ""))
        expanded_facts = ", ".join(f"{f}×{n}" for f, n in sorted(per_fact.items()) if n > 1) or "-"
        details.append(f"""### {name}

| | |
|---|---|
| Primary / Secondary / Supporting | {primary} / {secondary} / {supporting} |
| Bullet theo công ty | Galaxy {per_company['Galaxy FinX']} · Vietlink {per_company['Vietlink']} · VNPAY {per_company['VNPAY']} · EsolLabs {per_company['EsolLabs']} · Projects {per_company['Projects']} |
| Sự kiện giữ lại | {facts_kept}/{len(INVENTORY)} sự kiện, {got_aspects}/{total_aspects} aspects ({got_aspects*100//total_aspects}%) |
| Metric giữ lại | {len(metrics_kept)}/{len(METRICS)} |
| Sự kiện được mở rộng thành nhiều bullet | {expanded_facts} |
| Diễn giải cần xác nhận (review-needed Phần A) | {", ".join(f"{k}×{v}" for k, v in sorted(flags.items(), key=lambda x: int(x[0][1:]))) or "-"} |

**Mở rộng:** {expanded}

**Không đưa vào và lý do:** {excluded}
{"" if not missing else chr(10) + "Aspects chưa xuất hiện: " + "; ".join(missing) + chr(10)}""")

    header = """# Experience Coverage Report

Sinh tự động bởi `scripts/coverage-report.py` từ các tag trong `latex/*.tex`, đối chiếu với `analysis/experience-inventory.md`. Chạy lại script sau mỗi lần sửa CV.

- **Sự kiện** = 20 thành tích/trách nhiệm trong CV gốc (G1–G5, V1–V4, P1–P4, E1–E3, D1–D2, M1–M2).
- **Aspects** = các chi tiết bên trong mỗi sự kiện (công nghệ, số liệu, phạm vi).
- **Metric** = 12 con số đã xác nhận (5x, 20x, 150%, 50+, 20+, 100+, 80%, 15+, 5+, 1.5K, 80–100 ms, 99.95%).

## Tổng quan

| CV | Sự kiện | Aspects | Metric | Galaxy | Vietlink | VNPAY | EsolLabs | Projects |
|---|---|---|---|---|---|---|---|---|
"""
    table = "".join(
        f"| {n} | {fk}/{len(INVENTORY)} | {ga}/{ta} ({ga*100//ta}%) | {mk}/{len(METRICS)} | {pc['Galaxy FinX']} | {pc['Vietlink']} | {pc['VNPAY']} | {pc['EsolLabs']} | {pc['Projects']} |\n"
        for n, fk, ga, ta, mk, pc in rows)
    outro = """
## Nội dung không đưa vào CV nào
- **Freelance Blockchain Developer (09/2023 – 03/2024):** bạn đang comment trong `main.tex`, nên tôi tôn trọng quyết định ẩn mục này. Xem `review-needed.md`, mục C.
- **Skills chỉ có trong danh sách Skills** (Java, Spring Boot, FastAPI, RabbitMQ, Jenkins, ArgoCD, Consul, HashiCorp Vault, Postman): chỉ xuất hiện trong Technical Skills của các bản liên quan, không viết thành thành tích.
- **Postman:** bỏ khỏi mọi bản vì không thêm giá trị cho các vị trí mục tiêu.

## Chi tiết mới cần xác minh
- **Phần A** của `review-needed.md`: các diễn giải **đã có** trong CV, được đánh dấu `!A…` ở từng bullet. Số lần dùng của từng mã nằm trong bảng chi tiết bên dưới.
- **Phần B**: các chi tiết **chưa** đưa vào CV (worker/concurrency trong migration, outbox/retry/reconciliation, orchestration ETL, data volume, Helm/ArgoCD...).

## Chi tiết theo từng CV

"""
    with open(os.path.join(ROOT, "analysis", "experience-coverage-report.md"), "w") as fh:
        fh.write(header + table + outro + "\n".join(details))
    for n, fk, ga, ta, mk, pc in rows:
        print(f"{n:20} facts {fk}/{len(INVENTORY)}  aspects {ga}/{ta} ({ga*100//ta}%)  metrics {mk}/{len(METRICS)}")


if __name__ == "__main__":
    main()
