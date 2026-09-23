---
name: ai-sdlc-maintain
description: "AI-native SDLC Stage 6 (Maintain) — close the loop: a deterministic detector watches a metric with a rolling baseline, breaches invoke the agent with no person in the invocation path, and what it finds re-enters the pipeline as a new `intent.md`. Also covers scheduled codebase scans and on-call in a chat channel. Use when setting up autonomous monitoring, control bands, post-incident follow-through, or recurring security scans. Triggers: 'close the loop', 'monitor production and file a ticket automatically', 'control band', 'bands.yaml', 'scheduled security scan', 'on-call agent', 'the same incident keeps happening'. Requires ai-sdlc-plan (intent.md format), a review gate, and a rehearsed rollback."
---

# AI-Native SDLC · Stage 6: Maintain

## Boundary

One job: **a trigger invokes the agent with no person in the invocation path, and what it finds re-enters the pipeline as `intent.md`.**

Maintain does not fix things beyond a bounded PR. A finding that fits in one PR goes through the review gate; anything larger becomes an `intent.md` and starts at Plan. That is what makes the loop a loop rather than an alert with a person behind it.

## The shift this skill encodes

| | Traditional | AI-native |
|---|---|---|
| Nature | Reactive. An alert fires at 3am and can be missed | A trigger invokes the agent with no person in the path |
| Follow-through | Post-mortem actions may never reach the codebase | Findings re-enter the pipeline as `intent.md` and flow to Plan |
| Detection | Often manual, or a threshold nobody trusts | **Deterministic**, version-controlled, unit-tested, no model involved |
| Judgement | A person decides everything | Tiered: log at 1σ, diagnose at 2σ, propose at 3σ |

The load-bearing separation: **detection is deterministic; the model is invoked only once a band is breached.** A model deciding when to wake up is an unpredictable system monitoring a production one.

## Prerequisites

Everything the loop re-enters:

- `intent.md` format (`ai-sdlc-plan`) — the loop's structured output.
- The review gate (`ai-sdlc-deploy`) — findings route through it like any other change.
- A rehearsed rollback path (`ai-sdlc-deploy`) — the highest autonomy tier invokes it.

## Play: closing the loop

1. **Pick one metric with a stable rolling baseline.** One. Candidates: CI test failure rate, post-deploy 5xx rate, PR cycle time.
2. **Write the detection script.** Mean and standard deviation over a rolling window, with rules (Western Electric or similar) so the bands catch slow drift as well as spikes. The script is **version controlled and unit tested**, and detection involves **no model**. Getting this step wrong makes everything downstream noise.
3. **Define response tiers in version-controlled config** (`bands.yaml`, template in `references/bands-yaml.md`):
   - **1σ** — log only.
   - **2σ** — invoke the agent read-only to diagnose.
   - **3σ** — the agent may act, but only by opening a PR into the review gate or triggering a **pre-approved** runbook.
4. **Choose the trigger layer** — a scheduled workflow, a webhook from the existing monitoring stack, or a cron job inside the network. The agent run is stateless and non-interactive, which is what lets a loop begin and end without anyone starting it. In DSH, a genuinely headless trigger needs `dsh-webhook-github` mounted (not mounted by default) or an external scheduler; `schedule_create` is a session-local reminder, **not** a production scheduler — do not use it as one.
5. **Have the agent write its diagnosis as `intent.md`**, in the Stage 1 format: the anomaly and its evidence, a proposed outcome, affected systems, open questions. From there the finding goes through the pipeline like anything else.
6. **Triage the queue.** A service owner or on-call engineer routes product-facing findings to the product owner. Fix now, schedule, or dismiss.
7. **Add an eval for the incident** once a fix ships (`ai-sdlc-test`), so the class of problem is protected against.

The dismissal path matters: **dismissals tune the bands** and reduce noise. A dismissal with no feedback into the thresholds guarantees the same false positive forever.

## Tier discipline

| Tier | Action | Why |
|---|---|---|
| 1σ | log | Cheap, no model, builds the record you will need to tune the bands |
| 2σ | diagnose, read-only tools | A hypothesis costs nothing and tells a human where to look |
| 3σ | propose only: PR or pre-approved runbook | The agent's authority is bounded by routes someone approved in advance |

The alternates worth copying:
- CI test failure rate breaches 3σ → the agent quarantines the flaky test or opens a revert PR; the review gate decides.
- Post-deploy 5xx breaches 3σ with a deployment in the window → the agent triggers the existing rollback pipeline.
- PR cycle time trips a drift rule → the agent writes a report for engineering leadership. The same harness works for process metrics as well as production ones.

## Play: recurring codebase scans

A security scan is a point-in-time statement about a codebase under a particular model, and **both halves go stale**: the code changes weekly, and each model generation finds vulnerabilities the previous one missed.

1. Connect the repositories and organize them by repo, service, or team, so ownership of findings is clear.
2. **Run a first full scan as the baseline** — including repositories previously scanned by other tools or earlier models. Expect it to surface findings in code considered clean.
3. Set a schedule per project. Weekly is a sensible default for actively developed services; scope to a directory or branch where a repo is large or mixed.
4. **Triage with the confidence rating in hand.** Dismiss with a reason, so the dismissal is recorded and the same finding does not return as new next run.
5. A bounded finding becomes a patch through the PR review gate. The agent that proposed the fix has no route to approve it.
6. **Anything wider than one patch** — an architectural weakness, a pattern repeated across services — becomes an `intent.md` and starts at Plan.
7. When a fix reaches production, add an eval for that vulnerability class.
8. Export findings to the existing tracker and audit systems, where auditors already expect them.

Coverage is dated from the last run, not the first. Model-driven scanning **augments** static analysis and dependency scanning; the deterministic checks stay in CI.

## Play: on-call in the channel

Incidents also arrive as a 10pm message in a chat channel. Making the agent a member of that channel under its own identity gives each incident a first responder, and the response itself becomes part of the loop and the memory for future incidents.

- The **conversation and institutional knowledge stay in the channel**; anyone there can guide the response.
- Through MCP the agent verifies the metric is back at baseline and confirms it in the thread.
- It writes the post-mortem to a version-controlled lessons file that future investigations read.
- A small, well-bounded fix arrives as a PR through the review gate; anything larger becomes an `intent.md`.

The channel is the audit trail: request, diagnosis, human authorization, and fix all stay where the incident was handled.

In DSH there is no chat-channel agent. The nearest substitutes are a session a human opens with the incident context, or a webhook-mounted trigger. Say which one you are actually doing.

## Do not

- Do not let a model decide when to wake up. Detection stays deterministic.
- Do not give the 3σ tier unbounded authority. It may propose through pre-approved routes, nothing more.
- Do not dismiss a finding without feeding the dismissal back into the thresholds.
- Do not call `schedule_create` a production scheduler. It is session-local and delivers only while the session is live.

## Measure it

**Leading** — time from band breach to an `intent.md` in the triage queue (the detector's log has both timestamps); share of connected repositories on a schedule; time from finding to patch entering review.

**Lagging** — share of findings that become merged fixes; **repeat incidents of the same class** (should fall as fixes add cases to the eval suite); findings per scan on repositories that have been through several runs; vulnerabilities found by scheduled scan versus found in production.

## References

- `references/bands-yaml.md` — the tier config, the detector design, and the `intent.md` handoff from a breach.
- `references/harness-map.md` — triggers, scheduling, and scans in DSH: what is mounted, what needs mounting, what does not exist.

Chinese version at `SKILL.zh-CN.md`.
