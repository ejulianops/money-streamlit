import sqlite3
import pandas as pd
from datetime import datetime

def init_db():
    conn = sqlite3.connect('data/transactions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(amount, category, description, trans_type, date=None):
    date = date or datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect('data/transactions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO transactions (amount, category, description, date, type)
        VALUES (?, ?, ?, ?, ?)
    ''', (abs(amount), category, description, date, trans_type))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = sqlite3.connect('data/transactions.db')
    df = pd.read_sql('SELECT * FROM transactions ORDER BY date DESC', conn)
    conn.close()
    return df

def get_balance():
    conn = sqlite3.connect('data/transactions.db')
    income = pd.read_sql(
        "SELECT SUM(amount) as total FROM transactions WHERE type='income'", 
        conn
    ).iloc[0]['total'] or 0
    expenses = pd.read_sql(
        "SELECT SUM(amount) as total FROM transactions WHERE type='expense'", 
        conn
    ).iloc[0]['total'] or 0
    conn.close()
    return income - expenses