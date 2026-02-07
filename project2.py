import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def halaman_project2():
    st.header("Sales Time Series Forecasting: Predictive Analytics for Business Growth")
    st.markdown(
        "*Transformasi Data Historis Menjadi Strategi Proyeksi Penjualan Masa Depan*"
    )
    st.markdown("---")

    # ================= DESCRIPTION =================
    st.markdown("## **Latar Belakang**")
    st.markdown(
        """
Ketidakpastian fluktuasi pasar sering kali menyebabkan masalah manajemen stok dan inefisiensi anggaran. 
Proyek ini menggunakan teknik Time Series Forecasting untuk memodelkan pola data historis, menangkap tren jangka panjang, serta musiman (seasonality) guna memprediksi volume penjualan di masa mendatang secara akurat.
"""
    )

    # ================= Manfaat =================
    st.markdown("## **Manfaat (Value/Impact)**")
    points = [
        "Optimasi Operasional: Memberikan panduan bagi tim supply chain dalam mengatur stok barang (mencegah overstock atau stockout).",
        "Perencanaan Strategis: Membantu manajemen dalam menyusun target penjualan bulanan dan tahunan berbasis data.",
        "Agregasi Multi-Level: Memungkinkan analisis dari skala harian (operasional) hingga bulanan (strategis) untuk pengambilan keputusan yang lebih relevan.",
    ]
    for p in points:
        st.write(f"* {p}")
    # ================= BACK BUTTON =================
    st.markdown("---")
    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
