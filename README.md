# Startup Kit · Diagnose · Prescribe · Execute

> **A complete startup evaluation toolkit: preflight checks your odds, blueprint shows you how winners win.**

> 🇨🇳 中文版见 [`README.zh-CN.md`](README.zh-CN.md)

Six skills that take you from idea to execution, built on systematic analysis of **2,500+ failed startup post-mortems** and **5,000+ successful founder stories**.

A companion suite, the [**AI-Native SDLC Kit**](https://github.com/alpha-xone/ai-native-sdlc-kit), covers the software delivery process itself — the six stages of Anthropic's AI-Native SDLC playbook, plus the project skeleton that says where each artifact lives and which layer actually blocks. It lives in its own repository; see [below](#-companion-ai-native-sdlc-kit).

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
# Clone the kit
git clone https://github.com/alpha-xone/startup-kit

# Copy the six skills into your agent's user-level skill root.
# Pick the path that matches your harness:
#   CodeWhale   ~/.codewhale/skills/
#   DSH         ~/.dsh/skills/
#   WorkBuddy   ~/.workbuddy-ai/skills/
SKILLS=~/.dsh/skills

cp -r forge preflight blueprint pricing compass gtm "$SKILLS"/
```

Then ask your agent:

> **"Find me ideas in [domain]"** → Forge opportunity report
> **"Run Preflight on my idea"** → Diagnostic report
> **"Run Blueprint on my startup"** → Success pattern analysis
> **"How should I price my product?"** → Pricing analysis
> **"What metrics should I track?"** → Compass dashboard
> **"Which GTM channel for my stage?"** → Channel match analysis

### Syncing the whole skill set across machines

This repo ships the six skills above. A working agent usually has **more than six**
skills installed — third-party bundles that have no common upstream and cannot be
reproduced by installing the harness alone.

Those are mirrored separately in the **private** repo `alpha-xone/dsh-skills`,
whose root *is* the DSH skill root. On a new machine:

```powershell
git clone https://github.com/alpha-xone/dsh-skills.git
cd dsh-skills
powershell -ExecutionPolicy Bypass -File _sync\install.ps1   # first time
powershell -ExecutionPolicy Bypass -File _sync\sync.ps1      # updates
```

It is private because it contains third-party bundles whose redistribution terms
this repo does not control. The six skills in *this* repo remain the authoritative
source for their own content — edit them here, then re-copy into the mirror. (The
`ai-sdlc-*` skills have their own authoritative source: the
[AI-Native SDLC Kit](https://github.com/alpha-xone/ai-native-sdlc-kit).)

### Report rendering

Reports (HTML) are rendered by delegation, not by a stylesheet hardcoded in this repo:

| Layer | Owner | Default |
|---|---|---|
| Visual design | `impeccable` skill | **Light** mode |
| Every chart | `diagram-design` skill | **Light** templates |
| Content contract + status semantics | each skill's `references/web-design-guidelines.md` | GO / 迭代 / KILL |

Install those two skills alongside Startup Kit. Without them, preflight falls back to `scripts/generate-dashboard.py` — structurally complete, but styled with the deprecated palette.

## 🧭 Companion: AI-Native SDLC Kit

The six skills above cover the **startup** process. The **software delivery** process — the six stages of Anthropic's [The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook), turned into invocable skills plus a project skeleton — lives in its own repository:

> **[github.com/alpha-xone/ai-native-sdlc-kit](https://github.com/alpha-xone/ai-native-sdlc-kit)**

| Stage | Skill | The play |
|---|---|---|
| ① Plan | `ai-sdlc-plan` | Produce `intent.md` in the originator's own words; product owner accepts or closes |
| ② Design | `ai-sdlc-design` | Requirements and design in one session; policy applied as constraint; contradictions flagged |
| ③ Build | `ai-sdlc-build` | Nothing implemented without an approved `plan.md` |
| ④ Test | `ai-sdlc-test` | A feedback loop the agent runs itself |
| ⑤ Deploy | `ai-sdlc-deploy` | AI reviews both directions; the agent cannot pass the production gate |
| ⑥ Maintain | `ai-sdlc-maintain` | Deterministic detector + control bands; a breach returns as a new `intent.md` |

That repo also carries the **repository side**: `SDLC.md` (artifact → path binding, gate owners), `ENFORCEMENT.md` (enforced / advisory / missing), six policy-skill skeletons, a project template with a `venture/` handoff, and `factory/scripts/New-Project.ps1` — a generator that scaffolds a project self-contained, with its governance docs committed alongside it.

**Why it is separate**: it distills Anthropic's playbook; this repo distills founder case data (StarterStory / IndieHackers / YC / MicroConf). Different sources, different licensing to reason about, different release cadence — one repository would have forced one licence to cover both.

The two halves meet at stage 0: run `forge` → `preflight` → `blueprint` here, then land the result in a generated project's `venture/`, where it constrains every subsequent spec.

## 📁 Repository Structure

```
startup-kit/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── NOTICE
├── forge/            ← ① Find problems
├── preflight/        ← ② Diagnose risks
├── blueprint/        ← ③ Prescribe moves
├── pricing/          ← ④ Set pricing
├── compass/          ← ⑤ Track metrics
└── gtm/              ← ⑥ Go to market
```

Every skill at the same level. Each has its own SKILL.md, SKILL.zh-CN.md, and references/.

## 🔮 Roadmap

- **forge** ✅ — Idea generation engine (v0.5)
- **preflight** ✅ — 12-dimension diagnostic
- **blueprint** ✅ — Success playbook
- **pricing** ✅ — Pricing lab (v0.5)
- **compass** ✅ — KPI dashboard (v0.5)
- **gtm** ✅ — Go-to-market playbook (v0.5)
- **ai-sdlc** ✅ — moved to [its own repository](https://github.com/alpha-xone/ai-native-sdlc-kit) (v1.0)
- **raise** (WIP) — Fundraising suite: pitch deck patterns, financial modeling, investor mapping

## ⚠️ What This Is NOT

- **Not a crystal ball** — it uses historical patterns to tell you probabilities, not futures
- **Not a cheerleader** — tools tell you when data looks bad; they won't sugarcoat what you're missing
- **Not VC-only** — patterns are tagged by founder type (bootstrapped vs VC, solo vs co-founder)
- **Not survivorship bias unacknowledged** — each skill documents limitations in its `references/data-sources.md`
- **Not the final word** — the decision is yours. These tools just ensure it's an evidence-backed one

## License

MIT — see [`LICENSE`](LICENSE). These skills distill publicly available case data and published frameworks; [`NOTICE`](NOTICE) records those sources and states what the licence does and does not cover.

---

*Built by studying 2,500+ who failed and 5,000+ who succeeded — so you can spot the patterns before you commit.*
