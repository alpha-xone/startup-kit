---
name: gtm
description: "GTM — Go-to-market playbook for founders. 10 GTM channels distilled from 5,000+ founder stories (StarterStory + IndieHackers + blueprint). Stage-matched channel recommendations ($0→$1M+). Real case studies with revenue data. v0.5: 7 channels with strong data, 3 partial. Trigger when the user asks 'how should I go to market', 'growth channels', 'distribution strategy', 'get first users', 'GTM strategy', 'which channel should I use'. Chinese version at SKILL.zh-CN.md."
---

# GTM · Go-to-Market Playbook

> **Which channel when, backed by real founder outcomes.**

A structured GTM selection and execution guide distilled from **5,000+ founder stories** (StarterStory + IndieHackers + blueprint's own pattern extraction). v0.5 — covers 7 channels with strong data backing, 3 channels partial.

## Core Mental Model

**One channel, milk it dry, then add a second.** That's the pattern across every founder who crossed $50K MRR. The question isn't "which 5 channels should I try?" — it's "which 1 channel should I go 10x deeper on?"

### Three operating modes:

- **Channel Match**: "I'm at $5K MRR, SaaS, B2B — which two channels should I focus on?" → Matches you to the best channels for your stage + model + audience
- **Diagnostic**: "I'm trying [channel] but it's not working — what's wrong?" → Walks through the common failure patterns for that channel
- **Switch**: "I've maxed out my channel — what's next?" → Suggests the next channel based on data on which transitions work

### When NOT to use this:

- You're at $500K+ MRR with a working multi-channel engine → you need enterprise GTM, which v0.5 doesn't cover well
- You need a full PLG implementation guide → this covers PLG strategy but not implementation
- You're doing pure enterprise sales (10+ salespeople, 6-figure ACV) → this data skews bootstrapped/SaaS

---

## The 10 Channels

### Tier 1: Strong Data (7 channels)

| # | Channel | Best For | Stage Sweet Spot | Data Confidence |
|---|---|---|---|---|
| 1 | **Content / SEO** | All models | PMF → Engine (any stage after validation) | ⭐⭐⭐⭐⭐ |
| 2 | **Build in Public** | Solo founders, dev tools, creator businesses | Validation → Engine (every stage works) | ⭐⭐⭐⭐⭐ |
| 3 | **Product-Led Growth (PLG)** | SaaS, tools | Scaling → Engine (needs a working product first) | ⭐⭐⭐⭐ |
| 4 | **Community / Audience** | Creator businesses, dev tools, B2C | Validation → Team (build before you need it) | ⭐⭐⭐⭐ |
| 5 | **Product Hunt Launch** | B2C SaaS, dev tools, consumer | Validation (one-time launch ≠ distribution) | ⭐⭐⭐⭐ |
| 6 | **Productized Service → SaaS** | Services, agency, consultants | Validation → PMF (stair-step pattern) | ⭐⭐⭐⭐ |
| 7 | **API / Integrations** | API-first products, platform plays | PMF → Engine (needs working product) | ⭐⭐⭐ |

### Tier 2: Partial Data (3 channels — marked as such)

| # | Channel | Best For | Status |
|---|---|---|---|
| 8 | **Cold Email / Outbound** | B2B SaaS, services | ⚠️ Partial — enough for basic playbook, not deep benchmarks |
| 9 | **Partnership / Affiliate** | SaaS, content businesses | ⚠️ Partial — helps with channel transition decisions |
| 10 | **Paid Acquisition** | DTC/consumer at scale | ⚠️ Mostly failure data — more useful as "what to avoid" |

---

## Quick-Reference: Which Channel at Which Stage

| Stage | Revenue | Best Channels | Avoid |
|---|---|---|---|
| **Validation** | $0 → $1K/mo | Build in Public, Product Hunt, Community, Productized Service | Paid Ads, Enterprise Sales, SEO (too slow) |
| **PMF** | $1K → $10K/mo | Content/SEO, Community, Cold Email | Paid Ads, Enterprise Sales |
| **Scaling** | $10K → $50K/mo | Content/SEO, PLG, Cold Email | Product Hunt (one-time launch done) |
| **Team** | $50K → $200K/mo | SEO + PLG + Outbound + Partnerships | Single-channel dependency |
| **Engine** | $200K → $1M+/mo | All channels running + multi-product | Double down on what works |

---

## How to Run This Skill

### Step 1: Gather Context

- Current MRR (or stage)
- Business model
- B2B, B2C, or mixed?
- What channel(s) are you trying now?
- What's not working?

### Step 2: Channel Match

Match to stage + model → output top 2 recommended channels + concrete next steps + 2-3 case references.

### Step 3: Diagnostic (if applicable)

If a channel isn't working, run the common failure patterns for that channel:
- SEO → "How long have you been publishing?" (<6 months = not failure, it's time)
- PLG → "What's your activation metric? Conversion rate?"
- Build in Public → "Are you sharing struggles or just wins?"
- Cold Email → "What's your open rate? Reply rate?"

### Step 4: Output

```
## 📊 GTM Channel Analysis

### Your Context
[Stage / model / audience / current channels]

### Top 2 Recommended Channels
1. [Channel] — Why + concrete next steps + success metric
2. [Channel] — Why + concrete next steps + success metric

### Channels to Avoid (for now)
[Why they don't fit your stage/model]

### Case References
[2-3 founder cases at your stage using those channels]

### Your Channel Transition Path
[What to do after this channel maxes out]
```

---

## Channel Transition Patterns (When to Add a Second)

Based on data analysis of founders who successfully added a second channel:

| First Channel | Second Channel (when maxed) | Stage to Transition |
|---|---|---|
| Build in Public | Content/SEO | ~$3-5K MRR |
| Product Hunt | Content/SEO or Cold Email | ~$2-3K MRR |
| Community | Content/SEO | ~$5-10K MRR |
| Content/SEO | Cold Email or PLG | ~$20-50K MRR |
| PLG | Outbound or Partners | ~$50-100K MRR |
| API Integrations | Content/SEO or Partnerships | ~$10-20K MRR |
| Cold Email | Content/SEO | ~$10-30K MRR |

---

## Reference Files

| File | Purpose |
|---|---|
| `references/channel-profiles.md` | Deep-dive on each of the 10 channels: execution playbook, metrics, traps |
| `references/case-library.md` | Case studies for each channel with real founder names and revenue data |
| `references/stage-gtm.md` | Stage-matched GTM with diagnostic questions for stuck founders |
| `references/data-sources.md` | Data sources, confidence levels, and known gaps |

---

## Output Rules

- **Data confidence tagging**: Every recommendation labeled with its data confidence (⭐⭐⭐⭐⭐ Strong / ⚠️ Partial / ❌ Thin)
- **Stage-appropriate**: Don't recommend SEO to someone at $0 MRR who needs cash this month
- **Model-appropriate**: Don't recommend PLG to an agency founder
- **Real cases required**: Every channel recommendation backed by ≥1 named founder/company with revenue outcome
- **Honest about gaps**: Channels with partial data are clearly marked — no pretending
- **Language**: Match user's language. Chinese users see SKILL.zh-CN.md
