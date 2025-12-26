import streamlit as st
from router import pindah_halaman
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def halaman_project3():
    st.header("People Analytics")
    st.markdown("---")

    # ================= LOAD DATA =================
    df = pd.read_csv("./data/employee.csv")
