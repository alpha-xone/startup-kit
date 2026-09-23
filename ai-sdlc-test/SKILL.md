---
name: ai-sdlc-test
description: "AI-native SDLC Stage 4 (Test) — give the agent a feedback loop it can run itself, make verification part of 'done', protect the check from the agent it is checking, and treat the agent's own configuration as something that gets regression-tested. Use when setting up how work is verified, when a session must prove its change works before reporting done, or when asking whether the agent's config still performs. Triggers: 'how do I verify this', 'set up a feedback loop', 'make the agent test its own work', 'write the failing test first', 'regression-test the agent config', 'evals'. Requires the harness to be able to run the tests and the build."
---

# AI-Native SDLC · Stage 4: Test

## Boundary

One job: **every session checks its own work before a human sees it, and the configuration that steers the agent is regression-tested like code.**

Test does not decide whether a change should ship — that is `ai-sdlc-deploy`. It produces the evidence that makes that decision cheap.

## The shift this skill encodes

| | Traditional | AI-native |
|---|---|---|
| When the signal arrives | CI minutes later, a tester days later, production weeks later | The session checks itself before a person looks |
| Who is the bottleneck | Whoever must check all the agent's output | Nobody, if the loop is set up before the work starts |
| Evals | Stage-gate QA at boundaries | A live suite that runs whenever the agent's configuration changes |

The reason this matters more with agents: with a human writing code, a late signal costs a wait. With an agent, a late signal means a person has to check everything the agent produced — and that person becomes the bottleneck.

## Two things that are not the same

| | Feedback loop | Verifier subagent |
|---|---|---|
| Runs | Throughout the task, as many times as the work needs it | Once, after the session believes it is done |
| Context | The same session, same assumptions | A **fresh** context window |
| Purpose | Let the session fix its own mistakes | Get a verdict not coloured by the assumptions that produced the code |
| DSH mechanism | Ordinary test/build/run commands plus the workspace's test skills | `subagent_fork` — it inherits the plan and the change, and returns only a verdict |

Use both. The loop is what makes the work arrive clean; the verifier is what stops a confident session from grading itself.

## Prerequisites

None, but the loop is only worth what the repo can run. Before relying on it: a test suite and a build that each run locally with one command.

## How to execute

1. **Wrap checking into one command per concern** — `make test`, `npm test`, `pytest` — each exiting non-zero on failure. If checking the work currently needs a sequence of commands and some environment knowledge, that is the thing to fix first.
2. **List each command in `AGENTS.md`, with an example of healthy output.** The agent must be able to tell "passed" from "produced text".
3. **State a quantifiable target**, so the agent can check without asking: "all tests in `test_status.py` pass", "the endpoint returns 200 with the new field", "the screenshot matches the attached mock".
4. **For bug fixes, write the failing test first.** Ask the agent to reproduce the bug *as a test*, run it, and confirm it fails **for the reason you expect**. Commit that test. Only then ask for a fix, without editing the test.
5. **For UI work, close the loop visually.** Give the agent a way to run the app and take a screenshot, give it the mock, and let it iterate: implement, screenshot, compare, adjust. Two or three rounds is normal.
6. **Make verification part of "done."** The instruction lives in `AGENTS.md`. Run the checks before reporting a task complete, and show the output.
7. **Protect the loop from the agent.** An agent fixing code must not be able to weaken the check on that code. Block edits to test files during a fix task, or reject in review any fix-only change that touches a test.

The template for steps 2, 3 and 6 is in `references/feedback-loop.md`.

## Why "failing test first" is load-bearing

A test written *after* the fix proves nothing: it is shaped by the implementation, and it would pass whether or not the bug was real. A test that:

- existed before the fix,
- failed for the stated reason,
- and that the agent was not allowed to rewrite,

is proof the bug is gone. That is the whole argument, and it is why step 7 exists.

## Continuous evals

Evals are the AI-native equivalent of stage-gate QA — a suite that runs whenever **the agent's configuration** changes, not just the code.

1. Collect **20–50 real tasks** from recent work, each with its expected or accepted outcome.
2. Write each as an eval: the prompt, plus the checks that define acceptable (tests pass, lint clean, behaviour unchanged, policy followed).
3. Run the suite non-interactively on a schedule and on any change to `AGENTS.md`, `CLAUDE.md`, skills, or hooks. That configuration steers the agent and deserves the regression testing code gets.
4. **Gate configuration changes on the results.** A skill change that drops the pass rate gets reviewed before it merges.
5. Every production incident becomes an eval, written by the team that owned the incident, and stays in the suite.

Treat the suite as live: as models improve, cases that once discriminated stop discriminating, and new ones must be added from ongoing monitoring.

## DSH reality check

DSH has no built-in eval runner and no `claude -p` non-interactive mode for CI. Running evals means your own script driving the model API, or your existing CI with the checks you define. See `references/harness-map.md` for what maps and what does not — do not promise an eval harness the platform does not provide.

## Do not

- Do not accept a test written after the fix as proof.
- Do not let the agent edit the test it is being judged by.
- Do not report a task complete without pasting the actual output. The evidence must come from the toolchain, not from the agent's summary of it.
- Do not let the agent skip or delete a failing test to reach green.

## Measure it

**Leading** — first-pass CI success rate for agent-written changes; and for evals, the pass rate over time plus how long a production incident takes to become a permanent eval.

**Lagging** — review time per PR (should fall once the tests catch what reviewers used to catch), change failure rate, and regressions caught in CI versus regressions found in production.

## References

- `references/feedback-loop.md` — the `AGENTS.md` verification block, the bug-fix sequence, and the UI loop.
- `references/harness-map.md` — what DSH gives you for testing and what you must build.

Chinese version at `SKILL.zh-CN.md`.
