import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# FIXED: Menambahkan caching agar load data sangat cepat
@st.cache_data
def get_cleaned_data(file_path):
    df = pd.read_csv(file_path)
    df_clean = df.copy()

    # Preprocessing - FIXED: Menghilangkan FutureWarning Pandas 3.0
    num_cols = df_clean.select_dtypes(include="number").columns
    for col in num_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    cat_cols = df_clean.select_dtypes(include="object").columns
    for col in cat_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    df_clean.drop_duplicates(inplace=True)
    return df, df_clean


def halaman_project1():
    st.header("AI Churn Analysis")
    st.markdown("---")

    # Ambil data dari cache
    try:
        df_raw, df_clean = get_cleaned_data("./data/churn.csv")
    except FileNotFoundError:
        st.error("File churn.csv tidak ditemukan di folder data!")
        return

    st.markdown(
        "Project ini mendemonstrasikan analisis churn menggunakan machine learning."
    )

    # ================= RAW DATA =================
    with st.expander("📂 Lihat Dataset Mentah"):
        st.dataframe(df_raw, width="stretch")

    # ================= EDA SECTION =================
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    numeric_cols = df_clean.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        col_a, col_b = st.columns(2)

        with col_a:
            selected_line = st.selectbox(
                "Pilih Kolom Trend:", numeric_cols, key="line_col"
            )
            st.line_chart(df_clean[selected_line])

        with col_b:
            selected_hist = st.selectbox(
                "Pilih Kolom Distribusi:", numeric_cols, key="hist_col"
            )
            fig, ax = plt.subplots()
            ax.hist(df_clean[selected_hist], bins=30, color="#2563eb")
            st.pyplot(fig)

    # ================= HEATMAP =================
    st.markdown("### 🔗 Correlation Heatmap")
    if len(numeric_cols) >= 2:
        corr = df_clean[numeric_cols].corr()
        fig_corr, ax_corr = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_corr)
        st.pyplot(fig_corr)

    # ================= FOOTER =================
    st.markdown("---")
    if st.button("⬅ Back to Projects", key="back_proj"):
        pindah_halaman("projects")
