import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Fungsi Caching untuk performa maksimal
@st.cache_data
def get_cleaned_data(file_path):
    df = pd.read_csv(file_path)
    df_clean = df.copy()

    # Preprocessing (Cara modern tanpa inplace=True)
    num_cols = df_clean.select_dtypes(include="number").columns
    for col in num_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    cat_cols = df_clean.select_dtypes(include="object").columns
    for col in cat_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    df_clean = df_clean.drop_duplicates()
    return df, df_clean


def halaman_project1():
    st.header("AI Churn Analysis")
    st.markdown("---")

    # Load Data
    try:
        df_raw, df_clean = get_cleaned_data("./data/churn.csv")
    except FileNotFoundError:
        st.error(
            "File 'churn.csv' tidak ditemukan. Pastikan file ada di folder './data/'."
        )
        return

    st.markdown(
        """
        Analisis churn ini membantu bisnis mengidentifikasi pelanggan yang berisiko berhenti berlangganan.
        """
    )

    # ================= RAW DATA =================
    st.subheader("📂 Raw Dataset")
    # FIXED: Mengganti use_container_width dengan width="stretch"
    st.dataframe(df_raw, width="stretch")

    # ================= CLEAN DATA PREVIEW =================
    st.subheader("⚙️ Cleaned Dataset Preview")
    # FIXED: Mengganti use_container_width dengan width="stretch"
    st.dataframe(df_clean.head(), width="stretch")

    # ================= EDA SECTION =================
    st.markdown("---")
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    numeric_cols = df_clean.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📈 Trend Chart")
            selected_line = st.selectbox(
                "Pilih kolom numerik:", numeric_cols, key="line_sel"
            )
            st.line_chart(df_clean[selected_line])

        with col2:
            st.markdown("### 📊 Distribution")
            selected_hist = st.selectbox(
                "Pilih kolom distribusi:", numeric_cols, key="hist_sel"
            )
            fig, ax = plt.subplots()
            ax.hist(
                df_clean[selected_hist], bins=30, color="#1581BF"
            )  # Menggunakan biru dari palette kamu
            st.pyplot(fig)

    # ================= CORRELATION =================
    if len(numeric_cols) >= 2:
        st.markdown("### 🔗 Correlation Heatmap")
        corr = df_clean[numeric_cols].corr()
        fig_corr, ax_corr = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_corr)
        st.pyplot(fig_corr)

    # ================= FOOTER =================
    st.markdown("---")
    # Pastikan key unik agar tidak terjadi duplicate widget error
    if st.button("⬅ Kembali ke Proyek", key="btn_back_proj_1"):
        pindah_halaman("projects")
