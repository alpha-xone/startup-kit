# Harness map — Stage 3: Build

How each Claude Code mechanism named in the source playbook lands in DSH. Verified against the installed harness, not assumed.

## What DSH does natively

| Playbook mechanism | DSH equivalent | Notes |
|---|---|---|
| Plan mode | **Native.** `/plan` enters it, `/plan off` leaves, `exit_plan_mode` presents the plan for `Approve` / `Keep planning` | In DSH the agent *calls* `exit_plan_mode` with the plan as markdown; the user reviews and approves. |
| Plan mode cannot edit files until accepted | **Guidance, not enforcement** | DSH's own docs: "plan mode restrains through text only." To enforce read-only, set the permission preset to `read-only` as well. |
| `CLAUDE.md` as the knowledge file | `AGENTS.md` **or** `CLAUDE.md` | Both are default instruction candidates (`instructionFileCandidates: ['AGENTS.md', 'CLAUDE.md']`), loaded broad-to-specific from the project root down to the working directory. An identical duplicate of a sibling is rendered once, not twice. |
| `CLAUDE.local.md` overlay | `AGENTS.local.md` / `CLAUDE.local.md` | Same defaults. |
| `/init` to generate `CLAUDE.md` | No command; just ask | "Read the repo and draft a starting `AGENTS.md` for a new joiner, then cut it to one page." |
| Skills at `.claude/skills/<name>/` | Skills at `~/.dsh/skills/<name>/` or a repo skill directory | Same `SKILL.md` frontmatter contract. |
| Subagents defined in `.claude/agents/*.md` | `subagent` / `subagent_fork` tools, plus a repo file documenting the definition | DSH subagents are chosen per call, not loaded from a definitions folder. Keep the definition as a skill or a prompt template the team shares. |
| Parallel sessions, each in a git worktree | **Not available** | No worktree isolation in DSH. See below. |
| Auto-accept mode | Permission presets | `read-only` / `workspace-write` / `danger-full-access`, each bundling a sandbox mode with an approval policy. |

## Permission presets (the real "auto mode" knob)

The `web` profile exposes three presets. They bind sandbox mode and approval together:

| Preset | Sandbox | Approval | Sensible use |
|---|---|---|---|
| `read-only` | read-only | ask | Review, exploration, planning sessions where you want the read-only property actually enforced |
| `workspace-write` | workspace-write | ask | Ordinary implementation |
| `danger-full-access` | danger-full-access | never | Unsupervised autonomous work in a disposable or backed-up workspace only |

This is the deterministic layer the playbook wants behind an advisory skill. A skill makes the violation rare; the sandbox makes it impossible.

## Hooks: installed but not mounted

DSH ships `@deepseek-ai/dsh-hooks-claude-code`, a bridge that runs an existing Claude Code `hooks.json` (or a settings file with a `hooks` key) during agent runs. **It is not mounted in the `web` profile** — the package exists under `~/.dsh/profiles/node_modules/@deepseek-ai/` but no row loads it.

To mount it, add a row to `~/.dsh/profiles/web/cordis.patch.yml` (hot-reloaded — `patchReload: live`):

```yaml
- id: hooks-claude-code
  name: '@deepseek-ai/dsh-hooks-claude-code'
  config:
    configPath: ./.claude/hooks.json
    projectDir: .
```

Supported events and what they can do:

| Event | When | Can it block? |
|---|---|---|
| `SessionStart` | session starts | attaches context |
| `UserPromptSubmit` | prompt received | blocks the prompt, or adds context |
| `PreToolUse` | before a tool runs | **blocks the tool, or asks for approval** — the guardrail case |
| `PostToolUse` | after a tool runs | blocks the result with feedback, or adds context |
| `Stop` | run about to stop | forces another step |
| `SubagentStart` / `SubagentStop` | child lifecycle | start injects context (in-process only); stop observes only |

Exit code `2` from a `PreToolUse` hook blocks the action and the message reaches the agent.

**Honest limits** — do not overclaim the bridge:
- 23 of Claude Code's hook events are unsupported (`PermissionRequest`, `FileChanged`, `WorktreeCreate`, `SessionEnd`, and others).
- `PreToolUse` supports `deny` and `ask`; **`allow` does not pre-approve**, and `updatedInput` is not honored.
- Only shell-form command handlers run. `http`, `mcp_tool`, `prompt`, and `agent` handlers are skipped.
- One process-level `configPath`, parsed once at load. No layered project/user/policy discovery and no live reload of the hook config.
- `transcript_path` is always empty, and `systemMessage` is not model-visible.

For a policy that must hold without exception, prefer the sandbox/permission layer, which DSH enforces itself, over the bridge.

## Parallelism: what to do instead of worktrees

DSH has no git-worktree isolation for parallel sessions. Choose one:

1. **Sequential sessions** for tasks that share files. Simplest, and correct.
2. **Separate workspaces** for tasks that touch different repos or independent checkouts. The harness supports per-session workspaces.
3. **Subagents** for fan-out *within* one session, when the work is genuinely independent and read-mostly. A subagent inherits the parent's composition (same tools, same prompt sections), so it is not isolation from the parent's sandbox.
4. **The `workflow` tool** when the work fans out across many independent pieces. It runs a script that starts many subagents with `agent()`, `parallel()`, and `pipeline()`, and returns one final result to the parent. Constraints worth knowing: it runs in the foreground and blocks the parent turn, there is no journaling or resume, and it is not a worktree substitute — the children still operate in the same workspace.

Since there is no worktree isolation, **task splitting by file matters more in DSH than it does in the source playbook**, not less. Read `plan.md` to see where the work is independent before starting a second stream.

## Subagent definitions

`.claude/agents/*.md` has no direct loader in DSH. Keep the same information anyway — it is what makes a repeated job reusable:

```markdown
# Subagent: verifier
Use when: a session believes a change is done and needs an independent check.
Tools: read, pwsh (read-only commands)
Prompt: Start the app with `make run`. Exercise the changed behavior and the
two nearest neighbouring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

Store it as a skill (loaded on match) or as a documented prompt template the team copies. `subagent_fork` is the tool that matches this use case: it inherits the conversation and therefore the plan, and it hands back a verdict rather than intermediate steps.

## Deferred by default

`dsh-tool-ralph` (fresh-agent iteration over a build-time-fixed script) is **mounted disabled** in the base bundle. Leave it off unless a human explicitly asks for that mode.
