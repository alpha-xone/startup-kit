# Preflight · Startup Health Check

> **Check your startup's vitals before you commit your life to it.**

A 12-dimension evaluation system that turns "fuzzy idea → evidence-backed build decision." Doesn't just tell you whether your project will die — tells you *exactly how to survive*.

> 🇨🇳 中文版 SKILL 见 [`SKILL.zh-CN.md`](SKILL.zh-CN.md)

## 🔬 What This Does

Preflight is what you get when you cross a veteran VC with a bloodthirsty devil's advocate. It distills thousands of failed-company post-mortems into an executable diagnostic framework that finds fatal problems *before* you make the big bet.

**Not generic startup advice** — every dimension is backed by real data and real cases with real dollar amounts.

## 📊 Data Powering This Skill

Preflight is built on systematic analysis of **2,500+ public startup post-mortems** and **307 discontinued Big Tech products**:

| Source | Scale | Key Findings |
|---|---|---|
| **Loot Drop** | 1,749 failed startups, $535B burned | 7 failure anti-patterns, 22 categories, 16 industries |
| **CB Insights** | 483 post-mortems | Competition kills 53%, no market need 42%, ran out of cash 29% |
| **Failory** | 200+ analyses + Google Cemetery (100+) + Amazon Cemetery (50+) | Cross-industry deep-dives |
| **LOOTR Heatmap** | 16 industries × 12 failure causes | Competition is #1 in every single industry |
| **Killed by Google** | 307 discontinued products | Five Google death patterns |
| **Kaggle CB Insights Dataset** | 890 startups (1992-2024) | Avg lifespan 8 years; funding-lifespan correlation +19.8% |
| **Product Grave** | 99 dead tech products | Pixel-art graveyard + AI pre-mortem oracle |
| **Unbiased Ventures** | 2024-2025 major failures | 7 VC scoring dimension mapping |

## 🧬 The Pipeline: G0 → G4

```
G0: Discover    → Is there a real pain point worth solving?
G1: Validate    → Is the pain real, big enough, will someone pay?
G2: Stress-test → 12-dimension unified diagnosis (the core)
G3: Self-check  → Right timing? Right founder?
G4: Decide      → GO / Iterate / KILL + Kill Criteria
```

**Fail-fast mentality**: Gates get more expensive as you go. An idea that should die at G1 doesn't get a free pass to G3.

## 🩺 The 12 Dimensions (G2 — Core)

Every dimension is mandatory for all projects. Deep-dive depth adjusts automatically based on project characteristics (platform-dependent, hardware, regulated, marketplace, B2C consumer, policy-driven):

| # | Dimension | Historical Data | Key Question |
|---|-----------|----------------|---------------|
| 1 | Demand Reality | 42% of startups die from this | Who's paying? How do they solve it now? |
| 2 | Competitive Defensibility | #1 killer, 53% | Can a big player replicate you in one sprint? |
| 3 | Unit Economics | Consumer #2 killer, 114 cases | LTV > 3×CAC? Gets better or worse with scale? |
| 4 | Runway & Cash | 29%, China: 25% survive 6 months | How long is the runway? Kill criterion set? |
| 5 | Team Fit | 20-23%, 85% die from cognitive mismatch | Does anyone truly understand the user's domain? |
| 6 | Business Model Clarity | 10%, Vine 200M MAU→no monetization→dead | Why pay instead of using free alternatives? |
| 7 | Product/Tech Feasibility | 15% (Hardware #1) | Demo-to-production gap? |
| 8 | Regulatory & Legal | 12% (Finance/Telecom: fatal-level) | Need a license? Customer money in your hands? |
| 9 | Timing | 8%, too early kills more than too late | Do users need to change behavior? |
| 10 | Growth & Distribution | Universal | Specific channel for first 1,000 users? |
| 11 | Platform Dependency | 76% AI thin-wrapper deaths (generalizable) | If platform changes rules/pricing — can you survive? |
| 12 | Structural Resilience | China 5 cycles: getihu→solopreneur | Independent demand or policy/narrative-driven? |

## 🎯 Features

- **Multi-project comparison** — Rank multiple ideas, find which one deserves your attention
- **Loop review** — Re-evaluate the same project over time; track delta changes and kill criteria
- **Industry-specific diagnostics** — 16 industry failure profiles
- **Big Tech insights** — Learn from Google, Amazon, Microsoft, Apple patterns
- **HTML dashboard** — Self-contained, design-system-driven reports with radar charts

## 🚀 Quick Start

### Install as a DAG Skill

```bash
# Copy to your skills directory
cp -r preflight ~/.codewhale/skills/
```

Then just tell your agent:
> "Evaluate this idea with Preflight: [description]"

### Trigger Phrases

Anything that means "I want an evidence-based, honest assessment":
- Evaluate this idea
- Is this project viable?
- Help me decide whether to build this
- Will this survive?
- Compare these ideas — which one should I pursue?
- Post-mortem: why did this project fail?

## 📁 Structure

```
preflight/
├── SKILL.md                          ← Main evaluation pipeline + 12 dimensions (English)
├── SKILL.zh-CN.md                    ← Chinese version · 中文版
├── README.md
├── references/
│   ├── conditional-diagnostics.md    ← Deep-dive questions (indexed by project characteristic)
│   ├── industry-profiles.md          ← 16 industries × 12 failure causes
│   ├── big-tech-graveyard.md         ← Google/Amazon/Microsoft graveyard
│   ├── data-sources.md               ← Methodology & limitations
│   ├── discover.md                   ← G0 Discovery method
│   ├── validate.md                   ← G1 Validation method
│   ├── checklist.md                  ← G3 Self-check
│   ├── scoring.md                    ← G4 Scoring rubrics & thresholds
│   └── web-design-guidelines.md      ← HTML design system
├── assets/
│   └── scorecard-template.md         ← Loop scorecard template
└── scripts/
    ├── scorecard.py                  ← Init/append scorecards
    └── generate-dashboard.py         ← Generate HTML dashboards
```

## ⚠️ What This Is NOT

- Not a crystal ball — it won't tell you the future. It uses historical patterns to tell you probabilities.
- Not a cheerleader — if the data doesn't look good for your project, it'll say so.
- Not the final word — the G4 decision (GO/KILL) is **yours** to make. This just ensures it's an evidence-backed one.

---

*Built by studying 2,500+ startups that didn't make it — so you can.*
