---
name: ai-sdlc-plan
description: "AI-native SDLC Stage 1 (Plan) — turn a raw idea or triggered event into a committed `intent.md` proto-spec in the originator's own words, then gate it to Design. Use when someone has an idea, a ticket, or an alert and wants it written up as a machine-actionable artifact instead of a backlog entry. Triggers: 'write up this idea', 'turn this into intent.md', 'capture requirements', 'proto-spec', 'start a feature', 'the product owner needs to approve this idea'. Companion to ai-sdlc-design."
---

# AI-Native SDLC · Stage 1: Plan

## Boundary

One job: **produce a committed `intent.md` and get a product owner to accept or close it.**

Plan does not decide how to build (that is `ai-sdlc-design` and `ai-sdlc-build`) and does not estimate. If you find yourself writing file paths, a technical design, or story points, you have left this stage.

## The shift this skill encodes

| | Traditional | AI-native |
|---|---|---|
| Routing | Backlog entry → user story → story points → refinement meeting | `intent.md` in the originator's own words, committed to a shared home |
| Ownership | Transfers at every handoff, so meaning degrades | Originator stays the author; one artifact carries the meaning |
| Trigger | A person decides to write it up | A person, a ticket, or an alert can start the same five steps |

The artifact is the point. A committed `intent.md` is readable by a product owner **and** actionable by the next stage, and the commit is the audit record.

## Prerequisites

None. Plan is the only stage with no upstream dependency — start here.

Infrastructure you need once:
- A version-controlled home for intent. For a single product, `intent/` in the product repo. A separate intent repo is only worth it when intent spans many repositories.
- One written `intent.md` template, agreed by a lead.
- A decision on who can write to the intent home — contributors will come from across the organization.

In DSH, non-engineers skip git entirely: they describe the problem in session, and the agent commits the markdown on their behalf. See `references/harness-map.md`.

## How to execute

1. **The originator describes the problem in their own words.** What they cannot do today, who is affected, what better looks like, what is out of scope. No formal language, no template fields yet.
2. **Brainstorm until the idea is concrete.** Ask the questions an analyst would ask: scope, users, constraints, and what success looks like. Do not accept "improve the dashboard" as an outcome; get to the observable change.
3. **Write the result as `intent.md`** using the template in `references/intent-template.md`. Cover problem, proposed outcome, affected users and systems, constraints, and open questions.
4. **Have the originator correct it.** They own the meaning; the agent owns the prose. Never ship an `intent.md` the originator has not read.
5. **Commit it to the shared home** so author and timestamp join the record. The product owner picks it up from there.

Handle the two other entry routes with the same five steps:
- **Ticket filed** — read the ticket, draft `intent.md`, route to the product owner.
- **Alert fired** — this is the loop closing from `ai-sdlc-maintain`; the agent's diagnosis already arrives in Stage 1 format.

## The gate

| | |
|---|---|
| **Human owner** | Product owner |
| **Decision** | Accept into Design, or close |
| **How it is recorded** | The merge of the artifact, or the closed review |
| **What "accepted" fires** | Stage 2 (Design) — the requirements and design pass |

The product owner **reviews and corrects**, they do not write from scratch. That is the whole speed gain: the artifact exists before the meeting would have been scheduled.

## Do not

- Do not add story points, estimates, or delivery dates. They belong to no stage in this playbook and re-introduce the ritual Plan removes.
- Do not let the agent invent constraints the originator never stated. Constraints are facts, not suggestions.
- Do not leave open questions out to make the artifact look complete. Carried-forward open questions are exactly what Stage 2 must resolve or escalate.

## Measure it

**Leading** — time from first conversation to a committed `intent.md`, read from the commit's author and timestamp. Expect multi-week elicitation cycles to fall to hours.

**Lagging** — survival rate: the share of `intent.md` files accepted into Design rather than closed. Also count `intent.md` edits made *after* the first `spec.md` commit for the same change — each one is a requirement that leaked.

## References

- `references/intent-template.md` — the artifact template, with a filled example.
- `references/harness-map.md` — which steps DSH does natively and which need setup.

Chinese version at `SKILL.zh-CN.md`.
