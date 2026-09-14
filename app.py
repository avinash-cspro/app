import streamlit as st

st.set_page_config(
    page_title="Car Purchace Prediction",
    page_icon="🤖",
    layout="wide"
)

pages = {
    "Main": [
        st.Page("home.py", title="Home", icon="🏠"),
        st.Page("analysis.py", title="Data Analysis", icon="📊"),
        st.Page("model.py", title="Prediction", icon="🔮")]}

pg = st.navigation(pages)

pg.run()
