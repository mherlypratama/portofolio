import streamlit as st
from pathlib import Path
from router import pindah_halaman


def halaman_about():
    # ================= PATH =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets"

    # ================= PAGE HEADER =================
    st.markdown("## 🚀 About Me")
    st.markdown("From Real Data to Solution")
    st.markdown("---")

    st.markdown("---")

    # ================= BACK BUTTON =================
    if st.button("⬅ Kembali", key="back_home"):
        pindah_halaman("home")
