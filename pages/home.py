import streamlit as st
from router import pindah_halaman


def halaman_home():
    tab1, tab2, tab3 = st.tabs(["Dashboard", "Project", "About Me"])
    with tab1:
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Hi!")
                st.header("I'm M. Herly Pratama")
                st.subheader("a Data Scientist and Data Analyst")
            with col2:
                st.image("./assets/profile_pic.png")

    with tab2:
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

    with tab3:
        st.header("About Me")
        st.checkbox("Aktifkan mode gelap")

    if st.button("Ke Projects"):
        pindah_halaman("projects")
