# Data Sources & Methodology

This reference catalogs the data sources that power the Blueprint skill, including their strengths, limitations, and methodology notes.

---

## Primary Data Sources

### StarterStory (starterstory.com)

- **Scale**: 1,000+ founder interviews, each with verified revenue data
- **Data structure**: Per case: founder name, company, industry, revenue (MRR/ARR), founding year, team size, growth story, key moves, challenges, lessons
- **Strength**: The hardest data to fake — every revenue figure is researched and source-checked. Not self-reported fluff.
- **Limitation**: Self-selection bias — founders who agree to be interviewed are the ones with stories to tell. This skews toward success (we don't interview the ones who quit at $500 MRR).
- **Relevance to this skill**: Primary data source for Module 2 (Revenue Stage Patterns) and Module 4 (Founder Moves). The "80% charged from day 1" statistic comes from cross-referencing StarterStory revenue data and founder interview content.
- **Access**: Free tier available; paid for full database + ChatGPT export

### IndieHackers (indiehackers.com)

- **Scale**: 5,000+ founders who publicly share revenue, with community discussions and interviews
- **Data structure**: Per founder: product name, revenue (self-reported), founding date, employee count, interview content, community posts
- **Strength**: Massive sample size. Revenue-transparent culture. Longitudinal data — many founders have years of revenue history.
- **Limitation**: Revenue is self-reported and not independently verified. Some founders inflate numbers. Community skews toward bootstrapped/SaaS/developer tools.
- **Relevance to this skill**: Primary data source for stage transitions, especially bootstrapped founders. The community's culture of transparency makes it the best source for understanding HOW founders moved from stage to stage.
- **Access**: Free

### Y Combinator Startup School + YC Content

- **Scale**: 4,000+ YC companies. Public library of essays, videos, and talks from YC partners and alumni.
- **Data structure**: Essays (Paul Graham, Sam Altman, Michael Seibel), Startup School curriculum, YC founder stories, Demo Day data
- **Strength**: Highest-quality curation of startup advice. YC sees more startups than anyone — their pattern recognition is unmatched. Framework-heavy (do things that don't scale, default alive, make something people want).
- **Limitation**: YC bias — advice optimized for venture-scale startups, not lifestyle businesses. Silicon Valley-centric worldview.
- **Relevance to this skill**: Primary source for Module 1 (Seven Classic Success Frameworks) — Graham, Thiel, and YC ecosystem frameworks.
- **Access**: Free (startupschool.org, ycombinator.com/library)

### MicroConf

- **Scale**: Annual conference + content library for bootstrapped SaaS founders. Founded by Rob Walling (Drip, TinySeed).
- **Data structure**: Talks, interviews, and case studies from bootstrapped SaaS founders at $100K-$10M ARR.
- **Strength**: The best source for bootstrapped SaaS patterns. Speaker lineup is curated for practical, applicable advice — not hype. The "Stair-Step Approach" originated here.
- **Limitation**: Narrow focus — SaaS only, bootstrapped only. Does not cover VC-funded, marketplace, or non-software businesses.
- **Relevance to this skill**: Source for bootstrapped-specific stage patterns and founder moves (especially the Stair-Step Approach and PLG for bootstrappers).
- **Access**: Free content on YouTube; paid for conference

---

## Secondary Data Sources

### First Round Review

- **Scale**: 100+ in-depth articles from the First Round Capital network
- **Strength**: Data-driven articles with original research (e.g., "What do the best founders do differently?") Survey-based analysis of their portfolio.
- **Limitation**: VC portfolio bias — insights from well-funded startups, not bootstrapped ones.
- **Relevance**: Supplementary data for pricing patterns, hiring patterns at scale, and team-building advice.

### Lenny's Podcast / Lenny's Newsletter

- **Scale**: Weekly podcast + newsletter, top 1% in business/tech
- **Strength**: Deep, tactical conversations with founders and product leaders. Lenny asks "how specifically did you do that?" — gets the actual playbook.
- **Limitation**: Skews toward product/growth roles at tech companies, not solo founders.
- **Relevance**: Supplementary source for PLG patterns, growth tactics, and product development methodology.

### SaaSter / SaaStr

- **Scale**: Annual conference + content library, largest SaaS-focused community
- **Strength**: Comprehensive SaaS metrics benchmarks. "What's good churn for a $10M ARR SaaS?" — SaaStr has the answer.
- **Limitation**: SaaS-only. Sales-heavy perspective (most content is from sales-led companies, not PLG).
- **Relevance**: Source for SaaS critical metrics benchmarks and scaling-stage patterns.

---

## Methodology Notes

### How Patterns Are Extracted

1. **Cross-reference**: A pattern is only included if it appears across ≥3 independent sources (e.g., StarterStory + IndieHackers + YC content) AND across ≥5 founder stories.
2. **Counterexample check**: For every pattern, we check: "Do we have counterexamples — founders who did the opposite and still succeeded?" If counterexamples are abundant, the pattern is downgraded to "one of several valid approaches."
3. **Stage specificity**: Patterns are tagged by revenue stage. "Charge from day 1" is a Stage 0 pattern — it wouldn't be recommended to a $500K ARR founder.
4. **Model specificity**: Patterns are tagged by business model. A marketplace founder should not get SaaS-specific growth advice.

### Limitations

1. **Survivor bias**: We study the survivors. The founders who did the same things but still failed are invisible. This means patterns are correlational, not causal.
2. **Self-reporting bias**: Founders tell stories that make sense in retrospect. The messy, random, lucky things that contributed to their success are often omitted or attributed to skill.
3. **Publication bias**: StarterStory and IndieHackers publish interesting stories. "I built a boring CRM for insurance agents and grew slowly for 5 years" doesn't get coverage — but it might be the most common path to $1M ARR.
4. **Time period effects**: Many of the patterns (build in public, PLG) are products of the 2015-2025 era. They may not apply in 2030.
5. **Geography bias**: Most data is from US/European founders. Chinese, Indian, African, and Latin American founders operate in different ecosystems with different constraints.

### Integration with Preflight Data

Preflight's data sources (CB Insights, LOOTR, Failory, Killed by Google) study failures. This skill's data sources study successes. Together they provide a complete picture:

- **Preflight**: "Here's what kills startups, statistically."
- **Success Patterns**: "Here's what the survivors did, qualitatively."

The two are cross-referenced in Module 5: Preflight Countermoves.
