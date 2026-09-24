---
name: forge
description: "Forge — idea generation engine. Helps founders find real problems worth solving. G0 companion to preflight. Triggers: 'find me ideas', 'what should I build', 'idea generation', 'discover opportunities', 'brainstorm startup ideas'. Outputs structured opportunity report with pain evidence. Adapts web research to whatever search capability the runtime has (native tools, OpenCLI, browser automation, or human-in-the-loop). v0.6. Chinese version at SKILL.zh-CN.md."
---

# Forge · Idea Generation Engine

> **Find real problems before you write a line of code.**

Forge is the pre-G0 companion to preflight. While preflight asks "is this idea viable?", Forge asks "what problems are worth solving?" — before you have an idea.

## Core Thesis

**The best startup ideas come from problems you've personally experienced or observed — not from brainstorming "good ideas."** Forge helps you systematically surface and validate real pain points using structured discovery methods.

### Three modes:

- **Pain Mining**: "I want to build something in [domain] — what problems are worth solving?" → Surfaces pain evidence from industry profiles, user complaints, and competitor gaps
- **Idea Stress-Test (light)**: "I have an idea — does it pass the sniff test?" → Quick 5-question pre-screen before running full preflight
- **Adjacent Opportunity**: "I know [domain] — what adjacent problems could I solve?" → Maps pain points from preflight's 16-industry profile data

## The Forge Framework

### Step 1: Capability Probe

Before mining, determine which web-access tiers are live in **this** runtime. **Never assume a tier exists.**

| Tier | Mechanism | How to probe |
|---|---|---|
| **A** | Native web tools — WebSearch / WebFetch or the host's equivalent | Run one query that must return results |
| **B** | **OpenCLI** — turns any website into a CLI, driving your already-logged-in Chrome | `opencli doctor` (exit 0 = ready) · `opencli list` · `curl -s localhost:19825/status` |
| **C** | Generic browser automation — Playwright / agent-browser / chrome-devtools-style MCP | Open a known site and read back the DOM |
| **D** | Human in the loop — the user pastes raw threads, screenshots, exports | Just ask them |

Tier A is universal but blind behind login walls and to anti-scraped sites. Tier B is what gets through them, with structured output. Record the probe result — it goes into the report's capability section.

**Per-channel routing, the OpenCLI command reference, exit codes, and the degradation rules live in [`references/web-research-capabilities.md`](references/web-research-capabilities.md).**

### Step 2: Source Selection

Pick one or combine:

- **Personal pain** — What frustrated you recently? What manual process do you repeat?
- **Industry profile gaps** — Preflight's 16-industry failure data shows where startups die → the inverse is where opportunities live
- **Complaint mining** — Reddit, X, app store reviews, customer support forums, 小红书 / 知乎 / V2EX. Look for "I wish there was a tool that..." — **this is the one source that depends on web access, so route it by tier (Step 1)**
- **Workflow observation** — Watch people do their jobs. What takes too long? What requires workarounds?
- **Portfolio approach** — Build multiple small things. One will stick. 17 products in 12 months (Marc Lou method)

### Step 3: Pain Validation (Quick Filter)

For each candidate idea, score 0-2:

| Question | 0 | 1 | 2 |
|---|---|---|---|
| Do you experience this pain yourself? | No | Indirectly | Yes, personally |
| Can you name 5+ people with this pain? | No | Maybe | Yes, by name |
| Is someone already paying for a solution? | No | Free workarounds exist | Paid products exist |
| Is the pain getting worse? | Stable | Growing slowly | Growing fast |
| Would you pay to solve it? | No | Maybe $10/mo | Yes, $50+/mo |

**Score ≥6**: Promising → proceed to preflight G1.
**Score 3-5**: Interesting but needs more validation → run 15 Mom Test conversations.
**Score <3**: Not yet → keep mining.

### Step 4: Output

```
## 🔨 Forge: Opportunity Report

### Domain: [user's domain]

### Pain Points Found
1. [Pain] — Evidence: [link] — Via: [tier] — Retrieved: [date] — Score: [X/10]
2. [Pain] — Evidence: [link] — Via: [tier] — Retrieved: [date] — Score: [X/10]

### Top Opportunity
[Highest-scoring idea + why]

### Search Capability & Blind Spots
[Tiers available. Channels attempted but unreachable, and why.
Never write "no demand" when the truth is "could not reach".]

### Next Step
[Run preflight G1 / More Mom Tests / Keep mining]

### References
[Industry profile insights, competitor gaps, etc.]
```

## HTML Output (optional)

This skill defaults to structured Markdown. When the user wants a visual report, render it by **delegating**, not by styling it yourself:

- Visual layer → invoke the **`impeccable`** skill (Read mode for a report).
- Every chart → invoke the **`diagram-design`** skill, **light templates by default** (`assets/template.html`).
- Deliver one self-contained light-mode HTML file. Never hand-roll a palette or a chart.

## Reference Files

| File | Purpose |
|---|---|
| [`references/web-research-capabilities.md`](references/web-research-capabilities.md) | Web-access tiers, capability probe, per-channel routing, degradation rules |
| [`../preflight/references/discover.md`](../preflight/references/discover.md) | Channel map + cross-platform search phrases (owned by preflight) |
| [`../preflight/references/industry-profiles.md`](../preflight/references/industry-profiles.md) | 16-industry failure data — the inverse is where opportunities live |

## Output Rules

- **Pain-first**: No "great idea" without evidence of actual suffering
- **People, not markets**: "5 people with this exact pain" > "the market is $X billion"
- **Score honestly**: Low score = keep mining, not "convince yourself"
- **Declare blind spots**: "Unreachable on this channel" ≠ "no demand exists". State which tiers you had and what you could not reach
- **Date every claim**: a "this is a gap" finding expires in weeks, not quarters
- **Complement preflight**: Forge feeds into preflight G1. Don't duplicate G1's depth
