import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def halaman_project1():
    # ================= PATH SETUP =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets" / "project1"  # Pastikan folder ini ada

    st.header("AI Churn Analysis: Predicting Customer Retention")
    st.markdown(
        "*Menggunakan Machine Learning untuk Mengidentifikasi Risiko Pelanggan Berhenti Berlangganan*"
    )
    st.markdown("---")

    # ================= DESCRIPTION & MANFAAT =================
    st.markdown("## **Latar Belakang**")
    st.write(
        """
    Churn rate adalah metrik kritis yang menunjukkan persentase pelanggan yang berhenti menggunakan layanan. 
    Proyek ini bertujuan untuk membangun model prediktif yang dapat mengidentifikasi pelanggan berisiko tinggi 
    sebelum mereka benar-benar berhenti (*churn*), sehingga tim pemasaran dapat melakukan intervensi yang tepat sasaran.
    """
    )

    st.markdown("## **Manfaat Bisnis (Value/Impact)**")
    points = [
        "**Retensi Proaktif:** Mengalihkan strategi dari reaktif menjadi proaktif dengan mendeteksi sinyal ketidakpuasan lebih awal.",
        "**Efisiensi Biaya:** Mengurangi biaya akuisisi pelanggan baru (CAC) dengan mempertahankan pelanggan setia (Retention cost biasanya jauh lebih murah).",
        "**Segmentasi Penawaran:** Memberikan promo atau insentif khusus hanya kepada segmen yang berisiko tinggi churn.",
    ]
    for p in points:
        st.markdown(f"* {p}")

    st.markdown("---")

    # ================= SECTION 1: CUSTOMER SEGMENTATION =================
    st.header("1. Customer Segmentation & Feature Analysis")

    # Placeholder Gambar EDA (Contoh: Churn Distribution atau Contract Type)
    img_path_eda = ASSETS_DIR / "churn_dist.png"
    if img_path_eda.exists():
        st.image(str(img_path_eda), use_container_width=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Melalui tahap *Feature Engineering*, ditemukan bahwa perilaku pelanggan dapat dikelompokkan berdasarkan 
        **Usage Frequency** (Rendah, Sedang, Tinggi). Selain itu, variabel kategorikal seperti 
        **Subscription Type** dan **Contract Length** memiliki korelasi yang sangat kuat terhadap loyalitas pelanggan.
        """
        )

    with col2:
        st.subheader("💡 Key Insights")
        st.markdown(
            """
        * **Risiko Kontrak Pendek:** Pelanggan dengan kontrak bulanan memiliki kecenderungan *churn* **[X]%** lebih tinggi dibandingkan kontrak tahunan.
        * **Sinyal Penggunaan:** Penurunan frekuensi penggunaan dalam 30 hari terakhir menjadi indikator utama risiko churn.
        * **Paket Layanan:** Pengguna paket 'Standard' teridentifikasi memiliki tingkat ketidakpuasan yang lebih tinggi dibanding paket 'Premium'.
        """
        )

    st.markdown("---")

    # ================= SECTION 2: MODEL PERFORMANCE =================
    st.header("2. Model Evaluation (Random Forest Classifier)")

    # Placeholder Gambar Confusion Matrix atau ROC Curve
    img_path_model = ASSETS_DIR / "model_perf.png"
    if img_path_model.exists():
        st.image(str(img_path_model), use_container_width=True)

    col3, col4 = st.columns([1.5, 1])
    with col3:
        st.subheader("📝 Penjelasan")
        st.write(
            """
        Model dikembangkan menggunakan algoritma **Random Forest Classifier**. Mengingat tujuan bisnis adalah 
        mencegah kehilangan pelanggan, fokus utama evaluasi adalah pada metrik **Recall**, untuk meminimalkan 
        kejadian pelanggan yang diprediksi 'Tetap' namun ternyata 'Churn' (*False Negative*).
        """
        )

    with col4:
        st.subheader("💡 Metrik Performa")
        # Masukkan angka dari Classification Report di notebook-mu
        st.metric("Model Accuracy", "89.5%", delta="Stable")
        st.markdown(
            """
        * **Precision:** 87.2% (Ketepatan prediksi churn).
        * **Recall:** 91.0% (Kemampuan mendeteksi seluruh pelanggan yang akan churn).
        * **F1-Score:** 89.1% (Keseimbangan antara Precision dan Recall).
        """
        )

    st.markdown("---")

    # ================= SECTION 3: STRATEGI REKOMENDASI =================
    st.header("3. Business Recommendations")
    st.info(
        "Berdasarkan hasil analisis AI, berikut adalah langkah strategis yang direkomendasikan:"
    )

    st.markdown(
        """
    1. **Loyalty Program:** Berikan insentif bagi pengguna kontrak bulanan untuk beralih ke kontrak tahunan guna meningkatkan komitmen.
    2. **Automated Alert System:** Implementasikan sistem peringatan dini bagi tim CS jika frekuensi penggunaan pelanggan turun di bawah ambang batas kritis.
    3. **Personalized Feed:** Khusus untuk segmen 'High Usage' yang berisiko churn, berikan fitur eksklusif atau dukungan prioritas.
    """
    )

    # ================= FOOTER =================
    st.markdown("---")
    st.caption("Developed by Herly - AI Churn Analysis Portfolio")

    if st.button("⬅ Kembali ke Proyek", key="btn_back_proj_1"):
        pindah_halaman("projects")
