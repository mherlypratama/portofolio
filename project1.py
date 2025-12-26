import streamlit as st
from router import pindah_halaman


def halaman_project1():
    st.header("project1")
    if st.button("Kembali"):
        pindah_halaman("projects")
