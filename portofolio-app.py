import streamlit as st
from pathlib import Path
from PIL import Image, ImageOps


st.set_page_config(
    page_title="Portofolio - M. Herly Pratama",
    layout="wide",
)

# ===============================
# PATH GAMBAR
# ===============================
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "profile_pic.png"

# ===============================
# CSS
# ===============================
st.markdown(
    """
    <style>
    body {
        background-color: #eef2f5;
    }

    .main-container {
        background: #f9fbfd;
        border-radius: 20px;
        padding: 60px 80px;
        margin-top: 20px;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 60px;
    }

    .logo {
        font-size: 22px;
        font-weight: 700;
        color: #111;
    }

    .menu a {
        margin: 0 15px;
        text-decoration: none;
        color: #555;
        font-weight: 500;
    }

    .hero {
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        align-items: center;
        gap: 40px;
    }

    .hero h1 {
        font-size: 48px;
        line-height: 1.2;
        margin-bottom: 20px;
        color: #111;
    }

    .hero span.blue {
        color: #1f77ff;
    }

    .hero p {
        font-size: 16px;
        color: #666;
        max-width: 520px;
        margin-bottom: 30px;
    }

    .buttons {
        display: flex;
        gap: 15px;
    }

    .btn-primary {
        background: #1f77ff;
        color: white;
        padding: 12px 22px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
    }

    .btn-secondary {
        border: 1px solid #ddd;
        color: #333;
        padding: 12px 22px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
    }

    .profile-img img {
        max-width: 100%;
        border-radius: 18px;
    }

    @media (max-width: 900px) {
        .hero {
            grid-template-columns: 1fr;
            text-align: center;
        }

        .buttons {
            justify-content: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ===============================
# LAYOUT UTAMA
# ===============================
st.markdown(
    """
    <div class="main-container">
        <div class="navbar">
            <div class="logo">Portofolio</div>
            <div class="menu">
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Services</a>
                <a href="#">Projects</a>
                <a href="#">Blog</a>
            </div>
        </div>
    """,
    unsafe_allow_html=True,
)

# HERO SECTION
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown(
        """
        <h1>
            Hello 👋 <br/>
            I'm <b>M. Herly Pratama</b><br/>
            a <span class="blue">Data Scientist & Data Analyst</span>.
        </h1>

        <p>
            Hi, I'm Michele a Freelence web designer from San-Fransisco.
            I Help brands turn their ideas into high quality products
        </p>

        <div class="buttons">
            <a href="#" class="btn-primary">Book a Call</a>
            <a href="#" class="btn-secondary">Download CV</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_right:
    if IMAGE_PATH.exists():
        img = Image.open(IMAGE_PATH)

        # ROTASI MANUAL (ubah angka jika perlu)
        img = img.rotate(90, expand=True)  # coba 90
        # img = img.rotate(-90, expand=True)  # kalau kebalik
        # img = img.rotate(180, expand=True)

        img = ImageOps.fit(img, (300, 450))

        st.image(img, caption="foto profil", use_column_width=True)
    else:
        st.warning("File gambar tidak ditemukan: profil_pic.jpg")

st.markdown("</div>", unsafe_allow_html=True)
