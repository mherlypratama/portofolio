import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from PIL import Image


def local_css(file_name):
    if Path(file_name).exists():
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def halaman_project2():
    # ================= PATH SETUP =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets" / "project2"
    CSS_PATH = BASE_DIR / "style.css"

    # ===== LOAD CSS =====
    local_css(str(CSS_PATH))

    # ================= HEADER =================
    st.header("Sales Time Series Forecasting: Predictive Analytics for Business Growth")
    st.markdown(
        "*Transformasi Data Historis Menjadi Strategi Proyeksi Penjualan Masa Depan*"
    )
    st.markdown("---")

    # ================= DESCRIPTION & MANFAAT =================
    st.markdown("## **Latar Belakang**")
    st.write(
        """
    Ketidakpastian fluktuasi pasar sering kali menyebabkan masalah manajemen stok dan inefisiensi anggaran. 
    Proyek ini menggunakan teknik Time Series Forecasting untuk memodelkan pola data historis, menangkap tren jangka panjang, 
    serta musiman (seasonality) guna memprediksi volume penjualan di masa mendatang secara akurat.
    """
    )

    st.markdown("## **Manfaat (Value/Impact)**")
    points = [
        "**Optimasi Operasional:** Memberikan panduan bagi tim supply chain dalam mengatur stok barang.",
        "**Perencanaan Strategis:** Membantu manajemen dalam menyusun target penjualan berbasis data.",
        "**Agregasi Multi-Level:** Analisis dari skala harian hingga bulanan untuk keputusan yang relevan.",
    ]
    for p in points:
        st.markdown(f"* {p}")

    st.markdown("---")

    # ================= SECTION 1: SEASONAL DECOMPOSITION =================
    st.header("1. Seasonal Decomposition Analysis")

    img_path1 = ASSETS_DIR / "c4.png"
    if img_path1.exists():
        st.image(
            str(img_path1),
            use_container_width=True,
            caption="Dekomposisi Multiplikatif",
        )
    else:
        st.error(f"File tidak ditemukan: {img_path1.name}")

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Visualisasi ini menggunakan model **Multiplicative Decomposition** untuk membedah data penjualan harian menjadi empat komponen utama. 
        Penggunaan model multiplikatif sangat tepat karena menunjukkan bahwa variasi musiman berubah sebanding dengan level tren penjualan. 
        Dengan memisahkan Trend dari Seasonal dan Residual, kita dapat memahami apakah lonjakan penjualan disebabkan oleh pertumbuhan organik bisnis 
        atau sekadar siklus mingguan yang berulang.
        """
        )

    with col2:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Pertumbuhan Eksponensial**: Tren penjualan menunjukkan performa luar biasa dengan pertumbuhan sebesar **113,90%**.
        * **Stabilitas Penjualan**: Rata-rata dasar penjualan (baseline) berada di angka **94.370,19**.
        * **Pola Musiman Presisi**: Rentang indeks musiman sebesar **0,0355** menunjukkan fluktuasi mingguan yang sangat konsisten.
        * **Kualitas Model**: Nilai residual yang rendah (**0,0934**) mengindikasikan noise yang sangat minim.
        """
        )

    st.markdown("---")

    # ================= SECTION 2: MULTI-LEVEL GRANULARITY =================
    st.header("2. Multi-Level Granularity Analysis")

    list_gambar = ["c1.jpeg", "c2.jpeg", "c3.png"]
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
        Analisis ini membedah performa penjualan melalui tiga tingkat granulasi waktu: **Harian, Mingguan, dan Bulanan**. 
        Tinjauan harian digunakan untuk melihat volatilitas harian, sedangkan analisis mingguan membantu mengidentifikasi hari dengan trafik tertinggi. 
        Tinjauan bulanan menangkap pola musiman jangka panjang untuk perencanaan strategis tahunan.
        """
        )

    with col4:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Puncak Harian:** Penjualan tertinggi mencapai **166.577,69** pada Des 2019.
        * **Dominasi Selasa:** Performa tertinggi rata-rata terjadi pada hari **Selasa (95.967,46)**.
        * **Siklus Bulanan:** Desember adalah periode puncak dengan rata-rata **148.654,70**.
        * **Low-Season:** Januari dan September teridentifikasi sebagai periode dengan volume terendah.
        """
        )

    st.markdown("---")

    # ================= SECTION 3: MODEL EVALUATION =================
    st.header("3. Model Performance & Evaluation")

    # --- NAIVE FORECAST ---
    col_naive_text, col_naive_insight = st.columns([1.5, 1])
    with col_naive_text:
        st.subheader("📝 Penjelasan: Naive Forecast")
        img_path_m1 = ASSETS_DIR / "m1.png"
        if img_path_m1.exists():
            st.image(str(img_path_m1), use_container_width=True)
        st.write(
            """
        Model Naive Forecast menetapkan prediksi masa depan berdasarkan nilai terakhir yang diamati. 
        Ini digunakan sebagai **benchmark**; jika model ML yang kompleks tidak lebih baik dari Naive, 
        maka model tersebut tidak efisien.
        """
        )

    with col_naive_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **MAPE 11,90%:** Prediksi meleset rata-rata 11% dari nilai aktual.
        * **MAE 9.745,44:** Kesalahan absolut rata-rata sekitar 9,7 ribu unit.
        * **RMSE 13.234,69:** Menunjukkan sensitivitas terhadap varians data yang cukup besar.
        """
        )

    st.markdown("---")

    # --- HOLT-WINTERS ---
    col_hw_text, col_hw_insight = st.columns([1.5, 1])
    with col_hw_text:
        st.subheader("📝 Penjelasan: Holt-Winters")
        img_path_m2 = ASSETS_DIR / "m2.png"
        if img_path_m2.exists():
            st.image(str(img_path_m2), use_container_width=True)
        st.write(
            """
        Metode *Triple Exponential Smoothing* yang menangkap Level, Tren, dan Musiman. 
        Sangat populer karena adaptif terhadap pola berulang (*seasonality*).
        """
        )

    with col_hw_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **MAPE 18,62%:** Performa lebih rendah dari Naive pada data ini.
        * **RMSE 23.630,97:** Kesalahan yang tinggi menunjukkan kesulitan menangani lonjakan data ekstrim (*peak sales*).
        * **Evaluasi:** Memerlukan tuning parameter lebih lanjut untuk meningkatkan akurasi.
        """
        )

    st.markdown("---")
    # ================= SECTION: RANDOM FOREST INITIAL =================

    col_rf_init_text, col_rf_init_insight = st.columns([1.5, 1])

    with col_rf_init_text:
        st.subheader("📝 Penjelasan: Random Forest Regressor")
        # Sesuaikan nama file image jika ada (contoh: m3.png)
        img_path_m3 = ASSETS_DIR / "m4.png"
        if img_path_m3.exists():
            st.image(
                str(img_path_m3),
                use_container_width=True,
                caption="Initial Random Forest Fit",
            )

        st.write(
            """
            Random Forest adalah algoritma *ensemble learning* yang bekerja dengan menggabungkan hasil dari banyak 
            pohon keputusan (*decision trees*). Pada tahap awal ini, model dilatih untuk memetakan hubungan 
            non-linear antara fitur waktu (hari, bulan, tahun) dan variabel target. Hasil evaluasi pada 
            set ini menunjukkan kemampuan model dalam melakukan 'fitting' yang sangat rapat terhadap 
            pola data historis yang diberikan.
            """
        )

    with col_rf_init_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
            * **Akurasi Luar Biasa (High Precision):** Skor **MAPE 0,76%** mengindikasikan bahwa rata-rata kesalahan prediksi kurang dari 1%. Ini menunjukkan model mampu menangkap hampir seluruh varians dalam data.
            * **Kesalahan Absolut Minimal:** Dengan **MAE (654,23)**, rata-rata selisih antara prediksi dan kenyataan hanya sekitar 654 unit, angka yang sangat kecil dibandingkan rata-rata penjualan harian (~94rb).
            * **Stabilitas Error:** Nilai **RMSE (1.108,33)** yang tidak terpaut jauh dari MAE menunjukkan bahwa model ini tidak menghasilkan kesalahan ekstrem (*large outliers*) pada fase pengujian ini.
            * **Analisis Teknis:** Performa yang sangat tinggi ini menjadi fondasi bagi proses *retraining* untuk memastikan model tetap memiliki generalisasi yang baik saat menghadapi data masa depan yang belum pernah dilihat sebelumnya.
            """
        )
    st.markdown("---")

    # --- RANDOM FOREST ---
    col_rf_text, col_rf_insight = st.columns([1.5, 1])
    with col_rf_text:
        st.subheader("📝 Penjelasan: Re-Train Random Forest Regressor")
        img_path_m4 = ASSETS_DIR / "m5.png"
        if img_path_m4.exists():
            st.image(str(img_path_m4), use_container_width=True)

        st.write(
            """
        Algoritma *Ensemble Learning* yang menangkap hubungan non-linear kompleks. 
        Model ini dilatih menggunakan fitur waktu dan lag penjualan.
        """
        )

    with col_rf_insight:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **MAPE 11,29% (Best):** Model terbaik setelah proses *retraining*.
        * **MAE 8.176,80:** Kesalahan absolut paling minimum dibanding model lain.
        * **Champion Model:** Dipilih sebagai model utama untuk sistem produksi karena akurasi generalisasi yang stabil.
        """
        )

    # ================= FOOTER & NAVIGATION =================
    st.markdown("---")
    st.caption("Developed by Herly - Time Series Project Portfolio")

    if st.button("⬅ Back to Projects"):
        pindah_halaman("projects")


# Jalankan fungsi jika file dipanggil langsung
if __name__ == "__main__":
    halaman_project2()
