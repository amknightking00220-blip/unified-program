#  Preventive Employee Experience Diagnostics
# Palo Alto Networks · HR Analytics Project

# 📌 Project Overview

Most HR analytics answer the wrong question: **"Why did this employee leave?"**

This project answers the right one: **"Which employees are at risk — and what can we do about it now?"**

By combining burnout risk scoring, composite engagement indexing, and multi-dimensional segmentation across 1,470 employees, this analysis surfaces the early warning signals that precede attrition — enabling data-driven intervention before resignations occur.

---

# 🎯 Deliverables

| # | Deliverable | Audience | Format |
|---|-------------|----------|--------|
| 1 | **Research Paper** — Full EDA, insights & recommendations | HR Leadership, People Analytics Teams | `.docx` |
| 2 | **Executive Summary** — Strategic findings & action priorities | Government & Regulatory Stakeholders | `.docx` |

---

# 📂 Dataset Reference

| File | Description | Key Variables |
|------|-------------|---------------|
| `Palo_Alto_Networks.csv` | Primary employee dataset (1,470 records) | Demographics, compensation, job attributes, satisfaction scores |
| `unified_engagement_level_and_risky_emp_.csv` | Composite engagement + risk classification | `EngagementIndex`, `EngagementLevel`, `risky_emp`, `risk_rate` |
| `unified_risk_rate.csv` | Burnout risk segmentation | `risk_rate` (low / medium / high) |
| `burnout.csv` | Burnout indicator subset | Overtime, satisfaction dimensions |
| `engagement_attrition.csv` | Engagement vs. attrition correlation | `EngagementIndex` by `Attrition` group |
| `CareerStageEngagement.csv` | Engagement by job level, tenure, role tenure | Career progression engagement mapping |
| `Workload___Stress_Analysis.csv` | Overtime, business travel, commute stress | Workload-engagement relationships |

---

# 📊 Key Findings at a Glance

---
Overall Attrition Rate         →  16.1%   (237 of 1,470 employees)
Overtime Employee Attrition    →  30.5%   (3× the non-OT rate of 10.4%)
Low Engagement Tier Attrition  →  34.1%   (vs. 10.3% for High Engagement)
High Engagement Tier Attrition →  10.3%   (strongest retention predictor)
High-Risk Employees Flagged    →  126     (composite burnout + engagement score)
Income Gap (Leavers vs Stayed) →  -30.0%  ($4,787 vs $6,833 avg monthly income)
No Stock Option Attrition      →  24.4%   (2.6× rate of Level 1 holders at 9.4%)
Single Employee Attrition      →  25.5%   (2.5× the rate of divorced employees)


---

# 🧠 Methodology

# Engagement Index
A composite score (0–1 scale) derived from five normalized satisfaction dimensions:

---

EngagementIndex = mean(
    EnvironmentSatisfaction_norm,
    JobInvolvement_norm,
    JobSatisfaction_norm,
    RelationshipSatisfaction_norm,
    WorkLifeBalance_norm
)
---

| Tier | Range | Headcount | Attrition Rate |
|------|-------|-----------|----------------|
| 🔴 Low | < 0.42 | 176 (12.0%) | **34.1%** |
| 🟡 Medium | 0.42 – 0.67 | 972 (66.1%) | 14.8% |
| 🟢 High | > 0.67 | 322 (21.9%) | 10.3% |

# Risk Classification
Employees are assigned a `risk_rate` (low / medium / high) based on a composite of:
- Overtime status
- Engagement tier
- Satisfaction sub-dimension scores
- Historical attrition pattern alignment

The binary `risky_emp` flag identifies employees meeting **all** high-risk thresholds simultaneously.

---

# 🔬 Analysis Dimensions

---
├── Engagement vs. Attrition          → Core 14.2% engagement gap between leavers and stayers
├── Burnout & Workload Stress         → Overtime, business travel, commute distance
├── Career Stage & Role Tenure        → Job level, experience years, years in current role
├── Compensation & Equity             → Monthly income gaps, stock option level impact
├── Demographic Risk Factors          → Age cohort, marital status distributions
├── High-Risk Employee Segmentation   → 126 employees by department and job role
└── Department-Level Breakdown        → R&D (13.8%), Sales (20.6%), HR (19.0%)


---

# ⚠️ Critical Insights

**1. Overtime is a burnout accelerant, not a productivity signal**
Overtime workers show *higher* initial engagement (0.595 vs 0.566) — they self-select in. But they leave at **30.5%**, nearly 3× the non-OT rate. Among OT workers, 30.3% are flagged as high burnout risk; 0% of non-OT workers are.

**2. Low engagement precedes — and predicts — exit**
Employees who ultimately left averaged an engagement index of **0.504**, a 14.2% deficit versus retained staff at **0.588**. This gap is observable before resignation, making engagement the strongest leading indicator in the dataset.

**3. Role stagnation silently erodes engagement**
Employees in the same role for **15+ years** score **0.481** on engagement — a 17% deficit versus mid-tenure peers (0.579). This is the largest role-based gap identified and is rarely visible until it registers as attrition.

**4. Research Scientists are disproportionately at risk**
Research Scientists represent **25.4% of all high-risk employees** despite being less than 20% of total headcount — the most concentrated burnout cluster in the organization.

---

# 💡 Recommended Interventions

| Priority | Intervention | Timeline |
|----------|-------------|----------|
| 🔴 Critical | Overtime & Burnout Control Program | 0–30 days |
| 🔴 Critical | Low Engagement Re-Engagement Initiative | 30–60 days |
| 🟠 High | Research Scientist Burnout Audit | 30–60 days |
| 🟠 High | Compensation Band Equity Review | 60–120 days |
| 🟠 High | Stock Option Expansion (Level 0 holders) | 60–90 days |
| 🟠 High | Career Mobility & Anti-Stagnation Program | 60–90 days |
| 🟡 Moderate | Early-Career & Single Employee Retention Package | 90 days |

---

# 🎯 24-Month Targets

| Metric | Current | 12-Month Target | 24-Month Target |
|--------|---------|-----------------|-----------------|
| Overall Attrition Rate | 16.1% | < 13% | **< 10%** |
| Overtime Attrition Rate | 30.5% | < 22% | **< 15%** |
| Low Engagement Cohort | 12.0% | < 9% | **< 6%** |
| High-Risk Employee Count | 126 | < 80 | **< 40** |
| Avg. Engagement Index | 0.574 | > 0.610 | **> 0.650** |
| Est. Annual Attrition Cost | $8–15M | < $10M | **< $6M** |

---

# 🏢 Organization Context

| Attribute | Detail |
|-----------|--------|
| **Company** | Palo Alto Networks |
| **Workforce Analyzed** | 1,470 employees |
| **Departments** | Research & Development (65.4%), Sales (30.3%), Human Resources (4.3%) |
| **Analysis Period** | FY 2024 |
| **Classification** | Confidential |

---

# 🔒 Data & Ethics Notice

All employee data used in this analysis is anonymized and aggregated. No personally identifiable information (PII) is present in any dataset file. Analysis and recommendations comply with applicable labor law, data protection frameworks (including GDPR where relevant), and anti-discrimination guidelines. This repository is intended for internal HR and authorized regulatory audiences only.
