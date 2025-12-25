import streamlit as st

# Set the title of the app
st.title("Hello Streamlit World! 👋")

# Add some plain text
st.text("This is my first simple Streamlit application.")

# Add a markdown section
st.markdown("You can use **Markdown** to format text.")

# Add an interactive button
if st.button("Send balloons!"):
    st.balloons()
    st.success("Balloons sent!")
