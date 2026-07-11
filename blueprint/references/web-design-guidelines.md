# HTML Output Design Guidelines

When generating HTML reports for Blueprint, follow this design system. The goal is clean, professional, data-dense reports — not flashy marketing pages.

## Color Palette

```
Success Green: #16A34A (Completed / Healthy / 🟢)
Warning Amber: #CA8A04 (Partial / At-risk / 🟡)
Danger Red:   #DC2626 (Missing / Critical / 🔴)
Neutral Dark: #111827 (Text / Headings)
Neutral Mid:  #6B7280 (Secondary text / Labels)
Neutral Light:#F3F4F6 (Backgrounds / Cards)
White:        #FFFFFF (Card backgrounds)
Border:       #E5E7EB (Card borders / Dividers)
```

## Typography

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

h1: 24px, bold
h2: 20px, bold
h3: 16px, bold
body: 14px, #111827
secondary: 12px, #6B7280
```

## Layout

**Overall structure** (top to bottom):

```
┌─────────────────────────────────────────┐
│  Nav: Project Name · Mode · Date        │
├─────────────────────────────────────────┤
│  Project Overview Card                  │
│  Stage / Model / Founder Type / Challenge│
├──────────────┬──────────────────────────┤
│  Stage       │  Module Scores & Actions │
│  Progress    │  (5 modules, scored)     │
│  Indicator   │                          │
├──────────────┴──────────────────────────┤
│  Move Completion Radar (8 moves)        │
├─────────────────────────────────────────┤
│  Peer Benchmark Comparison              │
├─────────────────────────────────────────┤
│  Top 3 Actions (priority ordered)       │
└─────────────────────────────────────────┘
```

## Components

### Project Overview Card
- Top of the page, full width
- Title, revenue stage, business model, founder type
- One-line challenge description
- If Preflight data available: add a small Preflight score badge

### Stage Progress Indicator
- 5-stage ladder: Validation → PMF → Scaling → Team → Engine
- Current stage highlighted, completed stages in green
- Left side of the main content or top bar

### Module Score Cards
- 5 cards, one per module
- Each card: module name, 1-sentence score, 2-3 bullet gaps
- Color-coded: 🟢 (aligned with pattern) / 🟡 (partial) / 🔴 (missing)

### Move Completion Radar (optional, for detailed reports)
- 8-axis radar chart: Charge from Day 1, Build in Public, Micro-Niche, Stair-Step, PLG, Unscalable Moves, Empty-Room Demo, Pain-Ladder Pricing
- Score each 0-3 based on alignment with best practices
- Use a simple SVG or canvas radar chart

### Peer Benchmark Table
- 3-4 columns: Pattern | Your Status | Peers at This Stage | Gap
- Color-code gaps: 🟢 closed / 🟡 partial / 🔴 open

### Top 3 Actions
- Numbered list with bold titles
- Each: What to do + Why + Expected outcome + Timeframe
- "This week" actions

## Responsiveness

- Mobile-first: cards stack vertically, radar chart becomes a list
- Max width: 960px centered
- Print-friendly: hide shadows, keep colors

## CSS Reference

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14px; color: #111827; background: #F3F4F6; line-height: 1.5; }
.container { max-width: 960px; margin: 0 auto; padding: 24px; }
.card { background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 8px; padding: 20px; margin-bottom: 16px; }
.card h2 { font-size: 20px; margin-bottom: 12px; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; }
.badge-green { background: #DCFCE7; color: #166534; }
.badge-amber { background: #FEF9C3; color: #854D0E; }
.badge-red { background: #FEE2E2; color: #991B1B; }
.score-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; }
.action-item { border-left: 3px solid #16A34A; padding-left: 16px; margin-bottom: 16px; }
.action-item h3 { font-size: 16px; margin-bottom: 4px; }
table { width: 100%; border-collapse: collapse; }
th, td { text-align: left; padding: 8px 12px; border-bottom: 1px solid #E5E7EB; }
th { font-weight: 600; color: #6B7280; font-size: 12px; text-transform: uppercase; }
</style>
```
