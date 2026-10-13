import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Coca-Cola vs. PepsiCo | Comprehensive Equity Analytics",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: 700; color: #E41E2B; }
    .sub-text { font-size: 16px; color: #555555; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA LOADING & CACHING (ABSOLUTE PATHS)
# ==========================================
DATA_DIR = r"C:\Users\Admin\Desktop\Coca-cola-vs-Pepsi-Project\Data\coca-cola-vs-pepsi"
SUMMARY_PATH = r"C:\Users\Admin\Desktop\Coca-cola-vs-Pepsi-Project\Data\coca_cola_vs_pepsi_executive_summary.csv"

@st.cache_data
def load_all_data():
    try:
        ko_price = pd.read_csv(os.path.join(DATA_DIR, 'KO_stock_price.csv'))
        pep_price = pd.read_csv(os.path.join(DATA_DIR, 'PEP_stock_price.csv'))
        ko_div = pd.read_csv(os.path.join(DATA_DIR, 'KO_stock_dividend.csv'))
        pep_div = pd.read_csv(os.path.join(DATA_DIR, 'PEP_stock_dividend.csv'))
    except FileNotFoundError as e:
        st.error(f"Dataset file missing in directory {DATA_DIR}: {e}")
        return None, None, None, None

    for df in [ko_price, pep_price, ko_div, pep_div]:
        df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.tz_localize(None)
        df.sort_values('Date', inplace=True)
        df.reset_index(drop=True, inplace=True)
        
    return ko_price, pep_price, ko_div, pep_div

ko_price, pep_price, ko_div, pep_div = load_all_data()

if ko_price is None or pep_price is None:
    st.stop()

# ==========================================
# 3. ADVANCED QUANTITATIVE METRIC FUNCTIONS
# ==========================================
def compute_advanced_metrics(df):
    start_price = df['Close Price'].iloc[0]
    end_price = df['Close Price'].iloc[-1]
    years = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days / 365.25
    cagr = ((end_price / start_price) ** (1 / years) - 1) * 100
    
    df['Daily_Return'] = df['Close Price'].pct_change()
    ann_vol = df['Daily_Return'].std() * (252 ** 0.5) * 100
    
    rolling_max = df['Close Price'].cummax()
    df['Drawdown'] = (df['Close Price'] - rolling_max) / rolling_max
    max_dd = df['Drawdown'].min() * 100
    
    return cagr, ann_vol, max_dd

ko_cagr, ko_vol, ko_dd = compute_advanced_metrics(ko_price)
pep_cagr, pep_vol, pep_dd = compute_advanced_metrics(pep_price)

# ==========================================
# 4. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("🧭 Navigation Hub")
st.sidebar.markdown("---")
module = st.sidebar.radio("Select Project Module", [
    "🏠 Home & Executive Overview",
    "🔍 Exploratory Data Analysis (EDA)",
    "📈 Technical & Market Deep-Dive",
    "🛡️ Strategic Solutions & Portfolio",
    "📂 Raw Data & Export Explorer"
])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Author:** Data Analytics Student\n\n📌 **Project:** Coca-Cola vs. PepsiCo Comparative Portfolio")

# ==========================================
# MODULE 1: HOME & EXECUTIVE OVERVIEW
# ==========================================
if module == "🏠 Home & Executive Overview":
    st.markdown('<p class="main-title">🥤 Coca-Cola vs. PepsiCo: Global Market & Equity Analytics</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">An institutional-grade comparative financial research platform bridging quantitative data science with corporate strategy.</p>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎯 Core Business Problem")
        st.write("""
        Investors frequently categorize **The Coca-Cola Company (KO)** and **PepsiCo, Inc. (PEP)** as interchangeable defensive beverage investments. 
        However, beneath their consumer-staple branding lies a fundamental strategic divergence:
        * **Coca-Cola** operates as a pure-play beverage titan anchored by elite dividend aristocrat status and high liquidity.
        * **PepsiCo** operates as a diversified food and beverage conglomerate offering higher capital appreciation and balanced risk profiles.
        """)
    with col2:
        st.markdown("### 🛠️ Technology Stack")
        st.write("""
        * **Programming Language:** Python 3.13
        * **Data Analytics:** Pandas, NumPy
        * **Data Visualization:** Matplotlib, Seaborn
        * **Web Framework:** Streamlit
        * **Documentation & Publishing:** Jupyter Book & GitHub Pages
        """)

    st.markdown("---")
    st.subheader("📊 Key Performance Indicators (KPI) Scorecard")
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("KO Compound Annual Growth", f"{ko_cagr:.2f}%", "Defensive Anchor")
    kpi2.metric("PEP Compound Annual Growth", f"{pep_cagr:.2f}%", "Growth & Diversification")
    kpi3.metric("KO Annualized Volatility", f"{ko_vol:.2f}%", "Higher Swing Risk")
    kpi4.metric("PEP Annualized Volatility", f"{pep_vol:.2f}%", "Smoother Trajectory")

    st.markdown("---")
    st.subheader("📋 Automated Executive Summary Data Table")
    try:
        summary_df = pd.read_csv(SUMMARY_PATH)
        st.dataframe(summary_df, use_container_width=True)
    except FileNotFoundError:
        st.warning(f"Executive summary CSV not found at: {SUMMARY_PATH}")

# ==========================================
# MODULE 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================
elif module == "🔍 Exploratory Data Analysis (EDA)":
    st.markdown('<p class="main-title">🔍 Exploratory Data Analysis (EDA)</p>', unsafe_allow_html=True)
    st.markdown("Examine descriptive statistics, dataset structures, distributions, and missing value checks.")
    st.markdown("---")

    dataset_choice = st.selectbox("Select Dataset to Inspect", ["Coca-Cola Stock Price", "PepsiCo Stock Price", "Coca-Cola Dividends", "PepsiCo Dividends"])
    
    if dataset_choice == "Coca-Cola Stock Price":
        active_df = ko_price
    elif dataset_choice == "PepsiCo Stock Price":
        active_df = pep_price
    elif dataset_choice == "Coca-Cola Dividends":
        active_df = ko_div
    else:
        active_df = pep_div

    tab1, tab2, tab3 = st.tabs(["📊 Data Preview", "📈 Descriptive Statistics", "📉 Return Distribution"])
    
    with tab1:
        st.subheader("Dataset Head & Tail Preview")
        st.dataframe(active_df.head(10), use_container_width=True)
        st.write(f"Total Rows: {active_df.shape[0]} | Total Columns: {active_df.shape[1]}")
        
    with tab2:
        st.subheader("Statistical Summary Metrics")
        st.dataframe(active_df.describe(), use_container_width=True)
        
    with tab3:
        st.subheader("Daily Return Distribution Histogram")
        if 'Daily_Return' in active_df.columns:
            fig, ax = plt.subplots(figsize=(9, 4))
            sns.histplot(active_df['Daily_Return'].dropna(), bins=50, kde=True, color='#004B93', ax=ax)
            ax.set_title(f"{dataset_choice} - Daily Returns Distribution")
            ax.set_xlabel("Daily Return")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        else:
            st.info("Daily return data is only available for stock price datasets.")

# ==========================================
# MODULE 3: TECHNICAL & MARKET DEEP-DIVE
# ==========================================
elif module == "📈 Technical & Market Deep-Dive":
    st.markdown('<p class="main-title">📈 Technical & Market Deep-Dive Analysis</p>', unsafe_allow_html=True)
    st.markdown("Interactive analysis of price action, moving averages, rolling volatility, drawdowns, and correlation heatmaps.")
    st.markdown("---")

    analysis_view = st.selectbox("Select Analytical Tool", [
        "Price Trends & Moving Averages (SMA)", 
        "Rolling Volatility (30-Day & 90-Day)", 
        "Underwater Drawdown Curves",
        "Feature Correlation Heatmaps",
        "Historical Dividend Payout Trends"
    ])
    
    if analysis_view == "Price Trends & Moving Averages (SMA)":
        st.subheader("Historical Close Price with Configurable Simple Moving Averages")
        equity = st.radio("Choose Equity", ["Coca-Cola (KO)", "PepsiCo (PEP)"], horizontal=True)
        df = ko_price.copy() if equity == "Coca-Cola (KO)" else pep_price.copy()
        
        window_sma = st.slider("Select SMA Window (Days)", min_value=20, max_value=200, value=50, step=10)
        df[f'SMA_{window_sma}'] = df['Close Price'].rolling(window=window_sma).mean()
        
        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(df['Date'], df['Close Price'], label='Close Price', color='#E41E2B' if 'KO' in equity else '#004B93', alpha=0.7)
        ax.plot(df['Date'], df[f'SMA_{window_sma}'], label=f'{window_sma}-Day SMA', color='black', linestyle='--', linewidth=1.5)
        ax.set_title(f"{equity} - Price Action & {window_sma}-Day Simple Moving Average")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price ($ USD)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

    elif analysis_view == "Rolling Volatility (30-Day & 90-Day)":
        st.subheader("Comparative Rolling Annualized Volatility")
        ko_temp = ko_price.copy()
        pep_temp = pep_price.copy()
        
        ko_temp['Rolling_Vol'] = ko_temp['Daily_Return'].rolling(window=30).std() * (252 ** 0.5) * 100
        pep_temp['Rolling_Vol'] = pep_temp['Daily_Return'].rolling(window=30).std() * (252 ** 0.5) * 100
        
        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(ko_temp['Date'], ko_temp['Rolling_Vol'], label='Coca-Cola (KO) 30D Vol', color='#E41E2B', alpha=0.8)
        ax.plot(pep_temp['Date'], pep_temp['Rolling_Vol'], label='PepsiCo (PEP) 30D Vol', color='#004B93', alpha=0.8)
        ax.set_title("30-Day Rolling Annualized Volatility (%)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Volatility (%)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

    elif analysis_view == "Underwater Drawdown Curves":
        st.subheader("Historical Downside Drawdown Analysis")
        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(ko_price['Date'], ko_price['Drawdown'] * 100, label='Coca-Cola (KO) Drawdown', color='#E41E2B', alpha=0.8)
        ax.plot(pep_price['Date'], pep_price['Drawdown'] * 100, label='PepsiCo (PEP) Drawdown', color='#004B93', alpha=0.8)
        ax.set_title("Portfolio Underwater Equity Drawdowns (%)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Drawdown Magnitude (%)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

    elif analysis_view == "Feature Correlation Heatmaps":
        st.subheader("Multivariate Feature Correlation Matrix")
        equity = st.radio("Choose Equity", ["Coca-Cola (KO)", "PepsiCo (PEP)"], horizontal=True, key="hm_key")
        df = ko_price.copy() if equity == "Coca-Cola (KO)" else pep_price.copy()
        
        df['Daily_Spread'] = df['High Price'] - df['Low Price']
        corr_cols = ['Open Price', 'High Price', 'Low Price', 'Close Price', 'Volume', 'Daily_Spread']
        corr_matrix = df[corr_cols].corr()
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(corr_matrix, annot=True, cmap="vlag", fmt=".2f", linewidths=0.8, ax=ax)
        ax.set_title(f"{equity} - Feature Correlation Matrix")
        st.pyplot(fig)

    elif analysis_view == "Historical Dividend Payout Trends":
        st.subheader("Long-Term Dividend Distribution Growth (2000 Onward)")
        ko_div_f = ko_div[ko_div['Date'].dt.year >= 2000]
        pep_div_f = pep_div[pep_div['Date'].dt.year >= 2000]
        
        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.scatter(ko_div_f['Date'], ko_div_f['Dividend'], label='Coca-Cola Dividend', color='#E41E2B', s=35, alpha=0.7)
        ax.scatter(pep_div_f['Date'], pep_div_f['Dividend'], label='PepsiCo Dividend', color='#004B93', s=35, alpha=0.7)
        ax.set_title("Historical Dividend Payout Comparison")
        ax.set_xlabel("Date")
        ax.set_ylabel("Dividend Amount ($ USD)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

# ==========================================
# MODULE 4: STRATEGIC SOLUTIONS & PORTFOLIO
# ==========================================
elif module == "🛡️ Strategic Solutions & Portfolio":
    st.markdown('<p class="main-title">🛡️ Strategic Solutions & Portfolio Management</p>', unsafe_allow_html=True)
    st.markdown("Translating quantitative indicators into actionable institutional risk tiers and dual-asset portfolio allocation models.")
    st.markdown("---")

    st.subheader("1. Institutional Quantitative Risk-Tier Matrix")
    solutions_matrix = pd.DataFrame({
        'Strategic Dimension': [
            'Primary Investment Style', 
            'Compound Annual Growth Rate (CAGR)', 
            'Annualized Risk (Volatility)', 
            'Max Historical Downside Drawdown', 
            'Liquidity Profile (Avg Daily Volume)', 
            'Risk Tier Classification',
            'Recommended Portfolio Weighting'
        ],
        'Coca-Cola (KO)': [
            'Defensive Income & Value Anchor',
            f"{ko_cagr:.2f}%",
            f"{ko_vol:.2f}%",
            f"{ko_dd:.2f}%",
            f"{ko_price['Volume'].mean():,.0f} shares",
            'Low-Medium Risk (Defensive Blue-Chip)',
            '45% (Core Dividend Stability)'
        ],
        'PepsiCo (PEP)': [
            'Balanced Growth & Snack Diversification',
            f"{pep_cagr:.2f}%",
            f"{pep_vol:.2f}%",
            f"{pep_dd:.2f}%",
            f"{pep_price['Volume'].mean():,.0f} shares",
            'Low-Medium Risk (Growth Blue-Chip)',
            '55% (Core Capital Appreciation)'
        ]
    })
    st.table(solutions_matrix)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("2. Risk-Return Comparative Benchmarking")
        metrics_summary = pd.DataFrame({
            'Metric': ['CAGR (%)', 'Volatility (%)', 'Max Drawdown (%)'],
            'Coca-Cola (KO)': [ko_cagr, ko_vol, abs(ko_dd)],
            'PepsiCo (PEP)': [pep_cagr, pep_vol, abs(pep_dd)]
        }).set_index('Metric')

        fig, ax = plt.subplots(figsize=(6, 4.5))
        metrics_summary.plot(kind='bar', ax=ax, color=['#E41E2B', '#004B93'], width=0.7)
        ax.set_title("Strategic Risk & Return Trade-off")
        ax.set_ylabel("Percentage (%)")
        plt.xticks(rotation=0)
        ax.grid(True, axis='y', alpha=0.5)
        st.pyplot(fig)

    with col2:
        st.subheader("3. Optimal Dual-Asset Allocation Model")
        labels = ['Coca-Cola (KO) - 45%', 'PepsiCo (PEP) - 55%']
        sizes = [45, 55]
        colors = ['#E41E2B', '#004B93']

        fig, ax = plt.subplots(figsize=(5, 4.5))
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=140,
               wedgeprops=dict(width=0.4, edgecolor='white', linewidth=3), textprops={'fontsize': 10, 'weight': 'bold'})
        ax.set_title("Recommended Portfolio Weighting")
        st.pyplot(fig)

# ==========================================
# MODULE 5: RAW DATA & EXPORT EXPLORER
# ==========================================
elif module == "📂 Raw Data & Export Explorer":
    st.markdown('<p class="main-title">📂 Raw Data & Export Explorer</p>', unsafe_allow_html=True)
    st.markdown("Inspect and download raw CSV datasets and executive summary files directly from your workspace.")
    st.markdown("---")

    file_choice = st.selectbox("Select File to View", [
        "coca_cola_vs_pepsi_executive_summary.csv",
        "KO_stock_price.csv", 
        "PEP_stock_price.csv", 
        "KO_stock_dividend.csv", 
        "PEP_stock_dividend.csv"
    ])
    
    # Target path selector
    target_path = SUMMARY_PATH if "executive_summary" in file_choice else os.path.join(DATA_DIR, file_choice)
    
    if os.path.exists(target_path):
        df_view = pd.read_csv(target_path)
        st.success(f"Successfully loaded: `{file_choice}`")
        st.dataframe(df_view, use_container_width=True)
        
        csv_data = df_view.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"📥 Download {file_choice}",
            data=csv_data,
            file_name=file_choice,
            mime='text/csv'
        )
    else:
        st.error(f"File not found at path: {target_path}")