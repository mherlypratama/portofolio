import streamlit as st


def pindah_halaman(nama):
    st.session_state["page"] = nama
