# `intent.md` template

Keep it under a page. The originator must be able to read it and the next stage must be able to act on it.

```markdown
# Intent: <short name for the change>
Author: <name> (<team>). Status: draft | accepted | closed.

## Problem
What cannot be done today, and who is affected. State it in the
originator's terms, with whatever evidence exists (call volume, ticket
count, a quoted complaint). No solution language here.

## Proposed outcome
The observable change. What is true after this ships that is not true now.

## Affected users and systems
Named users, teams, repos, services, data.

## Constraints
Policy, technical, budget, deadline, or regulatory limits that the
solution must respect. Facts only.

## Open questions
What is genuinely undecided. Each one is a thing Stage 2 must answer or
carry forward — an empty section here is a warning sign, not a win.
```

## Filled example

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Affected users and systems
Claims handlers, portal team, claims-core API.

## Constraints
No new PII in the portal session. Existing authentication only.

## Open questions
Do third-party loss adjusters need access too?
```

## Quality checks before commit

- Could a reader who has never met the originator implement the *intent*? If not, the outcome is still too vague.
- Is every constraint a fact someone stated, rather than an inference?
- Does the proposed outcome describe a change in the world, or a change in the software? Describe the world.
- Is the author line a real person who has read this file?
