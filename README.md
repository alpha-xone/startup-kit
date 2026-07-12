# Startup Kit · Diagnose · Prescribe · Execute

> **A complete startup evaluation toolkit: preflight checks your odds, blueprint shows you how winners win.**

> 🇨🇳 中文版见 [`README.zh-CN.md`](README.zh-CN.md)

Six skills that take you from idea to execution, built on systematic analysis of **2,500+ failed startup post-mortems** and **5,000+ successful founder stories**.

## 📊 What Makes This Different

**Every claim is backed by real cases and real numbers.** This is not generic startup advice — it's pattern extraction from thousands of actual outcomes:

| What Most "Advice" Does | What Startup Kit Does |
|---|---|
| "Build a moat" → hand-wavy | "Build one of Helmer's 7 Powers" → each with real company examples |
| "Validate your idea" → vague | Mom Test with specific checklists, 15-conversation rule |
| "Know your unit economics" → generic | LTV > 3×CAC, GM >50%, with industry benchmarks |
| "Competition is tough" → obvious | Competition kills 53% — here's how ConvertKit beat Mailchimp |
| "Choose a channel" → abstract | One channel, milk it dry: Carrd grew to $1.5M ARR on SEO alone |

**Every skill in this repo follows the same rule**: frameworks grounded in analyzed case data, not hunches or blog post wisdom.

## 🗺️ The Pipeline

```
                    ┌──────────────┐
                    │    forge     │  ← Find problems worth solving
                    └──────┬───────┘
                           │ "What pain should I work on?"
                           ▼
                    ┌──────────────┐
                    │  preflight   │  ← 2,500+ failures
                    │ "how you die"│  ← 12-dimension stress test
                    └──────┬───────┘
                           │ "Your biggest risks are X, Y, Z"
                           ▼
                    ┌──────────────┐
                    │  blueprint   │  ← 5,000+ successes
                    │ "how you win"│  ← 5 modules, 8 founder moves
                    └──────┬───────┘
                           │ "Here's how survivors solved it"
                           ▼
                    ┌──────────────┐
                    │   pricing    │  ← Price what it's worth
                    └──────┬───────┘
                           │ "How much should I charge?"
                           ▼
                    ┌──────────────┐
                    │   compass    │  ← Track what matters
                    └──────┬───────┘
                           │ "What metrics at my stage?"
                           ▼
                    ┌──────────────┐
                    │     gtm      │  ← Go to market
                    │ "which channel│  ← backed by case data
                    │  when"       │
                    └──────────────┘
```

### What's Inside

| # | Directory | Description | Data Backing |
|---|---|---|---|
| 1 | [`forge/`](forge) | Idea generation: pain mining, quick filtering, opportunity discovery (v0.5) | Preflight G0 methodology + 16-industry failure profiles |
| 2 | [`preflight/`](preflight) | 12-dimension startup health check: demand, competition, unit economics, runway, team, etc. | 1,749 failed startups ($535B burned) · CB Insights (483 post-mortems) · LOOTR heatmap · Killed by Google (307 products) |
| 3 | [`blueprint/`](blueprint) | Success playbook: 7 frameworks, 5 revenue stages, 6 business model playbooks, 8 founder moves | StarterStory (1,000+ interviews) · IndieHackers (5,000+ founders) · YC Startup School · MicroConf |
| 4 | [`pricing/`](pricing) | Pricing lab: value-based pricing, tier design, price raise audits, 12+ real cases (v0.5) | Hormozi Value Equation + StarterStory + IndieHackers pricing outcomes |
| 5 | [`compass/`](compass) | KPI dashboard: stage-appropriate metrics ($0→$1M+), industry benchmarks, health thresholds (v0.5) | Blueprint revenue stage data + model-specific benchmarks |
| 6 | [`gtm/`](gtm) | Go-to-market playbook: 10 channels, stage-matched recommendations, 20+ case studies (v0.5) | StarterStory + IndieHackers + Blueprint cross-referencing (data confidence tags) |

### How to Use

```bash
# Clone the entire kit
git clone https://github.com/alpha-xone/startup-kit

# Or copy individual skills to your CodeWhale skills directory
cp -r forge ~/.codewhale/skills/
cp -r preflight ~/.codewhale/skills/
cp -r blueprint ~/.codewhale/skills/
cp -r pricing ~/.codewhale/skills/
cp -r compass ~/.codewhale/skills/
cp -r gtm ~/.codewhale/skills/
```

Then ask your agent:

> **"Find me ideas in [domain]"** → Forge opportunity report
> **"Run Preflight on my idea"** → Diagnostic report
> **"Run Blueprint on my startup"** → Success pattern analysis
> **"How should I price my product?"** → Pricing analysis
> **"What metrics should I track?"** → Compass dashboard
> **"Which GTM channel for my stage?"** → Channel match analysis

## 📁 Repository Structure

```
startup-kit/
├── README.md
├── README.zh-CN.md
├── forge/           ← ① Find problems
├── preflight/       ← ② Diagnose risks
├── blueprint/       ← ③ Prescribe moves
├── pricing/         ← ④ Set pricing
├── compass/         ← ⑤ Track metrics
└── gtm/             ← ⑥ Go to market
```

Every skill at the same level. Each has its own SKILL.md, SKILL.zh-CN.md, and references/.

## 🔮 Roadmap

- **forge** ✅ — Idea generation engine (v0.5)
- **preflight** ✅ — 12-dimension diagnostic
- **blueprint** ✅ — Success playbook
- **pricing** ✅ — Pricing lab (v0.5)
- **compass** ✅ — KPI dashboard (v0.5)
- **gtm** ✅ — Go-to-market playbook (v0.5)
- **raise** (WIP) — Fundraising suite: pitch deck patterns, financial modeling, investor mapping

## ⚠️ What This Is NOT

- **Not a crystal ball** — it uses historical patterns to tell you probabilities, not futures
- **Not a cheerleader** — tools tell you when data looks bad; they won't sugarcoat what you're missing
- **Not VC-only** — patterns are tagged by founder type (bootstrapped vs VC, solo vs co-founder)
- **Not survivorship bias unacknowledged** — each skill documents limitations in its `references/data-sources.md`
- **Not the final word** — the decision is yours. These tools just ensure it's an evidence-backed one

---

*Built by studying 2,500+ who failed and 5,000+ who succeeded — so you can spot the patterns before you commit.*
