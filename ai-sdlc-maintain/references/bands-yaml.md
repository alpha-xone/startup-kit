# `bands.yaml` and the detector

## The tier config

Version controlled. Changing a threshold is a reviewable change.

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose,
            tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose,
            routes: [pull_request, runbook:rollback-deploy] }
```

Read the tiers as an authority ladder, not a severity ladder:

| Tier | Action | Authority granted |
|---|---|---|
| 1σ | log | none |
| 2σ | diagnose | read-only tools |
| 3σ | propose | open a PR, or trigger a **pre-approved** runbook |

Every route in the 3σ tier was approved by a human before the loop ran. That is what keeps autonomy bounded: the agent's reach is an allowlist, not a general capability.

## Detector design

Requirements, in order of how badly things break without them:

1. **Deterministic.** No model in the detection path. A model deciding when to wake up makes an unpredictable system monitor a production one.
2. **A stable rolling baseline.** `rolling_30d`, not a fixed number set once. A threshold that never moves becomes either noise or a blind spot.
3. **Drift-aware rules** — Western Electric or similar. Mean-and-sigma alone catches spikes and misses slow drift, and slow drift is what actually degrades a service.
4. **Version controlled and unit tested.** The detector is code. A false positive at 3am costs more than the detector cost to write.
5. **One metric to start.** Add a second only once the first is trusted.

## From breach to `intent.md`

The agent's output is a Stage 1 artifact, in exactly the format `ai-sdlc-plan` expects:

```markdown
# Intent: <metric> breached <tier> at <timestamp>

## Problem
The anomaly: which metric, what the rolling baseline was, the observed
value, the deviation in sigma, and when it started.

## Proposed outcome
What should be true when this is resolved.

## Affected users and systems
Named services, teams, and the user-visible effect, if any.

## Constraints
What the response may not do.

## Open questions
What the evidence does not explain.
```

Because it is the same format, the breach enters the normal pipeline: triage → Plan → Design → Build → Test → Deploy. No special incident path, and no separate vocabulary to maintain.

## Triage, and why dismissals matter

A service owner or on-call engineer works the queue: **fix now, schedule, or dismiss.**

A dismissal must record a reason, and that reason must feed back into the thresholds. Without that feedback, the bands drift into either permanent noise (everyone ignores them) or permanent blindness (the threshold was raised until nothing fires). Dismissals are the tuning signal.

## After the fix

Add an eval for the incident (`ai-sdlc-test`) so the same class of problem is regression-tested against the agent's own configuration from then on. This is what makes the "repeat incidents" lagging indicator fall rather than plateau.

## Worked examples

| Breach | Agent action | Gate |
|---|---|---|
| CI test failure rate 3σ | Quarantine the flaky test, or open a revert PR | Review gate decides |
| Post-deploy 5xx 3σ with a deployment in the window | Trigger the existing rollback pipeline | Pre-approved runbook |
| PR cycle time trips a drift rule | Write a report for engineering leadership | Human reads it |

The third example matters: the same harness works for **process** metrics, not only production ones. A drift in review latency is a real signal about the SDLC itself.
