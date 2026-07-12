# Startup Kit · Diagnose · Prescribe · Execute

> **A complete startup evaluation toolkit: preflight checks your odds, blueprint shows you how winners win.**

> 🇨🇳 中文版见 [`README.zh-CN.md`](README.zh-CN.md)

Two complementary skills built on systematic analysis of **2,500+ failed startup post-mortems** and **5,000+ successful founder stories**. Run them back-to-back: first diagnose what could kill you, then find the exact moves that winning founders used to survive and thrive.

## 📊 What Makes This Different

**Every claim is backed by real cases and real numbers.** This is not generic startup advice — it's pattern extraction from thousands of actual outcomes:

| What Most "Advice" Does | What Startup Kit Does |
|---|---|
| "Build a moat" → hand-wavy | "Build one of Helmer's 7 Powers" → each with real company examples |
| "Validate your idea" → vague | Mom Test with specific checklists, 15-conversation rule |
| "Know your unit economics" → generic | LTV > 3×CAC, GM >50%, with industry benchmarks |
| "Competition is tough" → obvious | Competition kills 53% — here's how ConvertKit beat Mailchimp |
| "Choose a channel" → abstract | One channel, milk it dry: Carrd grew to $1.5M ARR on SEO alone |

**Every future skill added to this repo will follow the same rule**: frameworks grounded in analyzed case data, not hunches or blog post wisdom.

## 🗺️ The Toolkit

```
                  ┌─────────────────┐
                  │  preflight ·    │
                  │  "how you die"  │  ← 2,500+ failures
                  │  12-dimension   │
                  │  stress test    │
                  └────────┬────────┘
                           │ "Your biggest risks are X, Y, Z"
                           ▼
                  ┌─────────────────┐
                  │  blueprint ·    │
                  │  "how you win"  │  ← 5,000+ successes
                  │  5 modules      │
                  │  8 founder moves│
                  └────────┬────────┘
                           │ "Here's how survivors solved X, Y, Z"
                           ▼
                  ┌─────────────────┐
                  │   forge (WIP)   │  ← Idea generation
                  │  gtm (WIP)      │  ← Go-to-market playbook
                  │  pricing (WIP)  │  ← Pricing lab
                  │  compass (WIP)  │  ← KPI dashboard
                  │  raise (WIP)    │  ← Fundraising suite
                  └─────────────────┘
```

### What's Inside

| Directory | Description | Data Backing |
|---|---|---|
| [`preflight/`](preflight) | 12-dimension startup health check: demand, competition, unit economics, runway, team, etc. | 1,749 failed startups ($535B burned) · CB Insights (483 post-mortems) · LOOTR heatmap · Killed by Google (307 products) |
| [`blueprint/`](blueprint) | Success playbook: 7 frameworks, 5 revenue stages, 6 business model playbooks, 8 founder moves | StarterStory (1,000+ interviews) · IndieHackers (5,000+ founders) · YC Startup School · MicroConf |

### How to Use

```bash
# Clone the entire kit
git clone https://github.com/alpha-xone/startup-kit

# Or copy individual skills to your CodeWhale skills directory
cp -r preflight ~/.codewhale/skills/
cp -r blueprint ~/.codewhale/skills/
```

Then ask your agent:

> **"Run Preflight on my idea: [description]"** → Diagnostic report
> **"Run Blueprint on my startup: [description]"** → Success pattern analysis
> **"Preflight flagged Platform Dependency as 🔴 — run Blueprint in countermove mode"** → Combined flow

## 🔬 Data Sources

### Preflight's Cemetery Data

| Source | Scale |
|---|---|
| **Loot Drop** | 1,749 failed startups, $535B burned |
| **CB Insights** | 483 post-mortems |
| **Failory** | 200+ analyses + Google/Amazon cemeteries |
| **LOOTR Heatmap** | 16 industries × 12 failure causes |
| **Killed by Google** | 307 discontinued products |
| **Unbiased Ventures** | 2024-2025 major failures |

### Blueprint's Success Data

| Source | Scale |
|---|---|
| **StarterStory** | 1,000+ founder interviews (verified revenue) |
| **IndieHackers** | 5,000+ revenue-transparent founders |
| **YC Startup School + Library** | 4,000+ YC companies |
| **MicroConf** | 100+ bootstrapped SaaS founder talks |
| **First Round Review** | 100+ portfolio deep-dives |
| **Lenny's Podcast** | 200+ product leadership interviews |

## 🧬 Each Tool at a Glance

### Preflight: The 12-Dimension Stress Test

| # | Dimension | Key Question |
|---|---|---|
| 1 | Demand Reality | Who's paying? How do they solve it now? |
| 2 | Competitive Defensibility | Can a big player replicate you in one sprint? |
| 3 | Unit Economics | LTV > 3×CAC? Gets better or worse with scale? |
| 4 | Runway & Cash | Kill criterion set? Default alive or dead? |
| 5 | Team Fit | Does anyone truly understand the user's domain? |
| 6 | Business Model Clarity | Why pay instead of free alternatives? |
| 7 | Product/Tech Feasibility | Demo-to-production gap? |
| 8 | Regulatory & Legal | Need a license? |
| 9 | Timing | Too early or too late? |
| 10 | Growth & Distribution | Where do first 1,000 users come from? |
| 11 | Platform Dependency | If the platform changes rules — can you survive? |
| 12 | Structural Resilience | Would anyone still need this in a recession? |

**Pipeline**: G0 (Discover) → G1 (Validate) → G2 (Stress-test) → G3 (Self-check) → G4 (Decide)

### Blueprint: The 5 Success Modules

```
Module 1: Frameworks   → 7 classic frameworks (Helmer, Thiel, Graham, Hormozi, etc.)
Module 2: Stages       → Revenue stage patterns ($0→$1K→$10K→$50K→$200K→$1M+)
Module 3: Models       → Business model playbooks (SaaS, marketplace, e-com, service, content, hardware)
Module 4: Moves        → Founder move library (8 repeatable, copyable plays)
Module 5: Countermoves  → Preflight 12-dimension countermove mapping
```

**3 operating modes**: Benchmark · Gap Analysis · Countermove

## 📁 Repository Structure

```
startup-kit/
├── README.md                  ← You are here
├── README.zh-CN.md            ← 中文版
├── preflight/
│   ├── SKILL.md               ← Evaluation pipeline + 12 dimensions (English)
│   ├── SKILL.zh-CN.md         ← 中文版
│   ├── README.md
│   ├── assets/
│   │   └── scorecard-template.md
│   ├── references/            ← 9 reference files (industry profiles, methodology, etc.)
│   └── scripts/               ← Python dashboard generator
├── blueprint/
│   ├── SKILL.md               ← Success playbook (English)
│   ├── SKILL.zh-CN.md         ← 中文版
│   ├── assets/
│   │   └── scorecard-template.md
│   └── references/            ← 6 reference files (frameworks, patterns, moves, etc.)
└── skills/                    ← Future companion skills (forge, gtm, pricing, compass, raise)
    └── ...
```

## 🔮 Roadmap

Skills planned for the `skills/` directory — each built on the same data-driven, case-anchored philosophy:

- **forge** — Idea generation engine (expand existing idea-forge)
- **gtm** — Go-to-market playbook: channel selection, first 1,000 users, PLG vs sales-led, enterprise sales. Distilled from real GTM case studies and founder stories
- **pricing** — Pricing lab: WTP research, pricing models, tiering strategy, value-based pricing. Rooted in real pricing experiments and outcomes
- **compass** — KPI dashboard: stage-appropriate metrics, ceiling detection, health score. Cross-referenced with industry benchmarks
- **raise** — Fundraising suite: pitch deck patterns, financial modeling, investor hunting. Drawn from YC demo day analysis and funded founder stories

## ⚠️ What This Is NOT

- **Not a crystal ball** — it uses historical patterns to tell you probabilities, not futures
- **Not a cheerleader** — preflight will tell you if the data looks bad; blueprint won't sugarcoat what you're missing
- **Not VC-only** — patterns are tagged by founder type (bootstrapped vs VC, solo vs co-founder)
- **Not survivorship bias unacknowledged** — both tools have explicit methodology limitations documented in their `references/data-sources.md`
- **Not the final word** — the decision is yours. These tools just ensure it's an evidence-backed one

---

*Built by studying 2,500+ who failed and 5,000+ who succeeded — so you can spot the patterns before you commit.*
