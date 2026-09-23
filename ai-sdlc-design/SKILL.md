---
name: ai-sdlc-design
description: "AI-native SDLC Stage 2 (Design) — take an accepted `intent.md` and produce a committed `spec.md` in one prompted session, with organization policy (brand, security, compliance, UX) applied as constraints and areas of concern flagged. Use when an intent has been accepted and needs a requirements-and-design spec the engineering team can plan against. Triggers: 'write the spec', 'turn the intent into a design', 'requirements and design pass', 'spec.md', 'review this spec for policy concerns'. Requires an accepted ai-sdlc-plan artifact."
---

# AI-Native SDLC · Stage 2: Design

## Boundary

One job: **turn an accepted `intent.md` into a committed `spec.md`, with policy applied while writing and concerns flagged.**

Design does not plan the implementation (that is `ai-sdlc-build`) and does not re-litigate whether the change should happen. If the intent is wrong, send it back to `ai-sdlc-plan` rather than designing around it.

## The shift this skill encodes

| | Traditional | AI-native |
|---|---|---|
| Structure | Requirements and design are separate phases, run by separate teams | Both collapse into one prompted session |
| Policy | Discovered in a review weeks later | Read and applied while the spec is written |
| Output | Analyst's requirements, re-parsed by designers | One spec, constrained by organization skills, with concerns flagged |
| Product owner | Commissions both phases | Reviews and resolves flags; does not write the spec |

Policy as a constraint rather than a checkpoint is the core idea. A concern raised at spec time costs an edit; the same concern raised at review costs a rework cycle.

## Prerequisites

- An accepted `intent.md` (Stage 1). Do not start from a verbal request — the gate is what makes this stage cheap.
- Brand, security, compliance, and UX policy **written as skills**. If a policy exists only in a wiki page, encode it as a skill first; otherwise the agent cannot apply it as a constraint.
- A product owner with session access. No engineering skill is required.

## How to execute

1. **Open a session with the organization's policy skills available** and attach the accepted `intent.md`.
2. **Run the pass.** Point at the `intent.md`, name the constraints, and demand flagged concerns. The prompt is in `references/spec-prompt.md`.
   - Run it by hand the first few times.
   - Once the shape is stable, make the acceptance of `intent.md` the trigger. In DSH this is a prompt or a mountable webhook, not an automatic merge hook — see `references/harness-map.md`.
3. **Review the spec against the idea.** Does it solve the stated problem? Are the open questions from `intent.md` answered or explicitly carried forward?
4. **Work the flagged concerns first.** These are the points an analyst would have escalated. The product owner resolves each one with its named policy owner *before* engineering sees the spec.
5. **Commit `spec.md` alongside `intent.md`.** The file pair records what was asked for and what was decided.
6. **Make the progress call.** Accepting the spec is what starts Stage 3 (Build) plan mode. Consult a technical lead for anything the organization classes as higher risk — a human teammate always makes this call.

## The gate

| | |
|---|---|
| **Human owner** | Product owner; named policy owners for each flagged concern |
| **Decision** | Accept the spec into Build, or return it |
| **Evidence** | The committed spec, **the prompt that produced it**, and the skill versions in force — all in version control |
| **What "accepted" fires** | Stage 3 (Build) — plan mode |

Logging the prompt alongside the spec is deliberate. Without it, a later reader cannot tell which constraints were in force when the spec was written.

## When policies contradict

The most valuable output of this stage is a flagged contradiction, not a silently chosen side. Instruct the agent to surface it and stop rather than resolving it by preference:

> Where two policies cannot both hold, do not pick one. Name both, name the affected part of the spec, and flag it for the product owner.

That flag is what routes to a policy owner. An unflagged resolution is a governance defect discovered later, at the worst time.

## Do not

- Do not start from an unaccepted intent. The gate is the stage's whole value.
- Do not let the spec quietly resolve a policy contradiction.
- Do not let the design phase drift into implementation planning — file paths, ordering, and tests belong to `plan.md`.
- Do not discard the prompt. It is part of the audit record.

## Measure it

**Leading** — elapsed time between the `intent.md` commit and the `spec.md` commit for the same change, compared with the old requirements-plus-design cycle.

**Lagging** — requirements rework after build starts: count `spec.md` commits dated *after* the first `plan.md` commit for the same change. Each one is a design decision made too late.

## References

- `references/spec-prompt.md` — the pass prompt, the `spec.md` shape, and the contradiction rule.
- `references/harness-map.md` — how to load policy skills in DSH and what the trigger becomes.

Chinese version at `SKILL.zh-CN.md`.
