---
name: preflight
description: "Preflight — 12-dimension startup evaluation system that checks your project's survival odds before you commit. Powered by: Loot Drop (1,749 failed startups, $535B burned) · CB Insights (483 post-mortems: competition 53% / no market need 42% / ran out of cash 29%) · Failory (200+ analyses, Google Cemetery 100+ products, Amazon Cemetery 50+) · LOOTR heatmap (16 industries × 12 failure causes) · Killed by Google (307 discontinued products) · DANG! AI Graveyard (5,000+ AI tools tracked, 30% closed) · Kaggle CB Insights dataset (890 startups SQL analysis, 1992-2024) · Product Grave (99 dead tech products) · Unbiased Ventures (2024-2025 major failures, 7 VC dimensions). AI projects get 5 additional conditional deep-dive dimensions (wrapper depth, TC-PMF, AI trust, AI monetization, AI structural bubble). Chinese version available at SKILL.zh-CN.md. Trigger when the user says 'evaluate this idea', 'is this project viable', 'help me decide whether to build this', 'will this survive', 'compare these ideas', 'post-mortem analysis'. Outputs HTML dashboard/report, supports multi-project comparison and loop review. Five-gate pipeline (G0→G4), all industries and project types."
---

# Preflight · Startup Health Check

A structured evaluation system that turns "fuzzy idea → evidence-backed build decision." Powered by data from 2,500+ startup post-mortems, 16-industry failure heatmaps, 307 killed Big Tech products, and 5,000+ AI graveyard entries.

## Core Mental Model

**A funnel + a loop.**

- **Funnel (fail-fast)**: Five gates G0→G4, each more expensive than the last. An idea that should die at G1 doesn't get a free pass to G3.
- **Loop (review)**: After each run, write results to a scorecard. On re-evaluation, load the previous round → compute deltas → check kill criteria → update the decision.

**G2 is the core** — 12 universal dimensions covering all project types, plus **5 conditional AI deep-dive extensions**. Depth of questioning adapts automatically based on project characteristics:

| Project Characteristic | Deep-Dive Triggered |
|---|---|
| **AI-native** (calls LLM API, AI-first product, foundation-model dependent) | ALL 5 AI deep-dives: wrapper depth + inference cost (TC-PMF) + AI demand trust + AI monetization + AI structural bubble |
| Depends on 3rd-party API/platform (Shopify, AWS, iOS, payments, etc.) | Dimension 11 «Platform Dependency» deep-dive: wrapper depth, substitution risk, cost structure |
| Hardware / manufacturing | Dimension 7 «Product Feasibility» deep-dive: supply chain, mass production, yield rates |
| Finance / telecom / healthcare | Dimension 8 «Regulatory» deep-dive: licensing, capital requirements, consumer protection |
| Marketplace | Dimension 10 «Growth & Distribution» deep-dive: cold start, supply-demand balance |
| Policy / narrative-driven | Dimension 12 «Structural Resilience» deep-dive: cycle position, subsidy dependency |
| B2C consumer goods | Dimension 3 «Unit Economics» deep-dive: LTV/CAC, repurchase rate, return rate |
| Pure software / SaaS | No special deep-dive — standard diagnostics apply |

> **Core principle**: All 12 dimensions are **mandatory for every project** — because cemetery data shows a SaaS company and a hardware factory can die from the same knife (e.g., competition, team, cash). But the **depth of questioning** is determined by the project's specific characteristics — don't ask a bakery about their API cost ratio. For AI-native projects, run ALL 5 AI deep-dives in addition to the 12 universal dimensions.

## The Five Gates

| Gate | Name | Question | Kill Criteria |
|---|---|---|---|
| G0 | Discover | Is there a real pain point worth solving? | Can't find ≥1 pain point with organic complaint evidence |
| G1 | Validate | Is the pain real, big enough, and will someone pay? | Demand score < threshold |
| G2 | Stress-test | 12-dimension unified diagnosis (+ 5 AI deep-dives if AI): will it end up in the startup cemetery? | Composite kill risk 🔴 with no escape path |
| G3 | Self-check | Right timing? Right founder? | Any single-veto item triggered |
| G4 | Decide | GO / Iterate / KILL? | Output decision + kill criteria |

## Workflow

### Step 0: Position + Load State

- **Existing scorecard** → loop review mode
- **New project** → initialize scorecard, start from appropriate gate
- **No specific idea yet** → start from G0

Quick positioning (minimal questions — only what's needed for diagnostic depth):
1. **Industry**? (Consumer / Enterprise SaaS / Hardware / Marketplace / Fintech / Food / Healthcare / Logistics / Gaming / Education / Climate / Real Estate / Mobility / Telecom / Energy / Manufacturing / AI / Other)
2. **Stage**? (Idea / Validating PMF / Scaling / Revenue-generating)
3. **Project characteristics**? (Multi-select: AI-native / Platform-dependent / Hardware manufacturing / Regulated industry / Marketplace / Policy-driven / B2C consumer / Pure software — used to trigger dimension-specific deep-dives)

### Step 1: Execute Gates Sequentially

- **G0 Discover** → `references/discover.md`
- **G1 Validate** → `references/validate.md`
- **G2 Stress-test** → «G2 Unified 12 Dimensions» section below
- **G3 Self-check** → `references/checklist.md`
- **G4 Decide** → `references/scoring.md`

### Step 2: Write Scorecard

### Step 3: Generate HTML Output (default)

Render the report by **delegating**, not by styling it yourself:

1. Invoke the **`impeccable`** skill for the visual layer — Read mode for a single report, Operate for a batch dashboard.
2. Invoke the **`diagram-design`** skill for every chart — **light templates by default** (`assets/template.html`, or `template-full.html` for the long card layout).
3. `references/web-design-guidelines.md` holds the content contract, the status semantics, and the exact delegation flow. It no longer defines a palette — do not hand-roll one.

---

## G2 Unified 12-Dimension Stress Test

### Design Principles

1. **All 12 dimensions are mandatory for every project** — each has a core assessment question
2. **Deep-dive depth adjusts by project characteristic** — only load matching sections from `references/conditional-diagnostics.md`
3. **AI-native projects get 5 additional conditional deep-dives** injected into the relevant dimensions below
4. **All dimensions share the same data sources** — cemetery data (CB Insights, Loot Drop, LOOTR, Killed by Google, DANG! AI Graveyard) — no separate tracks for different project types
5. Big Tech graveyard insights are given once at the end, applicable to all

### Dimension Quick-Reference

| # | Dimension | Cemetery Data | Core Question (All Projects) | When to Deep-Dive |
|---|---|---|---|---|
| 1 | **Demand Reality** | CB Insights #2 (42%) | Who's paying for this? How do they solve it now without you? | Project is "tech-first looking for a problem" — check for solutionism trap. AI project → trust check + AI-for-everything trap |
| 2 | **Competitive Defensibility** | CB Insights #1 (53%), covers all industries | Can a big player replicate you in one sprint? What's the user switching cost? | Industry = IT/Telecom/Consumer → big-tech range + substitute threats. AI project → big-tech AI roadmap check |
| 3 | **Unit Economics** | LOOTR Consumer #2 (114 cases), overall 18% | Does each transaction make money? LTV > 3×CAC? Does marginal cost go up or down with scale? | B2C → repurchase/return. Platform-dependent → API cost. Hardware → BOM. **AI project → TC-PMF + inference cost + linear growth illusion** |
| 4 | **Runway & Cash** | CB Insights #3 (29%), Consumer 62 cases | How many months of runway? <12 🟡, <6 🔴. Do you have a kill criterion? | Capital-intensive → inventory + payables/receivables. AI project → inference cost as % of burn |
| 5 | **Team Fit** | CB Insights #4 (20-23%) | Does anyone truly understand the target domain? | Tech team tackling industry → cognitive mismatch. Solo founder → double coverage. AI project → domain expert + AI engineer balance |
| 6 | **Business Model Clarity** | Overall 10% | Why pay instead of free? How many revenue streams? | Free-then-monetize → conversion. Single stream → ceiling. **AI project → consumption pricing, margin squeeze, API dependency** |
| 7 | **Product/Tech Feasibility** | Overall 15%, Hardware #1 | Can you build it? Is the bottleneck tech or mfg? | Hardware → mfg/supply chain. Deep tech → prototype→production. AI → model quality + latency + reliability |
| 8 | **Regulatory & Legal** | Overall 12%, Finance 22, Telecom 25 | Will the law stop you? | Finance/Telecom/Healthcare → **mandatory deep-dive**. AI → AI Act/liability/bias disclosure |
| 9 | **Timing** | Overall 8% | Too early or too late? | Behavior change required → "20 years too early" risk |
| 10 | **Growth & Distribution** | Universal | First 1,000 users? Viral mechanism? | Marketplace → cold start. B2C → CAC. B2B → sales cycle. AI → PLG vs enterprise sales |
| 11 | **Platform Dependency** | 76% AI projects died from thin wrappers; generalizable to all platform-dependent businesses | How much of your business sits on someone else's platform? | 3rd-party API/platform dependence → wrapper depth 5-stage. **AI project → DANG! AI Graveyard data + deeper wrapper analysis** |
| 12 | **Structural Resilience** | China historical cycles; 70% solopreneurs are first-time founders | Driven by market demand or by policy/narrative? | Emerged after policy/narrative wave → cycle position. **AI project → AI hype cycle + narrative cargo-cult check** |

---

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

**🔴 AI deep-dive** (triggered when project is AI-native):
- **AI trust trap**: Your product is efficient — but does the customer trust AI enough to rely on it for this decision?
  - Ref: **Legion** (Legal AI) — died because clients didn't want "high-stakes legal matters handled by an opaque LLM." Efficiency ≠ trust.
  - Healthcare: patient data privacy, diagnosis accuracy, liability
  - Finance: KYC/AML, customer fund protection, explainability
  - **Key question**: Does your target market demand human-in-the-loop or high transparency? If yes, AI alone is not the solution.
- **AI-for-everything trap**: Is this problem "optimized by AI" or "AI created the problem"? If the latter, demand doesn't exist.
- "Users are solving this with AI tools already" — are they using general-purpose ChatGPT, or do they need your specialized solution? If ChatGPT can do it → demand is thin.

**Real cases**: Juicero ($120M, $699 WiFi juicer → hands squeeze faster), Magic Leap ($3.5B, died after 14 years), Google Stadia (gamers didn't need cloud gaming), **Legion Legal AI (efficiency ≠ trust)**

---

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

**🔴 AI deep-dive** (triggered when project is AI-native):
- **Big Tech AI roadmap**: Is your feature a checkbox on OpenAI/Google/Meta/Anthropic's roadmap? 75% of failed AI projects lost to tech giants.
- Can the big player ship your feature as a **free add-on** to their existing product? (ChatGPT memory, Gemini integration, Copilot expansion)
- **AI ecosystem risk**: Are you built on top of one model provider? If they deprecate your use case or change pricing → you die.
- **Open-source threat**: Is there an open-source model or library that could replace your core value? (Llama, Mistral, Stable Diffusion)
- **Key insight**: AI tools are universal — if you only have an idea + an API key, you have zero moat. The real question: **Is the big player ignoring this because they can't do it, or because they don't want to?** Can't = moat.

**Real cases**: Vine (200M MAU → crushed by Instagram copy), Quibi ($1.75B), Clubhouse ($1B → dead in 3 months), Neeva, **countless AI wrappers erased by a single ChatGPT update**

**Escape path**: Find niches big players won't touch (privacy-sensitive, high-customization, offline-integrated, compliance-required); build network effects or data flywheels; win a niche first, then expand

---

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

**🔴 AI deep-dive — TC-PMF (Technology Cost × Product-Market Fit)** (triggered when project is AI-native):
- **Inference cost per transaction vs revenue**: What % of revenue goes to model inference? >30% = 🔴
- **Linear growth illusion**: AI often makes "linear businesses" faster — writing an article in 1 day instead of 3 days, but you're still an individual freelancer. Efficiency gain ≠ business model upgrade.
  - **Test**: If every competitor had the same AI, would you still be special?
- **Gross margin pressure**: AI-wrapper gross margins are 50-60% (vs SaaS 80-90%). During rapid growth, can drop to 25%. Under 50% = 🔴.
- **Consumption-based cost structure**: Is your cost proportional to usage? (Linear scaling hurts — no economies of scale)
- **Free tier trap**: Who pays for free users' inference? If you're running inference on hope, that's a growing liability.
- **Price-drop dependency**: Is your business model built on the assumption that "model costs will keep falling"? (TC-PMF bet)
- **Layered inference strategy**: Simple queries → small model/cache/rule-based. Complex queries → large model. If you're using one model for everything, you're overpaying.

**Real cases**: Countless DTC brands died from "VC-subsidized CAC → loyal users disappeared when funding stopped". AI wrappers: gross margin drops as users grow faster than inference optimization.

---

### Dimension 4: Runway & Cash

**Cemetery data**: CB Insights #3 (29%). China micro-enterprises: 25% can survive 6 months of cash flow, 30%+ can't survive one month.

**Standard check** (all projects):
- How many months of runway? <12 🟡, <6 🔴
- Do you have a kill criterion? ("If we don't hit X by month Y, we shut down")
- "The next round will come" as the only cash strategy? → 🔴

**Deep-dive — capital-intensive** (hardware/manufacturing/retail):
- Inventory turnover days? Accounts payable vs. receivable gap?
- How much of upfront investment is sunk cost (molds, factory setup, renovations)?

**🔴 AI deep-dive** (triggered when project is AI-native):
- Inference cost as % of total burn rate? Is your cloud/AI bill growing faster than users?
- Are you paying for inference before you have paying users?
- **Key risk**: AI startups burn cash faster than traditional SaaS because of dual cost structure (engineering + inference). A traditional SaaS startup can run on $5K/month. An AI startup can burn $30K+/month just on API costs.
- Is cash consumption passive (dragged by API/cloud bills) or actively controllable?

**Escape path**: Charge from day one. YC wisdom: 90% of companies that wait for "scale" to start charging never make it to that day.

---

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

**🔴 AI deep-dive** (triggered when project is AI-native):
- **Double cognitive mismatch**: AI requires BOTH AI engineering expertise AND domain expertise. Missing either → failure.
- 85% of AI projects die from this mismatch — pure AI engineers building domain products without domain partners.
- Does the team include someone who understands the user's workflow, not just the tech stack?
- Is there an "AI native" culture risk — team too excited about the technology, not enough about the problem?

---

### Dimension 6: Business Model Clarity

**Cemetery data**: Overall 10%. Vine (200M MAU → no monetization → dead).

**Standard check** (all projects):
- Why would users pay instead of using free alternatives?
- How many revenue streams? (1 = 🔴, 2 = 🟡, ≥3 = 🟢)
- "Get traffic first, figure out monetization later" = 🔴

**Deep-dive**:
- Free-then-monetize → is the conversion path mapped? Validated with data?
- Does the pricing model match user psychology? (e.g., consumers hate SaaS subscriptions vs. enterprises accept consumption-based pricing)

**🔴 AI deep-dive** (triggered when project is AI-native):
- **Consumption pricing paradox**: Pricing based on tokens/usage is transparent but creates cost uncertainty for users. Flat-rate SaaS pricing is user-friendly but risky if heavy users spike your inference costs.
- **Is this a feature or a business?** Many AI products are features that a larger product should absorb. Features don't sustain standalone businesses.
- **AI monetization models** (from best to worst):
  - Enterprise licensing / white-label: high-ticket, long sales cycle
  - Consumption-based (per token/per query): revenue scales with usage, but billing complexity
  - SaaS subscription + usage cap: predictable for users, capped risk for you
  - Freemium + premium: works when free tier cost is near-zero (hard for AI)
  - Advertising: needs massive scale — unlikely for AI tools
- **Pricing benchmark**: If your pricing is close to the raw cost of the underlying model + a thin margin, you're in the "feature trap" — users will go directly to the model provider.

---

### Dimension 7: Product/Tech Feasibility

**Cemetery data**: Overall 15%, but this is Hardware #1 killer. Note: ranked sixth, not first — **startups don't die from inability to build, they die from inability to sell.**

**Standard check** (all projects):
- What's the hardest technical part and why are you confident you can solve it?
- What could fail? Do you have a known failure mode?

**Deep-dive — hardware/manufacturing** (see `references/conditional-diagnostics.md`):
- Supply chain verification, prototype→pilot→production, yield rates

**🔴 AI deep-dive** (triggered when project is AI-native):
- **Model quality and consistency**: Can the model reliably produce acceptable outputs? (Not 99% of the time — 99.999% if production critical)
- **Latency and reliability**: Is inference fast enough for real-time use? What happens when the API is down?
- **Hallucination / accuracy**: In regulated or high-stakes domains, even 1% hallucination is unacceptable. What's your mitigation?
- **Data pipeline**: Do you have the data infrastructure to collect, clean, and feed training/retrieval data?

---

### Dimension 8: Regulatory & Legal

**Cemetery data**: Overall 12%. Finance #3 (22 cases), Telecom (25 cases).

**Standard check** (all projects):
- Are there specific regulations or licensing requirements for this industry?
- Do you hold customer funds or sensitive personal data?

**Deep-dive — regulated industries** (Finance/Telecom/Healthcare — **mandatory**):
- Full licensing matrix, capital requirements, consumer protection, cross-border compliance

**🔴 AI deep-dive** (triggered when project is AI-native):
- **AI Act / AI liability**: Does your product fall under regulatory scrutiny (EU AI Act, US executive orders, China AI regulations)?
- **Bias and fairness**: Can the model produce discriminatory outputs? What's your mitigation?
- **Transparency and disclosure**: Do you need to tell users they're interacting with AI?
- **Data privacy**: Training data provenance? User data protection? GDPR/CCPA compliance?
- **Human-in-the-loop**: Is human oversight required for your use case?

---

### Dimension 9: Timing

**Cemetery data**: Overall 8%.

**Standard check** (all projects):
- Too early (users must change behavior)? Too late (unmovable incumbents)?
- "Why now?" — what changed to make this opportunity real today?

**Deep-dive** (behavior change required):
- "20 years too early" pattern (Webvan, Google Glass) — the technology works but the ecosystem doesn't

---

### Dimension 10: Growth & Distribution

**Cemetery data**: Universal.

**Standard check** (all projects):
- Where do the first 1,000 users come from?
- Is there a viral/word-of-mouth mechanism built into the product?
- Can you reach users without paid ads?

**Deep-dive — marketplace**:
- Cold start death loop, supply/demand side choice.

**🔴 AI deep-dive** (triggered when project is AI-native):
- **PLG vs enterprise sales**: AI tools tend to do well with PLG (product-led growth) — low friction, free trial. But enterprise AI sales cycles are long (compliance, security review, procurement).
- **API distribution**: Is your product embeddable? Can other tools consume your AI as an API?
- **Open-source community**: If you open-source your model/weights, distribution is free but monetization is hard.
- **The "ChatGPT as competitor" problem**: If a user can achieve 80% of your value with a prompt in ChatGPT, they won't pay.

---

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

**🔴 AI deep-dive** (triggered when project is AI-native):
- **DANG! AI Graveyard data**: 5,000+ AI tools tracked, 30% fully closed. 76% of AI projects died from thin wrappers.
- **Wrapper depth assessment**: Where are you on the 5-stage scale? Most AI projects are Stage 1-2 (🔴-🟡).
- **API dependency concentration**: Are you dependent on a single model provider? If OpenAI/Anthropic change their pricing, deprecate your use case, or release a competing feature → can you survive?
- **Model provider as competitor risk**: The provider can ship your feature as a ChatGPT/Gemini native capability. If your core value is "ChatGPT but for X" — you're in the bullseye.
- **TC-PMF cost dependency**: Is your business model viable at current API prices? At 2× current prices? At 0.5×? (Most AI wrappers fail because their pricing leaves no room for API price fluctuations.)
- **Inference cost ratio**: API cost as % of revenue. AI wrapper = 50-60% gross margin vs SaaS 80-90%. Under 50% = 🔴.

**Real cases**: Countless Shopify plugins, AI wrappers, and iOS-exclusive apps erased by a single rule change or built-in feature. **DANG! AI Graveyard**: 100 AI tools died in March 2025 alone.

---

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

**🔴 AI deep-dive** (triggered when project is AI-native):
- **AI narrative check**: Are you building because "AI is the next big thing" or because "this is a real problem that AI can solve"? If the former, you're riding hype, not building a business.
- **Structural AI bubble**: The "AI founder" narrative is the latest in a long line of employment-downturn coping stories (solopreneur 2025, gig economy 2020, mass entrepreneurship 2014). 70% of first-time founders are first-time founders — and AI makes it even easier to start, which means more competition.
- **Cargo-cult AI**: Just because you use AI, you're not building a defensible business. AI is a tool, not a business model.
- **Survivorship bias**: Each cycle produces a few winners who become the poster children. For every successful AI startup, 99.99% are foundation-layer casualties.
- **Key distinction**:
  - **Real AI business**: Created a new market or substantially improved an existing one in a way competitors can't easily replicate
  - **Narrative AI business**: Used AI to do the same thing faster (write articles, design graphics, translate) but the underlying business model is a freelancer with a new tool

**Real cases**: Theranos ($9B, AI-adjacent fraud), countless "AI-powered" agencies that are really human+GPT freelancers

---

### Industry × Failure Cause Quick-Reference

Detailed data in `references/industry-profiles.md`.

| Industry | #1 Killer | #2 Killer | Key Insight |
|---|---|---|---|
| **AI / AI Native** | Platform Dependency / Wrapper (76%) | No Market Need (42%) | Dual threat: thin wrapper + fake demand. Most AI "startups" are features, not businesses. See DANG! AI Graveyard. |
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

### DANG! AI Graveyard Insights

From DANG! AI Graveyard (5,000+ AI tools tracked, 30% closed, ~100 tools/month dying as of 2025):
- **Thin wrapper syndrome**: 76% of dead AI projects were thin wrappers — no proprietary data, no fine-tuning, just an API call with a UI
- **The "feature trap"**: Most AI tools are features that larger platforms absorb
- **Mar 2025 snapshot**: 100 AI tools died in one month — the graveyard is accelerating
- **AI failure rate > 90%** — higher than traditional tech startups (~20% higher)
- **Average AI startup survival**: ~18 months

### G2 Output Format

```
## 💀 G2 12-Dimension Stress Test (+ AI Deep-Dives)

### Project Characteristics Identified
[Auto-detected: AI-native / Platform-dependent / Hardware / Regulated / Marketplace / B2C Consumer / Policy-driven / Pure Software]

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
- [Standard deep-dives: Platform dependency, Marketplace, etc.]
- 🔴 AI Deep-Dives (5 active): TC-PMF, wrapper depth, AI trust, AI monetization, AI structural bubble

### Big Tech Graveyard Relevant Insight
[Analogy to Google/Amazon death patterns if applicable]

### DANG! AI Graveyard Relevant Insight
[AI-specific graveyard patterns if the project is AI-native]

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

Multiple ideas to rank: run G1+G2 quick version on each → composite score sort → top 1-2 get full pipeline. Output HTML dashboard (leaderboard cards + a comparison figure — grouped bars or a quadrant).

---

## HTML Output

The report must carry these blocks. The layout is impeccable's call — this is a content contract, not a template:

1. Decision header — project · round · date · decision badge (GO / 迭代 / KILL)
2. One-sentence verdict
3. Dimension scores — figure or table, with trend arrows
4. Dimension details (collapsible), plus expanded deep-dives
5. 🔴 AI deep-dives, when the project is AI-native
6. Industry risk profile + graveyard comparisons (Big Tech, and DANG! AI Graveyard for AI projects)
7. Kill criteria check — condition and whether it fired
8. Next actions + evidence gaps

Contract, status colors, and the exact delegation flow: `references/web-design-guidelines.md`. Visual layer via the `impeccable` skill; every figure via the `diagram-design` skill in **light mode**. The 12 dimensions do **not** fit a radar (5-axis cap) — use a bar chart, or aggregate to ≤5 axes first.

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
| `references/conditional-diagnostics.md` | Deep-dive questions indexed by project characteristic (includes AI-specific deep-dives) |
| `references/web-design-guidelines.md` | Report content contract, status semantics, render delegation |
| `assets/scorecard-template.md` | Scorecard template |

---

## Output Rules

- **Default**: Self-contained light-mode HTML page, rendered via the `impeccable` skill with every figure drawn by the `diagram-design` skill. `scripts/generate-dashboard.py` is a no-skill fallback only — see `references/web-design-guidelines.md` §5
- **Data citations**: Every diagnosis backed by ≥1 real case + dollar amount or statistic
- **Dimension coverage**: All 12 dimensions mandatory for every project. Don't skip Dimension 11 (Platform Dependency) just because the project "isn't AI" — a Shopify plugin faces the same platform dependency risk as an AI wrapper
- **AI deep-dives**: Only triggered for AI-native projects. Run all 5: wrapper depth, TC-PMF, AI demand trust, AI monetization, AI structural bubble
- **Deep-dives**: Only trigger when project characteristics match. Don't force irrelevant deep-dive questions
- **Language**: Match the user's language. For Chinese users, see `SKILL.zh-CN.md`
