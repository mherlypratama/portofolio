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
        **Penjelasan** Visualisasi ini menggunakan model Multiplicative Decomposition untuk 
        membedah data penjualan harian menjadi empat komponen utama. Penggunaan model multiplikatif 
        sangat tepat karena menunjukkan bahwa variasi musiman berubah sebanding dengan level tren penjualan. 
        Dengan memisahkan Trend dari Seasonal dan Residual, kita dapat memahami apakah lonjakan penjualan disebabkan
         oleh pertumbuhan organik bisnis atau sekadar siklus mingguan yang berulang.
        """
        )

    with col2:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Pertumbuhan Eksponensial**: Tren penjualan menunjukkan performa luar biasa dengan pertumbuhan sebesar 113,90% dari awal hingga akhir periode, menandakan ekspansi pasar yang sangat sehat.

        * **Stabilitas Penjualan**: Rata-rata dasar penjualan (baseline) berada di angka 94.370,19, memberikan angka patokan yang kuat untuk perencanaan inventaris.

        * **Pola Musiman Presisi**: Rentang indeks musiman sebesar 0,0355 menunjukkan fluktuasi mingguan yang sangat konsisten dan terukur, memungkinkan prediksi jangka pendek yang lebih akurat.

        * **Kualitas Model**: Nilai standar deviasi residual yang rendah (0,0934) mengindikasikan bahwa sebagian besar volatilitas data berhasil ditangkap oleh pola tren dan musiman, menyisakan sangat sedikit noise yang tidak terjelaskan.
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
            cols_img[idx].image(str(p), use_container_width=True)
        else:
            cols_img[idx].warning(f"{img_name} missing")

    col3, col4 = st.columns([1.5, 1])
    with col3:
            st.subheader("📝 Penjelasan")
            st.write(
                """
                Analisis ini membedah performa penjualan melalui tiga tingkat granulasi waktu: **Harian, Mingguan, dan Bulanan**. 
                Tinjauan harian digunakan untuk melihat volatilitas dan titik ekstrem operasional, sedangkan analisis 
                mingguan membantu mengidentifikasi hari dengan trafik tertinggi untuk optimasi staf. Terakhir, 
                tinjauan bulanan menangkap pola musiman (*seasonality*) jangka panjang yang krusial bagi 
                perencanaan stok inventaris dan strategi kampanye pemasaran tahunan.
                """
            )

        with col4:
            st.subheader("💡 Key Insights")
            st.markdown(
                """
                * **Puncak Operasional Harian:** Penjualan mencapai titik tertinggi sebesar **166.577,69** pada 4 Desember 2019. Namun, nilai standar deviasi yang tinggi (**26.068,96**) menunjukkan adanya volatilitas yang signifikan dalam aktivitas harian.
                * **Dominasi Hari Kerja:** Berbeda dengan retail fisik pada umumnya, performa tertinggi justru terjadi pada hari **Selasa (Rata-rata: 95.967,46)**, diikuti oleh hari Minggu. Ini menandakan pola belanja pelanggan yang aktif di awal pekan.
                * **Lonjakan Akhir Tahun:** Bulan **Desember** adalah periode paling produktif dengan rata-rata penjualan **148.654,70**, hampir tiga kali lipat dibandingkan bulan Januari. Terlihat tren kenaikan yang konsisten di kuartal keempat (Oktober–Desember).
                * **Identifikasi Low-Season:** Bulan Januari dan September tercatat sebagai periode terendah. Hal ini memberikan peluang bagi manajemen untuk melakukan kampanye diskon khusus atau perawatan infrastruktur pada periode tersebut.
                """
            )

    st.markdown("---")
    st.caption("Developed by Herly - Time Series Project Portfolio")

    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
