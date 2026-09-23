# Startup Kit · Diagnose · Prescribe · Execute

> **A complete startup evaluation toolkit: preflight checks your odds, blueprint shows you how winners win.**

> 🇨🇳 中文版见 [`README.zh-CN.md`](README.zh-CN.md)

Six skills that take you from idea to execution, built on systematic analysis of **2,500+ failed startup post-mortems** and **5,000+ successful founder stories**.

A second suite, [**AI-Native SDLC**](#-ai-native-sdlc-kit-skills-712), covers the software delivery process itself — the six stages of Anthropic's AI-Native SDLC playbook, mapped stage by stage onto this harness.

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
                    ┌───────────────┐
                    │  preflight    │  ← 2,500+ failures
                    │ "how you die" │  ← 12-dimension stress test
                    └──────┬────────┘
                           │ "Your biggest risks are X, Y, Z"
                           ▼
                    ┌───────────────┐
                    │  blueprint    │  ← 5,000+ successes
                    │ "how you win" │  ← 5 modules, 8 founder moves
                    └──────┬────────┘
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
                    ┌──────────────────────┐
                    │     gtm              │  ← Go to market
                    │ "which channel when" │  ← backed by case data
                    └──────────────────────┘
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

# AI-Native SDLC kit (six stages)
cp -r ai-sdlc-plan ai-sdlc-design ai-sdlc-build ~/.codewhale/skills/
cp -r ai-sdlc-test ai-sdlc-deploy ai-sdlc-maintain ~/.codewhale/skills/
```

Then ask your agent:

> **"Find me ideas in [domain]"** → Forge opportunity report
> **"Run Preflight on my idea"** → Diagnostic report
> **"Run Blueprint on my startup"** → Success pattern analysis
> **"How should I price my product?"** → Pricing analysis
> **"What metrics should I track?"** → Compass dashboard
> **"Which GTM channel for my stage?"** → Channel match analysis

### Report rendering

Reports (HTML) are rendered by delegation, not by a stylesheet hardcoded in this repo:

| Layer | Owner | Default |
|---|---|---|
| Visual design | `impeccable` skill | **Light** mode |
| Every chart | `diagram-design` skill | **Light** templates |
| Content contract + status semantics | each skill's `references/web-design-guidelines.md` | GO / 迭代 / KILL |

Install those two skills alongside Startup Kit. Without them, preflight falls back to `scripts/generate-dashboard.py` — structurally complete, but styled with the deprecated palette.

## 🧭 AI-Native SDLC Kit (skills 7–12)

The six skills above cover the **startup** process. These six cover the **software delivery** process: the six stages of Anthropic's [The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook), turned into invocable skills — with every harness mechanism **mapped to its DeepSeek Harness equivalent, or explicitly marked as having none**.

| Stage | Skill | The play |
|---|---|---|
| ① Plan | [`ai-sdlc-plan/`](ai-sdlc-plan) | Produce `intent.md` in the originator's own words; product owner accepts or closes |
| ② Design | [`ai-sdlc-design/`](ai-sdlc-design) | Requirements and design in one session; policy applied as constraint; contradictions flagged |
| ③ Build | [`ai-sdlc-build/`](ai-sdlc-build) | Nothing implemented without an approved `plan.md`; knowledge in `AGENTS.md` and skills |
| ④ Test | [`ai-sdlc-test/`](ai-sdlc-test) | A feedback loop the agent runs itself; the agent's own config gets regression-tested |
| ⑤ Deploy | [`ai-sdlc-deploy/`](ai-sdlc-deploy) | AI reviews both directions; gates enforced as policy; the agent cannot pass the production gate |
| ⑥ Maintain | [`ai-sdlc-maintain/`](ai-sdlc-maintain) | Deterministic detector + control bands; a breach returns as a new `intent.md` |

**Start here**: [`AI-SDLC-SKILLS.md`](AI-SDLC-SKILLS.md) — role→skill mapping, adoption order, a full worked example, and a dedicated section on **which controls do not exist in DSH** (network egress allowlists, per-path secret denies, a managed-settings tier, `claude -p`, worktree isolation).

> ⚠️ These six skills own **process** (what happens, what artifact it leaves, who approves at the gate). Craft belongs to the harness's existing skills: `test`, `verify`, `webapp-testing`, `review`, `security-review`, `debug`, `plan`, `frontend-design`, `impeccable`.

## 📁 Repository Structure

```
startup-kit/
├── README.md
├── README.zh-CN.md
├── AI-SDLC-SKILLS.md
├── forge/            ← ① Find problems
├── preflight/        ← ② Diagnose risks
├── blueprint/        ← ③ Prescribe moves
├── pricing/          ← ④ Set pricing
├── compass/          ← ⑤ Track metrics
├── gtm/              ← ⑥ Go to market
├── ai-sdlc-plan/     ← SDLC ① Plan
├── ai-sdlc-design/   ← SDLC ② Design
├── ai-sdlc-build/    ← SDLC ③ Build
├── ai-sdlc-test/     ← SDLC ④ Test
├── ai-sdlc-deploy/   ← SDLC ⑤ Deploy
└── ai-sdlc-maintain/ ← SDLC ⑥ Maintain
```

Every skill at the same level. Each has its own SKILL.md, SKILL.zh-CN.md, and references/.

## 🔮 Roadmap

- **forge** ✅ — Idea generation engine (v0.5)
- **preflight** ✅ — 12-dimension diagnostic
- **blueprint** ✅ — Success playbook
- **pricing** ✅ — Pricing lab (v0.5)
- **compass** ✅ — KPI dashboard (v0.5)
- **gtm** ✅ — Go-to-market playbook (v0.5)
- **ai-sdlc** ✅ — AI-native SDLC six-stage kit (v1.0); usage guide at [`AI-SDLC-SKILLS.md`](AI-SDLC-SKILLS.md)
- **raise** (WIP) — Fundraising suite: pitch deck patterns, financial modeling, investor mapping

## ⚠️ What This Is NOT

- **Not a crystal ball** — it uses historical patterns to tell you probabilities, not futures
- **Not a cheerleader** — tools tell you when data looks bad; they won't sugarcoat what you're missing
- **Not VC-only** — patterns are tagged by founder type (bootstrapped vs VC, solo vs co-founder)
- **Not survivorship bias unacknowledged** — each skill documents limitations in its `references/data-sources.md`
- **Not the final word** — the decision is yours. These tools just ensure it's an evidence-backed one

---

*Built by studying 2,500+ who failed and 5,000+ who succeeded — so you can spot the patterns before you commit.*
