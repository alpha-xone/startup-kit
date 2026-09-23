# The feedback loop

## The `AGENTS.md` verification block

Put this in the repo's `AGENTS.md` (or `CLAUDE.md`). The agent reads it at session start.

```markdown
## Verifying your work

- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

Three properties make this work, and each is easy to lose:

| Property | Why it matters |
|---|---|
| One command per concern | A sequence of commands with environment knowledge is a sequence the agent will get wrong or skip |
| **An example of healthy output** | "Ran successfully" is not checkable; `Build succeeded` is |
| An explicit prohibition | "Never skip or delete a failing test" closes the cheapest path to green |

## The bug-fix sequence

Order matters. Do not compress these steps.

1. **Reproduce as a test.** Ask for the bug written as a failing test. Not a fix.
2. **Run it and confirm it fails for the right reason.** A test that fails for an unrelated reason proves nothing about the bug.
3. **Commit the test.** Now it exists in history, before the fix.
4. **Fix without editing the test.** The instruction, verbatim: *make it pass without editing the test.*
5. **Enforce step 4.** Block test-file edits during the fix, or reject in review any fix that touches a test. Without this, step 4 is a request, not a constraint.
6. **Run the whole suite**, not only the new test.

The resulting pair — a committed test that predates the fix, plus a fix that could not have rewritten it — is the evidence.

## The UI loop

1. Give the agent a way to run the app and capture what it renders (a screenshot, or a browser it can drive).
2. Give it the approved mock.
3. Instruct it to iterate: implement → screenshot → compare against the mock → adjust.
4. Expect two or three rounds. Each round should visibly improve. If it does not, the target is not specific enough — go back and make step 3 quantifiable.

## What good evidence looks like

The evidence is what the **toolchain** emitted, not a summary of it:

- the literal output of `make test`,
- the build log,
- the screenshot diff,
- the HTTP status and response body.

An agent reporting "tests pass" without the output has given you a claim. Paste-or-it-did-not-happen is the rule, and it is what lets a reviewer concentrate on intent and risk instead of re-running the suite.

## The verifier pass

Once the session believes it is done, run an independent check in a **fresh context** so the verdict is not coloured by the assumptions that produced the code:

> Start the app with `make run`. Exercise the changed behaviour and the two nearest neighbouring flows. Report what you ran, what you saw, and any behaviour that does not match `plan.md`. Do not fix anything; report only.

In DSH, `subagent_fork` is the tool for this: it inherits the conversation (so it sees `plan.md`) and returns a verdict instead of intermediate steps. Note the "do not fix anything" clause — a verifier that fixes its own findings cannot also grade them.
