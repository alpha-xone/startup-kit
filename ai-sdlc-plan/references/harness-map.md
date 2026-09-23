# Harness map — Stage 1: Plan

How each Claude Code mechanism named in the source playbook lands in DSH. Verified against the installed harness, not assumed.

## What DSH does natively

| Playbook mechanism | DSH equivalent | Notes |
|---|---|---|
| Commit the markdown on the originator's behalf via a GitHub connector | `gh` CLI (authenticated) or filesystem tools | The agent commits directly. `gh` is already logged in on this machine. |
| `intent/` folder in the product repo | Same | Plain directory; no harness support needed. |
| Template "encoded as a skill set up by a technical team member" | A skill under `~/.dsh/skills/<name>/` or `<repo>/<skill>/` | This skill is that mechanism. |
| Version control as the audit trail | Same | Author and timestamp come from the commit. |

## What needs setup

| Playbook mechanism | Status in DSH | What to do instead |
|---|---|---|
| Claude.ai / Cowork access for non-engineers | No equivalent product | A non-engineer works in a DSH session with this skill loaded. Requires the harness running and a session open for them. |
| GitHub connector letting claude.ai commit for a non-git user | Not the same surface | The agent runs `git`/`gh` itself. Give the non-engineer a session, not a git client. |
| GitHub Actions trigger firing the Design pass on merge | `dsh-webhook-github` exists but is **not mounted** in the `web` profile | Mount it via `~/.dsh/cordis.patch.yml` (see below), or make the trigger a human prompt — "the intent was accepted, run the design pass". |

## Mounting a non-default DSH package

DSH composes from a profile. The active profile is `web` (`~/.dsh/profiles/web/`), and its user patch layer is `~/.dsh/profiles/web/cordis.patch.yml`, which the harness hot-reloads (`patchReload: live`). A package that is installed but not mounted appears as a row you add:

```yaml
- id: webhook-github
  name: '@deepseek-ai/dsh-webhook-github'
  config: {}
```

The package is already present under `~/.dsh/profiles/node_modules/@deepseek-ai/`, so no install step is needed. Do not edit `cordis.yml` — it is intentionally an empty root and is recomposed from bundles plus `cordis.patch.yml` on every boot.

## Honest limitation

Stage 1 is the stage where DSH is closest to parity, because the whole play is "write a markdown file and commit it". The parts that do **not** transfer are the cross-organization surfaces: a non-engineer getting their own Claude access without an engineer, and a merge automatically firing the next stage. In DSH those are a session and a prompt.
