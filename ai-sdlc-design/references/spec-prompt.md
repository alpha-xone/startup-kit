# The Design pass

## The prompt

Run this against the accepted `intent.md`, with the organization's policy skills loaded:

> Read the attached `intent.md` and produce a requirements and design spec for integrating it into our existing codebase. Apply the skills available to you so the plan conforms to our brand guidelines, security policies and UX standards. Document the spec fully as `spec.md`, ready to hand to the engineering team. Describe clearly any areas of concern, especially where you cannot satisfy contradicting policies.

Two things carry the weight:
- **"Apply the skills available to you"** — the policies must exist as skills, or this sentence does nothing.
- **"especially where you cannot satisfy contradicting policies"** — without this, the model resolves contradictions silently.

## `spec.md` shape

```markdown
# Spec: <change name> (from intent.md @ <commit>)

## What is being built
The requirements, in terms the engineering team can plan against.
Not a file list — behaviour, interfaces, data, states.

## How it fits the existing system
Affected services, modules, data stores, and the integration points.
Where the existing system already provides something, name it.

## Policy constraints applied
Brand / security / compliance / UX constraints and how the spec
satisfies each. Name the skill or policy that supplied it.

## Areas of concern
Each flagged item with: what the concern is, which policies are in
tension, what it affects, and who must resolve it.
This section being empty is acceptable; being empty when policies
conflict is a defect.

## Open questions carried from intent.md
Each one answered, deferred with a reason, or escalated.

## Out of scope
Explicit non-goals, so Build does not expand into them.
```

## The contradiction rule

Instruct explicitly, when two policies cannot both hold:

1. Do not choose a winner.
2. Name both policies and the exact part of the spec they collide on.
3. State the consequence of each choice.
4. Flag it as a concern for the product owner, who routes it to the named policy owner.

An agent that silently picks is producing a governance defect that surfaces months later.

## Quality checks before commit

- Does every policy claim cite the skill that supplied it?
- Is each `intent.md` open question answered, deferred with a reason, or escalated? "Answered" by assumption does not count.
- Could an engineer who has never seen the intent plan the work from this spec alone?
- Are the flagged concerns actually actionable, i.e. does each name a person or role who decides?

## Audit record

Commit together, in one commit or one PR:

- `intent.md` (accepted version)
- `spec.md`
- the prompt used
- the skill versions in force (the commit SHA of each policy skill)

The pair plus its provenance is what a later auditor reads to learn what was asked and what was decided.
