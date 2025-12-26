import streamlit as st
from router import pindah_halaman


def halaman_projects():
    st.header("My Project")
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        deskripsi = "AI Churn Analysis is a predictive analytics technique that uses machine learning algorithms to identify customers who are likely to stop doing business with a company, also known as customer churn. By analyzing historical data and behavior patterns, AI models can detect early warning signs of churn, such as changes in usage, engagement, or payment behavior. This enables businesses to proactively intervene with targeted retention strategies, such as personalized offers or support, to reduce churn rates and improve customer loyalty."
        with col1:
            st.image("./assets/churn analysis.png")
            st.subheader("AI Churn Analysis")
            with st.expander("Show More..."):
                st.write(
                    "AI Churn Analysis is a predictive analytics technique that uses machine learning algorithms to identify customers who are likely to stop doing business with a company, also known as customer churn. By analyzing historical data and behavior patterns, AI models can detect early warning signs of churn, such as changes in usage, engagement, or payment behavior. This enables businesses to proactively intervene with targeted retention strategies, such as personalized offers or support, to reduce churn rates and improve customer loyalty."
                )
        with col2:
            st.image("./assets/churn analysis.png")
            st.subheader("AI Churn Analysis")
            st.markdown(
                "AI Churn Analysis is a predictive analytics technique that uses machine learning algorithms to identify customers who are likely to stop doing business with a company, also known as customer churn. By analyzing historical data and behavior patterns, AI models can detect early warning signs of churn, such as changes in usage, engagement, or payment behavior. This enables businesses to proactively intervene with targeted retention strategies, such as personalized offers or support, to reduce churn rates and improve customer loyalty."
            )
        with col3:
            st.image("./assets/churn analysis.png")
            st.subheader("AI Churn Analysis")
            st.markdown(
                "AI Churn Analysis is a predictive analytics technique that uses machine learning algorithms to identify customers who are likely to stop doing business with a company, also known as customer churn. By analyzing historical data and behavior patterns, AI models can detect early warning signs of churn, such as changes in usage, engagement, or payment behavior. This enables businesses to proactively intervene with targeted retention strategies, such as personalized offers or support, to reduce churn rates and improve customer loyalty."
            )

    if st.button("Kembali"):
        pindah_halaman("home")
