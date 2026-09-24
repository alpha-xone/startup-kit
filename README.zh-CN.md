# Startup Kit · 诊断 · 对标 · 执行

> **完整的创业评估工具包：preflight 查你的生存几率，blueprint 告诉你赢家怎么赢。**

> 🇬🇧 English version at [`README.md`](README.md)

六个技能帮你从想法到执行，基于 **2,500+ 失败创业尸检报告** 和 **5,000+ 成功创始人故事** 的系统分析。

另有一套 [**AI 原生 SDLC 套件**](https://github.com/alpha-xone/ai-native-sdlc-kit) 覆盖软件研发流程本身——把 Anthropic 的 AI 原生 SDLC playbook 六个阶段做成可调用的 skill，并给出项目骨架：制品放哪、谁签字、哪一层真的在拦。它已独立成仓，见[下文](#-配套ai-原生-sdlc-套件)。

## 📊 有什么不同

**每条结论都来自真实案例和数据。** 这不是泛泛的创业建议——是从数千个真实结果中提取的模式：

| 大多数「建议」做的 | Startup Kit 做的 |
|---|---|
| 「建立护城河」→ 空泛 | 「建立 Helmer 7 种力量之一」→ 每个都有真实公司案例 |
| 「验证你的想法」→ 模糊 | Mom Test 具体清单、15 次对话规则 |
| 「了解你的单位经济」→ 笼统 | LTV > 3×CAC，GM >50%，附带行业基准 |
| 「竞争很激烈」→ 废话 | 竞争杀死 53% — 以下是 ConvertKit 如何打败 Mailchimp 的 |
| 「选个渠道」→ 抽象 | 一个渠道吃干榨净：Carrd 靠纯 SEO 做到 $1.5M ARR |

**本 repo 中每个技能都遵循同一规则**：框架扎根于经过分析的案例数据，而非直觉或博客智慧。

## 🗺️ 工具链

```
                  ┌─────────────────┐
                  │  preflight ·    │
                  │   "怎么死"       │  ← 2,500+ 失败案例
                  │  12 维诊断       │
                  └────────┬────────┘
                           │ "你的最大风险是 X, Y, Z"
                           ▼
                  ┌─────────────────┐
                  │  blueprint ·    │
                  │   "怎么赢"       │  ← 5,000+ 成功案例
                  │  5 大模块        │
                  │  8 个创始人招式  │
                  └────────┬────────┘
                           │ "幸存者是这么解决 X, Y, Z 的"
                           ▼
                  ┌─────────────────┐
                  │  forge ·         │  ← 想法生成
                  │  pricing ·       │  ← 定价实验室
                  │  compass ·       │  ← 指标仪表盘
                  │  gtm ·           │  ← Go-to-market
                  └────────┬────────┘
                           │ "用数据执行，而不是猜测"
```

### 内容概览

| 目录 | 描述 | 数据支撑 |
|---|---|---|
| [`preflight/`](preflight) | 12 维创业健康检查：需求、竞争、单位经济、现金流、团队等 | 1,749 家失败初创（$535B 烧掉）· CB Insights（483 份尸检）· LOOTR 热力图 · Killed by Google（307 产品） |
| [`blueprint/`](blueprint) | 成功手册：7 大框架、5 个收入阶段、6 种商业模式胜法、8 个创始人招式 | StarterStory（1,000+ 访谈）· IndieHackers（5,000+ 创始人）· YC Startup School · MicroConf |
| [`forge/`](forge) | 想法生成引擎：痛点挖掘、快速过滤、机会发现 | Preflight G0 方法论 + 16 行业失败剖面 |
| [`pricing/`](pricing) | 定价实验室：价值定价、分层设计、涨价审计、12+ 真实案例 | Hormozi 价值方程 + StarterStory + IndieHackers 定价结果 |
| [`compass/`](compass) | 指标仪表盘：阶段匹配指标（$0→$1M+）、行业基准、健康阈值 | Blueprint 收入阶段数据 + 模型特定基准 |
| [`gtm/`](gtm) | Go-to-market 策略手册：10 个渠道、阶段匹配推荐、20+ 案例研究 | StarterStory + IndieHackers + Blueprint 交叉引用（v0.5，数据可信度标签） |

### 使用方法

```bash
# 克隆工具包
git clone https://github.com/alpha-xone/startup-kit

# 把六个 skill 复制到你的 harness 用户级 skill 目录
#   CodeWhale   ~/.codewhale/skills/
#   DSH         ~/.dsh/skills/
#   WorkBuddy   ~/.workbuddy-ai/skills/
SKILLS=~/.dsh/skills

cp -r forge preflight blueprint pricing compass gtm "$SKILLS"/
```

然后告诉你的 agent：

> **"Run Preflight on my idea"** → 诊断报告
> **"Run Blueprint on my startup"** → 成功模式分析
> **"在 [某领域] 找想法"** → Forge 机会报告
> **"怎么给我的产品定价？"** → 定价分析
> **"该跟踪什么指标？"** → Compass 仪表盘
> **"什么阶段用什么渠道？"** → 渠道匹配分析

### 报告渲染

报告（HTML）靠**委派**渲染，不在本仓里硬编码样式表：

| 层 | 由谁负责 | 默认 |
|---|---|---|
| 视觉设计 | `impeccable` skill | **light 模式** |
| 每一张图 | `diagram-design` skill | **light 模板** |
| 内容契约 + 状态语义 | 各 skill 的 `references/web-design-guidelines.md` | GO / 迭代 / KILL |

请把这两个 skill 和 Startup Kit 一起装上。没装的话，preflight 会退回 `scripts/generate-dashboard.py`——结构完整，但用的是已废弃的旧配色。

## 🧭 配套：AI 原生 SDLC 套件

上面 6 个 skill 管**创业流程**。管**软件研发流程**的那一套——把 Anthropic《[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)》的 6 个阶段做成可调用的 skill，外加项目骨架——已独立成仓：

> **[github.com/alpha-xone/ai-native-sdlc-kit](https://github.com/alpha-xone/ai-native-sdlc-kit)**

| 阶段 | Skill | 核心玩法 |
|---|---|---|
| ① Plan | `ai-sdlc-plan` | 用提出者自己的话产出 `intent.md`，由产品负责人放行 |
| ② Design | `ai-sdlc-design` | 一次会话走完需求与设计，政策作为约束应用，冲突必须标出 |
| ③ Build | `ai-sdlc-build` | 没有已批准的 `plan.md` 不动手 |
| ④ Test | `ai-sdlc-test` | 给 agent 一条它自己能跑的反馈回路 |
| ⑤ Deploy | `ai-sdlc-deploy` | AI 双向评审；agent 过不去生产闸门 |
| ⑥ Maintain | `ai-sdlc-maintain` | 确定性检测器 + 控制带，突破后以新的 `intent.md` 回到 Plan |

kit 仓还带**仓库侧**那一半：`SDLC.md`（制品→路径绑定、闸门所有者）、`ENFORCEMENT.md`（被强制 / 建议性 / 缺失）、六份政策 skill 骨架、含 `venture/` 交接的项目模板，以及 `factory/scripts/New-Project.ps1`——一个把项目连同治理文档一起自包含生成出来的生成器。

**为什么拆开**：它蒸馏的是 Anthropic 的 playbook，本仓蒸馏的是创始人案例数据（StarterStory / IndieHackers / YC / MicroConf）。来源不同、许可要分别处理、发布节奏也不同——合在一仓会逼着一份许可证同时覆盖两者。

本仓的 `forge` → `preflight` → `blueprint` 正好喂给它的第 0 阶段：`preflight` 与 `blueprint` 的结论落在项目的 `venture/`，之后约束每一份 spec。

## 📁 仓库结构

```
startup-kit/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── NOTICE
├── preflight/       ← 12 维诊断
├── blueprint/       ← 成功手册
├── forge/           ← 想法生成 (v0.6)
├── pricing/         ← 定价实验室 (v0.5)
├── compass/         ← 指标仪表盘 (v0.5)
└── gtm/             ← Go-to-market (v0.5)
```

每个技能在同一层级，各自有 SKILL.md、SKILL.zh-CN.md 和 references/。

## 🔮 路线图

- **forge** ✅ — 想法生成引擎 (v0.6)
- **pricing** ✅ — 定价实验室 (v0.5)
- **compass** ✅ — 指标仪表盘 (v0.5)
- **gtm** ✅ — Go-to-market 策略手册 (v0.5)
- **ai-sdlc** ✅ — 已独立成仓：[alpha-xone/ai-native-sdlc-kit](https://github.com/alpha-xone/ai-native-sdlc-kit) (v1.0)
- **raise** (WIP) — 融资套件：Pitch deck 模式、财务模型、投资人 mapping

## ⚠️ 这不是什么

- **不是水晶球** — 它用历史模式告诉你概率，不是未来
- **不是啦啦队** — 工具在数据不好时说实话，不粉饰你的缺失
- **不只是 VC 的** — 模式按创始人类型标记（自举 vs VC、独立 vs 联合创始人）
- **不隐瞒幸存者偏差** — 每个技能在各自的 `references/data-sources.md` 中记录了方法论局限性
- **不是最终结论** — 决策权在你。这些工具只是确保你基于证据做决定

## 许可

MIT，见 [`LICENSE`](LICENSE)。这些 skill 蒸馏自公开可得的案例数据与已发表的框架；[`NOTICE`](NOTICE) 记录了那些来源，并说明本许可证覆盖与不覆盖的范围。

---

*研究 2,500+ 失败者和 5,000+ 成功者总结而来 — 让你在投入之前看清模式。*
