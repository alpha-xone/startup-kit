# Startup Kit · 诊断 · 对标 · 执行

> **完整的创业评估工具包：preflight 查你的生存几率，blueprint 告诉你赢家怎么赢。**

两个互补技能，基于 **2,500+ 失败创业尸检报告** 和 **5,000+ 成功创始人故事** 的系统分析。配合使用：先诊断什么可能杀死你，再找到赢家用来生存和壮大的具体招式。

## 🗺️ 工具链

```
                  ┌───────────────┐
                  │   preflight . │
                  │   "怎么死"     │  ← 2,500+ 失败案例
                  │   12 维诊断    │
                  └────────┬──────┘
                           │ "你的最大风险是 X, Y, Z"
                           ▼
                  ┌────────────────┐
                  │  blueprint ·   │
                  │   "怎么赢"      │  ← 5,000+ 成功案例
                  │  5 大模块       │
                  │  8 个创始人招式 │
                  └────────┬───────┘
                           │ "幸存者是这么解决 X, Y, Z 的"
                           ▼
                  ┌─────────────────┐
                  │   forge (WIP)   │  ← 想法生成
                  │  gtm (WIP)      │  ← 市场策略手册
                  │  pricing (WIP)  │  ← 定价实验室
                  │  compass (WIP)  │  ← 指标仪表盘
                  │  raise (WIP)    │  ← 融资套件
                  └─────────────────┘
```

### 内容概览

| 目录 | 描述 | 数据支撑 |
|---|---|---|
| [`preflight/`](preflight) | 12 维创业健康检查：需求、竞争、单位经济、现金流、团队等 | 1,749 家失败初创（$535B 烧掉）· CB Insights（483 份尸检）· LOOTR 热力图 · Killed by Google（307 产品） |
| [`blueprint/`](blueprint) | 成功手册：7 大框架、5 个收入阶段、6 种商业模式胜法、8 个创始人招式 | StarterStory（1,000+ 访谈）· IndieHackers（5,000+ 创始人）· YC Startup School · MicroConf |

### 使用方法

```bash
# 克隆整个工具包
git clone https://github.com/alpha-xone/startup-kit

# 或者将单个 skill 复制到你的 CodeWhale skills 目录
cp -r preflight ~/.codewhale/skills/
cp -r blueprint ~/.codewhale/skills/
```

然后告诉你的 agent：

> **"Run Preflight on my idea: [描述]"** → 诊断报告
> **"Run Blueprint on my startup: [描述]"** → 成功模式分析
> **"Preflight 标了我的平台依赖为 🔴 — 用 Blueprint 反击模式"** → 组合流程

## 🔬 数据来源

### Preflight 的墓园数据

| 来源 | 规模 |
|---|---|
| **Loot Drop** | 1,749 家失败初创，$535B 烧掉 |
| **CB Insights** | 483 份尸检报告 |
| **Failory** | 200+ 分析 + Google/Amazon 墓园 |
| **LOOTR 热力图** | 16 个行业 × 12 个失败原因 |
| **Killed by Google** | 307 个停产品 |
| **Unbiased Ventures** | 2024-2025 重大失败 |

### Blueprint 的成功数据

| 来源 | 规模 |
|---|---|
| **StarterStory** | 1,000+ 创始人访谈（已验证收入） |
| **IndieHackers** | 5,000+ 收入透明的创始人 |
| **YC Startup School + Library** | 4,000+ YC 公司 |
| **MicroConf** | 100+ 自举 SaaS 创始人演讲 |
| **First Round Review** | 100+ 投资组合深度分析 |
| **Lenny's Podcast** | 200+ 产品领导力访谈 |

## 🧬 各工具一览

### Preflight：12 维压力测试

| # | 维度 | 关键问题 |
|---|---|---|
| 1 | 需求真伪 | 谁在付钱？他们现在怎么解决？ |
| 2 | 竞争护城河 | 大公司一个 sprint 能复制你吗？ |
| 3 | 单位经济 | LTV > 3×CAC？规模越大越好还是越差？ |
| 4 | 现金流 & 跑道 | 设了斩杀线吗？Default alive 还是 dead？ |
| 5 | 团队匹配 | 有人真正懂用户的领域吗？ |
| 6 | 商业模式清晰度 | 为什么有人付钱而不去用免费的替代品？ |
| 7 | 产品/技术可行性 | Demo 到量产的差距？ |
| 8 | 监管/法律 | 需要牌照吗？ |
| 9 | 时机 | 太早还是太晚？ |
| 10 | 增长与分发 | 前 1000 个用户从哪来？ |
| 11 | 平台依赖 | 平台改规则/定价 — 你能活吗？ |
| 12 | 结构韧性 | 经济衰退时还有人需要这个吗？ |

**管道**：G0（发现）→ G1（验证）→ G2（压力测试）→ G3（自查）→ G4（决策）

### Blueprint：5 大成功模块

```
模块 1: 框架       → 7 大经典框架（Helmer, Thiel, Graham, Hormozi 等）
模块 2: 阶段       → 收入阶段模式（$0→$1K→$10K→$50K→$200K→$1M+）
模块 3: 模式       → 商业模式胜法（SaaS、平台、电商、服务、内容、硬件）
模块 4: 招式       → 创始人招式库（8 个可重复、可复制的打法）
模块 5: 反击       → Preflight 12 维反击映射
```

**3 种运行模式**：对标 · 差距分析 · 反击

## 📁 仓库结构

```
startup-kit/
├── README.md                  ← English
├── README.zh-CN.md            ← 中文版
├── preflight/
│   ├── SKILL.md               ← 评估管道 + 12 维度 (英文)
│   ├── SKILL.zh-CN.md         ← 中文版
│   ├── README.md
│   ├── assets/
│   │   └── scorecard-template.md
│   ├── references/            ← 9 个参考文件
│   └── scripts/               ← Python 仪表盘生成器
├── blueprint/
│   ├── SKILL.md               ← 成功手册 (英文)
│   ├── SKILL.zh-CN.md         ← 中文版
│   ├── assets/
│   │   └── scorecard-template.md
│   └── references/            ← 6 个参考文件
└── skills/                    ← 未来配套技能 (forge, gtm, pricing, compass, raise)
    └── ...
```

## 🔮 路线图

计划添加进 `skills/` 目录的技能：

- **forge** — 想法生成引擎（完善现有 idea-forge）
- **gtm** — Go-to-market 策略手册：渠道、首批 1000 用户、PLG、企业销售
- **pricing** — 定价实验室：WTP 调研、模型、分层、价值定价
- **compass** — 指标仪表盘：各阶段 KPI、天花板识别、健康扫描
- **raise** — 融资套件：Pitch deck、财务模型、投资人 mapping

## ⚠️ 这不是什么

- **不是水晶球** — 它用历史模式告诉你概率，不是未来
- **不是啦啦队** — preflight 会在数据不好时说实话；blueprint 不会粉饰你的缺失
- **不只是 VC 的** — 模式按创始人类型标记（自举 vs VC、独立 vs 联合创始人）
- **不隐瞒幸存者偏差** — 两个工具都在 `references/data-sources.md` 中明确记录了方法论局限性
- **不是最终结论** — 决策权在你。这些工具只是确保你基于证据做决定

---

*研究 2,500+ 失败者和 5,000+ 成功者总结而来 — 让你在投入之前看清模式。*
