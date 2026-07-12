---
name: blueprint
description: "Blueprint — the success playbook to preflight's diagnostic. Distills winning patterns from 5,000+ founder stories (StarterStory + IndieHackers + YC + MicroConf). Complements preflight: preflight asks 'how will you die?', Blueprint asks 'how do winners win?' 5 modules: 7 classic frameworks, revenue stage patterns, business model playbooks, founder move library, and Preflight 12-dimension countermoves. Trigger: 'how do successful startups do X', 'how do I win at this stage', 'founder playbook for Y', 'success pattern analysis', 'blueprint for my startup', 'what should I do to win'. Outputs structured Markdown + stage-matched benchmarks + prioritized action list. Optional HTML dashboard. Chinese version at SKILL.zh-CN.md."
---

# Blueprint · 从成功者视角提炼

A structured success-pattern extraction engine. While Preflight asks "what kills startups" from 2,500+ post-mortems, this skill asks "what do the winners actually do" from 5,000+ verified revenue stories.

**Core thesis**: Success leaves fingerprints. Across StarterStory (1,000+ cases), IndieHackers (5,000+ revenue-transparent founders), YC Startup School, and MicroConf, the same patterns repeat. Founders who break $10K MRR, then $100K, then $1M+ are not lucky — they run the same plays. This skill catalogs those plays.

## Core Mental Model

**A mirror, not a rulebook.** Every startup is different, but the patterns that work are finite. This skill works in three modes:

- **Benchmark Mode**: "I'm at $5K MRR building SaaS — what did others at this stage do to reach $50K?" → Matches you to revenue stage + business model + founder type peers
- **Gap Analysis Mode**: "Here's my startup. Which of the proven success patterns am I missing?" → Runs all 5 modules against your description, flags gaps
- **Countermove Mode**: "Preflight flagged my Platform Dependency as 🔴 — how did successful founders solve this?" → Cross-references Preflight dimensions with success countermoves

---

## The Five Modules

### Module 1: Seven Classic Success Frameworks

The theoretical backbone. These are the frameworks that successful founders consistently rediscover — tested across decades and thousands of companies. Details in `references/success-frameworks.md`.

| # | Framework | Core Question | Best For |
|---|---|---|---|
| 1 | **Helmer's 7 Powers** | What's your sustainable competitive advantage? | Strategy, defensibility |
| 2 | **Thiel's 7 Questions** | Are you building a monopoly or competing? | Zero-to-one ventures |
| 3 | **Graham's "Do Things That Don't Scale"** | What unscalable move will create your moat? | $0→$1K stage |
| 4 | **The Mom Test** | Are you learning or collecting false positives? | Idea validation |
| 5 | **Lean MVP Loop** | Are you building the smallest thing that teaches? | Product development |
| 6 | **Hormozi's Value Equation** | Why would anyone pay for this? | Pricing, positioning |
| 7 | **Rachleff's PMF Test** | Are users pulling the product out of your hands? | Growth inflection |

> **Usage**: When a user asks "how do I build a moat" or "how do I validate this idea," map the question to the right framework and walk through the diagnostic.

### Module 2: Revenue Stage Patterns

What successful founders actually did at each revenue milestone. Based on cross-referencing StarterStory + IndieHackers revenue data. Details in `references/stage-patterns.md`.

| Stage | Revenue | Core Challenge | Winning Pattern | Signal You're Stuck |
|---|---|---|---|---|
| **Validation** | $0 → $1K/mo | Does anyone pay? | Pre-sell + charge day 1 | "Great idea" but no money |
| **PMF** | $1K → $10K/mo | Do they stay and tell others? | One channel + narrow pricing | Churn > growth |
| **Scaling** | $10K → $50K/mo | Can you grow without breaking? | Outbound + pricing + upsell | 3-month plateau |
| **Team** | $50K → $200K/mo | Can you delegate? | Process + specialists + paid ads | Founder is bottleneck |
| **Engine** | $200K → $1M+/mo | Can you compound? | Multi-channel + PLG + brand | Only optimizing, not expanding |

**Key stat from StarterStory data**: 42% of founders who crossed $10K MRR attributed their first growth inflection to **word of mouth** — not ads, not content marketing, not cold outreach. They did something so right that users told other users.

### Module 3: Business Model Playbooks

Different models demand different success patterns. A marketplace founder needs completely different moves than a SaaS founder. Details in `references/model-patterns.md`.

| Model | Winning Pattern | Critical Metric | Classic Trap |
|---|---|---|---|
| **SaaS** | Vertical-first → land-and-expand | Churn <5%, LTV:CAC >3 | Building horizontal too early |
| **Marketplace** | Supply constraint → one geo → expand | Liquidity ratio, take rate >15% | Too big too fast |
| **E-commerce/DTC** | Differentiated product + organic content | GM >60%, repeat purchase >30% | VC-subsidized CAC |
| **Services/Agency** | Specialize → productize → scale process | Utilization >70%, margin >40% | Founder as bottleneck |
| **Content/Media** | Niche authority → community → monetize | Revenue per subscriber | Ad-only ceiling |
| **Hardware** | Pre-sell → crowdfund → iterate → DTC | GM >40%, return <5% | Demo ≠ mass production |

### Module 4: Founder Move Library

Repeatable, tested "plays" that successful founders run. These are not strategies — they are specific, copyable actions. Details in `references/founder-moves.md`.

| # | Move | What It Looks Like | Data Backing | Stage |
|---|---|---|---|---|
| 1 | **Charge from Day 1** | Pre-sell, consulting, waitlist deposits | 80% of $100K/yr+ StarterStory founders | Validation |
| 2 | **Build in Public** | Share revenue, struggles on Twitter/LinkedIn | 5-10x audience growth, 2-3x conversion | All stages |
| 3 | **Micro-Niche Domination** | "CRM for dog groomers" not "CRM" | 2x win rate, 40% lower churn | PMF, Scaling |
| 4 | **Stair-Step Approach** | Services → productize → SaaS → scale | 70% higher survival (TinySeed data) | Bootstrapped |
| 5 | **PLG Flywheel** | Free tier → aha moment → viral → upgrade | 30-50% lower CAC vs sales-led | Scaling+ |
| 6 | **Do Unscalable Things** | Manual onboarding, hand-written emails | Airbnb, Stripe, Zapier — all did this | Validation |
| 7 | **Empty-Room Demo** | Bare prototype → watch hesitation → build that | 60% of features added AFTER first paying users | Validation |
| 8 | **Pain-Ladder Pricing** | Save $10K = charge $3K. Nice-to-have = $10/mo | Consistently separates $1M+ from $100K founders | PMF, Scaling |

### Module 5: Preflight Countermoves

For every way a startup can die (Preflight's 12 dimensions), there is a proven countermove that successful founders used to neutralize that risk. Details in `references/preflight-countermoves.md`.

| Preflight Dimension | Success Countermove | Key Principle |
|---|---|---|
| 1. Demand Reality | Extract commitments, not opinions | Mom Test: pre-orders > "sounds great" |
| 2. Competitive Defensibility | Build one of Helmer's 7 Powers BEFORE scaling | Last-mover advantage > first-mover advantage |
| 3. Unit Economics | LTV:CAC >3 from day 1, GM >50% | Charge what it's worth, not what competitors charge |
| 4. Runway & Cash | Default-alive plan. Bootstrapped: profitable at $10K | "The next round will come" is not a plan |
| 5. Team Fit | Founder-market fit: domain expertise OR obsessive empathy | Solo founders compensated with speed |
| 6. Business Model Clarity | One dollar from one customer before many | One clear revenue stream first |
| 7. Product/Tech Feasibility | Ship ugly. v1 should embarrass you. | "If not embarrassed by v1, you launched too late" |
| 8. Regulatory | Build compliance as moat, not obstacle | "Only we can" because "we understand the rules" |
| 9. Timing | Catch a wave you didn't create | "Why now?" > "why?" |
| 10. Growth & Distribution | One channel, milk it dry, then add a second | Depth > breadth in go-to-market |
| 11. Platform Dependency | Stage 3+ on Wrapper Depth Scale | Proprietary data/vertical knowledge as moat |
| 12. Structural Resilience | Demand must exist regardless of macro | "Would anyone still need this in a recession?" |

---

## How to Run This Skill

### Step 1: Determine Mode

Ask the user — or infer from their question:
- "How did others at my stage succeed?" → **Benchmark Mode**
- "What am I missing?" → **Gap Analysis Mode**
- "Preflight flagged X — how to fix?" → **Countermove Mode**

### Step 2: Gather Context

For Gap Analysis and Benchmark modes, collect:
- Current revenue (or stage: idea / validation / launched / growing)
- Business model (SaaS / marketplace / e-commerce / service / content / hardware)
- Founder profile (solo / co-founder, technical / non-technical, bootstrapped / VC)
- Biggest current challenge (one sentence)

### Step 3: Match and Report

| Mode | Action |
|---|---|
| **Benchmark** | Match to revenue stage + business model → pull stage patterns + model playbook → report 3-5 most relevant peer moves |
| **Gap Analysis** | Run all 5 modules against context → flag "patterns present" vs "patterns missing" → prioritize top 3 gaps with specific moves |
| **Countermove** | Map Preflight dimension to success countermove → show 2-3 real-world examples of founders who solved this → suggest specific action |

### Step 4: Output

Default format: Structured Markdown report.

```
## 📊 Blueprint Analysis

### Your Context
[Revenue stage / model / founder type / challenge]

### Module 1: Framework Fit
[Most relevant framework + diagnostic]

### Module 2: Stage Benchmark
| Pattern | You | Peers | Gap |
|---|---|---|---|

### Module 3: Model Playbook
[Business-model-specific winning moves + your status]

### Module 4: Founder Moves
[Ranked list of highest-impact moves you should try]

### Module 5: Preflight Countermoves
[If Preflight was run: dimension-by-dimension countermoves]

### Top 3 Actions
1. [Most immediate, highest-impact move]
2. [Next]
3. [Next]

### Peer References
[2-3 real founder stories at your stage from StarterStory/IndieHackers]
```

---

## Multi-Project Comparison Mode

Compare 2-4 projects against success patterns: run Benchmark Mode on each → output side-by-side stage-appropriateness and move completion.

## HTML Output

When the user wants a visual report: generate self-contained HTML with:
- Project overview card
- Stage-progress indicator (which stage are you at? which stage patterns are you hitting?)
- Move completion radar (8 founder moves, scored)
- Peer benchmark table
- Action priority list

Styling: `references/web-design-guidelines.md`.

---

## Integration with Preflight

This skill is designed to be the **second step** after Preflight:

1. **Run Preflight** → "Here's how you could die. Biggest risks: [X, Y, Z]"
2. **Run Blueprint (Countermove Mode)** → "Here's how founders who survived those risks did it. Top moves: [A, B, C]"

The two skills share vocabulary: Preflight's 12 dimensions map 1:1 to Module 5 countermoves. When running Countermove Mode, always pull the latest Preflight scorecard first.

---

## Reference Files

| File | Purpose |
|---|---|
| `references/success-frameworks.md` | Deep-dive on each of the 7 classic frameworks |
| `references/stage-patterns.md` | Detailed revenue stage patterns with case data |
| `references/model-patterns.md` | Business-model-specific playbooks |
| `references/founder-moves.md` | Full founder move library with examples |
| `references/preflight-countermoves.md` | 12-dimension countermove mapping |
| `references/data-sources.md` | Data sources, methodology, and credibility notes |
| `references/web-design-guidelines.md` | HTML output design system |
| `assets/scorecard-template.md` | Standard scorecard template |

---

## Output Rules

- **Real cases required**: Every pattern recommendation must be backed by ≥1 real founder story (name + company + outcome) from StarterStory, IndieHackers, YC, or MicroConf
- **Stage-appropriateness**: Don't recommend PLG to someone at $0 MRR. Don't recommend "charge from day 1" to someone with $500K MRR who needs an acquisition channel
- **Model-appropriateness**: Don't recommend SaaS patterns to a marketplace founder
- **Action-first**: Every report must end with a concrete Top 3 Actions the founder can take THIS week
- **Language**: Match the user's language. For Chinese users, see `SKILL.zh-CN.md`
- **Complement, don't compete**: If user has Preflight data, always cross-reference. If they haven't run Preflight, suggest it for the full picture
