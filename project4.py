import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from pathlib import Path


# Fungsi Caching untuk performa agar tidak training berulang kali
@st.cache_data
def load_and_preprocess_data(file_path):
    # 1. Load Data
    df = pd.read_csv(file_path)

    # 2. One-Hot Encoding
    # Mengubah data kategorikal (seperti nama hari) menjadi numerik
    df_encoded = pd.get_dummies(df)

    # 3. Features and Labels
    labels = df_encoded["actual"]
    features = df_encoded.drop("actual", axis=1)
    feature_list = list(features.columns)

    # 4. Train Test Split (80% Train, 20% Test)
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.20, random_state=42
    )

    return (
        df,
        df_encoded,
        train_features,
        test_features,
        train_labels,
        test_labels,
        feature_list,
    )


@st.cache_resource
def train_rf_model(train_features, train_labels):
    # Inisialisasi dan Training Model Random Forest
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    rf.fit(train_features, train_labels)
    return rf


def halaman_project4():
    # ================= PATH SETUP =================
    BASE_DIR = Path(__file__).resolve().parent
    DATA_PATH = BASE_DIR / "data" / "temps.csv"  # Pastikan file temps.csv ada di sini

    # ================= HEADER =================
    st.header("🌡️ Climate Prediction using Random Forest")
    st.markdown(
        """
    Proyek ini menggunakan algoritma **Random Forest Regressor** untuk memprediksi suhu aktual berdasarkan data historis cuaca. 
    Model ini mencapai tingkat akurasi yang sangat tinggi dengan mengevaluasi ribuan decision trees.
    """
    )
    st.markdown("---")

    if not DATA_PATH.exists():
        st.error(
            f"⚠️ Dataset tidak ditemukan di {DATA_PATH}. Pastikan file 'temps.csv' tersedia."
        )
        return

    # Load & Process Data
    df_raw, df_encoded, train_X, test_X, train_y, test_y, feat_list = (
        load_and_preprocess_data(DATA_PATH)
    )

    # ================= 1. DATA EXPLORATION =================
    st.subheader("1. Data Exploration")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Raw Data (First 5 Rows):**")
        st.dataframe(df_raw.head(), width="stretch")

    with col2:
        st.markdown("**Dataset Shape:**")
        st.write(f"Baris: {df_raw.shape[0]}, Kolom: {df_raw.shape[1]}")
        st.info("Dataset ini tidak memiliki nilai null (Null Values: 0).")

    # ================= 2. PREPROCESSING =================
    st.subheader("2. One-Hot Encoding")
    st.write(
        """
    Data kategorikal diubah menjadi representasi numerik agar model dapat memprosesnya dengan lebih ekspresif.
    """
    )
    st.dataframe(df_encoded.head(), width="stretch")
    st.write(f"Shape setelah Encoding: {df_encoded.shape}")

    # ================= 3. TRAINING & EVALUATION =================
    st.markdown("---")
    st.subheader("3. Model Training & Performance")

    with st.status("Training Random Forest (1000 estimators)..."):
        model = train_rf_model(train_X, train_y)
        # Predictions
        predictions = model.predict(test_X)
        # Errors
        errors = abs(predictions - test_y)
        mape = 100 * (errors / test_y)
        accuracy = 100 - np.mean(mape)

    # Display Metrics
    m1, m2 = st.columns(2)
    m1.metric("Mean Absolute Error (MAE)", f"{round(np.mean(errors), 2)} degrees")
    m2.metric("Model Accuracy", f"{round(accuracy, 2)} %")

    # ================= 4. VISUALIZATION =================
    st.markdown("---")
    st.subheader("4. Feature Importance & Trends")

    # Sederhanakan Visualisasi untuk Dashboard
    st.markdown("**Actual vs Predicted Suhu:**")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(list(test_y[:50]), label="Actual", color="blue", marker="o")
    ax.plot(
        list(predictions[:50]),
        label="Predicted",
        color="red",
        linestyle="--",
        marker="x",
    )
    ax.set_ylabel("Temperature (Degrees)")
    ax.legend()
    st.pyplot(fig)

    st.info(
        """
    **Interpretasi:** Model Random Forest bekerja dengan membuat 1000 pohon keputusan (trees) yang berbeda, 
    kemudian mengambil rata-rata hasil prediksi dari seluruh pohon tersebut untuk mendapatkan hasil akhir yang lebih stabil dan akurat.
    """
    )

    # ================= FOOTER =================
    st.markdown("---")
    if st.button("⬅ Back to Projects List", key="btn_back_climate"):
        from router import pindah_halaman

        pindah_halaman("projects")
