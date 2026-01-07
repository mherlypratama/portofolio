import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def halaman_project2():
    st.header("Time Series Forecasting")
    st.markdown("---")

    # ================= DESCRIPTION =================
    st.markdown(
        """
Time Series Forecasting is a technique used to predict future values based on historical, 
time-ordered data. This project focuses on analyzing sales behavior over time to identify 
patterns such as trend, seasonality, and fluctuations.

By understanding temporal patterns, businesses can:
- Forecast future sales more accurately  
- Optimize inventory planning  
- Detect seasonal demand  
- Support strategic decision-making  

This page demonstrates data preprocessing and exploratory data analysis (EDA) 
for time series modeling.
"""
    )

    # ================= LOAD DATA =================
    df = pd.read_csv("./data/timeseries.csv")

    st.markdown("---")
    st.subheader("📂 Raw Dataset")
    st.dataframe(df.head())

    # ================= PREPROCESSING =================
    st.markdown("---")
    st.subheader("⚙️ Data Preprocessing")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Missing Values")
        missing = df.isna().sum()
        st.write(
            missing[missing > 0] if missing.sum() > 0 else "No missing values found."
        )

    with col2:
        st.markdown("### Duplicate Rows")
        dup_count = df.duplicated().sum()
        st.write(f"Total duplicated rows: **{dup_count}**")

    # Handle missing values
    df_clean = df.copy()

    # numeric → median
    num_cols = df_clean.select_dtypes(include="number").columns
    for col in num_cols:
        df_clean[col].fillna(df_clean[col].median(), inplace=True)

    # categorical → mode
    cat_cols = df_clean.select_dtypes(include="object").columns
    for col in cat_cols:
        df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

    # remove duplicates
    df_clean.drop_duplicates(inplace=True)

    st.success("✅ Missing values handled and duplicates removed")

    # ================= TIME INDEX PROCESSING =================
    st.markdown("---")
    st.subheader("🕒 Time Index Preparation")   

    if "Order Date" not in df_clean.columns:
        st.error("Column **'Order Date'** not found in dataset.")
        return

    df_clean["Order Date"] = pd.to_datetime(df_clean["Order Date"], errors="coerce")

    df_clean = df_clean.sort_values("Order Date")
    df_clean = df_clean.set_index("Order Date")

    st.write("Datetime index successfully created.")
    st.dataframe(df_clean.head())

    # ================= DAILY AGGREGATION =================
    st.markdown("---")
    st.subheader("📅 Daily Aggregation")

    df_daily = df_clean.resample("D").agg(
        {"Quantity Ordered": "sum", "Price Each": "mean", "Sales": "sum"}
    )

    # stabilizer for log / modeling
    df_daily["Sales_Adjusted"] = df_daily["Sales"] + 0.001

    st.dataframe(df_daily.head())

    # ================= EDA =================
    st.markdown("---")
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    # -------- LINE CHART --------
    st.markdown("### 📈 Daily Sales Trend")

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(df_daily.index, df_daily["Sales"])
    ax.set_title("Total Daily Sales")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    st.pyplot(fig)

    # -------- WEEKLY SEASONALITY --------
    st.markdown("### 📆 Weekly Seasonal Pattern")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x=df_daily.index.dayofweek, y=df_daily["Sales"], ax=ax)
    ax.set_xticks(range(7))
    ax.set_xticklabels(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    ax.set_xlabel("Day of Week")
    ax.set_ylabel("Sales")
    ax.set_title("Weekly Seasonality Pattern")
    st.pyplot(fig)

    # -------- MONTHLY SEASONALITY --------
    st.markdown("### 🗓 Monthly Seasonal Pattern")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x=df_daily.index.month, y=df_daily["Sales"], ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Monthly Seasonality Pattern")
    st.pyplot(fig)

    # ================= BACK BUTTON =================
    st.markdown("---")
    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
