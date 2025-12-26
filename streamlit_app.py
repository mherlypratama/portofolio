import streamlit as st
from home import halaman_home
from projects import halaman_projects

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    halaman_home()
#
elif st.session_state.page == "projects":
    halaman_projects()
