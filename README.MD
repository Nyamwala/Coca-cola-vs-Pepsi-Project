# 🥤 Coca-Cola vs. PepsiCo: Global Market & Equity Comparative Analytics

[![Jupyter Book Badge](https://img.shields.io/badge/Jupyter_Book-Published-blue?style=flat-square&logo=jupyter)](https://jupyter.org)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end data science portfolio project and interactive 3-page web publication comparing **The Coca-Cola Company (KO)** and **PepsiCo, Inc. (PEP)** across multi-decade financial time series. Hosted live via Jupyter Book and GitHub Pages.

---

## 📖 Project Overview & Structure

This project bridges quantitative data engineering with executive-level financial strategy. The publication is structured into three core modules:

1. **`01_Home.ipynb`**: High-level executive summary, dataset schema validation, core KPI dashboard (CAGR, Volatility, Max Drawdown), and multi-asset price trajectory visualizations.
2. **`02_Analysis.ipynb`**: Exploratory Data Analysis (EDA) covering intra-day price spreads, 200-day Simple Moving Average (SMA) crossovers, feature correlation heatmaps, and historical dividend growth.
3. **`03_Solutions.ipynb`**: Quantitative risk-tier matrix, risk vs. return benchmarking, strategic asset allocation model (45/55 Dual-Asset Portfolio), and automated CSV data export functionality.

---

## 🛠️ Tech Stack & Libraries

* **Language**: Python 3.8+
* **Data Manipulation & Math**: `pandas`, `numpy`
* **Data Visualization**: `matplotlib`, `seaborn`
* **Publishing**: `jupyter-book`, GitHub Pages, Git Bash

---

## 📊 Key Insights & Strategic Findings

* **Growth vs. Defense:** While Coca-Cola (`KO`) is traditionally viewed as the benchmark defensive stock, quantitative analysis reveals that PepsiCo (`PEP`) achieved a superior Compound Annual Growth Rate (CAGR) with a shallower maximum drawdown during major macroeconomic downturns, driven by its snack and food division (Frito-Lay).
* **Liquidity Profile:** `KO` consistently demonstrates higher daily trading volume (~10.8M shares) compared to `PEP` (~5.2M shares), highlighting distinct retail and institutional liquidity appetites.
* **Optimal Allocation:** We propose an optimized **45% KO (Defensive Income) / 55% PEP (Growth & Diversification)** dual-asset portfolio weighting to balance yield and capital appreciation.

---

## 🚀 Local Installation & Book Build

To clone, run, and build this repository locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/coca-cola-vs-pepsi.git
cd coca-cola-vs-pepsi

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter-book

# 3. Build the Jupyter Book locally
python -m jupyter_book build book/

# 4. (Optional) Publish live to GitHub Pages
python -m jupyter_book publish book/ --gh-pages
```

---

## 💾 Automated Data Engineering Output
The analytics pipeline programmatically compiles and exports a clean summary table of all computed metrics to:
`data/coca_cola_vs_pepsi_executive_summary.csv`

---

## 👤 Author & License
Developed as a professional data science portfolio piece. Licensed under the [MIT License](LICENSE).