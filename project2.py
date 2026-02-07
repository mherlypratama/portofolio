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

    st.image(str(img_path1), use_container_width=True)
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

    with col_naive_text:
    st.subheader("📝 Penjelasan: Naive Forecast")
    img_path4 = ASSETS_DIR / "m1.png"

    st.image(str(img_path4), use_container_width=True)
    st.write(
        """
        Model Naive Forecast menetapkan prediksi masa depan berdasarkan nilai terakhir yang diamati. 
        Dalam data science, ini adalah 'reality check' yang sangat penting. Model ini membantu kita 
        memahami baseline akurasi; jika model Machine Learning yang kompleks tidak mampu memberikan 
        error yang lebih rendah dari Naive, maka kompleksitas model tersebut tidak memberikan nilai tambah.
        """
    )

    with col_naive_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
            * **Akurasi Benchmark:** Nilai **MAPE sebesar 11,90%** menunjukkan bahwa secara rata-rata, prediksi sederhana ini meleset sekitar 11% dari nilai aktual.
            * **Evaluasi Error:** Nilai **MAE (9.745,44)** memberikan gambaran bahwa rata-rata kesalahan absolut prediksi adalah sekitar 9,7 ribu unit penjualan.
            * **Sensitivitas Outlier:** Dengan **RMSE (13.234,69)** yang lebih tinggi dari MAE, terlihat adanya fluktuasi data (varians) yang cukup besar yang mempengaruhi stabilitas prediksi baseline.
            """
        )
    st.markdown("---")
    with col_hw_text:
    st.subheader("📝 Penjelasan: Holt-Winters")
    img_path5 = ASSETS_DIR / "m2.png"

    st.image(str(img_path5), use_container_width=True)
    st.write(
        """
        Holt-Winters adalah metode *Triple Exponential Smoothing* yang dirancang untuk menangkap 
        tiga komponen sekaligus: Level, Tren, dan Musiman. Model ini sangat populer dalam peramalan 
        bisnis karena sifatnya yang adaptif terhadap pola berulang (seasonality) seperti yang 
        teridentifikasi pada analisis dekomposisi sebelumnya.
        """
    )

    with col_hw_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
            * **Performa Model:** Skor **MAPE (18,62%)** ternyata lebih tinggi dibandingkan model Naive. Ini mengindikasikan bahwa pola musiman pada data validasi mungkin terlalu volatil atau tidak konsisten dengan pola historis yang dipelajari model.
            * **Magnitudo Kesalahan:** **RMSE (23.630,97)** yang cukup tinggi menunjukkan bahwa model ini mengalami kesulitan dalam menangani lonjakan data ekstrim (*peak sales*), menyebabkan simpangan yang lebar pada hasil prediksi.
            * **Kesimpulan Teknis:** Model statistik klasik ini memerlukan tuning parameter (alpha, beta, gamma) yang lebih lanjut atau data yang lebih stasioner untuk meningkatkan akurasi.
            """
        )
    st.markdown("---")
    with col_rf_text:
    st.subheader("📝 Penjelasan: Random Forest Regressor")
    img_path6 = ASSETS_DIR / "m4.png"
    img_path7 = ASSETS_DIR / "m5.png"

    st.image(str(img_path6), use_container_width=True)
    st.image(str(img_path7), use_container_width=True)
    st.write(
        """
        Random Forest merupakan algoritma *Ensemble Learning* yang bekerja dengan membangun banyak 
        pohon keputusan (*decision trees*). Dalam peramalan ini, model dilatih untuk mengenali 
        hubungan kompleks antar fitur (seperti lag penjualan atau komponen waktu) yang mungkin 
        terlewatkan oleh model statistik tradisional.
        """
    )

    with col_rf_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
            * **Akurasi Superior (Retrain):** Setelah dilakukan *retraining*, model menghasilkan **MAPE 11,29%**. Ini adalah performa terbaik dibandingkan Naive (11,90%) dan Holt-Winters (18,62%).
            * **Optimasi Signifikan:** Model awal menunjukkan MAPE 0,76% (teridentifikasi *overfitting* pada data latih), namun hasil **Retrain (MAPE 11,29%)** memberikan angka yang jauh lebih realistis dan andal untuk data masa depan (*generalization*).
            * **Presisi Prediksi:** Nilai **MAE (8.176,79)** adalah yang terendah di antara semua model, membuktikan bahwa Random Forest adalah model yang paling presisi dalam meminimalkan kesalahan absolut harian.
            * **Kesiapan Produksi:** Dengan error terendah, Random Forest dipilih sebagai model utama (*champion model*) untuk digunakan dalam sistem proyeksi penjualan perusahaan.
            """
        )
    st.markdown("---")
    st.caption("Developed by Herly - Time Series Project Portfolio")

    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")
