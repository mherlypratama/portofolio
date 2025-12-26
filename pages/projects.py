import streamlit as st
from router import pindah_halaman


def halaman_projects():
    st.title("Projects")

    if st.button("Kembali"):
        pindah_halaman("home")
