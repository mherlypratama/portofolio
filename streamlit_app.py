import streamlit as st
from home import halaman_home
from projects import halaman_projects
from project1 import halaman_project1

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    halaman_home()
#
elif st.session_state.page == "projects":
    halaman_projects()
elif st.session_state.page == "project1":
    halaman_project1()
elif st.session_state.page == "project2":
    halaman_project2()
elif st.session_state.page == "project3":
    halaman_project3()
