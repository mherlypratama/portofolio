import streamlit as st

st.set_page_config(
    page_title="Portofolio M. Herly Pratama",
    page_icon="✨",
    layout="wide",  # Bisa 'centered' atau 'wide'
    initial_sidebar_state="expanded",  # Bisa 'auto', 'expanded', 'collapsed'
)

st.subheader("Hi!")
st.header("I'm M. Herly Pratama")
st.subheader("a Data Scientist and Data Analyst")
st.sidebar.header("Filter & Navigasi")
st.sidebar.slider("Pilih nilai:", 0, 100, 50)

# Konten aplikasi lainnya
