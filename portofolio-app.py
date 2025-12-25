import streamlit as st

st.set_page_config(
    page_title="Portofolio M. Herly Pratama",
    page_icon="✨",
    layout="wide",  # Bisa 'centered' atau 'wide'
    initial_sidebar_state="expanded",  # Bisa 'auto', 'expanded', 'collapsed'
)

tab1, tab2, tab3 = st.tabs(["Dashboard", "Prediksi", "Settings"])

with tab1:
    st.header("Dashboard Utama")
    st.write("Ini adalah tampilan ringkasan data.")

with tab2:
    st.header("Halaman Prediksi")
    st.number_input("Masukkan nilai untuk prediksi:")

with tab3:
    st.header("Pengaturan Aplikasi")
    st.checkbox("Aktifkan mode gelap")


st.subheader("Hi!")
st.header("I'm M. Herly Pratama")
st.subheader("a Data Scientist and Data Analyst")

st.sidebar.header("Filter & Navigasi")
st.sidebar.slider("Pilih nilai:", 0, 100, 50)
# Konten aplikasi lainnya
