import streamlit as st

st.set_page_config(
    page_title="Portofolio M. Herly Pratama",
    page_icon="✨",
    layout="wide",  # Bisa 'centered' atau 'wide'
    initial_sidebar_state="expanded",  # Bisa 'auto', 'expanded', 'collapsed'
)

tab1, tab2, tab3 = st.tabs(["Dashboard", "Project", "About Me"])

with tab1:
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hi!")
            st.header("I'm M. Herly Pratama")
            st.subheader("a Data Scientist and Data Analyst")
        with col2:
            st.image("profile_pic.png")

with tab2:
    st.header("My Project")
    with st.container():
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("churn analysis.png")
            st.subheader("AI Churn Analysis")
            st.markdown(
                "AI Churn Analysis is a predictive analytics technique that uses machine learning algorithms to identify customers who are likely to stop doing business with a company, also known as customer churn. By analyzing historical data and behavior patterns, AI models can detect early warning signs of churn, such as changes in usage, engagement, or payment behavior. This enables businesses to proactively intervene with targeted retention strategies, such as personalized offers or support, to reduce churn rates and improve customer loyalty."
            )
            


with tab3:
    st.header("About Me")
    st.checkbox("Aktifkan mode gelap")


# Konten aplikasi lainnya
