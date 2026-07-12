---
name: forge
description: "Forge — idea generation engine. Helps founders find real problems worth solving. G0 companion to preflight. Triggers: 'find me ideas', 'what should I build', 'idea generation', 'discover opportunities', 'brainstorm startup ideas'. Outputs structured opportunity report with pain evidence. v0.5. Chinese version at SKILL.zh-CN.md."
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

### Step 1: Source Selection

Pick one or combine:

- **Personal pain** — What frustrated you recently? What manual process do you repeat?
- **Industry profile gaps** — Preflight's 16-industry failure data shows where startups die → the inverse is where opportunities live
- **Complaint mining** — Reddit, Twitter, app store reviews, customer support forums. Look for "I wish there was a tool that..."
- **Workflow observation** — Watch people do their jobs. What takes too long? What requires workarounds?
- **Portfolio approach** — Build multiple small things. One will stick. 17 products in 12 months (Marc Lou method)

### Step 2: Pain Validation (Quick Filter)

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

### Step 3: Output

```
## 🔨 Forge: Opportunity Report

### Domain: [user's domain]

### Pain Points Found
1. [Pain] — Evidence: [source] — Score: [X/10]
2. [Pain] — Evidence: [source] — Score: [X/10]

### Top Opportunity
[Highest-scoring idea + why]

### Next Step
[Run preflight G1 / More Mom Tests / Keep mining]

### References
[Industry profile insights, competitor gaps, etc.]
```

## Reference Files

| File | Purpose |
|---|---|
| `references/industry-pain-map.md` | Mapping industry failure data to opportunity spaces |
| `references/discover.md` | Pain mining methods from preflight's G0 |

## Output Rules

- **Pain-first**: No "great idea" without evidence of actual suffering
- **People, not markets**: "5 people with this exact pain" > "the market is $X billion"
- **Score honestly**: Low score = keep mining, not "convince yourself"
- **Complement preflight**: Forge feeds into preflight G1. Don't duplicate G1's depth
