import pandas as pd
from src.pipeline import process_transactions

def test_process_transactions_basic():
    df = pd.DataFrame({
        "Date": ["2025-01-01", "2025-01-15", "2025-02-01"],
        "Merchant": ["A", "B", "C"],
        "Category": ["Groceries", "Groceries", "Travel"],
        "Amount": [10.0, 20.0, 30.0]
    })
    out = process_transactions(df)
    assert {"Month", "Category", "Amount"} <= set(out.columns)
    assert out.groupby("Month")["Amount"].sum().sum() == 60.0
