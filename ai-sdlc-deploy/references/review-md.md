# `REVIEW.md` — the review policy

Lives at the repo root. Reviewed like code. The tech lead owns it.

```markdown
# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarize the rest as a count.

## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

## Why each section exists

| Section | Problem it prevents |
|---|---|
| **Passes** | Unstructured review that finds whatever it happens to notice. Tagging each finding with its pass lets you see which pass is underperforming. |
| **What Important means here** | Severity inflation. Without a local definition, everything is critical and the human threshold becomes meaningless. |
| **Cap the nits** | Nit floods that bury the two findings that mattered. |
| **Do not report** | Reviewing generated code and re-reporting what CI already enforces — pure noise, and it trains reviewers to skim. |

## The compliance pass

Compliance is the pass that makes the artifact chain pay off. It checks the change against three things:

1. `spec.md` — does it do what was asked?
2. `plan.md` — does it do it the way that was approved? A diff that departs from the plan without an updated plan is a finding.
3. Design principles — the standing conventions.

This is only possible because those artifacts are committed. A repo without them cannot run this pass.

## The feedback rule

**When a review flags the same mistake for the second time, the correction goes into `AGENTS.md` as part of that review.**

Not a backlog item, not a note — the review itself adds it. Because review reads `AGENTS.md`, the mistake is then caught from the next PR onwards. This is the mechanism that makes review get quieter over time instead of repeating itself forever.

Review should also flag when a change has made `AGENTS.md` **outdated** — a convention that moved, a command that changed.

## Monthly tuning

1. Rate the findings so the reviewer improves — mark the ones that were real and the ones that were noise.
2. Adjust the nit cap based on what the rating shows.
3. Add newly generated paths to the do-not-report list.
4. Diff the policy against what CI already enforces, and remove the overlap.

## Machine-readable threshold

If you want to gate merges on findings rather than leaving it to the code owner's judgement, publish the severity counts as a machine-readable tally and let a required check read it. Keep the rule explicit about which severities block — an unstated threshold will be argued about per PR.

## Separation of duties

The agent that wrote the code must have no way to approve it. Review findings inform the human decision; they do not become the decision. Branch protection requiring a code owner's approval is what preserves this, and it must be configured in the repo rather than assumed.
