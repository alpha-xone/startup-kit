---
name: preflight
description: "Preflight — 12-dimension startup evaluation system that checks your project's survival odds before you commit. Powered by: Loot Drop (1,749 failed startups, $535B burned) · CB Insights (483 post-mortems: competition 53% / no market need 42% / ran out of cash 29%) · Failory (200+ analyses, Google Cemetery 100+ products, Amazon Cemetery 50+) · LOOTR heatmap (16 industries × 12 failure causes) · Killed by Google (307 discontinued products) · Kaggle CB Insights dataset (890 startups SQL analysis, 1992-2024) · Product Grave (99 dead tech products) · Unbiased Ventures (2024-2025 major failures, 7 VC dimensions). Chinese version available at SKILL.zh-CN.md. Trigger when the user says 'evaluate this idea', 'is this project viable', 'help me decide whether to build this', 'will this survive', 'compare these ideas', 'post-mortem analysis'. Outputs HTML dashboard/report, supports multi-project comparison and loop review. Five-gate pipeline (G0→G4), all industries and project types."
---

# Preflight · Startup Health Check

A structured evaluation system that turns "fuzzy idea → evidence-backed build decision." Powered by data from 2,500+ startup post-mortems, 16-industry failure heatmaps, and 307 killed Big Tech products.

## Core Mental Model

**A funnel + a loop.**

- **Funnel (fail-fast)**: Five gates G0→G4, each more expensive than the last. An idea that should die at G1 doesn't get a free pass to G3.
- **Loop (review)**: After each run, write results to a scorecard. On re-evaluation, load the previous round → compute deltas → check kill criteria → update the decision.

**G2 is the core** — 12 universal dimensions covering all project types. Depth of questioning adapts automatically based on project characteristics:

| Project Characteristic | Deep-Dive Triggered |
|---|---|
| Depends on 3rd-party API/platform (AI models, Shopify, AWS, iOS, etc.) | Dimension 11 «Platform Dependency» deep-dive: wrapper depth, substitution risk, cost structure |
| Hardware / manufacturing | Dimension 7 «Product Feasibility» deep-dive: supply chain, mass production, yield rates |
| Finance / telecom / healthcare | Dimension 8 «Regulatory» deep-dive: licensing, capital requirements, consumer protection |
| Marketplace | Dimension 10 «Growth & Distribution» deep-dive: cold start, supply-demand balance |
| Policy / narrative-driven | Dimension 12 «Structural Resilience» deep-dive: cycle position, subsidy dependency |
| B2C consumer goods | Dimension 3 «Unit Economics» deep-dive: LTV/CAC, repurchase rate, return rate |
| Pure software / SaaS | No special deep-dive — standard diagnostics apply |

> **Core principle**: All 12 dimensions are **mandatory for every project** — because cemetery data shows a SaaS company and a hardware factory can die from the same knife (e.g., competition, team, cash). But the **depth of questioning** is determined by the project's specific characteristics — don't ask a bakery about their API cost ratio.

## The Five Gates

| Gate | Name | Question | Kill Criteria |
|---|---|---|---|
| G0 | Discover | Is there a real pain point worth solving? | Can't find ≥1 pain point with organic complaint evidence |
| G1 | Validate | Is the pain real, big enough, and will someone pay? | Demand score < threshold |
| G2 | Stress-test | 12-dimension unified diagnosis: will it end up in the startup cemetery? | Composite kill risk 🔴 with no escape path |
| G3 | Self-check | Right timing? Right founder? | Any single-veto item triggered |
| G4 | Decide | GO / Iterate / KILL? | Output decision + kill criteria |

## Workflow

### Step 0: Position + Load State

- **Existing scorecard** → loop review mode
- **New project** → initialize scorecard, start from appropriate gate
- **No specific idea yet** → start from G0

Quick positioning (minimal questions — only what's needed for diagnostic depth):
1. **Industry**? (Consumer / Enterprise SaaS / Hardware / Marketplace / Fintech / Food / Healthcare / Logistics / Gaming / Education / Climate / Real Estate / Mobility / Telecom / Energy / Manufacturing / Other)
2. **Stage**? (Idea / Validating PMF / Scaling / Revenue-generating)
3. **Project characteristics**? (Multi-select: Platform-dependent / Hardware manufacturing / Regulated industry / Marketplace / Policy-driven / B2C consumer / Pure software — used to trigger dimension-specific deep-dives)

### Step 1: Execute Gates Sequentially

- **G0 Discover** → `references/discover.md`
- **G1 Validate** → `references/validate.md`
- **G2 Stress-test** → «G2 Unified 12 Dimensions» section below
- **G3 Self-check** → `references/checklist.md`
- **G4 Decide** → `references/scoring.md`

### Step 2: Write Scorecard

### Step 3: Generate HTML Output (default)

Styling from `references/web-design-guidelines.md`.

---

## G2 Unified 12-Dimension Stress Test

### Design Principles

1. **All 12 dimensions are mandatory for every project** — each has a core assessment question
2. **Deep-dive depth adjusts by project characteristic** — only load matching sections from `references/conditional-diagnostics.md`
3. **All dimensions share the same data sources** — cemetery data (CB Insights, Loot Drop, LOOTR, Killed by Google) — no separate tracks for different project types
4. Big Tech graveyard insights are given once at the end, applicable to all

### Dimension Quick-Reference

| # | Dimension | Cemetery Data | Core Question (All Projects) | When to Deep-Dive |
|---|---|---|---|---|
| 1 | **Demand Reality** | CB Insights #2 (42%) | Who's paying for this? How do they solve it now without you? | Project is "tech-first looking for a problem" — check for solutionism trap |
| 2 | **Competitive Defensibility** | CB Insights #1 (53%), covers all industries | Can a big player replicate you in one sprint? What's the user switching cost? | Industry = IT / Telecom / Consumer (highest competition-death sectors) — check big-tech range + substitute threats |
| 3 | **Unit Economics** | LOOTR Consumer #2 (114 cases), overall 18% | Does each transaction make money? LTV > 3×CAC? Does marginal cost go up or down with scale? | B2C consumer → repurchase/return rates. Platform-dependent → API cost ratio + price-drop assumptions. Hardware → BOM + yield |
| 4 | **Runway & Cash** | CB Insights #3 (29%), Consumer 62 cases | How many months of runway? <12 🟡, <6 🔴. Do you have a kill criterion? | Capital-intensive (hardware/mfg/retail) → inventory turnover + payables/receivables gap |
| 5 | **Team Fit** | CB Insights #4 (20-23%) | Does anyone on the team truly understand the target user's domain? Is tech + business balanced? | Tech team tackling industry app → cognitive mismatch risk. Solo founder → product + market coverage |
| 6 | **Business Model Clarity** | Overall 10% | Why would users pay instead of using free alternatives? How many revenue streams? | Free-then-monetize → conversion path. Single revenue stream → pricing ceiling |
| 7 | **Product/Tech Feasibility** | Overall 15%, Hardware #1 | Can you build it? Is the bottleneck tech or manufacturing? | Hardware → manufacturing/supply chain/mass production. Deep tech → prototype→pilot→production path. Software → standard |
| 8 | **Regulatory & Legal** | Overall 12%, Finance 22 cases, Telecom 25 cases | Will the law stop you? Do you need a license? Is customer money in your hands? | Finance/Telecom/Healthcare → **mandatory deep-dive** (licensing, capital requirements, consumer protection, cross-border) |
| 9 | **Timing** | Overall 8% | Too early (users must change habits) or too late (unmovable incumbents)? | Project requires behavior change → "20 years too early" risk (Webvan pattern) |
| 10 | **Growth & Distribution** | Universal | Where do the first 1,000 users come from? Is there a viral mechanism? Can you reach users without paid ads? | Marketplace → cold start (chicken-and-egg). B2C → CAC + channels. B2B → sales cycle + procurement |
| 11 | **Platform Dependency** | 76% AI projects died from thin wrappers; generalizable to all platform-dependent businesses | How much of your business sits on someone else's platform? If they change rules/pricing/ban you — can you survive? | Depends on 3rd-party API (AI models, payments, maps, etc.) → wrapper depth 5-stage. Single-channel dependency (iOS/Shopify/AWS) → substitution cost |
| 12 | **Structural Resilience** | China historical cycles: getihu→xiahai→mass entrepreneurship→gig economy→solopreneur | Is your project driven by independent market demand, or by policy/narrative? If subsidies/hype disappear, does demand remain? | Project emerged after a policy/narrative wave (solopreneur, carbon-neutral subsidies, etc.) → cycle position + subsidy dependency |

### Dimension 1: Demand Reality

**Cemetery data**: CB Insights #2 killer, 42% of startups die from no market need. High-frequency sectors: Telecom (80), IT (46).

**Standard check** (all projects):
- How do users solve this problem today?
- How painful is it? "Annoying but tolerable" vs "can't function without solving it"?
- Has anyone already paid for a similar solution?
- "How do they solve it now?" — if the answer is "they don't" or "Google Sheets", demand is fake

**Deep-dive** (triggered when project is "tech-first looking for a problem"):
- Is your product "born from a real pain point, optimized by tech" or "tech existed, so we invented a use case"?
- Is your efficiency gain built on a market that fundamentally doesn't trust you? (Healthcare, legal, finance — ref: Legion case: efficiency ≠ trust)
- Where are 5 paying seed users? Go talk to them — don't guess

**Real cases**: Juicero ($120M, $699 WiFi juicer → hands squeeze faster), Magic Leap ($3.5B, died after 14 years), Google Stadia (gamers didn't need cloud gaming)

### Dimension 2: Competitive Defensibility

**Cemetery data**: CB Insights #1 killer, 53%. LOOTR heatmap covers all industries. IT (260), Telecom (257), Consumer (178).

**Standard check** (all projects):
- Is your core feature a checkbox on an incumbent's roadmap?
- What's the barrier to entry? (Not just "better UI")
- User switching cost? <5 minutes = 🔴

**Deep-dive** (IT/Telecom/Consumer — highest competition-death sectors):
- What's the marginal cost for a big player to build the same feature? (Nearly free if integrated into existing product = 🔴)
- Does the big player ignore this because they **can't** do it or because they **don't want to**? (Can't = your moat)
- If you succeed, will they notice you? (The later, the better)
- Competitive niche: Big player core battlefield → 🔴 / Big player fringe → 🟡 / Big player can't/won't do → 🟢

**Real cases**: Vine (200M MAU → crushed by Instagram copy), Quibi ($1.75B), Clubhouse ($1B → dead in 3 months), Neeva (ad-free search → users wouldn't switch)

**Escape path**: Find niches big players won't touch (privacy-sensitive, high-customization, offline-integrated, compliance-required); build network effects or data flywheels; win a niche first, then expand

### Dimension 3: Unit Economics

**Cemetery data**: LOOTR Consumer #2 killer (114 cases). Classic "Consumer Trap" — CAC > LTV.

**Standard check** (all projects):
- Does each transaction make money? Gross margin without subsidies?
- LTV / CAC ≥ 3×?
- Does marginal cost go up or down with scale?

**Deep-dive — by project characteristic**:
- **B2C Consumer**: Repurchase rate? Return rate? DTC or platform? — Watch for the classic trap: "VC-subsidized CAC → loyal users vanish when funding stops"
- **Platform-dependent**: API cost as % of revenue? If the underlying API doubles in price, can you survive? Gross margin >50%? (Ref: AI wrappers 50-60% vs traditional SaaS 80-90%. Under 50% = 🔴)
- **Hardware**: BOM cost? Manufacturing yield? Inventory turnover days?
- **Marketplace**: Subsidizing supply or demand side? Does transaction volume hold when subsidies stop?

**Real cases**: Countless DTC brands died from "VC-subsidized CAC → loyal users disappeared when funding stopped"

### Dimension 4: Runway & Cash

**Cemetery data**: CB Insights #3 (29%). China micro-enterprises: 25% can survive 6 months of cash flow, 30%+ can't survive one month.

**Standard check** (all projects):
- How many months of runway? <12 🟡, <6 🔴
- Do you have a kill criterion? ("If we don't hit X by month Y, we shut down")
- "The next round will come" as the only cash strategy? → 🔴

**Deep-dive — capital-intensive** (hardware/manufacturing/retail):
- Inventory turnover days? Accounts payable vs. receivable gap?
- How much of upfront investment is sunk cost (molds, factory setup, renovations)?

**Escape path**: Charge from day one. YC wisdom: 90% of companies that wait for "scale" to start charging never make it to that day.

### Dimension 5: Team Fit

**Cemetery data**: CB Insights #4 (20-23%). 85% of AI projects die from "cognitive mismatch" — technologists who don't know the domain, domain experts who don't know tech. But this isn't AI-specific — any tech-driven industry play has this risk.

**Standard check** (all projects):
- Does anyone on the team truly understand the target user's domain? (Not from reading about it)
- Is technical ability balanced with business ability?
- Has the founder met a target user? — If not = 🔴

**Deep-dive**:
- Tech team tackling industry app → is there a domain expert partner? Ref: Zillow Offers (lost $500M because algorithms said houses were valuable but nobody smelled the formaldehyde)
- Solo founder → do you cover both product and market?
- First-time founder → significantly higher failure rate (70% of solopreneurs are first-timers)

### Dimension 6: Business Model Clarity

**Cemetery data**: Overall 10%. Vine (200M MAU → no monetization → dead).

**Standard check** (all projects):
- Why would users pay instead of using free alternatives?
- How many revenue streams? (1 = 🔴, 2 = 🟡, ≥3 = 🟢)
- "Get traffic first, figure out monetization later" = 🔴

**Deep-dive**:
- Free-then-monetize → is the conversion path mapped? Validated with data?
- Does the pricing model match user psychology? (e.g., consumers hate SaaS subscriptions vs. enterprises accept consumption-based pricing)

### Dimension 7: Product/Tech Feasibility

**Cemetery data**: Overall 15%, but this is Hardware #1 killer. Note: ranked sixth, not first — **startups don't die from being unable to build products; they die from being unable to sell them.**

**Standard check** (all projects): Can you build it? Where's the bottleneck?

**Deep-dive**:
- **Hardware**: Demo ≠ mass production. Completed a small-batch pilot run (100-1,000 units)? Physically verified every link in the supply chain? — A hardware founder's key skill isn't design, it's manufacturing project management
- **Deep tech** (new materials, new drugs, new processes): Is the prototype→pilot→production path clear? Time and capital requirements at each stage?
- **Pure software**: Standard diagnostics suffice — tech risk is usually not the primary killer

### Dimension 8: Regulatory & Legal

**Cemetery data**: Overall 12%, but fatal-level for Finance (22) and Telecom (25).

**Standard check** (all projects): Will the law stop you?

**Deep-dive — Finance/Telecom/Healthcare only** (these sectors trigger mandatory deep-dive):
- Need a license? Timeline and cost to obtain?
- Capital requirements?
- Is customer money in your hands? → Consumer protection law > your innovation
- Cross-border? (Incorporation jurisdiction + customer location laws = dual compliance)
- Crypto/DeFi: Registering in a "regulatory haven" ≠ safe — when crisis hits, your jurisdiction determines who protects your customers (and whether you go to prison)
- Ref: FTX ($32B → zero in weeks), Celsius ($4.7B frozen) — regulatory failure isn't a footnote, it's the kill shot

> If you're NOT in Finance/Telecom/Healthcare, standard check suffices.

### Dimension 9: Timing

**Cemetery data**: Overall 8%. "Too early" kills more than "too late."

**Standard check** (all projects):
- Do users need to change behavior? → You're in the "too early" quadrant
- Are there immovable incumbents? → You're in the "too late" quadrant

**Real cases**: Webvan ($1.2B, 1999→2001) was right — just 20 years early. Google Wave (2010) was 5 years early — Slack/Notion later won the same market.

### Dimension 10: Growth & Distribution

**Standard check** (all projects):
- Where do the first 1,000 users come from? (Specific channel, not "marketing")
- Does the product have a viral mechanism?
- Can you reach users without paid ads?

**Deep-dive — by project characteristic**:
- **Marketplace**: Cold start strategy — supply-first or demand-first? Which side gets subsidized? Does transaction volume hold when subsidies stop? — If you don't see organic growth (non-subsidized new users) within 3 months, you're not building a platform — you're burning cash
- **B2C**: CAC? Primary acquisition channel? Retention/repurchase rate?
- **B2B**: Sales cycle? Who signs the check? (User ≠ buyer) — Enterprise procurement is the invisible killer

**Real case**: Neeva ($77.5M still couldn't break cold start)

### Dimension 11: Platform Dependency

**Cemetery data**: 76% of AI projects die from thin wrappers — but the underlying "platform dependency" logic applies to ALL businesses relying on a single platform/API.

**Standard check** (all projects):
- What % of your business sits on someone else's platform? (API, app store, e-commerce platform, cloud provider)
- If the platform changes rules/pricing/bans you/builds the same feature → can you survive?

**Deep-dive — triggered when: project depends on 3rd-party API or platform**:
- **Wrapper Depth 5-Stage** (originally from Monica co-founder Suki, generalized from AI wrappers to all platform-dependent businesses):
  1. Direct API call / basic platform feature → competing on UI/price = 🔴
  2. Combine multiple APIs / platform features → competing on design and UX = 🟡
  3. Embed proprietary data / content / vertical knowledge → competing on domain depth = 🟢
  4. Self-reinforcing data flywheel → more users = better product = 🟢
  5. Self-built core infrastructure → competing on R&D capability = 🟢
- What % of your margin is consumed by platform/API costs? >30% = 🔴
- Switching cost? (Technical migration + user impact + data portability)
- At least one backup/redundancy? (Multi-cloud, multi-platform)

**Real cases**: Countless Shopify plugins, AI wrappers, and iOS-exclusive apps erased by a single rule change or built-in feature

### Dimension 12: Structural Resilience

**Cemetery data**: From China market deep analysis — entrepreneurship/freelancing has clear **historical cycle patterns**. Every employment downturn → government calls for "self-reliance" → a new narrative emerges.

**China entrepreneurship cycles**: Getihu (1979) → Xiahai (1992) → Mass Entrepreneurship (2014) → Gig Economy (2020) → Solopreneur (2025)

**Standard check** (all projects):
- Is your project driven by independent market demand, or by policy/hype/narrative?
- If subsidies/hype/media coverage disappear, does demand remain?

**Deep-dive — triggered when: project emerged after a policy/narrative wave**:
- Are you building because "X is the next big thing" or because "this is a real problem"?
- Strip away the buzzwords ("solopreneur", "AI startup") — what is your business model, really? (Freelancing? Small business? Actual scalable business?)
- Renaming yourself with a new tool ("solopreneur") doesn't change business fundamentals — efficiency gain ≠ business model upgrade
- **Core test**: Would anyone still need your product in a strong economy with full employment?

**70% of solopreneurs are first-time founders** — significantly higher failure rate.

---

### Industry × Failure Cause Quick-Reference

Detailed data in `references/industry-profiles.md`.

| Industry | #1 Killer | #2 Killer | Key Insight |
|---|---|---|---|
| **Consumer** | Competition (178) | Unit Economics (114) | Consumer Trap: VC-subsidized CAC, profits never arrive |
| **Telecom** | Competition (257) | No Market Need (80) | Lowest barrier → bloodiest arena |
| **IT** | Competition (260) | No Market Need (46) | Easiest to enter = most bodies |
| **Finance** | Competition | Regulatory (22) | Dual hurdle: market + compliance |
| **Hardware** | Tech Feasibility | Mfg/Supply Chain | Demo ≠ Mass Production |
| **Marketplace** | Cold Start | Competition | Chicken-and-egg problem |
| **Food/Hospitality** | Ran Out of Cash (54%) | Competition | Low margin + high upfront = lethal combo |
| **Retail** | Ran Out of Cash (69%) | Competition | CAC + rent = death spiral |
| **Manufacturing** | Ran Out of Cash (53%) | Competition | Supply chain disruption = cash runs dry |

### Stage Risk Quick-Reference

| Stage | Most Likely Killers |
|---|---|
| **Idea stage** | #1 Demand Reality / #9 Timing |
| **PMF validation** | #1 Demand Reality / #7 Product Feasibility |
| **Scaling** | #2 Competitive Defensibility / #3 Unit Economics / #4 Runway & Cash |
| **Revenue/Profit** | #2 Competitive Defensibility / #5 Team Fit / #6 Business Model Clarity |

### Big Tech Graveyard Insights

Killed by Google (307 products) + Amazon Cemetery (50+). Details in `references/big-tech-graveyard.md`.

**Google's Five Death Patterns**: Strategic acquisition/strangulation → Internal politics/attention shift → Experiment mentality (plant 100, harvest 5) → Self-cannibalization → Free → no monetization → killed

**Core lessons**: Big Tech validation ≠ market validation; Big Tech abandonment ≠ market gone (Google Reader died → Feedly lived); Free + infinite money ≠ success; Too early = latecomers win.

### G2 Output Format

```
## 💀 G2 12-Dimension Stress Test

### Project Characteristics Identified
[Auto-detected: Platform-dependent / Hardware / Regulated / Marketplace / B2C Consumer / Policy-driven / Pure Software]

### Dimension Matching
| # | Dimension | Risk | Match Evidence | Escape Path |
|---|---|---|---|---|
| 1 | Demand Reality | 🔴/🟡/🟢 | ... | ... |
| 2 | Competitive Defensibility | ... | ... | ... |
| ... | ... | ... | ... | ... |
| 12 | Structural Resilience | ... | ... | ... |

### [Industry] Special Risk Profile
[Industry #1/#2 killers + whether this project triggers them]

### Deep-Dives Triggered
[List dimensions where deep-dive was activated + findings]

### Big Tech Graveyard Relevant Insight
[Analogy to Google/Amazon death patterns if applicable]

### Overall Kill Risk
**Composite Rating: 🔴 High / 🟡 Medium / 🟢 Low**
**Biggest Killers:** [Top 1-3 most dangerous dimensions]
```

---

## Loop Mode (Review)

1. Load previous scorecard → compute per-dimension delta ↑/↓/→ → focus on worsening dimensions
2. Check each kill criterion → any triggered → KILL recommendation
3. GO/Iterate/KILL + write new scorecard + HTML report

---

## Batch Mode

Multiple ideas to rank: run G1+G2 quick version on each → composite score sort → top 1-2 get full pipeline. Output HTML dashboard (leaderboard cards + overlay radar chart).

---

## HTML Output

```
┌─────────────────────────────────────────┐
│  Nav: Project Name · Round · Date · Status │
│  Decision Badge (🟢/🟡/🔴)              │
├─────────────────────────────────────────┤
│  One-Sentence Verdict                     │
├──────────────┬──────────────────────────┤
│  Radar (12d) │  Dimension Score Cards     │
├──────────────┴──────────────────────────┤
│  Dimension Details (collapsible)          │
│  + Deep-Dives expanded                   │
│  Industry Risk + Big Tech Insights        │
├─────────────────────────────────────────┤
│  Kill Criteria Check                      │
├─────────────────────────────────────────┤
│  Next Actions + Evidence Gaps             │
└─────────────────────────────────────────┘
```

Styling: `references/web-design-guidelines.md`.

---

## Reference Files

| File | Purpose |
|---|---|
| `references/discover.md` | G0 Discovery methodology |
| `references/validate.md` | G1 Validation methodology |
| `references/checklist.md` | G3 Self-check |
| `references/scoring.md` | G4 Scoring rubrics & thresholds |
| `references/industry-profiles.md` | 16 industries × 12 failure cause profiles |
| `references/big-tech-graveyard.md` | Google/Amazon/Microsoft graveyard |
| `references/conditional-diagnostics.md` | Deep-dive questions indexed by project characteristic |
| `references/web-design-guidelines.md` | HTML design system |
| `assets/scorecard-template.md` | Scorecard template |

---

## Output Rules

- **Default**: Self-contained HTML page
- **Data citations**: Every diagnosis backed by ≥1 real case + dollar amount or statistic
- **Dimension coverage**: All 12 dimensions mandatory for every project. Don't skip Dimension 11 (Platform Dependency) just because the project "isn't AI" — a Shopify plugin faces the same platform dependency risk as an AI wrapper
- **Deep-dives**: Only trigger when project characteristics match. Don't force irrelevant deep-dive questions
- **Language**: Match the user's language. For Chinese users, see `SKILL.zh-CN.md`
