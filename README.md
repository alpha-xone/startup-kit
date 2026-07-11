# Blueprint · Startup Success Playbook

> **How winners win. The success playbook to preflight's diagnostic.**

A structured success-pattern extraction engine that distills winning moves from **5,000+ verified founder stories** (StarterStory + IndieHackers + YC + MicroConf). While preflight asks "how will you die?", Blueprint asks "**how do winners win?**"

> 🇨🇳 中文版 SKILL 见 [`SKILL.zh-CN.md`](SKILL.zh-CN.md)

## 🔬 What This Does

Blueprint is the companion to [preflight](https://github.com/alpha-xone/preflight). Preflight diagnoses — Blueprint prescribes. It catalogs the specific, repeatable patterns that founders who broke $10K → $100K → $1M+ MRR actually ran — not generic advice, but **evidence-backed plays** with real names, real companies, and real outcomes.

**Not "think positive" — think *pattern-match.** * Every recommendation comes with data backing, execution checklists, and contra-indications.

## 📊 Data Powering This Skill

Blueprint is built on systematic cross-referencing of **5,000+ successful founder stories** across four primary sources:

| Source | Scale | What It Provides |
|---|---|---|
| **StarterStory** | 1,000+ founder interviews | Verified revenue data. Every figure source-checked. |
| **IndieHackers** | 5,000+ revenue-transparent founders | Longitudinal stage-transition data. Best HOW source. |
| **YC Startup School + Library** | 4,000+ YC companies | Frameworks (Graham, Thiel, Rahleff). Venture-scale patterns. |
| **MicroConf** | 100+ bootstrapped SaaS founder talks | Bootstrapped-specific patterns. The Stair-Step Approach. |
| **First Round Review** | 100+ portfolio deep-dives | Scaling-stage hiring, pricing, and team-building data. |
| **Lenny's Podcast** | 200+ product leadership interviews | PLG and growth tactics. Deep tactical conversations. |

**Methodology**: A pattern is only included if it appears across ≥3 independent sources and ≥5 founder stories. Stage-specific and model-specific tagging prevents inappropriate recommendations.

## 🧬 The Five Modules

```
Module 1: Frameworks  → 7 classic success frameworks (Helmer, Thiel, Graham, etc.)
Module 2: Stages      → Revenue stage patterns ($0→$1K→$10K→$50K→$200K→$1M+)
Module 3: Models      → Business model playbooks (SaaS, marketplace, e-com, service, content, hardware)
Module 4: Moves       → Founder move library (8 repeatable, copyable plays)
Module 5: Countermoves → Preflight 12-dimension countermove mapping
```

**Three operating modes**:
- **Benchmark Mode**: "I'm at $5K MRR building SaaS — what did others at this stage do to reach $50K?"
- **Gap Analysis**: Runs all 5 modules against your project, flags what's missing, prioritizes gaps
- **Countermove Mode**: "Preflight flagged Platform Dependency as 🔴 — how did successful founders solve this?"

## 🎯 The 8 Founder Moves

| # | Move | Best For | Data Backing |
|---|---|---|---|
| 1 | **Charge from Day 1** | Validation | 80% of $100K+/yr StarterStory founders did it |
| 2 | **Build in Public** | All stages | 5-10x audience growth, 2-3x conversion |
| 3 | **Micro-Niche Domination** | PMF + Scaling | 2x win rate, 40% lower churn |
| 4 | **Stair-Step Approach** | Bootstrapped | 70% higher survival (TinySeed) |
| 5 | **PLG Flywheel** | Scaling+ | 30-50% lower CAC vs sales-led |
| 6 | **Do Unscalable Things** | Validation | Airbnb, Stripe, Zapier — all did it |
| 7 | **Empty-Room Demo** | Idea → Validation | 60% of features added AFTER first paying users |
| 8 | **Pain-Ladder Pricing** | PMF + Scaling | $1M+ founders charge value, not cost |

## 🚀 Quick Start

### Install as a DAG Skill

```bash
# Copy to your skills directory
cp -r blueprint ~/.codewhale/skills/
```

Then just tell your agent:
> "Run Blueprint on my startup: [description]"

### Trigger Phrases

- How do successful startups do X?
- What worked for others at my stage?
- Founder playbook for [Y]
- Revenue stage benchmark
- Success pattern analysis
- Compare my startup to successful ones
- Preflight said [X] is 🔴 — how do I fix it?

## 📁 Structure

```
blueprint/
├── SKILL.md                          ← Main skill: 5 modules + 3 operating modes (English)
├── SKILL.zh-CN.md                    ← Chinese version · 中文版
├── README.md
├── references/
│   ├── success-frameworks.md         ← 7 classic frameworks (Helmer, Thiel, Graham, Hormozi, etc.)
│   ├── stage-patterns.md             ← Revenue stage patterns with case data
│   ├── model-patterns.md             ← Business model playbooks (6 models)
│   ├── founder-moves.md              ← 8 founder moves with execution checklists
│   ├── preflight-countermoves.md     ← 12-dimension Preflight countermove mapping
│   ├── data-sources.md               ← Data sources, methodology & limitations
│   └── web-design-guidelines.md      ← HTML output design system
└── assets/
    └── scorecard-template.md         ← Standard scorecard template (supports Loop review)
```

## ⚠️ What This Is NOT

- Not a formula — every startup is different. The patterns show what's worked before, not a guaranteed path.
- Not a substitute for preflight — run preflight first to find your risks, then blueprint to find your attack plan.
- Not survivorship bias unacknowledged — we explicitly catalog methodology limitations in `references/data-sources.md` (survivor bias, self-reporting bias, publication bias, geography bias).
- Not VC-only — patterns are tagged by founder type (bootstrapped vs VC, solo vs co-founder, technical vs non-technical).

---

*Built by studying 5,000+ founders who made it — so you can see the patterns they didn't know they were leaving.*
