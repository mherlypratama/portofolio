import streamlit as st
from router import pindah_halaman
from pathlib import Path
from PIL import Image, ImageOps


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def halaman_home():
    BASE_DIR = Path(__file__).resolve().parent
    IMAGE_PATH = BASE_DIR / "assets" / "profile_pic.png"
    CSS_PATH = BASE_DIR / "style.css"
    # ===== LOAD CSS =====
    if CSS_PATH.exists():
        local_css(CSS_PATH)

    # ===== HERO CONTENT =====
    with st.container():
        left, right = st.columns([1.2, 1])

        with left:
            st.markdown("## Hi!")
            st.markdown("# I'm M. Herly Pratama")
            st.markdown("a Data Scientist and Data Analyst")

            btn1, btn2, _ = st.columns([2, 2, 6])

            with btn1:
                if st.button("Ke Projects"):
                    pindah_halaman("projects")

            with btn2:
                if st.button("About Me"):
                    pindah_halaman("about")

        with right:
            if IMAGE_PATH.exists():
                img = Image.open(IMAGE_PATH)
                img = ImageOps.exif_transpose(img)
                img.thumbnail((580, 700))
                st.image(img)
