import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def halaman_project1():
    st.header("AI Churn Analysis")
    st.markdown("---")

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
