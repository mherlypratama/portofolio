import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

    # ================= FOOTER =================
    st.markdown("---")
    # Pastikan key unik agar tidak terjadi duplicate widget error
    if st.button("⬅ Kembali ke Proyek", key="btn_back_proj_1"):
        pindah_halaman("projects")
