---
name: ai-sdlc-deploy
description: "AI-native SDLC Stage 5 (Deploy) — AI runs both directions of PR review, human approval gates are enforced as deterministic policy rather than convention, the agent acts up to the production gate and cannot pass it, and CI/CD hands the agent judgment steps inside a sandbox with scoped credentials. Use when setting up review, wiring approval gates before automation, or deciding how much autonomy an environment gets. Triggers: 'set up AI code review', 'REVIEW.md', 'review policy', 'approval gate', 'release authorization', 'can the agent deploy', 'tier autonomy by environment', 'sandbox and permissions for agents'. Requires a review gate before automating anything through it."
---

# AI-Native SDLC · Stage 5: Deploy

## Boundary

One job: **review runs in both directions, governance is enforced as the agent acts, and the agent does everything up to the production gate and nothing past it.**

Deploy does not write code (`ai-sdlc-build`) or produce the verification evidence (`ai-sdlc-test`). It decides what is allowed to reach production, and proves it was allowed.

## The shift this skill encodes

| | Traditional | AI-native |
|---|---|---|
| Review | Capacity planned around human output; quality varies with reviewer load | Every PR gets an identical set of passes, findings ranked by severity |
| Human attention | Reading the whole diff | Judging intent and risk: does it do what the plan intended, is the risk acceptable |
| Governance | Review cycles, enforced inconsistently | Enforced as the agent acts; approval gates are deterministic |
| Agent reach | Varies by what the agent was told | Everything up to the production gate, and structurally nothing past it |

## Play: AI in the PR review loop

AI gives and receives reviews: it reviews incoming PRs against organization policy, and it addresses review comments on its own PRs.

1. **Pick the implementation.** A managed code-review service, or a CI action that runs the review. In DSH there is no managed review service — use the `review` and `security-review` skills in a session, or a CI action on a repo.
2. **Write the review policy as `REVIEW.md` at the repo root**, divided into the passes the organization cares about: bugs and logical errors; security and vulnerabilities; compliance against `spec.md`, `plan.md`, and design principles. It also defines what counts as `Important` versus a nit, and what to skip entirely. Template in `references/review-md.md`.
3. **Set the human threshold.** Findings do not approve or block a PR on their own. Branch protection still requires a code owner's approval. If you want to gate merges on findings, read the severity counts the review publishes as a machine-readable tally.
4. **Close the fix loop.** When a reviewer or author tags the agent on a comment, it addresses the comment and pushes the fix; the PR thread records both the request and the change. Better still: sweep the unresolved comments and failing checks until the PR is green and waiting only on code-owner approval.
5. **Feed findings back into `AGENTS.md`.** **When a review flags the same mistake twice, the correction goes into `AGENTS.md` as part of that review** — and because review reads `AGENTS.md`, the mistake is caught from the next PR onwards. Review should also flag when a change has made `AGENTS.md` outdated.
6. **Tune monthly.** Rate findings so the reviewer improves, and cap nit volume in `REVIEW.md`. Exclude generated paths and anything CI already enforces.

## Play: approval gates that are actually enforced

This is the play most often done as a convention and claimed as a control. Do not do that.

1. **List the human approval gates that must survive** — change-management sign-off, release authorization, edits to protected paths — with engineering leadership, change management, and compliance in the room.
2. **Express each gate as something deterministic.** A gate that exists only as a policy document is not a gate. The enforcement layers available, in order of strength:
   - **Sandbox / permission preset** (strongest, DSH-native): `read-only` for sessions that must not write at all; `workspace-write` for ordinary work; `danger-full-access` only for disposable workspaces.
   - **Hooks** (Claude Code-style `PreToolUse`): can block or ask a human before a tool runs. The bridge exists in DSH but is **not mounted** — see `references/harness-map.md`.
   - **Branch protection** (repo-side): turns anything the agent writes into a PR, with no direct path to main. Platform-independent; do this first.
3. **A block must explain itself.** When a gate stops an action, the reason and the route to approval must appear in the agent's output. A silent denial teaches nobody and gets worked around.
4. **Record what "approval" means** — an approved change ticket, or the release manager's sign-off, named.

## Play: tiering autonomy by environment

| Environment | Agent may |
|---|---|
| Development | Deploy freely |
| Staging | Somewhere in the middle — prepare and deploy, with gates on destructive operations |
| Production | **Prepare the release only.** The release manager authorizes it; a gate enforces this |

The governing principle, stated once and never violated: **the agent may act up to the production gate and cannot pass it.**

Corollaries:
- Everything the agent writes arrives as a PR through branch protection. No route to push to main.
- Each non-interactive run acts under the agent's own identity, so the log separates what the agent did from what the engineer who triggered it did.
- Per-environment permission tiers set how much the agent may do on the way to the gate.

## Play: CI/CD and rollback

1. **Start with read-only judgment steps** — triage a failed build, summarize a flaky test, draft the changelog. These need no write access and pay off immediately.
2. **Add write steps behind the existing gates** — fixing lint, updating generated docs, addressing review comments. Arrives as a PR.
3. **Sandbox the execution.** Agent jobs run with no standing production credentials.
4. **Expose deployment as scoped tools**, not as a shell script with credentials, so the agent's deployment powers are an allowlist.
5. **Rehearse rollback before it is needed.** Rollback should be the most rehearsed path in the pipeline: a single command the agent can run, exercised regularly in staging. `ai-sdlc-maintain` calls this rollback when a control band is breached, so it must be proven in advance.

## Security posture: what is enforced where

Do not present a soft layer as a hard control. In DSH the enforcement surface is **coarser than the source playbook assumes**:

| Concern | DSH enforcement |
|---|---|
| File effects | Real. Three modes: `read-only` / `workspace-write` / `danger-full-access`, per session, recorded in the session log, surviving restart. |
| Network egress | **Not covered by the sandbox.** DSH's own docs: the file-effect mode "governs file effects; network and process policy are outside its vocabulary." A domain allowlist like the playbook's is not available at this layer. |
| Secret files (`~/.ssh`, `.env`, credentials) | **No per-path deny list** is exposed in this profile. Do not claim one. Keep secrets out of the workspace, or use a session whose workspace excludes them. |
| Tool allow/deny lists | Not exposed as a managed policy list. The permission preset is the knob. |
| Splitting what the agent did from what the engineer did | Achieved by identity and PR route (branch protection), not by a managed-settings feature. |

The playbook's managed-settings block (per-path denies, network domain allowlists, credential stripping, `allowManagedHooksOnly`, MCP allowlists) has **no DSH equivalent**. If an auditor asks, say that plainly and point at the layers that do exist: branch protection, PR-only route to main, per-environment permission tiers, agent identity in the log.

## Do not

- Do not call a policy document an enforced gate. Name the layer that blocks.
- Do not let the agent that wrote the code approve it. Separation of duties is the point.
- Do not give an agent standing production credentials.
- Do not automate past a gate that does not exist yet. The gates come first; automation accelerates whatever is there.

## Measure it

**Leading** — time to first review (should fall to minutes); share of review comments resolved without a human touching the branch; share of pipeline failures triaged without paging a human; time spent waiting on each approval gate.

**Lagging** — defects and vulnerabilities caught before merge versus those escaping to production; DORA measures (deployment frequency, lead time, change failure rate, time to restore).

## References

- `references/review-md.md` — the `REVIEW.md` review policy, with a filled example.
- `references/harness-map.md` — approval gates, sandbox modes, and the hooks bridge in DSH: what is native, what needs mounting, what has no equivalent.

Chinese version at `SKILL.zh-CN.md`.
