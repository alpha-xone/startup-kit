---
name: compass
description: "Compass — KPI dashboard for startups. Stage-appropriate metrics ($0→$1M+) from blueprint + preflight data. Industry benchmarks for SaaS, marketplace, e-com, services, content, hardware. Triggers: 'my metrics', 'KPI dashboard', 'stage metrics', 'growth benchmarks', 'health check numbers'. v0.5. Chinese version at SKILL.zh-CN.md."
---

# Compass · KPI Dashboard

> **Know which numbers matter at your stage — and what healthy looks like.**

A stage-appropriate metrics reference built from cross-referencing blueprint's revenue stage benchmarks, preflight's failure indicators, and industry data. Shows you what to measure, what healthy looks like, and where to look when something's off.

## Core Principle

**The metrics that matter change as you grow.** Tracking enterprise benchmarks at $0 MRR is noise. Tracking "total users" at $50K MRR instead of revenue is a distraction. Compass matches metrics to your current stage.

### Three modes:

- **Dashboard**: "What metrics should I track at my stage?" → Stage-matched KPI set with healthy/warning/red thresholds
- **Diagnostic**: "My [metric] is off — what's wrong?" → Walks through failure patterns associated with that metric
- **Transition**: "Am I ready for the next stage?" → Checks key metrics against next-stage thresholds

## Stage-by-Stage Metrics

### Stage 0: Validation ($0 → $1K MRR)

| Metric | Why It Matters | 🟢 Healthy | 🟡 Warning | 🔴 Red |
|---|---|---|---|---|
| **Paying customers** | Real demand signal | ≥3 | 1-2 | 0 |
| **Revenue per paying customer** | Price-point validation | ≥$20/mo | $10-20/mo | <$10/mo |
| **Mom Test commitments** | Conversations quality | ≥3 concrete commitments from 15 convos | 1-2 | 0 |
| **Time to first paid customer** | Speed of feedback | <30 days | 30-60 days | >60 days |

**Focus**: Revenue > users. One paying customer > 1,000 free signups.

### Stage 1: PMF ($1K → $10K MRR)

| Metric | 🟢 Healthy | 🟡 Warning | 🔴 Red |
|---|---|---|---|
| **Monthly churn** | <5% | 5-8% | >8% |
| **Word-of-mouth % of new users** | >20% | 10-20% | <10% |
| **LTV:CAC** | >3:1 | 2-3:1 | <2:1 |
| **Net revenue retention** | >100% | 90-100% | <90% |
| **NPS** | >40 | 20-40 | <20 |

**Focus**: Retention > acquisition. If churn > growth, nothing else matters.

### Stage 2: Scaling ($10K → $50K MRR)

| Metric | 🟢 Healthy | 🟡 Warning | 🔴 Red |
|---|---|---|---|
| **Monthly MRR growth** | >15% | 10-15% | <10% |
| **Annual plan %** | >30% | 15-30% | <15% |
| **Gross margin (SaaS)** | >80% | 60-80% | <60% |
| **Expansion revenue** | >20% of new | 10-20% | <10% |
| **CAC payback** | <12 months | 12-18 months | >18 months |

**Focus**: Growth efficiency + pricing optimization.

### Stage 3: Team ($50K → $200K MRR)

| Metric | 🟢 Healthy | 🟡 Warning | 🔴 Red |
|---|---|---|---|
| **Revenue per employee (SaaS)** | >$150K | $100-150K | <$100K |
| **Customer concentration** | <15% | 15-30% | >30% |
| **Support tickets per customer/mo** | <3 | 3-5 | >5 |
| **Employee churn** | <10% | 10-20% | >20% |

**Focus**: Delegation, process, team scalability.

### Stage 4: Engine ($200K → $1M+ MRR)

| Metric | 🟢 Healthy | 🟡 Warning | 🔴 Red |
|---|---|---|---|
| **Growth channels** | ≥4 independent | 2-3 | 1 |
| **Revenue per employee (SaaS)** | >$200K | $150-200K | <$150K |
| **Net revenue retention** | >110% | 100-110% | <100% |
| **Multi-product % of revenue** | >20% | 10-20% | <10% |

**Focus**: Multi-channel compounding, product-line expansion.

## Model-Specific Benchmarks

| Model | Critical Metric | 🟢 Healthy | 🟡 Warning | Source |
|---|---|---|---|---|
| **SaaS** | Monthly churn | <3% | 3-5% | Blueprint model-patterns |
| **Marketplace** | Take rate | >15% | 10-15% | Blueprint model-patterns |
| **E-commerce DTC** | Gross margin | >65% | 50-65% | Blueprint model-patterns |
| **Services** | Billable utilization | >70% | 50-70% | Blueprint model-patterns |
| **Content/Media** | Revenue per subscriber | >$2/mo | $1-2/mo | Blueprint model-patterns |
| **Hardware** | Return rate | <5% | 5-10% | Blueprint model-patterns |

## Output Format

```
## 🧭 Compass: KPI Dashboard

### Your Stage: [PMF / Scaling / etc.]

### Critical Metrics
| Metric | Your Value | Benchmark | Status |
|---|---|---|---|
| [Metric 1] | [value] | [healthy range] | 🟢/🟡/🔴 |
| [Metric 2] | [value] | [healthy range] | 🟢/🟡/🔴 |

### Top Risk
[Metric furthest from healthy + action recommendation]

### Next-Stage Readiness
[Key blockers before transitioning]
```

## Reference Files

| File | Purpose |
|---|---|
| `references/stage-metrics.md` | Full stage-by-stage metric table with formulas |
| `references/model-benchmarks.md` | Business-model-specific benchmarks |

## Output Rules

- **Stage-appropriate**: Only show metrics relevant to the user's current stage
- **Thresholds matter**: Every metric has 🟢🟡🔴 thresholds — no "track this" without "what good looks like"
- **Action-oriented**: A red metric includes a recommendation, not just a warning
- **Cross-reference preflight**: If preflight flagged a risk, highlight the corresponding metric
