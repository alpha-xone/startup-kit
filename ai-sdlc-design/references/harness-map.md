# Harness map — Stage 2: Design

How each Claude Code mechanism named in the source playbook lands in DSH. Verified against the installed harness.

## What DSH does natively

| Playbook mechanism | DSH equivalent | Notes |
|---|---|---|
| "Run it by hand at first" | An ordinary session prompt | No setup. This is the right way to start. |
| Policies "guided by the organization's skills" | Skills in `~/.dsh/skills/<name>/` or `<repo>/<skill>/` | Same mechanism as Claude Code: a folder with `SKILL.md`, discovered and loaded on match. |
| `CLAUDE.md` supplying repo conventions | `AGENTS.md` **or** `CLAUDE.md` | DSH's instruction loader treats both as base candidates by default, so an existing `CLAUDE.md` needs no change. |
| Codify the pass "as an organization-level slash command" | A skill, or a project skill directory | A skill is the DSH-native equivalent of a slash command that travels with the repo. |
| Claude Design for front-end mockups | Not available | Use the DSH design skills: `frontend-design`, `impeccable`, `design-taste-frontend`, or `stitch-design-taste`. |

## What needs setup

| Playbook mechanism | Status in DSH | What to do instead |
|---|---|---|
| Merge of `intent.md` triggers a non-interactive job that commits `spec.md` | `dsh-webhook-github` is installed but **not mounted** in the `web` profile | Mount it, or make the trigger an explicit prompt: "the intent was accepted — run the design pass". |
| `claude -p` non-interactive run committing a PR | No `-p` equivalent for a repo-side job | Run the pass in a DSH session, or drive it from CI with your own script calling the model API. |

## Mounting the webhook trigger

Add a row to `~/.dsh/profiles/web/cordis.patch.yml` (hot-reloaded; do not edit `cordis.yml`):

```yaml
- id: webhook-github
  name: '@deepseek-ai/dsh-webhook-github'
  config: {}
```

## Loading the policy skills

Three workable placements, in order of how much they travel with the team:

1. **Repo, committed** — `<repo>/<skill-name>/SKILL.md`, e.g. `<repo>/secure-api-review/SKILL.md`. Ships with the code, so the policy versions are in the same history as the specs they constrained. Recommended for engineering-led teams.
2. **Workspace-level** — the skill folder in the repo root of the workspace. Same discovery, no per-repo duplication.
3. **User-global** — `~/.dsh/skills/<name>/`. Convenient, but a policy that lives only on one machine is not a control.

For a policy that must hold without exception, a skill alone is advisory in DSH exactly as it is in Claude Code. The deterministic layer is the harness sandbox and approval policy (`danger-full-access` / `workspace-write` / `read-only` presets), which can block whole classes of action. See `ai-sdlc-deploy` for the full treatment.

## Skill triggering

A skill loads on match against its `description`. Write the description as *when to use it*, and then test that it triggers: ask for the task several different ways and confirm the skill loads each time.
