import streamlit as st
from app import pindah_halaman


def halaman_1():
    st.title("Halaman Lain")
    if st.button("Kembali ke Home"):
        pindah_halaman("home")
