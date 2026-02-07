import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from PIL import Image, ImageOps


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def halaman_project2():
    # ================= PATH =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets" / "project2"
    CSS_PATH = BASE_DIR / "style.css"

    # ===== LOAD CSS =====
    if CSS_PATH.exists():
        local_css(CSS_PATH)

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

    # --- SECTION 1: SEASONAL DECOMPOSITION ---
    st.header("1. Seasonal Decomposition Analysis")
    col1, col2 = st.columns([1.5, 1])
    img_path1 = ASSETS_DIR / "c4.jpeg"
    st.image(img_path1, use_container_width=True)

    with col1:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Visualisasi ini memisahkan data penjualan mentah menjadi empat komponen utama: **Observed** (data asli), 
        **Trend** (arah jangka panjang), **Seasonal** (pola berulang), dan **Residual** (noise/gangguan). 
        Proses dekomposisi ini sangat krusial dalam Data Science untuk memahami apakah fluktuasi penjualan 
        disebabkan oleh pertumbuhan bisnis yang organik atau sekadar pola musiman yang terjadi secara periodik.
        """
        )

    with col2:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Pola Tren:** Mengidentifikasi apakah bisnis sedang dalam fase ekspansi atau kontraksi secara jangka panjang.
        * **Kekuatan Musiman:** Menunjukkan seberapa konsisten pola kenaikan penjualan di periode tertentu.
        * **Deteksi Anomali:** Komponen *Residual* membantu mendeteksi kejadian luar biasa (seperti *outliers*) yang tidak mengikuti pola tren maupun musiman.
        """
        )

    # Simulasi penempatan gambar di bawah kontainer teks
    st.info(
        "🖼️ *Tempatkan visualisasi 'Seasonal Decomposition' (4 panel: Observed, Trend, Seasonal, Residual) di sini.*"
    )
    #

    st.markdown("---")

    # --- SECTION 2: MULTI-LEVEL TIME SERIES (DAILY, WEEKLY, MONTHLY) ---
    st.header("2. Multi-Level Granularity Analysis")
    col3, col4 = st.columns([1.5, 1])

    img_path2 = ASSETS_DIR / "c1.jpeg"
    img_path3 = ASSETS_DIR / "c2.jpeg"
    img_path4 = ASSETS_DIR / "c3.jpeg"

    st.image(img_path2, use_container_width=True)
    st.image(img_path3, use_container_width=True)
    st.image(img_path4, use_container_width=True)

    with col3:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Analisis ini membandingkan fluktuasi penjualan pada tiga tingkat agregasi: **Harian, Mingguan, dan Bulanan**. 
        Data harian seringkali sangat bergejolak (*noisy*), sementara agregasi mingguan dan bulanan membantu 
        menghaluskan variansi tersebut. Perbedaan perspektif ini memungkinkan kita untuk beralih dari pengamatan 
        operasional yang mendetail ke pengamatan strategis yang lebih luas.
        """
        )

    with col4:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Level Harian (Operational):** Efektif untuk mendeteksi *peak hours* dan pola perilaku belanja harian guna penyesuaian stok harian.
        * **Level Mingguan (Tactical):** Mengurangi *noise* harian; sangat berguna untuk mengevaluasi efektivitas kampanye promosi jangka pendek.
        * **Level Bulanan (Strategic):** Menghilangkan fluktuasi kecil untuk fokus pada performa bisnis makro, perencanaan anggaran, dan proyeksi tahunan.
        """
        )

    # Simulasi penempatan gambar di bawah kontainer teks
    st.info(
        "🖼️ *Tempatkan visualisasi perbandingan grafik garis (Daily vs Weekly vs Monthly) di sini.*"
    )
    #

    st.markdown("---")

    st.caption("Developed by Herly - Time Series Project Portfolio")
    # ================= BACK BUTTON =================
    st.markdown("---")
    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
