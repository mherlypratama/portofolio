import streamlit as st
from pathlib import Path
from router import pindah_halaman


def halaman_about():
    BASE_DIR = Path(__file__).resolve().parent
    IMAGE_PATH = BASE_DIR / "assets" / "profile_pic.png"

    # ===== CSS =====
    st.markdown(
        """
    <style>
    /* container utama */
    section.main > div:first-child {
        min-height: 100vh;
        display: flex;
        align-items: center;
    }

    /* tombol */
    div[data-testid="column"] button {
        padding: 10px 22px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 15px;
    }

    .stButton > button:first-child {
        background-color: #2563eb;
        color: white;
        border: none;
    }

    .stButton > button:last-child {
        background-color: white;
        color: #2563eb;
        border: 1px solid #d1d5db;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # ===== HERO CONTENT =====
    with st.container():
        left, right = st.columns([1.2, 1])

        with right:
            st.markdown("## Hi!")
            st.markdown("# I'm M. Herly Pratama")
            st.markdown("a Data Scientist and Data Analyst")

        with left:
            if IMAGE_PATH.exists():
                img = Image.open(IMAGE_PATH)
                img = ImageOps.exif_transpose(img)
                img.thumbnail((580, 700))
                st.image(img)

    # ================= BACK BUTTON =================
    if st.button("⬅ Kembali", key="back_home"):
        pindah_halaman("home")
