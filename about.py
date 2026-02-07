import streamlit as st
from pathlib import Path
from router import pindah_halaman
from PIL import Image, ImageOps


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def halaman_about():
    BASE_DIR = Path(__file__).resolve().parent
    IMAGE_PATH = BASE_DIR / "assets" / "profile_pic.png"
    CSS_PATH = BASE_DIR / "style.css"

    # ===== LOAD CSS =====
    if CSS_PATH.exists():
        local_css(CSS_PATH)

    # ================= BACK BUTTON =================
    if st.button("⬅ Home", key="back_home"):
        pindah_halaman("home")

    # ===== HERO CONTENT =====
    with st.container():
        left, right = st.columns([1.2, 1])

        with right:
            st.markdown("## Hi!")
            st.markdown("# I'm M. Herly Pratama")
            st.markdown(
                "As a data science professional with a robust background in analytics and scientific research, I specialize in transforming complex datasets into actionable insights. My expertise includes data analysis, machine learning, and data-driven decision-making, supported by certifications in Cloud Computing and Cyber Security. I am proficient in Python, R, SQL, and data visualization tools such as Tableau and Power BI. My career has spanned roles as an AI/ML Programmer and Software Developer, where I integrated predictive models and automated data processing pipelines into scalable applications."
            )

        with left:
            if IMAGE_PATH.exists():
                img = Image.open(IMAGE_PATH)
                img = ImageOps.exif_transpose(img)
                img.thumbnail((580, 700))
                st.image(img)

            # Link Button LinkedIn
            st.link_button(
                "Kunjungi LinkedIn Saya", "https://www.linkedin.com/in/mherlypratama/"
            )
