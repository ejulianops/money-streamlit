import streamlit as st
from utils.database import init_db

# Initialize database
init_db()

# App config
st.set_page_config(
    page_title="Personal Money Tracker",
    page_icon="💰",
    layout="wide"
)

# Main header
st.title("💰 Personal Money Tracker")
st.markdown("Track your income and expenses in one place")

# Page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Add Transaction"])

# Display the selected page
if page == "Dashboard":
    from pages import 1_📊_Dashboard
    st.experimental_rerun()
elif page == "Add Transaction":
    from pages import 2_➕_Add_Transaction
    st.experimental_rerun()