#!/usr/bin/env python3
"""
idea-forge 记分卡辅助脚本 — 让循环的状态管理可确定、可复用。

用法:
  # 新建一张记分卡（不存在才创建，已存在会报错保护历史）
  python scorecard.py init "cup世界杯预测" --one-liner "世界杯比赛预测+球员Tag玩法" \
      --dir /path/to/workspace

  # 读取记分卡里最近一轮的各维度分数（供循环时算 delta）
  python scorecard.py last /path/to/scorecard-cup世界杯预测.md

  # 追加新一轮（分数/决策以 JSON 传入，脚本负责排版与轮次编号）
  python scorecard.py append /path/to/scorecard-xxx.md --round-json round.json

round.json 结构见文件末尾 EXAMPLE_ROUND。
脚本只做机械的读写与排版，判断/打分仍由使用 skill 的 Claude 完成。
"""
import argparse
import json
import os
import re
import sys
from datetime import date

DIMENSIONS = ["需求", "斩杀线", "时机", "自身契合", "分发", "机会成本", "合规"]

TEMPLATE = """# 🔨 记分卡 · {project}

> idea-forge 循环状态文件。每跑一轮 append 一节，永远不删旧轮次——历史本身是判断趋势的依据。

**项目一句话**：{one_liner}
**创建于**：{created}
**当前状态**：进行中
**当前决策**：待评估

## 生效中的止损线（Kill Criteria）
<!-- 每条：条件 + 时限 + 触发后动作。循环时逐条核对。 -->
- [ ] （首轮 G4 后填写）

---

## 轮次记录

<!-- APPEND_ANCHOR -->
"""

ROUND_TMPL = """### 第 {n} 轮 · {rdate}

**位置**：{gate}　**决策**：{decision}　**综合分**：{composite}

| 维度 | 本轮 | 上轮 | 趋势 | 依据 |
|---|---|---|---|---|
{rows}

**止损线核对**：{kill_check}
**下一步**：{next_step}
**本轮新增待补证据**：{todo}

---
"""


def slug(name: str) -> str:
    return re.sub(r"\s+", "_", name.strip())


def path_for(directory: str, project: str) -> str:
    return os.path.join(directory, f"scorecard-{slug(project)}.md")


def cmd_init(args):
    p = path_for(args.dir, args.project)
    if os.path.exists(p):
        sys.exit(f"已存在，拒绝覆盖以保护历史：{p}")
    os.makedirs(args.dir, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(
            project=args.project,
            one_liner=args.one_liner or "（待填）",
            created=date.today().isoformat(),
        ))
    print(p)


def parse_rounds(text: str):
    """返回所有轮次的 (n, dim->score) 列表，按出现顺序。"""
    rounds = []
    for m in re.finditer(r"### 第 (\d+) 轮.*?(?=### 第 \d+ 轮|\Z)", text, re.S):
        n = int(m.group(1))
        block = m.group(0)
        scores = {}
        for dim in DIMENSIONS:
            row = re.search(rf"\|\s*{re.escape(dim)}\s*\|\s*([^|]+?)\s*\|", block)
            if row:
                scores[dim] = row.group(1).strip()
        rounds.append((n, scores))
    return rounds


def cmd_last(args):
    with open(args.file, encoding="utf-8") as f:
        text = f.read()
    rounds = parse_rounds(text)
    if not rounds:
        print(json.dumps({"round": 0, "scores": {}}, ensure_ascii=False))
        return
    n, scores = rounds[-1]
    print(json.dumps({"round": n, "scores": scores}, ensure_ascii=False))


def cmd_append(args):
    with open(args.file, encoding="utf-8") as f:
        text = f.read()
    with open(args.round_json, encoding="utf-8") as f:
        r = json.load(f)

    existing = parse_rounds(text)
    prev = existing[-1][1] if existing else {}
    n = (existing[-1][0] + 1) if existing else 1

    rows = []
    for dim in DIMENSIONS:
        cur = str(r.get("scores", {}).get(dim, ""))
        old = str(prev.get(dim, ""))
        trend = trend_arrow(cur, old)
        basis = r.get("basis", {}).get(dim, "")
        rows.append(f"| {dim} | {cur} | {old} | {trend} | {basis} |")

    block = ROUND_TMPL.format(
        n=n,
        rdate=r.get("date", date.today().isoformat()),
        gate=r.get("gate", ""),
        decision=r.get("decision", ""),
        composite=r.get("composite", ""),
        rows="\n".join(rows),
        kill_check=r.get("kill_check", "（无生效止损线）"),
        next_step=r.get("next_step", ""),
        todo=r.get("todo", ""),
    )
    # 新一轮插在 anchor 之后（保留历史，新轮在最上）
    text = text.replace("<!-- APPEND_ANCHOR -->",
                        "<!-- APPEND_ANCHOR -->\n\n" + block, 1)
    # 更新头部当前状态/决策
    text = re.sub(r"\*\*当前决策\*\*：.*", f"**当前决策**：{r.get('decision','')}", text, 1)
    text = re.sub(r"\*\*当前状态\*\*：.*", f"**当前状态**：{r.get('gate','进行中')}", text, 1)
    with open(args.file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"已追加第 {n} 轮")


def trend_arrow(cur: str, old: str) -> str:
    try:
        c, o = float(cur), float(old)
        return "↑" if c > o else "↓" if c < o else "→"
    except ValueError:
        return "—"


def main():
    ap = argparse.ArgumentParser(description="idea-forge 记分卡辅助")
    sub = ap.add_subparsers(required=True)

    i = sub.add_parser("init", help="新建记分卡")
    i.add_argument("project")
    i.add_argument("--one-liner", default="")
    i.add_argument("--dir", default=".")
    i.set_defaults(func=cmd_init)

    l = sub.add_parser("last", help="读取最近一轮分数(JSON)")
    l.add_argument("file")
    l.set_defaults(func=cmd_last)

    a = sub.add_parser("append", help="追加新一轮")
    a.add_argument("file")
    a.add_argument("--round-json", required=True)
    a.set_defaults(func=cmd_append)

    args = ap.parse_args()
    args.func(args)


EXAMPLE_ROUND = {
    "date": "2026-07-09",
    "gate": "G3",
    "decision": "🟡 迭代",
    "composite": "3.1",
    "scores": {"需求": "4", "斩杀线": "2.5", "时机": "4",
               "自身契合": "3", "分发": "2", "机会成本": "2", "合规": "待查"},
    "basis": {"需求": "r/soccer 高频求预测工具; 竞品差评集中在无好友联赛"},
    "kill_check": "落地页止损线未到期",
    "next_step": "先解决合规红线：确认预测玩法是否触发博彩监管",
    "todo": "香港/内地/目标用户所在地 预测类产品合规判定",
}

if __name__ == "__main__":
    main()
