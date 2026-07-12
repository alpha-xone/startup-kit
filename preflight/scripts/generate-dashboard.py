#!/usr/bin/env python3
"""
idea-forge HTML Dashboard Generator
读取记分卡数据，生成单项目报告或批量对比仪表盘的 HTML 页面。
用法:
  python generate-dashboard.py single <project-name> <score-file.json>
  python generate-dashboard.py batch <batch-file.json>

输出的 HTML 遵循 references/web-design-guidelines.md 设计系统。
"""

import json
import sys
import os
import re
from html import escape

# ─── 设计系统常量（与 web-design-guidelines.md 对应） ───

COLORS = {
    "go": "#16a34a",
    "iterate": "#d97706",
    "kill": "#dc2626",
    "neutral": "#6b7280",
    "bg": "#f8fafc",
    "card": "#ffffff",
    "primary": "#1e293b",
    "accent": "#3b82f6",
    "border": "#e2e8f0",
    "text": "#1e293b",
    "text_secondary": "#64748b",
}

RADAR_COLORS = [
    "#3b82f6", "#f59e0b", "#10b981", "#ef4444",
    "#8b5cf6", "#ec4899", "#14b8a6", "#f97316",
]

DIMENSIONS = ["需求", "斩杀线", "时机", "自身契合", "分发", "机会成本"]

CSS = """/* design system from web-design-guidelines.md */
:root {
    --go: #16a34a; --iterate: #d97706; --kill: #dc2626;
    --bg: #f8fafc; --card: #ffffff; --primary: #1e293b;
    --accent: #3b82f6; --border: #e2e8f0;
    --text: #1e293b; --text-secondary: #64748b;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                 "PingFang SC", "Microsoft YaHei", sans-serif;
    background: var(--bg); color: var(--text); line-height: 1.5;
}
.dashboard { max-width: 1200px; margin: 0 auto; padding: 24px; }
.header {
    background: var(--primary); color: #fff; padding: 16px 24px;
    border-radius: 12px; margin-bottom: 20px;
    display: flex; justify-content: space-between; align-items: center;
}
.header h1 { font-size: 1.5rem; font-weight: 700; }
.header .meta { font-size: 0.875rem; opacity: 0.85; }
.decision-badge {
    display: inline-block; padding: 4px 14px; border-radius: 20px;
    font-weight: 700; font-size: 0.875rem; color: #fff;
}
.decision-go { background: var(--go); }
.decision-iterate { background: var(--iterate); }
.decision-kill { background: var(--kill); }
.conclusion {
    background: #e8f5e9; padding: 12px 16px; border-radius: 8px;
    font-size: 1rem; font-weight: 600; margin-bottom: 20px;
    border-left: 4px solid var(--go);
}
.conclusion.iterate-bg { background: #fff8e1; border-left-color: var(--iterate); }
.conclusion.kill-bg { background: #ffebee; border-left-color: var(--kill); }
.grid-2col {
    display: grid; grid-template-columns: 1fr 1fr; gap: 20px;
    margin-bottom: 20px;
}
@media (max-width: 640px) { .grid-2col { grid-template-columns: 1fr; } }
.radar-container {
    background: var(--card); border-radius: 12px; padding: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
.radar-container canvas { width: 100%; max-width: 300px; height: auto; display: block; margin: 0 auto; }
.score-grid {
    display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;
}
@media (max-width: 480px) { .score-grid { grid-template-columns: 1fr 1fr; } }
.score-card {
    background: var(--card); border-radius: 10px; padding: 12px;
    text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,0.06);
    transition: transform 150ms ease, box-shadow 150ms ease;
    cursor: default;
}
.score-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.score-card .dim-name { font-size: 0.75rem; color: var(--text-secondary); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.score-card .dim-score { font-size: 2rem; font-weight: 700; line-height: 1.2; }
.score-card .dim-trend { font-size: 0.75rem; }
.details-section { margin-bottom: 20px; }
.details-section details {
    background: var(--card); border-radius: 8px; margin-bottom: 6px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.details-section summary {
    padding: 12px 16px; cursor: pointer; font-weight: 600;
    font-size: 0.9rem; list-style: none;
    display: flex; justify-content: space-between; align-items: center;
}
.details-section summary::-webkit-details-marker { display: none; }
.details-section summary::after {
    content: "▸"; font-size: 0.8rem; transition: transform 150ms;
}
.details-section details[open] summary::after { transform: rotate(90deg); }
.details-section .detail-content { padding: 0 16px 12px; font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; }
.kill-zone { background: var(--card); border-radius: 12px; padding: 16px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.kill-zone h3 { font-size: 1rem; margin-bottom: 10px; }
.kill-item { display: flex; align-items: center; gap: 8px; padding: 6px 0; font-size: 0.85rem; }
.kill-item .icon { width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #fff; flex-shrink: 0; }
.kill-item .icon-ok { background: var(--go); }
.kill-item .icon-warn { background: var(--kill); }
.kill-triggered { background: #fef2f2; border-radius: 6px; padding: 4px 8px; }
.next-steps { background: var(--card); border-radius: 12px; padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.next-steps h3 { font-size: 1rem; margin-bottom: 8px; }
.evidence-list { list-style: none; font-size: 0.85rem; }
.evidence-list li { padding: 4px 0; position: relative; padding-left: 16px; }
.evidence-list li::before { content: "•"; position: absolute; left: 4px; color: var(--accent); }

/* ─── Batch Dashboard ─── */
.sort-controls { margin-bottom: 16px; display: flex; gap: 12px; align-items: center; }
.sort-controls select {
    padding: 6px 12px; border: 1px solid var(--border); border-radius: 6px;
    background: var(--card); font-size: 0.875rem; cursor: pointer;
}
.batch-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px; margin-bottom: 20px;
}
.batch-card {
    background: var(--card); border-radius: 12px; padding: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08); text-decoration: none; color: inherit;
    display: block; transition: transform 150ms ease, box-shadow 150ms ease;
}
.batch-card:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
.batch-card .bc-name { font-size: 1.125rem; font-weight: 600; margin-bottom: 4px; }
.batch-card .bc-desc { font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 10px; }
.batch-card .bc-score { font-size: 2.25rem; font-weight: 700; }
.batch-card .bc-mini-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 10px; font-size: 0.75rem; }
.batch-card .bc-mini-item { text-align: center; }
.batch-card .bc-mini-item .label { color: var(--text-secondary); }
.comparison-radar { background: var(--card); border-radius: 12px; padding: 16px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.comparison-radar canvas { width: 100%; max-width: 420px; height: auto; display: block; margin: 0 auto; }
.recommendations { background: var(--card); border-radius: 12px; padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.recommendations h3 { font-size: 1rem; margin-bottom: 8px; }
.rec-item { padding: 6px 0; font-size: 0.875rem; }
.rec-go { color: var(--go); }
.rec-iterate { color: var(--iterate); }
.rec-kill { color: var(--kill); }
"""


def decision_class(score):
    if score is None:
        return "decision-kill"
    if score >= 3.5:
        return "decision-go"
    elif score >= 2.5:
        return "decision-iterate"
    return "decision-kill"


def decision_label(score):
    if score is None:
        return "KILL"
    if score >= 3.5:
        return "GO"
    elif score >= 2.5:
        return "迭代"
    return "KILL"


def score_color(score):
    if score is None:
        return COLORS["kill"]
    if score >= 3.5:
        return COLORS["go"]
    elif score >= 2.5:
        return COLORS["iterate"]
    return COLORS["kill"]


def conclusion_class(score):
    if score is None:
        return "conclusion kill-bg"
    if score >= 3.5:
        return "conclusion"
    elif score >= 2.5:
        return "conclusion iterate-bg"
    return "conclusion kill-bg"


# ─── 雷达图 JS 生成（Canvas 原生绘制） ───

def radar_chart_js(canvas_id, datasets, labels=None):
    """生成 Canvas 雷达图的 JS 代码。datasets: [{label, data, color}]"""
    if labels is None:
        labels = DIMENSIONS
    js = f"""
    (function() {{
        var canvas = document.getElementById("{canvas_id}");
        if (!canvas) return;
        var ctx = canvas.getContext("2d");
        var W = canvas.width, H = canvas.height;
        var cx = W / 2, cy = H / 2;
        var R = Math.min(cx, cy) * 0.72;
        var n = {len(labels)};
        var labels = {json.dumps(labels, ensure_ascii=False)};
        var datasets = {json.dumps(datasets, ensure_ascii=False)};

        function angle(i) {{ return -Math.PI / 2 + (2 * Math.PI * i) / n; }}

        // 清除
        ctx.clearRect(0, 0, W, H);

        // 背景网格 + 刻度标签
        for (var level = 1; level <= 5; level++) {{
            var r = (R * level) / 5;
            ctx.beginPath();
            for (var i = 0; i <= n; i++) {{
                var a = angle(i % n);
                var x = cx + r * Math.cos(a);
                var y = cy + r * Math.sin(a);
                if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
            }}
            ctx.strokeStyle = "#e2e8f0";
            ctx.lineWidth = 1;
            ctx.stroke();
        }}

        // 轴线 + 标签
        ctx.font = "11px -apple-system, sans-serif";
        ctx.fillStyle = "#64748b";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        for (var i = 0; i < n; i++) {{
            var a = angle(i);
            var x1 = cx, y1 = cy;
            var x2 = cx + R * Math.cos(a), y2 = cy + R * Math.sin(a);
            ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
            ctx.strokeStyle = "#e2e8f0"; ctx.lineWidth = 1; ctx.stroke();
            var tx = cx + (R + 22) * Math.cos(a);
            var ty = cy + (R + 22) * Math.sin(a);
            ctx.fillText(labels[i], tx, ty);
        }}

        // 数据
        datasets.forEach(function(ds) {{
            var data = ds.data;
            ctx.beginPath();
            for (var i = 0; i <= n; i++) {{
                var idx = i % n;
                var r = (R * Math.min(data[idx] || 0, 5)) / 5;
                var a = angle(idx);
                var x = cx + r * Math.cos(a);
                var y = cy + r * Math.sin(a);
                if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
            }}
            ctx.closePath();
            ctx.fillStyle = ds.color.replace(")", ",0.12)").replace("rgb", "rgba");
            ctx.fill();
            ctx.strokeStyle = ds.color;
            ctx.lineWidth = 2;
            ctx.stroke();

            // 数据点
            for (var i = 0; i < n; i++) {{
                var r = (R * Math.min(data[i] || 0, 5)) / 5;
                var a = angle(i);
                var x = cx + r * Math.cos(a);
                var y = cy + r * Math.sin(a);
                ctx.beginPath(); ctx.arc(x, y, 4, 0, Math.PI * 2);
                ctx.fillStyle = ds.color;
                ctx.fill();
                ctx.strokeStyle = "#fff";
                ctx.lineWidth = 1.5;
                ctx.stroke();
            }}
        }});

        // 图例
        if (datasets.length > 1) {{
            var ly = H - 8;
            datasets.forEach(function(ds, i) {{
                var lx = 20 + i * 110;
                ctx.fillStyle = ds.color;
                ctx.fillRect(lx, ly - 4, 12, 12);
                ctx.fillStyle = "#1e293b";
                ctx.font = "11px -apple-system, sans-serif";
                ctx.textAlign = "left";
                ctx.textBaseline = "middle";
                ctx.fillText(ds.label.substring(0, 10), lx + 16, ly + 2);
            }});
        }}
    }})();
    """
    return js


# ─── HTML 生成：单项目报告 ───

def generate_single_report(project):
    """
    project: {
        "name": "...",
        "description": "...",
        "round": 1,
        "date": "2026-07-09",
        "composite_score": 3.8,
        "decision": "GO" | "迭代" | "KILL",
        "dimensions": {"需求": 4.0, "斩杀线": 3.5, ...},
        "trends": {"需求": "↑", "斩杀线": "→", ...},
        "conclusion": "...",
        "details": {"需求": {"evidence": "..."}, ...},
        "kill_criteria": [{"condition": "...", "triggered": false}],
        "next_steps": "...",
        "evidence_pending": ["..."]
    }
    """
    name = escape(project.get("name", "未命名项目"))
    desc = escape(project.get("description", ""))
    rnd = project.get("round", 1)
    date = project.get("date", "-")
    comp = project.get("composite_score", 0)
    dims = project.get("dimensions", {})
    trends = project.get("trends", {})
    conclusion = escape(project.get("conclusion", ""))
    details = project.get("details", {})
    kills = project.get("kill_criteria", [])
    next_steps = escape(project.get("next_steps", ""))
    pending = project.get("evidence_pending", [])

    dec_class = decision_class(comp)
    dec_label = decision_label(comp)
    conc_class = conclusion_class(comp)

    # 评分卡片
    score_cards_html = ""
    radar_datasets = [{"label": name, "data": [], "color": f"rgb({','.join(str(int(c.lstrip('#')[i:i+2],16)) for i in (0,2,4))})" if False else COLORS['accent']}]
    import struct
    hexcolor = COLORS['accent'].lstrip('#')
    r, g, b = struct.unpack('BBB', bytes.fromhex(hexcolor))
    radar_datasets[0]["color"] = f"rgb({r},{g},{b})"

    for dim in DIMENSIONS:
        score = dims.get(dim)
        trend = trends.get(dim, "")
        if score is not None:
            radar_datasets[0]["data"].append(score)
            sc = score_color(score)
            trend_arrow = {"↑": "📈", "↓": "📉", "→": "➡️", "": ""}.get(trend, "")
            score_cards_html += f"""
            <div class="score-card">
                <div class="dim-name">{dim}</div>
                <div class="dim-score" style="color:{sc}">{score}</div>
                <div class="dim-trend">{trend_arrow}</div>
            </div>"""
        else:
            radar_datasets[0]["data"].append(0)
            score_cards_html += f"""
            <div class="score-card">
                <div class="dim-name">{dim}</div>
                <div class="dim-score" style="color:{COLORS['neutral']}">-</div>
                <div class="dim-trend"></div>
            </div>"""

    # 详情手风琴
    details_html = ""
    for dim in DIMENSIONS:
        det = details.get(dim, {})
        evidence = escape(det.get("evidence", ""))
        if not evidence:
            # 从 dimensions 的备注找
            evidence = escape(dims.get(dim, ""))
        score = dims.get(dim, "-")
        sc_color = score_color(score) if score != "-" else COLORS["neutral"]
        details_html += f"""
        <details>
            <summary>
                <span>{dim} <span style="color:{sc_color};font-weight:700;">{score}</span></span>
            </summary>
            <div class="detail-content">{evidence if evidence else "暂无详细证据"}</div>
        </details>"""

    # 止损线
    kill_html = ""
    for k in kills:
        cond = escape(k.get("condition", ""))
        triggered = k.get("triggered", False)
        if triggered:
            kill_html += f"""<div class="kill-item kill-triggered"><span class="icon icon-warn">!</span> {cond} ⚠️ 已触发</div>"""
        else:
            kill_html += f"""<div class="kill-item"><span class="icon icon-ok">✓</span> {cond} ✅ 未触发</div>"""

    # 待补证据
    pending_html = ""
    for p in pending:
        pending_html += f"<li>{escape(p)}</li>"

    # 雷达图 JS
    radar_js = radar_chart_js("radar-chart", radar_datasets)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>idea-forge · {name}</title>
<style>{CSS}</style>
</head>
<body>
<div class="dashboard">

    <div class="header">
        <div>
            <h1>{name}</h1>
            <div class="meta">第 {rnd} 轮 · {date}</div>
        </div>
        <div class="decision-badge {dec_class}">{dec_label}</div>
    </div>

    <div class="{conc_class}">
        {conclusion if conclusion else "暂无结论"}
    </div>

    <div class="grid-2col">
        <div class="radar-container">
            <canvas id="radar-chart" width="300" height="300"></canvas>
        </div>
        <div class="score-grid">
            {score_cards_html}
        </div>
    </div>

    <div class="details-section">
        <h3 style="font-size:0.9rem;margin-bottom:8px;color:var(--text-secondary);">各维度详情</h3>
        {details_html}
    </div>

    <div class="kill-zone">
        <h3>止损线检查</h3>
        {kill_html if kill_html else "<div style='color:var(--text-secondary);font-size:0.85rem;'>未设置止损线</div>"}
    </div>

    <div class="next-steps">
        <h3>下一步行动</h3>
        <p style="font-size:0.875rem;">{next_steps if next_steps else "无"}</p>
        {f'<h3 style="margin-top:12px;font-size:0.9rem;">待补证据</h3><ul class="evidence-list">{pending_html}</ul>' if pending_html else ""}
    </div>

</div>
<script>{radar_js}</script>
</body>
</html>"""
    return html


# ─── HTML 生成：批量仪表盘 ───

def generate_batch_dashboard(projects):
    """
    projects: [project_1, project_2, ...]  每个 project 字段同单报告格式，但只需 quick-mode 字段
    """
    cards_html = ""
    radar_datasets = []

    for i, p in enumerate(projects):
        name = escape(p.get("name", f"Idea {i+1}"))
        desc = escape(p.get("description", ""))
        comp = p.get("composite_score", 0)
        dims = p.get("dimensions", {})
        dec_label = decision_label(comp)
        dec_class = decision_class(comp)
        sc_color = score_color(comp)

        mini_dims = {"需求": dims.get("需求", "-"), "斩杀线": dims.get("斩杀线", "-"), "分发": dims.get("分发", "-")}
        color = RADAR_COLORS[i % len(RADAR_COLORS)]

        # 雷达数据集
        ds = {"label": name, "data": [dims.get(d, 0) if dims.get(d) is not None else 0 for d in DIMENSIONS[:3]], "color": color}
        radar_datasets.append(ds)

        cards_html += f"""
        <div class="batch-card" data-score="{comp}">
            <div class="bc-name">{name}</div>
            <div class="bc-desc">{desc}</div>
            <div class="bc-score" style="color:{sc_color}">{comp:.1f}</div>
            <div><span class="decision-badge {dec_class}" style="font-size:0.75rem;padding:2px 10px;">{dec_label}</span></div>
            <div class="bc-mini-grid">
                <div class="bc-mini-item"><div class="label">需求</div><div>{mini_dims["需求"]}</div></div>
                <div class="bc-mini-item"><div class="label">斩杀线</div><div>{mini_dims["斩杀线"]}</div></div>
                <div class="bc-mini-item"><div class="label">分发</div><div>{mini_dims["分发"]}</div></div>
            </div>
        </div>"""

    radar_js = radar_chart_js("comparison-radar", radar_datasets, labels=DIMENSIONS[:3])

    # 推荐排序
    sorted_projects = sorted(projects, key=lambda p: p.get("composite_score", 0), reverse=True)
    rec_html = ""
    for p in sorted_projects:
        name = escape(p.get("name", "?"))
        comp = p.get("composite_score", 0)
        dl = decision_label(comp)
        cls = "rec-go" if dl == "GO" else "rec-iterate" if dl == "迭代" else "rec-kill"
        action = "→ MVP 开工" if dl == "GO" else "→ 调整方向再评估" if dl == "迭代" else "→ 建议斩杀"
        rec_html += f"""<div class="rec-item {cls}">{"🟢" if dl == "GO" else "🟡" if dl == "迭代" else "🔴"} <strong>{name}</strong> ({comp:.1f}) {action}</div>"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>idea-forge · 仪表盘 · 比较模式</title>
<style>{CSS}</style>
</head>
<body>
<div class="dashboard">

    <div class="header">
        <div>
            <h1>⚡ idea-forge · 仪表盘 · 比较模式</h1>
            <div class="meta">{len(projects)} 个想法</div>
        </div>
        <div class="sort-controls">
            <label style="font-size:0.875rem;opacity:0.85;">排序:</label>
            <select id="sort-select" onchange="sortCards(this.value)">
                <option value="composite">综合分 ↓</option>
                <option value="demand">需求 ↓</option>
                <option value="kill">斩杀线 ↓</option>
                <option value="distribution">分发 ↓</option>
            </select>
        </div>
    </div>

    <div class="batch-grid" id="batch-grid">
        {cards_html}
    </div>

    <div class="comparison-radar">
        <canvas id="comparison-radar" width="420" height="360"></canvas>
    </div>

    <div class="recommendations">
        <h3>💡 推荐行动</h3>
        {rec_html}
    </div>

</div>
<script>
{radar_js}

function sortCards(by) {{
    var grid = document.getElementById("batch-grid");
    var cards = Array.from(grid.children);
    cards.sort(function(a, b) {{
        var va = parseFloat(a.dataset[by] || a.dataset.score || 0);
        var vb = parseFloat(b.dataset[by] || b.dataset.score || 0);
        return vb - va;
    }});
    cards.forEach(function(c) {{ grid.appendChild(c); }});
}}
</script>
</body>
</html>"""
    return html


# ─── CLI ───

def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python generate-dashboard.py single <project.json>")
        print("  python generate-dashboard.py batch <batch.json>")
        print("  python generate-dashboard.py demo             # 生成演示 HTML")
        sys.exit(1)

    if sys.argv[1] == "demo":
        # 演示数据：生成所有三种 HTML
        demo_project = {
            "name": "Demo Idea",
            "description": "一个示例项目",
            "round": 1,
            "date": "2026-07-09",
            "composite_score": 3.8,
            "dimensions": {"需求": 4.0, "斩杀线": 3.5, "时机": 3.0, "自身契合": 4.5, "分发": 3.8, "机会成本": 2.5},
            "trends": {"需求": "↑", "斩杀线": "→", "时机": "↑", "自身契合": "→", "分发": "→", "机会成本": "↓"},
            "conclusion": "需求真实，用户付费意愿强，分发路径清晰，建议推进 MVP。",
            "details": {
                "需求": {"evidence": "Reddit r/SaaS 同一痛点出现 15+ 条原生抱怨。G2 竞品 2-3 星差评集中在 X 功能缺失。目标用户已在为凑合方案付费（$29/月）。"},
                "斩杀线": {"evidence": "ai-graveyard 评估：🟡 低风险。需求真实（非自嗨），单位经济可正（预计毛利 72%），非薄套壳。"},
                "时机": {"evidence": "YC 2026 Spring RFS 点名此方向。Google Trends 显示搜索量 12 个月上升 40%。"},
                "自身契合": {"evidence": "团队有 5 年行业经验，现有社群 2000+ 潜在用户。"},
                "分发": {"evidence": "首批用户来自现有社群 + 特定 Reddit 子版块 + Product Hunt 发布计划。"},
                "机会成本": {"evidence": "需要投入约每周 10 小时，对主线 Borki 影响可控。"},
            },
            "kill_criteria": [
                {"condition": "落地页上线后 30 天内拿不到 50 注册", "triggered": False},
                {"condition": "首批 20 个访谈中 <3 人愿意预付", "triggered": False},
                {"condition": "6 周内单位经济做不到毛利为正", "triggered": False},
            ],
            "next_steps": "🟢 GO：2 周内上线 MVP 落地页 + 启动首批 20 个用户访谈。2 周后 loop 复查。",
            "evidence_pending": ["搜索关键词月量 >=500 且难度 <30 的确认", "合规审查（预测/押注类产品形态）"],
        }
        html = generate_single_report(demo_project)
        with open("idea-forge-report-demo.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ 已生成: idea-forge-report-demo.html")

        # 批量演示
        batch = []
        for i, name in enumerate(["世界杯预测 App", "AI 代码审查工具", "知识付费平台", "宠物社交"]):
            comp = [4.2, 3.1, 2.8, 1.5][i]
            base_desc = ["足球迷的预测工具", "开发者代码质量助手", "面向 PM 的知识社区", "宠物主社交 App"][i]
            batch.append(demo_project | {
                "name": name,
                "description": base_desc,
                "composite_score": comp,
                "dimensions": {"需求": [3.8, 3.0, 2.5, 1.2][i],
                               "斩杀线": [3.5, 2.8, 3.0, 2.2][i],
                               "分发": [4.5, 3.5, 2.0, 1.2][i]},
            })
        html_batch = generate_batch_dashboard(batch)
        with open("idea-forge-dashboard-demo.html", "w", encoding="utf-8") as f:
            f.write(html_batch)
        print("✅ 已生成: idea-forge-dashboard-demo.html")
        print("  打开 HTML 文件在浏览器中查看仪表盘效果。")
        return

    if sys.argv[1] == "single":
        if len(sys.argv) < 3:
            print("需提供项目 JSON 文件路径")
            sys.exit(1)
        with open(sys.argv[2], encoding="utf-8") as f:
            project = json.load(f)
        html = generate_single_report(project)
        out_name = f"idea-forge-{project.get('name', 'report')}.html"
        with open(out_name, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ 已生成: {out_name}")

    elif sys.argv[1] == "batch":
        if len(sys.argv) < 3:
            print("需提供批量 JSON 文件路径")
            sys.exit(1)
        with open(sys.argv[2], encoding="utf-8") as f:
            projects = json.load(f)
        html = generate_batch_dashboard(projects)
        out_name = "idea-forge-dashboard.html"
        with open(out_name, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ 已生成: {out_name}")


if __name__ == "__main__":
    main()
