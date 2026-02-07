import streamlit as st
from pathlib import Path
from router import pindah_halaman

# Impor data dari file baru
from data_projects import LIST_PROJECTS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def halaman_projects():
    # ================= PATH =================
    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets"
    CSS_PATH = BASE_DIR / "style.css"

    # ===== LOAD CSS =====
    if CSS_PATH.exists():
        local_css(CSS_PATH)

    # ================= PAGE HEADER =================
    st.markdown("## 🚀 My Projects")
    st.markdown("A collection of data science and machine learning projects.")
    st.markdown("---")

    # ================= GRID RENDER (3 Kolom) =================
    # Kita bagi data menjadi baris-baris yang berisi maksimal 3 item
    n_cols = 3

    # Loop untuk membuat baris (rows)
    for i in range(0, len(LIST_PROJECTS), n_cols):
        cols = st.columns(n_cols)

        # Ambil potongan list sebanyak 3 project
        batch_projects = LIST_PROJECTS[i : i + n_cols]

        for j, project in enumerate(batch_projects):
            with cols[j]:
                img_path = ASSETS_DIR / project["image"]

                if img_path.exists():
                    st.image(img_path, use_container_width=True)
                else:
                    # Placeholder jika gambar tidak ada
                    st.info(f"🖼️ {project['title']}")

                st.subheader(project["title"])
                st.caption(project["description"])

                # Key tombol harus unik, gabungkan indeks i dan j
                if st.button("See More...", key=f"btn_{i}_{j}"):
                    pindah_halaman(project["page"])

    st.markdown("---")

    # ================= BACK BUTTON =================
    if st.button("⬅ Kembali", key="back_home"):
        pindah_halaman("home")
