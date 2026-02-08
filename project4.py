import streamlit as st
from pathlib import Path
from router import pindah_halaman


def halaman_project4():
    # ================= PATH SETUP =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets" / "project4"

    # ================= Logo  & HEADER =================
    col_logo, col_title = st.columns([1, 8])  # Rasio 1 untuk logo, 8 untuk judul

    with col_logo:
        img_logo = ASSETS_DIR / "logo.png"
        if img_logo.exists():
            st.image(str(img_logo), width=200)  # Ukuran 80px agar tidak terlalu besar
        else:
            st.warning("⚠️ Logo missing")

    with col_title:
        st.header("🌡️ Climate Prediction: Random Forest Analysis")
        st.markdown(
            """
        **Project Overview:** Prediksi suhu maksimum harian menggunakan algoritma *Ensemble Learning* (Random Forest). 
        Project ini berfokus pada evaluasi performa model regresi non-linear terhadap data cuaca historis.
        """
        )

    st.markdown("---")

    # ================= 1. MODEL PERFORMANCE (KEY METRICS) =================
    st.subheader("1. Quantitative Results")
    st.write(
        "Berdasarkan hasil testing pada dataset (20% Test Split), diperoleh performa berikut:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Model Accuracy", value="93.99%", delta="High Precision")

    with col2:
        st.metric(
            label="Mean Absolute Error (MAE)",
            value="3.83°",
            delta="- Low Error",
            delta_color="inverse",
        )

    with col3:
        st.metric(
            label="n_Estimators (Trees)",
            value="1,000",
            help="Jumlah pohon keputusan dalam hutan acak.",
        )

    st.info(
        """
    **Interpretasi:** Rata-rata kesalahan prediksi model hanya menyimpang **3.83 derajat** dari suhu aktual. 
    Dengan akurasi **~94%**, model ini sangat andal untuk peramalan cuaca jangka pendek.
    """
    )

    # ================= 2. METHODOLOGY & DATA STRUCTURE =================
    st.markdown("---")
    st.subheader("2. Methodology & Data Structure")

    tab1, tab2 = st.tabs(["🛠️ Data Processing", "🌲 Model Architecture"])

    with tab1:
        st.markdown("### Feature Engineering")
        st.write(
            """
        Tantangan utama dalam data cuaca adalah adanya variabel kategorikal (seperti nama hari: 'Senin', 'Selasa'). 
        Notebook ini menerapkan teknik **One-Hot Encoding** untuk mengubahnya menjadi format numerik matriks.
        """
        )

        # Hardcoded data shape from notebook output (Cell 10 & 16)
        data_structure = {
            "Metric": [
                "Original Data Shape",
                "After One-Hot Encoding",
                "Training Data (80%)",
                "Testing Data (20%)",
            ],
            "Dimensions": ["(348, 9)", "(348, 17)", "(278, 17)", "(70, 17)"],
        }
        st.table(data_structure)
        st.caption(
            "Penambahan kolom dari 9 ke 17 terjadi akibat ekspansi fitur One-Hot Encoding."
        )

    with tab2:
        st.markdown("### Random Forest Configuration")
        st.write(
            """
        Model dibangun menggunakan library `scikit-learn` dengan konfigurasi hyperparameter berikut:
        """
        )
        st.code(
            """
        rf = RandomForestRegressor(
            n_estimators = 1000, 
            random_state = 42
        )
        """,
            language="python",
        )

        st.markdown(
            """
        **Kenapa 1000 Trees?**
        Penggunaan 1000 *estimators* memastikan model tidak *overfitting* pada satu pola data tertentu. 
        Setiap pohon memprediksi nilai secara independen, dan hasil akhirnya adalah rata-rata dari seluruh pohon tersebut.
        """
        )

    st.markdown("---")
    # ================= Documentation =================
    st.header("Dokumentasi Laporan")
    list_gambar = ["doc1.png", "doc2.png"]
    cols_img = st.columns(len(list_gambar))
    for idx, img_name in enumerate(list_gambar):
        p = ASSETS_DIR / img_name
        if p.exists():
            cols_img[idx].image(str(p), use_container_width=True, caption=img_name)
        else:
            cols_img[idx].warning(f"{img_name} missing")

    # ================= FOOTER =================
    st.markdown("---")
    if st.button("⬅ Kembali ke Daftar Project", key="back_climate_static"):
        pindah_halaman("projects")
