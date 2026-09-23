---
name: ai-sdlc-build
description: "AI-native SDLC Stage 3 (Build) — nothing is implemented without an accepted `plan.md`. Start in DSH plan mode, commit the approved plan, keep institutional knowledge in `AGENTS.md`/`CLAUDE.md` and skills, and run guardrail hooks or sandbox policy instead of relying on habits. Use when implementing an accepted spec, when asked to plan an implementation before coding, or when setting up repo conventions and guardrails for agents. Triggers: 'plan the implementation', 'plan.md', 'implement this spec', 'set up CLAUDE.md or AGENTS.md', 'write a skill for this policy', 'run these tasks in parallel', 'spawn a subagent'. Requires an accepted spec from ai-sdlc-design, or an intent for small changes."
---

# AI-Native SDLC · Stage 3: Build

## Boundary

One job: **produce a committed `plan.md`, then implement it — with institutional knowledge encoded as files the agent reads and guardrails enforced as policy rather than habits.**

Build does not decide what to build (that is `ai-sdlc-design`) and does not certify the result (that is `ai-sdlc-test`).

## The shift this skill encodes

| | Traditional | AI-native |
|---|---|---|
| Start | Engineer reads the design and starts coding | `plan.md` commits first; plan mode enforces it |
| Where the plan lives | The engineer's head, or a ticket comment nobody can review | A committed artifact the later stages check the diff against |
| Knowledge | In people's heads and on wikis | `AGENTS.md`/`CLAUDE.md` and skills the agent reads at session start |
| Guardrails | Habits and reviewer vigilance | Hooks (deterministic) and sandbox policy behind advisory skills |
| Concurrency | One task at a time | Several streams, an engineer steering and reviewing |

The single highest-value rule in this stage: **the plan is reviewed while changing course still means editing a document.**

## Prerequisites

- An implementation plan is expected: the accepted `spec.md` (or `intent.md` for small changes).
- A repo the agent can read.
- Helpful: an `AGENTS.md` (or an existing `CLAUDE.md`) at the repo root.

## Play: plan mode as the default start

1. **Start the session in plan mode** — `/plan` in DSH. Plan mode is guidance plus a reviewed exit, not a capability lock, so also set the sandbox to `read-only` if you want the read-only property enforced. See `references/harness-map.md`.
2. **Give the agent the `intent.md` and `spec.md`** and ask for an implementation plan naming the files that change, the order of work, and the tests that prove it.
3. **Interrogate the plan.** Ask: what could this break? Which step is most risky? What options did you reject, and why?
4. **Iterate until the plan is enough on its own** — a test: an engineer who never saw the conversation could implement the change from `plan.md` alone.
5. **Commit the approved plan as `plan.md`.** Template in `references/plan-template.md`. It joins the audit trail, and PR review checks the eventual diff against it.
6. **Accept and implement.** With a solid plan, implementation is often a single pass.
7. **When implementation departs from the plan, update `plan.md` in the same commit.** A plan that silently diverges from the diff is worse than no plan.

The gate sits before any code exists: review happens when the change is still a document.

## Play: autonomous implementation

Once the guardrails mature — a tuned `AGENTS.md`, skills that encode policy, hooks or sandbox policy that block unsafe actions, and a test suite the agent can run — autonomous execution becomes the default for routine work: a tight spec, a small blast radius, code the tests cover. Route the rest to human review.

In DSH the knob is the permission preset (`read-only` / `workspace-write` / `danger-full-access`), chosen per session. Note what it is not: DSH has no per-edit auto-accept toggle, so "auto mode" here means the session's sandbox and approval policy, not a per-file prompt bypass.

## Play: institutional knowledge as files

**`AGENTS.md`** — the context a new joiner would need: conventions, commands, architecture, and the mistakes the agent keeps making.

1. Have the agent draft a starting `AGENTS.md` from what it finds in the repo.
2. Cut it down to what a new joiner needs on day one: build/test/lint commands, the conventions that matter, the things the agent keeps getting wrong.
3. Commit it at the repo root so the whole team shares one version.
4. Working rule: **when the agent makes a mistake twice, the correction goes into `AGENTS.md`.**
5. Keep it under about a page — it is read at the start of every session, and anything stale is pure cost.

**Skills** — for knowledge that must be applied *consistently*, not just known. The rule of thumb:

| Put it in | When |
|---|---|
| A skill | Institutional knowledge that must be applied consistently, with a named policy owner |
| `AGENTS.md` | Repo context every session needs: conventions, commands, architecture, recurring mistakes |
| A prompt | One-off instructions for this task |

1. Pick one thing enforced inconsistently today: a security standard, an API convention, a brand rule.
2. Write it as a folder with a `SKILL.md`: frontmatter says *when it triggers*, the body says *what to do*. Write it from the policy owner's source of truth.
3. Put it in the repo so it ships with the code, or user-global to distribute. (See `ai-sdlc-design/references/harness-map.md` for placements.)
4. **Test that it triggers.** Ask for the relevant task several different ways and confirm it loads each time.
5. When policy changes, change the skill and have the policy owner sign off.

## Play: guardrails behind advisory skills

A skill is **advisory**: it makes the agent likely to comply, and nothing forces a session to. A policy that must always hold needs something deterministic behind it.

- **Deterministic local gates** — in DSH, the sandbox and approval policy. Choosing `read-only` for a review session, or `workspace-write` instead of `danger-full-access` for unsupervised work, is the enforceable layer.
- **Claude Code-style hooks** — DSH ships a bridge (`dsh-hooks-claude-code`) that runs an existing `hooks.json` during agent runs, supporting `PreToolUse` (block / ask a human), `PostToolUse`, `SessionStart`, `UserPromptSubmit`, `Stop`, and subagent events. It is **installed but not mounted** in the `web` profile; mounting instructions and the honest limits are in `references/harness-map.md`.

Useful build-phase hooks: block edits to protected paths (generated code, a frozen package), run the formatter and linter after edits, keep credentials out of the diff. Keep build-phase hooks fast and scoped to the changed file; heavy checks belong at the commit or the PR.

A hook that asks a **human** for approval belongs to release gating (`ai-sdlc-deploy`), not here — an approval prompt mid-build puts a person back on the critical path of every parallel session.

## Play: parallel work and subagents

Two distinct mechanisms, often confused:

| | What it is | DSH mechanism |
|---|---|---|
| **Parallel workstreams** | Independent tasks that must not collide | Separate sessions/workspaces. Split by files, using `plan.md` to see where the work is independent. Tasks that share files go in one session, sequentially. |
| **Subagent** | A scoped helper *inside* one session, with its own context and tool limits, for jobs that recur across tasks | `subagent` (fresh context) and `subagent_fork` (inherits this conversation). Background by default; `send_message` steers one; `list_agents` recalls them. |

Rules that matter:
- Two or three concurrent streams is a sensible start. The ceiling is **how many streams one person can review properly.**
- Turn repeated jobs into reusable subagent prompts: a verifier that runs the app and reports, a code simplifier that strips needless complexity, a researcher that explores and reports without flooding the main context.
- A subagent definition is a file in the repo (name, when to use it, what it may touch) so the whole team shares it. In DSH that file is a skill or a documented prompt template — see `references/harness-map.md`.

For work that fans out across many independent pieces, DSH's `workflow` tool runs a script that orchestrates many subagents at once.

## Do not

- Do not implement without an accepted `plan.md`. The gate is the stage.
- Do not let the diff drift from the plan without updating the plan.
- Do not treat a skill as an enforced control. Say which layer actually blocks.
- Do not run more parallel streams than review can absorb. Unreviewed throughput is not throughput.

## Measure it

**Leading** — share of changes that merge from the first implementation pass, and time from plan approval to merged PR (both from PR metadata).

**Lagging** — rework cycles per change, and how often the merged diff still matches the committed `plan.md`.

## References

- `references/plan-template.md` — the `plan.md` shape, with a filled example and the interrogation questions.
- `references/harness-map.md` — plan mode, permission presets, hooks bridge, subagents: what is native, what needs mounting.

Chinese version at `SKILL.zh-CN.md`.
