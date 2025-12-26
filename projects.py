import streamlit as st
from pathlib import Path
from router import pindah_halaman


def halaman_projects():
    # ================= PATH =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets"

    # ================= DATA PROJECT =================
    projects = [
        {
            "title": "AI Churn Analysis",
            "description": "Predict customer churn using machine learning and behavioral analytics.",
            "image": "churn analysis.png",
            "page": "project1",
        },
        {
            "title": "Sales Forecasting",
            "description": "Time series forecasting to predict future product sales.",
            "image": "project2.png",
            "page": "project2",
        },
        {
            "title": "People Analytics",
            "description": "Clustering-based segmentation for Employee.",
            "image": "project3.png",
            "page": "project3",
        },
    ]

    # ================= PAGE HEADER =================
    st.markdown("## 🚀 My Projects")
    st.markdown("A collection of data science and machine learning projects.")
    st.markdown("---")

    # ================= GRID RENDER =================
    cols = st.columns(3)

    for i, project in enumerate(projects):
        with cols[i % 3]:
            img_path = ASSETS_DIR / project["image"]

            if img_path.exists():
                st.image(img_path, use_container_width=True)
            else:
                st.warning("Image not found")

            st.subheader(project["title"])
            st.caption(project["description"])

            if st.button("See More...", key=f"project_btn_{i}"):
                pindah_halaman(project["page"])

    st.markdown("---")

    # ================= BACK BUTTON =================
    if st.button("⬅ Kembali", key="back_home"):
        pindah_halaman("home")
