import streamlit as st
from router import pindah_halaman


def halaman_home():

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hi!")
            st.header("I'm M. Herly Pratama")
            st.subheader("a Data Scientist and Data Analyst")
        with col2:
            st.image("./assets/profile_pic.png")

    if st.button("Ke Projects"):
        pindah_halaman("projects")
