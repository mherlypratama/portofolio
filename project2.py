import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from PIL import Image


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def halaman_project2():
    # ================= PATH =================
    # Menggunakan .parent dengan hati-hati tergantung struktur folder Anda
    BASE_DIR = Path(__file__).resolve().parent
    # Pastikan folder adalah: assets/project2/ (case-sensitive di Linux/Streamlit Cloud)
    ASSETS_DIR = BASE_DIR / "assets" / "project2"
    CSS_PATH = BASE_DIR / "style.css"

    # ===== LOAD CSS =====
    if CSS_PATH.exists():
        local_css(str(CSS_PATH))

    st.header("Sales Time Series Forecasting: Predictive Analytics for Business Growth")
    st.markdown(
        "*Transformasi Data Historis Menjadi Strategi Proyeksi Penjualan Masa Depan*"
    )
    st.markdown("---")

    # ================= DESCRIPTION =================
    st.markdown("## **Latar Belakang**")
    st.write(
        """
    Ketidakpastian fluktuasi pasar sering kali menyebabkan masalah manajemen stok dan inefisiensi anggaran. 
    Proyek ini menggunakan teknik Time Series Forecasting untuk memodelkan pola data historis, menangkap tren jangka panjang, 
    serta musiman (seasonality) guna memprediksi volume penjualan di masa mendatang secara akurat.
    """
    )

    # ================= Manfaat =================
    st.markdown("## **Manfaat (Value/Impact)**")
    points = [
        "**Optimasi Operasional:** Memberikan panduan bagi tim supply chain dalam mengatur stok barang.",
        "**Perencanaan Strategis:** Membantu manajemen dalam menyusun target penjualan berbasis data.",
        "**Agregasi Multi-Level:** Analisis dari skala harian hingga bulanan untuk keputusan yang relevan.",
    ]
    for p in points:
        st.markdown(f"* {p}")

    st.markdown("---")

    # --- SECTION 1: SEASONAL DECOMPOSITION ---
    st.header("1. Seasonal Decomposition Analysis")

    img_path1 = ASSETS_DIR / "c4.png"

    # PERBAIKAN: Cek keberadaan file dan konversi ke string
    if img_path1.exists():
        st.image(str(img_path1), use_container_width=True)
    else:
        st.error(f"File tidak ditemukan: {img_path1.name} di folder assets/project2/")

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Visualisasi ini memisahkan data penjualan mentah menjadi empat komponen utama: **Observed**, 
        **Trend**, **Seasonal**, dan **Residual**. Memahami apakah fluktuasi disebabkan oleh pertumbuhan 
        organik atau sekadar pola musiman.
        """
        )

    with col2:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Pola Tren:** Arah bisnis jangka panjang.
        * **Kekuatan Musiman:** Konsistensi kenaikan di periode tertentu.
        * **Deteksi Anomali:** *Residual* membantu melihat pencilan (*outliers*).
        """
        )

    st.markdown("---")

    # --- SECTION 2: MULTI-LEVEL TIME SERIES ---
    st.header("2. Multi-Level Granularity Analysis")

    # List gambar untuk looping agar kode lebih bersih
    list_gambar = ["c1.jpeg", "c2.jpeg", "c3.png"]

    # Container untuk gambar agar rapi
    cols_img = st.columns(len(list_gambar))
    for idx, img_name in enumerate(list_gambar):
        p = ASSETS_DIR / img_name
        if p.exists():
            cols_img[idx].image(str(p), use_container_width=True, caption=img_name)
        else:
            cols_img[idx].warning(f"{img_name} missing")

    col3, col4 = st.columns([1.5, 1])
    with col3:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Perbandingan agregasi: **Harian, Mingguan, dan Bulanan**. 
        Membantu menghaluskan *noise* data harian untuk melihat pandangan strategis yang lebih luas.
        """
        )

    with col4:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Daily:** Deteksi *peak hours* operasional.
        * **Weekly:** Evaluasi taktis promosi mingguan.
        * **Monthly:** Fokus pada performa bisnis makro dan budget.
        """
        )

    st.markdown("---")
    st.caption("Developed by Herly - Time Series Project Portfolio")

    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
