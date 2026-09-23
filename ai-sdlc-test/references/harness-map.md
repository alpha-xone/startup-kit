# Harness map — Stage 4: Test

How each Claude Code mechanism named in the source playbook lands in DSH. Verified against the installed harness.

## What DSH does natively

| Playbook mechanism | DSH equivalent | Notes |
|---|---|---|
| "Give Claude a way to verify its own work" | Workspace commands via `pwsh` (Windows) | The agent runs the same commands a human would. This is the whole feedback loop. |
| Wrapping checks into one target (`make test`) | Unchanged — it is a repo concern | Nothing harness-specific. Do this first. |
| Commands listed in `CLAUDE.md` with healthy output | Same, in `AGENTS.md` or `CLAUDE.md` | Loaded at session start. |
| Browser / screenshot verification wired via MCP | Do it with what is on the machine | Headless browser + screenshot is available (Edge CDP on this machine is the established route). `webapp-testing` and `verify` skills cover the procedure. |
| Subagent verifier in a fresh context | `subagent_fork` / `subagent` | `subagent_fork` inherits the conversation, so it can compare against `plan.md`, and returns a verdict not intermediate steps. |
| Session transcript as the evidence log | Session log under `~/.dsh/sessions` | Locally persisted per session, replayable. |
| OpenTelemetry export to an observability stack | `dsh-session-telemetry-otel` **is mounted** in the base bundle | Defaults to `mode: FEEDBACK_ONLY` — ordinary activity is *not* exported. An explicit user feedback action releases a session-log prefix. A non-empty `DSH_TELEMETRY_DISABLED` opts out entirely; `DSH_TELEMETRY_OTLP_URL` overrides the endpoint. Do not assume a full activity trace exists. |

## What needs setup

| Playbook mechanism | Status in DSH | What to do instead |
|---|---|---|
| `claude -p` non-interactive runs in CI | **No equivalent** | Write your own script against the model API, or run evals as a session-driven task with a human in the invocation path. |
| The GitHub Actions eval workflow with `--allowedTools` / `--output-format json` | Not applicable | Same: your own runner. The *design* of the eval suite transfers; the YAML does not. |
| Evals gating merges on a pass-rate threshold | No built-in eval runner | Enforce it in your CI as an ordinary check that calls your runner. |
| Hooks blocking edits to test files during a fix | Available via the hooks bridge, **not mounted** | Mount `dsh-hooks-claude-code` (see `ai-sdlc-build/references/harness-map.md`), or enforce it in PR review, or run the fix session with a permission preset that cannot write to the test paths. |

## What to use from DSH's own skill set

Rather than reimplementing procedure, load the skills that already cover it:

| Need | Skill |
|---|---|
| Run the project's test stack, narrowest useful tests first, report gaps honestly | `test` |
| Exercise the real app/CLI/API and collect observable evidence — tests alone do not count | `verify` |
| Start or reuse a local app, wait for readiness, inspect rendered state/console/network, act from observed selectors | `webapp-testing` |
| Reproduce, minimize, localize, and identify a root cause | `debug` |
| Correctness review with file/line evidence | `review` |

## Honest limitation

This is the stage where DSH diverges most from the source playbook. The playbook's Test stage leans on running Claude non-interactively inside CI with machine-readable output and an API key budgeted for eval runs. DSH has no non-interactive mode and no eval runner.

What still transfers in full:
- the feedback loop itself (commands, targets, paste-the-output),
- failing-test-first for bug fixes,
- not letting the agent weaken its own check,
- the eval *suite design* (20–50 real tasks, expected outcomes, gate config changes on pass rate, every incident becomes an eval).

What does not transfer: the CI plumbing. Say so plainly rather than configuring something that will not run.
