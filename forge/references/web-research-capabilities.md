# 联网检索能力层 · Web Research Capabilities

Forge 的痛点挖掘要读真实用户抱怨，而最有价值的渠道——Reddit、X、小红书、知乎——恰好是最容易被匿名抓取挡住的。

**所以顺序是：先探测这台机器上有哪些联网手段 → 再按渠道路由 → 最后声明哪些渠道没够到。** 跳过任何一步，报告的可信边界就是未知的。

## Step 0 · 能力探测

依次探测，记录哪些 Tier 可用。**不要假设 Tier 存在。**

| Tier | 机制 | 探测方式 | 可用时能做什么 |
|---|---|---|---|
| **A** | 宿主运行时的原生联网工具（WebSearch / WebFetch 或等价物） | 发一条必然有结果的检索（目标领域的通用词），看是否返回 | 万能，但受索引限制：登录墙后与反爬站点拿不到 |
| **B** | **OpenCLI** —— 把网站变成 CLI，复用你已登录的 Chrome 会话 | `opencli doctor`（退出码 0 = 就绪）· `opencli list` 看装了哪些适配器 · 守护进程 `curl -s localhost:19825/status` | 能穿登录墙与反爬，拿到结构化 JSON |
| **C** | 通用浏览器自动化（Playwright / agent-browser / chrome-devtools 类 MCP） | 打开一个已知站点并取回 DOM | 无适配器站点的兜底；慢且脆 |
| **D** | 人工介入 —— 用户粘贴原帖、截图、导出文件 | 直接问用户 | 自动化全部失效时的唯一诚实出路 |

探测结果写进报告的「检索能力与盲区」段。**读者看不到 Tier，就无法判断证据的可信边界。**

## Tier B · OpenCLI 操作要点

**安装**（按推荐顺序）：

- 桌面版 `https://opencli.info/download` → 在 System 页安装/修复 `opencli` 命令（macOS / Windows）
- `npm install -g @jackwener/opencli`（需 Node ≥ 20.18.1；CLI-only / CI / 服务器）
- 浏览器侧**必须**装 Browser Bridge 扩展：Chrome 应用商店搜 OpenCLI；或从 GitHub Releases 下载 `opencli-extension-v{version}.zip` 解压 → `chrome://extensions` → 开启开发者模式 → 加载已解压的扩展程序

**验证**：`opencli doctor`

**调用形态**：`opencli <site> <command> [args] [-f json|md|csv|table|yaml]`

### 采集只用只读命令

| 渠道 | 只读命令 |
|---|---|
| Reddit | `opencli reddit search "<句式>" -f json` · `opencli reddit subreddit <name>` · `opencli reddit read <id>` |
| X / Twitter | `opencli twitter search "<句式>" -f json` · `opencli twitter trending` |
| Hacker News | `opencli hackernews search` · `opencli hackernews ask` · `opencli hackernews show` |
| 小红书 | `opencli xiaohongshu search` · `opencli xiaohongshu comments <id>` |
| 知乎 | `opencli zhihu search` · `opencli zhihu question <id>` |
| B 站 | `opencli bilibili search` · `opencli bilibili comments` |
| 抖音 / 微博 | `opencli douyin ...` · `opencli weibo ...` |
| LinkedIn | `opencli linkedin search` · `opencli linkedin posts`（需登录态） |
| Upwork | `opencli upwork search` —— 直接看到需求方在为**什么**付钱 |
| Amazon | `opencli amazon search` · `opencli amazon discussion` · `opencli amazon bestsellers` —— 差评即缺口清单 |
| Google Scholar | `opencli google-scholar ...` |
| 其余 100+ | `opencli list` 自查 |

**禁止用写命令采集证据。** `post` `comment` `reply` `follow` `like` `upvote` `save` `publish` 这类会以用户身份留下痕迹、改变社区状态、或违反平台条款。**采集是只读行为。**

### 退出码与排障

遵循 `sysexits.h`：

- `0` 成功
- `66` 空结果 —— 该渠道确实没有信号，**这是结论，不是故障**
- `69` Browser Bridge 未启动 → 确认 Chrome 在跑、扩展已加载、`opencli doctor` 通过
- `75` 超时
- `77` 需要登录 → 让用户到 Chrome 里重新登录该站点后重试；**不要**自己造登录流程
- `78` 配置错误
- `130` Ctrl-C

多 Chrome profile：`opencli profile list` → `opencli profile use <name>`，或单次 `--profile <name>`。
会话模式：`OPENCLI_SITE_SESSION=ephemeral`（用完关窗）或 `persistent`（复用站点会话）。

`-f json` 的输出直接喂给模型或 `jq` 过滤，**不要靠人眼读表格**。

## 渠道 × Tier 路由表

按优先级从左到右尝试。

| 渠道 | 首选 | 次选 | 兜底 | 备注 |
|---|---|---|---|---|
| Reddit | B | A（常被反爬） | D | 本环境历史上 A 不可达，必须声明 |
| X / Twitter | B | — | D | A 基本检索不到，历史固定盲区 |
| Hacker News | B | A（A 表现良好） | C | Ask HN / Show HN 含金量最高 |
| 小红书 | B | C | D | 需登录态 |
| 知乎 | B | A（部分） | C | |
| B 站 / 抖音 / 微博 | B | C | D | |
| LinkedIn | B | — | D | 需登录态 |
| Upwork | B | A | D | 直接暴露付费意愿 |
| Amazon 差评 | B | A | C | 缺口清单来源 |
| G2 / Capterra | A | C | D | 无适配器，走浏览器自动化 |
| Product Hunt / Indie Hackers | A | C | D | |
| V2EX / 即刻 / 少数派 | A | B | D | |
| YC Request for Startups | A | — | — | 官方页面，A 足够 |

## 降级与声明规则（硬性）

1. **未找到 ≠ 不存在。** 只有 Tier A 时，把「未发现抱怨」写成「Tier A 对该渠道不可达，未发现」——**不能**写成「该需求不存在」。
2. **每条证据带三件事**：来源链接 + 采集 Tier + 采集日期。缺一项即视为未核实。
3. **「这是空位」必须附检索日期**，有效期按周计——存活区半衰期已短到周级。
4. **连续 3 次检索失败就停手，转推导。** 别再换关键词硬搜；改推导结构性约束（「纯前端在结构上只能满足免死条件 2 和 5」这类结论比检索结论更耐用）。
5. **单源数字一律标「未核实」。** 估值/流量/收入类数字必须交叉验证。
6. **命中判据沿用 `discover.md`**：同一痛点出现 ≥10 次且无人给出满意方案 → 候选机会。
7. **报告必须含「检索能力与盲区」段**：列出可用 Tier、已尝试但不可达的渠道及原因。**没有这段，报告不可信。**

## 合规边界

复用用户自己的登录态意味着所有请求**以用户身份发出**。因此：

- 只读、限速、不绕过付费墙、不批量下载受版权保护的内容
- 不代用户发帖、评论、关注、点赞
- 采集前确认目标平台条款允许该用途；不确定时降级到 Tier D（让用户自己提供）
