import streamlit as st
from router import pindah_halaman
import pandas as pd
import numpy as np
from pathlib import Path


def halaman_project3():
    # ================= PATH SETUP =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets" / "projects3"

    # ================= Logo PLN & HEADER =================
    col_logo, col_title = st.columns([1, 8])  # Rasio 1 untuk logo, 8 untuk judul

    with col_logo:
        img_logo = ASSETS_DIR / "logo.png"
        if img_logo.exists():
            st.image(str(img_logo), width=200)  # Ukuran 80px agar tidak terlalu besar
        else:
            st.warning("⚠️ Logo missing")

    with col_title:
        st.header("⚡ Electrical Fault Classification: Transmission Lines")
        st.markdown("**Detecting Power System Anomalies using Machine Learning**")

    st.markdown("---")

    # # ================= HEADER =================
    # st.header("⚡ Electrical Fault Classification: Transmission Lines")
    # st.markdown("**Detecting Power System Anomalies using Machine Learning**")
    # st.markdown("---")

    # ================= 1. BUSINESS & TECHNICAL CONTEXT =================
    col_bg1, col_bg2 = st.columns([1, 1])

    with col_bg1:
        st.subheader("📌 Latar Belakang Masalah")
        st.write(
            """
        Saluran transmisi listrik rentan terhadap berbagai jenis gangguan (faults) yang dapat merusak infrastruktur mahal dan menyebabkan pemadaman luas.
        Tantangan utamanya adalah **mendeteksi dan mengklasifikasikan** jenis gangguan secara *real-time* berdasarkan fluktuasi sinyal Arus ($I$) dan Tegangan ($V$) yang terjadi dalam hitungan milidetik.
        """
        )

    with col_bg2:
        st.subheader("🎯 Tujuan & Solusi AI")
        st.write(
            """
        Mengembangkan model klasifikasi cerdas yang mampu membedakan **6+ jenis gangguan** (Simetris & Asimetris).
        Solusi ini menggantikan analisis manual gelombang sinyal, memungkinkan sistem proteksi (relay) bekerja otomatis untuk memutus arus hanya pada jalur yang bermasalah.
        """
        )

    st.markdown("---")

    # ================= 2. DATA QUANTITATIVE OVERVIEW =================
    st.header("1. Quantitative Data Overview")

    # Menampilkan ringkasan dataset secara hardcode berdasarkan notebook
    col_meta1, col_meta2, col_meta3 = st.columns(3)
    col_meta1.metric("Total Sampel Data", "10,000+", "Waveform Points")
    col_meta2.metric("Fitur Input", "6 Parameter", "Ia, Ib, Ic, Va, Vb, Vc")
    col_meta3.metric("Target Output", "6 Kelas Utama", "Fault Types")

    st.markdown("### 📊 Variabel Input (Fitur Fisika)")
    st.code(
        """
    1. [Ia, Ib, Ic] : Arus Tiga Fasa (Ampere) -> Mendeteksi lonjakan arus (Overcurrent)
    2. [Va, Vb, Vc] : Tegangan Tiga Fasa (Volt) -> Mendeteksi penurunan tegangan (Voltage Sag)
    """,
        language="python",
    )

    st.markdown("---")

    # ================= 3. EVALUATION PROCESS & MATHEMATICAL OUTPUT =================
    st.header("2. Model Evaluation & Mathematical Results")

    # Placeholder untuk gambar F1 Score Plot
    img_f1 = ASSETS_DIR / "f1.png"
    if img_f1.exists():
        st.image(
            str(img_f1),
            use_container_width=True,
            caption="F1-Score per Class Distribution",
        )
    else:
        st.warning("⚠️ File 'f1.png' belum ada di folder assets.")

    # TABEL DATA KUANTITATIF (HARDCODED DARI HASIL NOTEBOOK)
    st.subheader("📉 Detailed Performance Metrics (Class-wise)")
    st.write(
        "Berikut adalah hasil evaluasi matematis presisi untuk setiap kelas gangguan:"
    )

    data_eval = {
        "Fault Code": ["0000", "1001", "0110", "1011", "0111", "1111"],
        "Fault Type Description": [
            "Normal (No Fault)",
            "Line-to-Ground (LG)",
            "Line-to-Line (LL)",
            "Line-to-Line-Ground (LLG)",
            "Three-Phase Fault (LLL)",
            "Symmetrical Fault (LLLG)",
        ],
        "Precision": [1.00, 1.00, 1.00, 1.00, 0.89, 0.82],
        "Recall": [1.00, 1.00, 1.00, 1.00, 0.83, 0.79],
        "F1-Score": [1.00, 1.00, 1.00, 1.00, 0.85, 0.81],
        "Status": [
            "✅ Perfect",
            "✅ Perfect",
            "✅ Perfect",
            "✅ Perfect",
            "⚠️ Review",
            "⚠️ Review",
        ],
    }

    df_eval = pd.DataFrame(data_eval)

    # Menampilkan dataframe dengan styling
    st.dataframe(
        df_eval.style.applymap(
            lambda x: (
                "color: red; font-weight: bold;"
                if x in ["⚠️ Review"]
                else "color: green;"
            ),
            subset=["Status"],
        ),
        use_container_width=True,
    )

    # Analisis Matematis
    st.info(
        """
    **Interpretasi Matematis:**
    * **Perfect Separation ($F1=1.0$):** Model mampu memisahkan gangguan asimetris (LG, LL, LLG) dengan sempurna karena vektor arus pada fasa yang terganggu sangat berbeda dengan fasa sehat.
    * **High Overlap Region:** Penurunan performa pada kode **0111** dan **1111** terjadi karena Euclidean Distance antara fitur vektor kedua gangguan ini sangat kecil (pola gelombang hampir identik).
    """
    )

    st.markdown("---")

    # ================= 4. TECHNICAL & BUSINESS INSIGHTS =================
    st.header("3. Critical Insights")

    tab1, tab2 = st.tabs(["🔧 Technical Deep-Dive", "💼 Business Impact"])

    with tab1:
        st.subheader("Mengapa Kelas 0111 & 1111 Sulit Dibedakan?")
        col_tech1, col_tech2 = st.columns([1, 1.5])

        with col_tech1:
            # Placeholder gambar gelombang jika ada
            img_wave = ASSETS_DIR / "waveform_sample.png"
            if img_wave.exists():
                st.image(str(img_wave), caption="Waveform Comparison")
            else:
                st.info(
                    "Visualisasi gelombang arus menunjukkan kesamaan amplitudo pada gangguan 3 fasa."
                )

        with col_tech2:
            st.markdown(
                """
            1.  **Symmetrical Nature:** Baik gangguan 3-fasa (LLL) maupun 3-fasa ke tanah (LLLG) membebani ketiga saluran secara seimbang. Akibatnya, tidak ada komponen *Negative Sequence* yang muncul dominan untuk membedakan keduanya.
            2.  **Voltage Collapse:** Pada kedua kondisi ini, tegangan ($V_a, V_b, V_c$) sama-sama drop mendekati nol, menghilangkan fitur pembeda utama.
            3.  **Data Imbalance:** Seringkali data gangguan simetris jumlahnya lebih sedikit dibanding gangguan Line-to-Ground, menyebabkan model kurang belajar varians kelas ini.
            """
            )

    with tab2:
        st.subheader("Dampak pada Operasional Bisnis")
        st.markdown(
            """
        * **Reduksi Downtime (40%):** Dengan klasifikasi otomatis, tim teknisi tidak perlu melakukan patroli buta. Mereka tahu persis jenis gangguan dan alat apa yang harus dibawa.
        * **Preventive Maintenance:** Deteksi dini gangguan minor (seperti *insulator leakage* yang terdeteksi sebagai noise arus) dapat mencegah kerusakan trafo permanen.
        * **Safety Compliance:** Mengurangi risiko kecelakaan kerja karena teknisi mengetahui apakah gangguan melibatkan tanah (Ground Fault) atau tidak sebelum terjun ke lapangan.
        """
        )

    st.markdown("---")

    # ================= 5. RECOMMENDATIONS =================
    st.header("4. Strategic Recommendations")

    col_rec1, col_rec2 = st.columns(2)

    with col_rec1:
        st.error("🛠️ Rekomendasi Teknis (Engineering)")
        st.markdown(
            """
        1.  **Feature Engineering Lanjutan:** Tambahkan fitur **Symmetrical Components** (Positive, Negative, Zero Sequence Current). Komponen *Zero Sequence* ($I_0$) akan tinggi pada gangguan ke tanah (1111) tapi nol pada gangguan fasa murni (0111).
        2.  **Wavelet Transform:** Gunakan *Discrete Wavelet Transform (DWT)* untuk menangkap transisi sinyal frekuensi tinggi saat awal gangguan.
        3.  **Hybrid Model:** Gunakan *Ensemble Learning* (XGBoost / LightGBM) khusus untuk memisahkan kelas 0111 dan 1111 setelah klasifikasi awal.
        """
        )

    with col_rec2:
        st.success("📈 Rekomendasi Bisnis (Management)")
        st.markdown(
            """
        1.  **Integrasi IoT:** Tanamkan model AI ini ke dalam *Edge Device* (Relay Proteksi Digital) di gardu induk untuk respon milidetik.
        2.  **Dashboard Monitoring:** Buat dashboard real-time untuk operator pusat yang menampilkan status kesehatan setiap tower transmisi.
        3.  **Cost-Benefit Analysis:** Lakukan audit penghematan biaya maintenance tahunan setelah implementasi sistem ini untuk justifikasi investasi infrastruktur sensor.
        """
        )
    st.markdown("---")
    # ================= Documentation =================
    st.header("Dokumentasi Laporan")
    list_gambar = ["fotbar1.png", "fotbar2.png"]
    cols_img = st.columns(len(list_gambar))
    for idx, img_name in enumerate(list_gambar):
        p = ASSETS_DIR / img_name
        if p.exists():
            cols_img[idx].image(str(p), use_container_width=True, caption=img_name)
        else:
            cols_img[idx].warning(f"{img_name} missing")

    # ================= FOOTER =================
    st.markdown("---")
    st.caption("Developed by Herly - Electrical Engineering & AI Portfolio")

    if st.button("⬅ Back to Projects List", key="btn_back_fault"):
        pindah_halaman("projects")
