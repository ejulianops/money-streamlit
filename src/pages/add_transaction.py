import streamlit as st
from datetime import datetime
from utils.database import add_transaction

def show():
    st.title("➕ Add Transaction")
    
    with st.form("transaction_form"):
        trans_type = st.radio("Type", ["Income", "Expense"])
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
        category = st.selectbox(
            "Category",
            ["Salary", "Freelance", "Investments"] if trans_type == "Income" 
            else ["Food", "Transport", "Housing", "Entertainment", "Other"]
        )
        description = st.text_input("Description (optional)")
        date = st.date_input("Date", datetime.now())
        
        submitted = st.form_submit_button("Add Transaction")
        
        if submitted:
            add_transaction(
                amount if trans_type == "Income" else -amount,
                category,
                description,
                trans_type.lower(),
                date.strftime('%Y-%m-%d')
            )
            st.success("Transaction added successfully!")