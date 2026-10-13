# 🥤 Coca-Cola vs. PepsiCo: Comparative Market Analytics & Strategic Portfolio Study

## 1. What is the Problem You Are Solving?
Investors, portfolio managers, and market analysts frequently face the challenge of evaluating legacy consumer staple giants—specifically **The Coca-Cola Company (KO)** and **PepsiCo, Inc. (PEP)**—beyond surface-level stock tickers. While both corporations dominate the global beverage industry, their underlying operational models differ significantly: Coca-Cola operates primarily as a high-margin beverage concentrate and licensing powerhouse, whereas PepsiCo operates a vertically integrated business model combining beverage distribution with a massive snack and food portfolio (Frito-Lay). 

Without rigorous quantitative modeling, stakeholders struggle to answer critical questions: *Does PepsiCo's snack diversification truly translate into superior long-term growth and lower downside risk? How do their trading liquidity profiles and dividend aristocrat structures compare across multi-decade market cycles?* This project solves this analytical gap by delivering a structured, data-driven equity comparison to guide optimal capital allocation.

---

## 2. What Tools Did You Use?
This project was engineered using an end-to-end Python data stack and published as an interactive 3-page web portfolio via Jupyter Book:
* **Python (`pandas`, `numpy`):** Utilized for data ingestion, cleaning, historical time-series transformation, and metric computation (CAGR, rolling volatility, intra-day price spreads, and drawdown calculations).
* **Matplotlib & Seaborn:** Deployed to build 8+ custom-styled financial visualizations, including long-term price trajectories, grouped annual trading volume bar charts, 200-day moving average trend lines, feature correlation heatmaps, and portfolio allocation donut charts.
* **Jupyter Book & Git Bash:** Configured for local book compilation and live web publishing to GitHub Pages, showcasing full-stack deployment capabilities.

---

## 3. What Insights Did You Discover & What Solutions Do You Offer?
* **The Growth vs. Defense "Aha!" Moment:** While Coca-Cola (`KO`) is traditionally viewed as the ultimate defensive anchor, our data reveals that PepsiCo (`PEP`) achieved a substantially higher Compound Annual Growth Rate (CAGR) over the multi-decade window while maintaining a shallower maximum drawdown ($-42.43\%$ vs. $-55.66\%$). This proves that PepsiCo's snack division acts as an effective stabilizer during macroeconomic contractions.
* **Liquidity Divergence:** Coca-Cola consistently sustained a significantly higher average daily trading volume (~10.8M shares/day) compared to PepsiCo (~5.2M shares/day), highlighting distinct institutional and retail liquidity profiles.
* **Actionable Solution — Dual-Asset Portfolio Weighting:** Rather than treating KO and PEP as mutually exclusive investments, we offer an optimized **45% KO (Defensive Income) / 55% PEP (Growth & Snack Diversification)** asset allocation model that captures the stability of beverage dividends alongside food-sector capital appreciation.

---

## 4. How Would a Business or Community Benefit From Your Work?
* **Capital Efficiency:** Institutional and retail investors benefit by avoiding sub-optimal single-stock concentration, utilizing our data-backed risk-tier matrix to balance growth and risk.
* **Automated Data Engineering:** By implementing a programmatic script that cleans data and exports a structured summary (`coca_cola_vs_pepsi_executive_summary.csv`), financial analysts save hours of manual reporting time, ensuring reproducible downstream analytics.
* **Executive Decision-Making:** Translates raw historical CSV data into clear, recruiter-ready visual frameworks that empower stakeholders to make defensible, long-term capital deployment decisions.