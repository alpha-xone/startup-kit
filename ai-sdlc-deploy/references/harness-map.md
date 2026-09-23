# Harness map — Stage 5: Deploy

How each Claude Code mechanism named in the source playbook lands in DSH. Verified against the installed harness. This stage has the most "no equivalent" rows — read them before promising a control to anyone.

## What DSH does natively

| Playbook mechanism | DSH equivalent | Notes |
|---|---|---|
| AI reviewing PRs against policy | `review` and `security-review` skills, or a CI action on the repo | No managed review service. The *review policy* (`REVIEW.md`) is portable; the service is not. |
| Agent addressing review comments on its own PR | `gh` CLI (authenticated) | Comment → fix → push is a normal session task. |
| Agent babysitting a PR to green | Same, driven by a prompt or a skill | "Sweep unresolved review comments and failing checks, fix them, push, repeat until only code-owner approval is missing." |
| Per-session permission tiers | **Native.** `read-only` / `workspace-write` / `danger-full-access` | Bind sandbox mode and approval policy together. Chosen per session; recorded in the session log; survives restart. |
| Branch protection as the only route to main | Repo setting, platform-independent | Do this first. It is the strongest available control and needs nothing from DSH. |
| Rollback path | Repo concern | Unchanged. Rehearse in staging. |

## The permission presets, precisely

| Preset | Sandbox mode | Approval policy |
|---|---|---|
| `read-only` | read-only | ask |
| `workspace-write` | workspace-write | ask |
| `danger-full-access` | danger-full-access | never |

Sandbox semantics, from the harness's own documentation:

- **`read-only`** — "Any available operation enforced by the DSH file sandbox cannot modify files in the standing mode."
- **`workspace-write`** — "may modify files under the session workspace: `<workspace root>`. Some platform temporary areas may also be writable."
- **`danger-full-access`** — "The DSH file sandbox does not restrict file modifications by available operations."

Environment override: `DSH_PERMISSION_MODE` sets the deployment default (`workspace-write` is the mounted default; `danger-full-access` also flips the approval policy to `never`).

## Approval gates

A hook that **asks a human** is the release-gate mechanism in the source playbook. In DSH:

1. **Hooks bridge** — `@deepseek-ai/dsh-hooks-claude-code` runs Claude Code command hooks. `PreToolUse` supports `deny` (block) and `ask` (request approval). It is installed under `~/.dsh/profiles/node_modules/@deepseek-ai/` but **not mounted** in the `web` profile.

   Mount it in `~/.dsh/profiles/web/cordis.patch.yml` (hot-reloaded):

   ```yaml
   - id: hooks-claude-code
     name: '@deepseek-ai/dsh-hooks-claude-code'
     config:
       configPath: ./.claude/hooks.json
       projectDir: .
   ```

   A `PreToolUse` hook that exits `2` blocks the action and its stderr reaches the agent — the playbook's `production-gate.sh` pattern works as written, provided it lives in a Claude Code `hooks.json` shape.

2. **Branch protection** — platform-independent, no mount needed, and the one that actually guarantees no direct route to main.

3. **Permission presets** — the coarsest but most reliable layer. If a session must not deploy, `read-only` is a fact rather than an instruction.

Honest limits of the bridge: 23 of Claude Code's hook events are unsupported; `allow` does not pre-approve, only `deny` and `ask` work; only shell-form command handlers run (`http`, `mcp_tool`, `prompt`, `agent` are skipped); the config is parsed once at load with no live reload; `transcript_path` is always empty; `systemMessage` is not model-visible.

## What has NO DSH equivalent

Do not configure these or promise them. Each row is a real control the source playbook relies on.

| Playbook control | Status |
|---|---|
| `permissions.deny` per-path rules (`Read(.env*)`, `Read(./secrets/**)`) | **Not exposed.** The filesystem sandbox enforces the session mode, not a per-path deny list. |
| `permissions.allow` pre-approvals | **Not exposed** as a managed list. |
| `disableBypassPermissionsMode`, `allowManagedPermissionRulesOnly` | **No managed-policy layer.** A session's preset can be changed; there is no admin-pinned floor. |
| `sandbox.network.allowedDomains` (egress allowlist) | **Not available.** The harness states plainly that network and process policy are outside the sandbox mode vocabulary. |
| `sandbox.credentials` (deny reads of `~/.ssh`, `~/.aws/credentials`, strip env vars) | **Not available** at this layer. Keep secrets outside the workspace. |
| `allowManagedHooksOnly`, `disableSideloadFlags`, `strictKnownMarketplaces` | **Not available.** There is no managed-settings tier above the user. |
| `allowManagedMcpServersOnly` | **Not available.** MCP servers are not composed in this profile by default; adding one is a profile edit. |
| `requiredMinimumVersion` | **Not available.** |
| `claude -p` non-interactive runs inside CI | **No equivalent.** Use your own script against the model API. |

## What to tell an auditor

Say what is enforced and by which layer:

- **Enforced:** the file-effect boundary per session (`read-only` / `workspace-write` / `danger-full-access`); the PR-only route to main (branch protection); agent identity separated from triggering-engineer identity in the pipeline log; each gate's allow/block verdict logged with a timestamp when hooks are mounted.
- **Advisory:** skills and `AGENTS.md`. They make a violation rare, not impossible.
- **Absent:** per-path secret denies, network egress allowlisting, credential stripping, and any admin-pinned policy floor above the user.

Promising an absent control is worse than acknowledging the gap, because the gap is what an audit is designed to find.
