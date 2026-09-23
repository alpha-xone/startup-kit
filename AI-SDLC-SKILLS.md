# AI-Native SDLC Skills — 使用说明

如何正确使用这 6 个 skill。读完这一份，你就能判断该在什么时候调哪个、按什么顺序引入、以及哪些能力在 DSH 里其实并不存在。

**信源**：[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)（Anthropic，2026-08-21）。

---

## 1. 先回答一个问题：角色能做成 skill 吗？

**角色本身不能，阶段可以。**

文章里的角色——产品负责人、分析师、设计师、工程师、QA、发布负责人、值班工程师——只是各阶段里的**职责标签**，不是可以独立执行的工作流。一个"产品负责人 skill"没有可执行的步骤，它的内容无非是"审阅并在关卡上做决定"，那是某个阶段里的一步。

可以做成 skill 的是文章真正的骨架：**6 个阶段，每个阶段里有明确的玩法、上下游依赖、和一个"人在哪里介入"的关卡。** 角色被编码在这些阶段内部：

- 每个 skill 的**关卡**一节点名谁在这一点上做决定、决定记录在哪。
- 阶段之间的交接是**制品**（`intent.md` → `spec.md` → `plan.md` → diff+测试 → PR+评审发现 → 事故记录 → 新的 `intent.md`），不是人员交接。这正是文章说"人保持问责、注意力随制品移动"的意思。

所以：**6 个阶段 skill，角色作为关卡的所有者嵌在里面。** 下面的角色对照表让你按组织里的岗位找到该看的 skill。

---

## 2. 角色 → skill 对照表

按你实际的身份查。

| 文章里的角色 | 在哪个阶段 | 这个阶段里它的工作 | 该加载的 skill |
|---|---|---|---|
| 产品负责人 | Plan | 审阅并修正 agent 写的 `intent.md`，做出接受或关闭的决定 | `ai-sdlc-plan` |
| 提出者 / 业务方（非工程） | Plan | 用自己的话说清问题，纠正 agent 的误解 | `ai-sdlc-plan` |
| 分析师（被替代的一方） | Design | 原本负责把想法形式化成需求——现在由 agent 完成，产品负责人审阅 | `ai-sdlc-design` |
| 产品负责人 | Design | 审阅 spec，把标记出的关注点逐个找政策负责人解决 | `ai-sdlc-design` |
| 品牌 / 安全 / 合规 / UX 政策负责人 | Design | 提供权威来源，签核编码该政策的 skill，收关注点 | `ai-sdlc-design`（政策写成 skill 的部分）+ `ai-sdlc-build`（skill 的写法） |
| 设计师 | Design | 前端工作在会话里做原型并迭代 | `ai-sdlc-design` + `frontend-design` / `impeccable` |
| 工程师 | Build | 计划模式里盘问方案、提交 `plan.md`、接受后实现 | `ai-sdlc-build` |
| 技术负责人 / 架构师 | Build | 高风险改动的方案批准 | `ai-sdlc-build` |
| 平台 / 工程团队 | Build | 一次性搭好意图存放处、`AGENTS.md`、skill、护栏 | `ai-sdlc-build` |
| 安全 / 政策负责人 | Build | 把必须一致应用的知识写成 skill，并在 PR 上审阅它的变更 | `ai-sdlc-build` |
| 工程师 | Test | 给会话搭好反馈回路 | `ai-sdlc-test` |
| 平台工程师 | Test | 建 eval 套件并接进 CI | `ai-sdlc-test` |
| QA | Test | 从阶段闸门 QA 转为维护一套活的 eval 套件 | `ai-sdlc-test` |
| 技术负责人 | Deploy | 写 `REVIEW.md`，设人工阈值，每月调优 | `ai-sdlc-deploy` |
| 代码所有者（评审者） | Deploy | 只看意图与风险，机械性证据已随 PR 附上 | `ai-sdlc-deploy` |
| 工程负责人 + 变更管理 + 合规 | Deploy | 列出必须存活的人工审批闸门 | `ai-sdlc-deploy` |
| 平台工程师 | Deploy | 把闸门实现为确定性策略，接 CI/CD | `ai-sdlc-deploy` |
| 发布负责人 | Deploy | 生产发布授权——这是 agent 过不去的那道闸门 | `ai-sdlc-deploy` |
| 服务负责人 | Maintain | 选指标、写检测脚本、定义响应层级、研判队列 | `ai-sdlc-maintain` |
| 值班工程师 / on-call | Maintain | 研判队列，驳回时反馈给阈值 | `ai-sdlc-maintain` |
| 安全负责人 | Maintain | 接入仓库、安排扫描、带置信度评级研判 | `ai-sdlc-maintain` |
| 拥有事故的团队 | Maintain | 把事故写成 eval 并永久留在套件里 | `ai-sdlc-maintain` + `ai-sdlc-test` |

**同一个角色会出现在多个阶段**——这是有意的，也是文章的观点：人的注意力沿制品链移动，而不是被固定在一个部门里。

---

## 3. 引入顺序（和文章的阶段顺序不是一回事）

文章明确说了：play 的**阶段编号**和**引入顺序**是两件事。箭头指向谁，谁就得先做。

以 Plan 为起点是安全的：它没有上游依赖。但如果你已经有一个能跑的流水线，从成本最低、收益最快的地方切入更实际。

**推荐的第一个落点（按你的处境选一个）：**

| 你的处境 | 从哪开始 | 为什么 |
|---|---|---|
| 有一个真实的仓库，agent 已经在写代码 | `ai-sdlc-test`（反馈回路）+ `ai-sdlc-build`（`AGENTS.md` + `plan.md`） | 这两个直接决定 agent 产出能不能被人快速审。不需要组织层面的推动。 |
| 已有 CI 和 PR 流程，评审是瓶颈 | `ai-sdlc-deploy`（`REVIEW.md` + 分支保护） | 评审策略是纯文本，当天就能落地，且立刻降低人工评审负担。 |
| 想法很多但落不下来，工程排队 | `ai-sdlc-plan`（`intent.md` + 意图存放处） | 解决上游排队。需要产品负责人参与，属于组织动作。 |
| 事故反复发生、告警没人跟 | `ai-sdlc-maintain`（检测器 + `bands.yaml`） | 见效最明显，但前置依赖最多（评审闸门 + 排练过的回滚）。 |

**依赖关系（必须在前面的）：**

```
ai-sdlc-plan ──> ai-sdlc-design ──> ai-sdlc-build ──> ai-sdlc-test
                                          │                 │
                                          └──> ai-sdlc-deploy <──┘
                                                    │
                                                    ▼
                                            ai-sdlc-maintain
```

硬性前置，不要跳过：

- `ai-sdlc-design` 需要一份**已接受**的 `intent.md`。从口头需求开始会让这个阶段失去全部价值。
- `ai-sdlc-build` 需要一份**已批准**的方案。没有 `plan.md` 就实现，等于放弃了这道关卡。
- `ai-sdlc-deploy` 的自动化需要**闸门先存在**。自动化只会加速已经在那儿的东西——包括坏东西。
- `ai-sdlc-maintain` 需要 `intent.md` 格式、评审闸门、和排练过的回滚。三者缺一，"闭环"就变成"自动开一堆没人处理的事故"。

---

## 4. 怎么调用这些 skill

### 自动触发

skill 靠 `description` 匹配触发。用自然语言描述你在做的事就行，不需要记名字：

```
我们要给理赔状态做一个自助查询，先把它写成 intent.md
```

```
实现这个 spec 之前，先给我一份实现方案让我审
```

```
让 agent 自己验证改动能不能跑起来，别等 CI
```

### 显式调用

想直接点名时，用 skill 名字。在 DSH 里技能可被 `skill` 工具加载，也可以直接说：

```
用 ai-sdlc-deploy 的评审策略部分，帮我把 REVIEW.md 写出来
```

### 跨 skill 的转场

阶段 skill 之间靠**制品**交接。实际用法是：完成一个阶段的制品，然后明确说进入下一个阶段。

| 完成 | 制品 | 下一句该说什么 |
|---|---|---|
| Plan | `intent.md`（已接受） | "intent 已接受，跑设计那一遍" |
| Design | `spec.md`（已批准） | "spec 批准了，先进计划模式出 `plan.md`" |
| Build | `plan.md` + 实现 | "实现完了，让 agent 自测并贴输出" |
| Test | 测试与构建输出 | "证据齐了，进评审闸门" |
| Deploy | 已合并的 PR | "上线后盯这几个控制带" |
| Maintain | 新的 `intent.md` | 回到第一行 |

---

## 5. 一次完整的走查

以一个真实形状的需求为例，展示每一步说什么、产出什么、谁做决定。

**Step 1 — Plan（`ai-sdlc-plan`）**

> "客服三分之一的时间在回答'我的理赔到哪一步了'。我想让客户在门户里自己看到状态、下一步和预计时间。把它写成 `intent.md`。"

Agent 产出 `intent.md`，含问题、期望结果、受影响的系统、约束（门户会话不得出现新的 PII、沿用现有认证）、待决问题（第三方理算师要不要也能访问）。

**关卡**：产品负责人逐条修正 → 提交 → 接受。

**Step 2 — Design（`ai-sdlc-design`）**

> "intent 已接受。跑设计那一遍，用上我们品牌、安全、合规、体验的 skill。有和政策冲突的地方明确标出来。"

Agent 产出 `spec.md`：要建什么、怎么接进现有系统、应用了哪些政策约束（各自点名来源 skill）、**关注点列表**、待决问题的处理、明确的非目标。

**关卡**：产品负责人对照想法审阅 → 关注点逐个找政策负责人解决 → 连同提示词与 skill 版本一起提交 → 批准。

**Step 3 — Build（`ai-sdlc-build`）**

> "/plan 打开计划模式。这是 `intent.md` 和 `spec.md`，出一份实现方案，点明改哪些文件、工作顺序、以及证明它成立的测试。"

盘问：可能弄坏什么？哪一步风险最高？放弃了哪些选项？——迭代到方案能独立成立，提交为 `plan.md`，接受，实现。

**关卡**：常规改动由工程师批准；高风险找技术负责人。

**Step 4 — Test（`ai-sdlc-test`）**

先在 `AGENTS.md` 里写好验证区块（命令 + 健康输出样例 + "修代码不是修测试"）。会话自查并在报告完成前贴出输出。然后用 `subagent_fork` 起一个全新上下文的验证者，对照 `plan.md` 检查行为，只报告不修复。

**Step 5 — Deploy（`ai-sdlc-deploy`）**

`REVIEW.md` 定义三个 pass（bug / 安全 / 合规）。合规 pass 对照 `spec.md` 和 `plan.md`。代码所有者只看意图与风险——机械性证据已随 PR 附上。生产发布由发布负责人授权，闸门拦住 agent。

**关卡**：代码所有者批准 + 分支保护。

**Step 6 — Maintain（`ai-sdlc-maintain`）**

部署后 5xx 率突破 3σ 且窗口内有部署 → 确定性检测器触发 → agent 触发既有的回滚流水线（事先批准的路由）→ 诊断写成 `intent.md` 进研判队列 → 值班工程师研判 → 修复发布后补一个 eval。

**环闭上**：一次突破变成了一份新的 `intent.md`，走回 Step 2。

---

## 6. DSH 能力边界：哪些能做，哪些不能

这一节决定你能不能把上面那套真正跑起来。**不要向任何人（包括你自己）承诺不存在的管控。**

### 原生支持，直接用

| 能力 | DSH 里的东西 |
|---|---|
| 计划模式 | `/plan` 进入，`exit_plan_mode` 提交方案供批准。**注意：这是文本引导，不是能力锁。** 要只读这个性质真被强制，把权限预设同时设为 `read-only`。 |
| 仓库知识文件 | `AGENTS.md` **或** `CLAUDE.md`，两者都是默认候选，从项目根到工作目录逐层加载。现成的 `CLAUDE.md` 不用改。 |
| 权限分级 | `read-only` / `workspace-write` / `danger-full-access` 三个预设，按会话选，记录在会话日志、重启后保持。 |
| 子 agent | `subagent`（全新上下文）、`subagent_fork`（继承本对话，适合验证者）、`send_message` 转向、`list_agents` 召回。 |
| 大量扇出 | `workflow` 工具：一段脚本编排大量子 agent，前台阻塞、返回单一结果。 |
| 会话内的定时提醒 | `schedule_create` —— 但它是**会话内**的，会话不活着就不投递。别当生产调度器。 |
| 遥测 | `dsh-session-telemetry-otel` 已挂载，但默认 `FEEDBACK_ONLY`：普通活动**不导出**。别声称有完整的调用审计流。 |

### 已安装但要挂载

DSH 的 profile 是组合出来的。以下包已在 `~/.dsh/profiles/node_modules/@deepseek-ai/` 里，但 `web` profile 默认不加载。

挂载方式：往 `~/.dsh/profiles/web/cordis.patch.yml` 加一行（该文件热重载，改完即生效）。**不要编辑 `cordis.yml`**——它是刻意留空的根，每次启动由 bundle 加 patch 重新组合。

```yaml
# Claude Code 钩子桥：在 agent 运行期间执行现有 hooks.json
- id: hooks-claude-code
  name: '@deepseek-ai/dsh-hooks-claude-code'
  config:
    configPath: ./.claude/hooks.json
    projectDir: .

# GitHub webhook 触发（把"合并 intent 自动跑设计"这类接起来）
- id: webhook-github
  name: '@deepseek-ai/dsh-webhook-github'
  config: {}
```

钩子桥的**诚实限制**（别过度承诺）：

- Claude Code 现有 30 个钩子事件里，**23 个不支持**（`PermissionRequest`、`FileChanged`、`WorktreeCreate`、`SessionEnd` 等）。
- `PreToolUse` 支持 `deny`（拦截）和 `ask`（转人工审批）；**`allow` 不能预先批准**，`updatedInput` 不生效。
- 只运行 shell 形式的命令处理器；`http`、`mcp_tool`、`prompt`、`agent` 处理器会被跳过。
- 一个进程级 `configPath`，加载时解析一次，**钩子配置不热重载**。
- `transcript_path` 永远是空字符串；`systemMessage` 对模型不可见。

因此：**必须无条件成立的政策，优先用沙箱/权限层**（DSH 自己强制），而不是钩子桥。

### 没有对应物——不要配，也不要承诺

| playbook 里的管控 | DSH 状况 |
|---|---|
| `permissions.deny` 按路径拒绝（`Read(.env*)`、`Read(./secrets/**)`） | **没有暴露。** 文件沙箱强制的是会话模式，不是按路径的拒绝列表。 |
| `permissions.allow` 预先批准 | 没有作为受管列表暴露。 |
| `disableBypassPermissionsMode`、`allowManagedPermissionRulesOnly` | **没有受管策略层。** 会话预设可以被改，没有管理员钉住的地板。 |
| `sandbox.network.allowedDomains`（网络出口白名单） | **不可用。** 官方文档明说网络与进程策略不在沙箱模式词汇表内。 |
| `sandbox.credentials`（拒绝读 `~/.ssh`、剥离环境变量） | **这一层不可用。** 把密钥挡在工作区之外。 |
| `allowManagedHooksOnly`、`disableSideloadFlags`、`strictKnownMarketplaces` | 没有用户之上的受管设置层。 |
| `allowManagedMcpServersOnly` | 不可用。本 profile 默认不组合 MCP server。 |
| `requiredMinimumVersion` | 不可用。 |
| `claude -p` 非交互 CI 调用 | **没有对应物。** 自己写脚本调模型 API。 |
| `claude --worktree` 并行工作区隔离 | **没有。** 并行任务要按文件切分，或用独立工作区，或顺序执行。 |
| Claude Security（托管定时扫描） | 没有对应物。用外部扫描器，或定时 agent 运行。 |
| Claude Tag（agent 加入 Slack/Teams 频道） | 没有对应物。人开会话带上下文进来，或挂 webhook。 |
| 托管 Code Review 服务 | 没有。用 `review` / `security-review` skill 或 CI 动作。 |

### 对审计方怎么说

- **被强制的**：按会话的文件写入边界（三档模式）；只能走 PR 到主干（分支保护）；流水线日志里 agent 身份与触发工程师身份分离；挂载钩子后每次闸门判定的允许/拦截与时间戳。
- **建议性的**：skill 和 `AGENTS.md`。它们让违规变罕见，不是不可能。
- **缺失的**：按路径的密钥拒绝、网络出口白名单、凭据剥离，以及任何用户之上的受管策略地板。

**承诺一个不存在的管控，比承认这个缺口更糟——缺口正是审计要发现的东西。**

---

## 7. skill 之间的配合，以及和 DSH 既有 skill 的分工

这 6 个 skill 只负责**流程**（谁在什么时候做什么、制品是什么、关卡在哪）。具体手艺交给 DSH 已有的 skill：

| 需要 | 用 |
|---|---|
| 实际跑测试、诚实报告覆盖缺口 | `test` |
| 真跑应用/CLI/API 并收集可观察证据 | `verify` |
| 起本地应用、读渲染状态与控制台、按观察到的选择器操作 | `webapp-testing` |
| 复现、最小化、定位、找根因 | `debug` |
| 带文件行号证据的正确性评审 | `review` |
| 信任边界、注入、密钥、依赖、可利用性 | `security-review` |
| 前端视觉方向与反模板化 | `frontend-design`、`impeccable`、`design-taste-frontend` |
| 出一份实现方案 | `plan`、`implement` |
| 并行扇出到大量子 agent | `batch`、`workflow` 工具 |
| 把长内容蒸馏成 skill | `cangjie-skill` |
| 写/改 skill | `skill-creator` |

**关系**：这 6 个 skill 说"这一步该做什么、产物是什么、谁批准"；上表那些 skill 说"这件事怎么做得好"。两者互补，不要用这 6 个替代手艺 skill。

---

## 8. 翻译说明：文章原味 vs DSH 落地

每个 skill 目录里都有：

- `SKILL.md` —— 英文，紧贴文章原意，**逐条标注 DSH 等价物或"无等价物"**。
- `SKILL.zh-CN.md` —— 中文版，同样的结构。
- `references/harness-map.md` —— 该阶段的 DSH 能力映射表，区分三种状态：原生支持 / 已安装要挂载 / 没有对应物。
- 其他 `references/*.md` —— 制品模板与具体做法（`intent.md` 模板、`plan.md` 模板、`REVIEW.md` 模板、`bands.yaml` 模板、验证区块等）。

**读法**：先读 `SKILL.md` 的正文，需要落地细节时再打开对应的 `references/` 文件。

---

## 9. 三条最容易被做错的

1. **把政策文档当闸门。** "我们有 `REVIEW.md` 要求代码所有者批准"不等于分支保护真的配了。每一条闸门都要能回答：**哪一层在拦？** 答不出来就不是闸门。
2. **跳过 `plan.md` 直接实现。** 这是投入产出比最高、也最容易被"这次改动很小"说服而跳过的一步。agent 写的 diff 之所以可审，靠的是有一份已批准的方案可以对照。
3. **让 skill 承担它承担不了的确定性。** skill 是建议性的。必须永远成立的东西要垫沙箱、分支保护或钩子。说清哪一层在强制，是这套 skill 反复强调的唯一纪律。
