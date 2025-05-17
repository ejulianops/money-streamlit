import streamlit as st
import plotly.express as px
from utils.database import get_all_transactions, get_balance

def show():
    st.title("📊 Dashboard")
    
    # Get data
    transactions = get_all_transactions()
    balance = get_balance()
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Balance", f"${balance:,.2f}")
    
    if not transactions.empty:
        income = transactions[transactions['type'] == 'income']['amount'].sum()
        expenses = transactions[transactions['type'] == 'expense']['amount'].sum()
        col2.metric("Total Income", f"${income:,.2f}")
        col3.metric("Total Expenses", f"${expenses:,.2f}")
    
        # Spending by category
        st.subheader("Spending by Category")
        expense_df = transactions[transactions['type'] == 'expense']
        if not expense_df.empty:
            fig = px.pie(
                expense_df,
                names='category',
                values='amount',
                title='Expense Breakdown'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Recent transactions
    st.subheader("Recent Transactions")
    st.dataframe(
        transactions.head(10),
        hide_index=True,
        use_container_width=True
    )