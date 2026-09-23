# `plan.md` template

Written before code, reviewed before code, committed with the change. An engineer who never saw the conversation must be able to implement from this file alone.

```markdown
# Plan: <change name> (from intent.md @ <commit>)

## Files that change
<path> (new | modified | deleted), <path>, ...

## Order of work
1. <step, in the order it must happen>
2. ...

## Risks
What could break, and the specific mechanism. Not "this is risky" —
name the rate limit, the migration, the shared state.

## Proof
The tests and checks that demonstrate it works. Name them concretely.

## Options considered and rejected
What else was possible and why it was not chosen. This is what a
reviewer needs in order to disagree usefully.

## Departures from the plan
(Filled in during implementation, in the same commit as the change.)
```

## Filled example

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)

## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py

## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.

## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.

## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

## Interrogate the plan

Ask these before approving. A plan that cannot answer them is not finished:

- What could this change break, specifically?
- Which step is most risky, and what is the blast radius if it goes wrong?
- What other options did you consider and reject, and why?
- Which of these steps is reversible, and which is not?
- What will the diff look like if this goes well — roughly how large?

## Keeping the plan honest

- When implementation departs from the plan, **update `plan.md` in the same commit as the code.**
- Consider a check that fails when a commit touches implementation files without touching `plan.md`. In DSH this is a repo-side git check or a mounted `PreToolUse` hook, not a built-in feature.
- PR review reads the diff against `plan.md`. That comparison is what makes a large agent-written diff reviewable at all.
