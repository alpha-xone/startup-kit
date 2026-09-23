# Harness map — Stage 6: Maintain

How each Claude Code mechanism named in the source playbook lands in DSH. Verified against the installed harness. This stage depends most on triggers the harness does not run for you.

## What DSH does natively

| Playbook mechanism | DSH equivalent | Notes |
|---|---|---|
| Structured output that restarts the loop | `intent.md` (a file convention, not a harness feature) | Unchanged, and the reason the loop closes. |
| Agent writes the post-mortem to a version-controlled lessons file | Plain file writes | Repo convention. |
| Triage queue | A file directory, a repo issue list, or the channel | No harness feature needed. |
| Agent verifying the metric is back at baseline | Read-only tools | As long as the metric store is reachable. |

## What needs mounting or building

| Playbook mechanism | Status in DSH | What to do instead |
|---|---|---|
| A service that receives webhooks and starts a run | `dsh-webhook` and `dsh-webhook-github` are **installed but not mounted** in the `web` profile | Mount in `~/.dsh/profiles/web/cordis.patch.yml`, or trigger externally (a scheduled CI job that opens a session/task). |
| Headless, stateless, non-interactive invocation | **No `claude -p` equivalent** | Your own script against the model API, or a session that a human or CI starts. This is the biggest gap in the stage. |
| `schedule_create` used as a scheduler | **Available but session-local** — do not use it for production monitoring | It delivers reminders only while the session is live, has no external notification, uses fixed intervals (≥5 min) rather than cron, and catches up to the latest occurrence only. Mounting it also requires the Schedule overlay (the `ui-schedule` row ships disabled). |
| GitHub Actions scheduled workflow | Platform-independent | This remains a good trigger layer. The workflow starts your job; the job does the work. |
| Claude Security (hosted scheduled scanning) | **No DSH equivalent** | Use an external scanner, or a scheduled agent run that reads the repo and writes findings as `intent.md`. |
| Claude Tag (agent as a member of a Slack/Teams channel) | **No equivalent** | A session a human opens with the incident context, or a mounted webhook. Say which you are doing. |
| OpenTelemetry export of every invocation, finding, and triage decision | `dsh-session-telemetry-otel` **is mounted**, but `mode: FEEDBACK_ONLY` by default | Ordinary activity is not exported. `DSH_TELEMETRY_OTLP_URL` overrides the endpoint; a non-empty `DSH_TELEMETRY_DISABLED` opts out. Do not claim a complete invocation audit trail. |

## Mounting a webhook trigger

```yaml
- id: webhook-github
  name: '@deepseek-ai/dsh-webhook-github'
  config: {}
```

Add to `~/.dsh/profiles/web/cordis.patch.yml`. The harness hot-reloads that file (`patchReload: live`), so no restart is needed. Do not edit `cordis.yml` — it is an intentionally empty root recomposed from bundles plus the patch on every boot.

## Design the loop around the gaps

Because DSH has no headless invocation and no external scheduler for sessions, the honest architecture is:

```
metric store ──> deterministic detector (your code, versioned, unit-tested)
                        │ breach + tier
                        ▼
              external scheduler or CI job
                        │
                        ├─ read-only diagnosis: run via your own model-API script, or
                        └─ propose: open a PR (branch protection) / trigger a pre-approved runbook
                        │
                        ▼
              intent.md committed to the triage home
                        │
                        ▼
              human triage ──> ai-sdlc-plan ──> … ──> review gate
```

The detector, the tiers, the routes, and the `intent.md` handoff all transfer unchanged. What changes is step three: **the invocation is CI or a human, not the harness.**

## Honest limitation

Two properties of the source playbook's Stage 6 cannot be reproduced here:

1. **"No person in the invocation path."** With no headless mode, either CI starts the run (a person configured CI once, which is close enough) or a person starts the session. Be precise about which.
2. **"Invocations are logged with a timestamp"** as a governance claim. Telemetry defaults to feedback-only, so unless you set `DSH_TELEMETRY_OTLP_URL` and change the mode, the record is the session log on this machine, not an audit stream.

The parts that matter most — deterministic detection, tiered authority, pre-approved routes, and the finding re-entering as `intent.md` — all transfer intact. Build those first; the trigger plumbing is the replaceable part.
