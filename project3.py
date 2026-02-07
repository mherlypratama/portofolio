import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def halaman_project3():
    # ================= PATH SETUP =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets" / "project3"  # Sesuaikan folder assets

    st.header("Electrical Fault Classification in Transmission Lines")
    st.markdown(
        "*Otomasi Deteksi dan Klasifikasi Gangguan Listrik menggunakan Machine Learning*"
    )
    st.markdown("---")

    # ================= DESCRIPTION =================
    st.markdown("## **Latar Belakang**")
    st.write(
        """
    Saluran transmisi adalah tulang punggung distribusi energi listrik. Gangguan (fault) pada saluran ini dapat menyebabkan kerusakan infrastruktur yang mahal dan pemadaman luas. 
    Proyek ini bertujuan untuk mengklasifikasikan jenis gangguan listrik secara otomatis berdasarkan data arus dan tegangan, guna mempercepat waktu respons perbaikan sistem proteksi.
    """
    )

    # ================= TECHNICAL SCOPE =================
    st.markdown("## **Cakupan Teknis**")
    points = [
        "**Multi-Class Classification:** Mengidentifikasi berbagai jenis gangguan (Line-to-Line, Line-to-Ground, Three-Phase Fault, dll).",
        "**Monitoring Parameter:** Menganalisis perubahan besaran arus dan tegangan pada tiga fasa saat terjadi gangguan.",
        "**Keandalan Sistem:** Memastikan model memiliki akurasi tinggi pada kelas gangguan yang paling kritis.",
    ]
    for p in points:
        st.markdown(f"* {p}")

    st.markdown("---")

    # ================= SECTION 1: PERFORMANCE ANALYSIS =================
    st.header("1. Model Evaluation: Class-wise Performance")

    # Gambar F1-Score dari Notebook (misal: f1_plot.png)
    img_path_f1 = ASSETS_DIR / "f1_score_plot.png"
    if img_path_f1.exists():
        st.image(
            str(img_path_f1),
            use_container_width=True,
            caption="Perbandingan F1-Score per Kelas Gangguan",
        )

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Evaluasi model difokuskan pada **F1-Score** karena dataset klasifikasi gangguan seringkali memiliki sebaran kelas yang unik. 
        Analisis ini menunjukkan sejauh mana model mampu membedakan antara gangguan simetris dan asimetris dengan presisi yang stabil di hampir semua kategori.
        """
        )

    with col2:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Performa Tinggi:** Mayoritas kelas gangguan berhasil diklasifikasikan dengan F1-score yang sangat baik.
        * **Kecualian Kritis:** Terdapat dua kelas (misalnya fasa 0111 dan 1111) yang menunjukkan skor sedikit lebih rendah, menandakan adanya kemiripan fitur arus antara gangguan fasa-ke-fasa tertentu.
        * **Stabilitas Model:** Model menunjukkan ketahanan dalam menangani data input yang bervariasi pada kondisi beban yang berbeda.
        """
        )

    st.markdown("---")

    # ================= SECTION 2: FAULT TYPE INFERENCES =================
    st.header("2. Deep Dive: Fault Inferences")

    col3, col4 = st.columns([1, 1.5])

    with col3:
        st.subheader("🛠️ Jenis Gangguan")
        st.markdown(
            """
        * **0111:** Fault antara tiga fasa (*Three-phase fault*).
        * **1111:** Gangguan simetris sempurna pada seluruh fasa.
        * **L-G / L-L:** Gangguan fasa ke tanah atau fasa ke fasa lainnya.
        """
        )

    with col4:
        st.subheader("📈 Analisis Inferensi")
        st.info(
            """
        Berdasarkan hasil pemodelan, kelas dengan akurasi terendah biasanya disebabkan oleh transisi sinyal yang sangat cepat saat gangguan terjadi. 
        Rekomendasi teknis adalah dengan menambahkan fitur *lagging* atau transformasi gelombang (Wavelet) untuk memperjelas batas antar kelas gangguan.
        """
        )

    # ================= FOOTER & NAVIGATION =================
    st.markdown("---")
    st.caption("Developed by Herly - Electrical Engineering & AI Portfolio")

    if st.button("⬅ Kembali ke Proyek", key="btn_back_proj_3"):
        pindah_halaman("projects")
