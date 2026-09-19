# web-design-guidelines — Blueprint report rendering spec

> **This file no longer defines colors or fonts.** The visual layer of a Blueprint report belongs to the `impeccable` skill; every chart belongs to the `diagram-design` skill.
> This file defines exactly three things: **render delegation**, **status semantics**, and **the content contract the report must carry**.
>
> The old hardcoded palette here (success/warning/danger + `-apple-system` type ramp) is **deprecated**. Do not reuse it.

---

## 1. Render delegation (mandatory flow)

When producing any Blueprint HTML report, follow this order without skipping steps.

### 1.1 Visual layer → invoke the `impeccable` skill

- A Blueprint report is an impeccable **Read** surface (the reader is understanding a playbook against their own stage); a multi-project comparison is closer to **Operate**. Follow the matching mode.
- Run `node <skill-base-dir>/scripts/context.mjs --target <report path>` once, follow its directives for which playbook to load, and load `reference/craft-floor.md` immediately before editing UI.
- A report is a one-shot artifact: do **not** run `init` to author PRODUCT.md / DESIGN.md first, and do not stop to ask the user because no DESIGN.md exists. Build the Read surface directly, then mention that `init` is available afterward.
- Honor impeccable's quality floor. The rules that bite hardest on this report (the deprecated spec violated all of them):
  - **No eyebrow / kicker label above a heading.** This one is a hard ban.
  - **No colored `border-left` / `border-right` rule** as decoration on cards, list items, or callouts.
  - **No emoji or Unicode glyphs standing in for an icon system.** Status icons are one consistent set of drawn SVGs — see `references/primitive-icons.md` in `diagram-design`.
  - **No same-size icon + heading + text cards as the page skeleton.** A module score card is data (module · score · gaps), not a card wall.
  - No gradient text, decorative glass/blur, zero-offset colored halos, or hard offset shadows.

### 1.2 Chart layer → invoke the `diagram-design` skill

- Every chart in the report is drawn with diagram-design, producing self-contained HTML with inline SVG. Do **not** hand-roll a radar, do **not** pull in Chart.js or any chart library, do **not** use canvas.
- **Default to light**: start from `assets/template.html` (minimal light); use `assets/template-full.html` when the report is a card-based long-form piece. Unless the user explicitly asks for dark, do **not** use `template-dark.html` or any `example-*-dark.html`.
- The first diagram in a project triggers its style-guide gate. For a report, **take option (e), keep the default tokens** (paper + ink + atomic-tangerine accent) rather than interrupting the user; only branch to a real profile when the report targets a project that already ships DESIGN.md / brand tokens.
- **Load the chosen type's `references/type-*.md` before drawing**, and respect the complexity budgets it states.
- Run the skill's self-check before delivery: `python scripts/self_check.py <file>` (plus any geometry verifier available in a repo checkout).

#### Chart → type mapping (report defaults)

| What the report shows | Diagram type | Notes |
|---|---|---|
| Move completion across the 8 founder moves | **Bar chart** (`type-bar.md`) | ⚠️ Radar caps at **5** axes. 8 moves do **not** fit a radar — use a bar chart, or group to ≤5 |
| Module scores (5 modules) | **Bar chart**, or a plain table | Five values rarely earn a chart |
| Stage ladder (Validation → Engine) | **Flowchart** (`type-flowchart.md`) or a ladder table | ≤9 nodes |
| Peer benchmark gaps | **Table** | A table is the right answer here; do not draw it |
| Revenue-stage trajectory against case data | **Line** (`type-line.md`) or **Scatter** (`type-scatter.md`) | ≤5 series / ≤30 points |
| Two-axis prioritisation of actions | **Quadrant** (`type-quadrant.md`) | ≤12 items |
| Benchmarking against peer cases | **Slopegraph** or **Bar** | |

- Ask first whether the figure is needed at all: if a three-row table says it, write the table.
- Keep charts scarce: **1–2 primary figures** per report, tables for the rest.

#### Embedding diagram-design output

- Take the produced **`<svg>` node** (with its `<title>` / `<desc>`) and inline it into the report HTML. Do **not** iframe it, do **not** `<img src>` it, do **not** screenshot it.
- Rename each figure's `<title>` / `<desc>` ids with a per-figure prefix (`<slug>-title` / `<slug>-desc`) so multiple figures in one report never collide.
- Fonts: diagram-design loads one Google Fonts `<link>`. The report may keep **that single** external link (with `preconnect` + `display=swap`); nothing else may be external. For a fully offline report, drop the link, fall back to system families, and say so in the delivery note.
- The report stays **self-contained**: inline `<style>`, no framework, no build step. Small interactions may use inline `<script>`; the figures themselves must not depend on JS to render.

### 1.3 This file → content and semantics only

---

## 2. Mode: light by default

- Reports are **light**: paper/white ground, dark ink type. Dark is opt-in and never mixed with light inside one delivery.
- Print / PDF export must stay readable: light ground, status colors preserved.
- Body and table text ≥ 4.5:1 contrast; large type ≥ 3:1.

---

## 3. Status semantics (the only colors this skill fixes)

Status color is **content semantics** (green/amber/red *is* the finding), not visual style, so it is pinned here and consumed as a semantic token by both skills:

| Status | Value | Used for |
|---|---|---|
| 🟢 Aligned | `#16A34A` | Pattern matched, gap closed, healthy |
| 🟡 Partial | `#D97706` | Partial alignment, at-risk |
| 🔴 Missing | `#DC2626` | Gap open, critical omission |
| ⚪ Not scored / neutral | `#6B7280` | No data, baseline reference |

Rules:

- **Every other** color (ground, cards, borders, emphasis, categorical chart fills) comes from the impeccable / diagram-design theme. Do not re-declare a palette in the report.
- **Never signal status by color alone**: pair it with text (Aligned / Partial / Missing) or shape (filled / hollow / hatched).
- One status, one color, throughout a single report.
- Do not reintroduce the old fixed categorical sequence. Multi-series fills come from diagram-design's style guide — except when the categories *are* aligned/partial/missing, in which case use the three values above.

---

## 4. Content contract

This is the information a Blueprint report must carry — not a layout. Layout belongs to impeccable. Every item below must be findable.

### Single-project report

1. **Project overview** — name, revenue stage, business model, founder type, the one-line challenge.
2. **Stage position** — where they are on Validation → PMF → Scaling → Team → Engine, and which stage patterns they are currently hitting or missing.
3. **Module scores** — the 5 modules, each with its one-sentence verdict and its 2–3 concrete gaps. Missing data is labelled "not scored" — never defaulted to a passing score.
4. **Move completion** — the 8 founder moves, scored, with the top 2–3 gaps named explicitly.
5. **Peer benchmark** — pattern · their status · what peers at this stage do · the gap.
6. **Preflight cross-reference** — when a Preflight scorecard exists, show the mapped risk and its countermove.
7. **Top 3 actions** — what to do, why, expected outcome, timeframe. "This week" specificity required.

### Multi-project comparison

1. One column/card per project: stage · module coverage · move completion · biggest gap.
2. One comparison figure (grouped bar or quadrant).
3. A ranked recommendation naming each project's next move.

### Responsive

- Single column on narrow screens, two columns or side-by-side when wide. Tables may scroll horizontally rather than compress.
- Max width is decided by impeccable; do not pin px here.

---

## 5. Fallback path (only when both skills are unavailable)

There is no scripted generator for Blueprint. If neither skill is installed, hand-author the report from the content contract in §4, render figures as plain HTML tables, and tell the user that the visual and diagram layers were not available.

---

## 6. Pre-delivery checklist

- [ ] Report is **light** and self-contained (except the one diagram-design Google Fonts link).
- [ ] Visual layer genuinely went through impeccable (Read/Operate mode + `craft-floor.md`).
- [ ] Every figure came from diagram-design, with the matching `type-*.md` loaded, inside budget, and passing `self_check.py`.
- [ ] The 8 moves were **not** forced into a radar (cap is 5 axes).
- [ ] Only the four status colors are fixed; nothing else is re-declared.
- [ ] No eyebrow, no colored `border-left`, no emoji as icons, no gradient text or glass.
- [ ] §4 items 1–7 (or the multi-project 1–3) are all present and findable.
- [ ] Print preview is readable; nothing overflows on narrow screens.
