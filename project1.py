import streamlit as st
from router import pindah_halaman
import pandas as pd


def halaman_project1():
    st.header("AI Churn Analysis")
    st.markdown("---")

    st.markdown(
        """
    Customer churn analysis is a predictive analytics technique that identifies customers who are likely to stop doing business with a company. Churn rate refers to the percentage of customers who discontinue a service or product over a certain period. This analysis uses historical customer data, such as purchase behavior, interactions with the company, and demographic characteristics, to detect patterns and factors influencing churn decisions. Machine learning algorithms predict which customers are likely to churn soon. The goal is to help companies identify high-risk customers and take proactive retention strategies, improving customer loyalty, reducing acquisition costs, and boosting revenue.

    Examples include:
    - Identifying at-risk customers and sending targeted offers
    - Optimizing marketing strategies for retention
    - Addressing factors driving churn

    By leveraging churn analysis, companies make data-driven decisions to enhance customer retention and revenue growth.
    """
    )

    st.markdown("---")
    if st.button("Kembali"):
        pindah_halaman("projects")
