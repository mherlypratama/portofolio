import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def halaman_project1():
    st.header("AI Churn Analysis")
    st.markdown("---")

    # ================= LOAD DATA =================
    df = pd.read_csv("./data/churn.csv")

    st.markdown(
        """
Customer churn analysis is a predictive analytics technique that identifies customers who are likely 
to stop doing business with a company. By analyzing historical behavioral and demographic data, 
companies can anticipate churn risk and take preventive actions.

This project demonstrates:
- Data preprocessing  
- Exploratory Data Analysis (EDA)  
- Visualization for insight discovery  
"""
    )

    # ================= RAW DATA =================
    st.markdown("---")
    st.subheader("📂 Raw Dataset")
    st.dataframe(df)

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

    # ---- HANDLE MISSING VALUES ----
    df_clean = df.copy()

    # numerical → median
    num_cols = df_clean.select_dtypes(include="number").columns
    for col in num_cols:
        df_clean[col].fillna(df_clean[col].median(), inplace=True)

    # categorical → mode
    cat_cols = df_clean.select_dtypes(include="object").columns
    for col in cat_cols:
        df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

    # ---- REMOVE DUPLICATES ----
    df_clean.drop_duplicates(inplace=True)

    st.success("✅ Missing values handled & duplicates removed")

    # ================= CLEAN DATA PREVIEW =================
    st.markdown("### Cleaned Dataset Preview")
    st.dataframe(df_clean.head())

    # ================= EDA SECTION =================
    st.markdown("---")
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    # ---------- NUMERIC COLUMNS ----------
    numeric_cols = df_clean.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        st.markdown("### 📈 Line Chart (Numeric Trend)")
        selected_line = st.selectbox(
            "Select numeric column for line chart:",
            numeric_cols,
            key="line_col",
        )

        st.line_chart(df_clean[selected_line])

        # ---------- HISTOGRAM ----------
        st.markdown("### 📊 Histogram Distribution")
        selected_hist = st.selectbox(
            "Select column for histogram:",
            numeric_cols,
            key="hist_col",
        )

        fig, ax = plt.subplots()
        ax.hist(df_clean[selected_hist], bins=30)
        ax.set_title(f"Distribution of {selected_hist}")
        ax.set_xlabel(selected_hist)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # ---------- CORRELATION ----------
    if len(numeric_cols) >= 2:
        st.markdown("### 🔗 Correlation Heatmap")

        corr = df_clean[numeric_cols].corr()

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            linewidths=0.5,
            ax=ax,
        )
        st.pyplot(fig)

    # ================= FOOTER =================
    st.markdown("---")
    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
