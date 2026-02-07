import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Fungsi untuk Load & Preprocessing (Hanya jalan 1x)
@st.cache_data
def get_cleaned_data(file_path):
    df = pd.read_csv(file_path)
    df_clean = df.copy()

    # Preprocessing
    num_cols = df_clean.select_dtypes(include="number").columns
    for col in num_cols:
        df_clean[col].fillna(df_clean[col].median(), inplace=True)

    cat_cols = df_clean.select_dtypes(include="object").columns
    for col in cat_cols:
        df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

    df_clean.drop_duplicates(inplace=True)
    return df, df_clean


def halaman_project1():
    st.header("AI Churn Analysis")
    st.markdown("---")

    # Ambil data dari cache
    # Data mentah dan bersih hanya diproses sekali di awal!
    df_raw, df_clean = get_cleaned_data("./data/churn.csv")

    # ... (bagian narasi Markdown kamu tetap sama) ...

    # ================= RAW DATA =================
    with st.expander("📂 Lihat Dataset Mentah"):  # Gunakan expander agar tidak penuh
        st.dataframe(df_raw)

    # ================= EDA SECTION =================
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    numeric_cols = df_clean.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        # Gunakan kolom untuk menghemat ruang dan rapi
        c1, c2 = st.columns(2)

        with c1:
            selected_line = st.selectbox("Trend Column:", numeric_cols, key="line_col")
            st.line_chart(df_clean[selected_line])

        with c2:
            selected_hist = st.selectbox(
                "Distribution Column:", numeric_cols, key="hist_col"
            )
            fig, ax = plt.subplots()
            ax.hist(
                df_clean[selected_hist], bins=30, color="#3DB6B1"
            )  # Pakai warna palette kamu
            st.pyplot(fig)

    # ---------- CORRELATION (Caching juga jika dataset sangat besar) ----------
    st.markdown("### 🔗 Correlation Heatmap")

    # Tips: Hitung korelasi hanya sekali
    corr = df_clean[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

    # ================= FOOTER =================
    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
