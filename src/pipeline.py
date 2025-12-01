import pandas as pd

def process_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and enrich raw transaction data.
    Expects columns: Date, Merchant, Category, Amount
    Returns a DataFrame aggregated by Month and Category.
    """
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Category", "Amount"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Amount"])

    # Create a standard Month column (Timestamp version)
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()

    # Summary grouped by month + category
    summary = df.groupby(["Month", "Category"], as_index=False)["Amount"].sum()
    return summary


def get_monthly_totals(summary_df: pd.DataFrame) -> dict:
    """
    Returns { '2025-01': total_amount, '2025-02': total_amount, ... }
    """
    monthly = summary_df.groupby("Month")["Amount"].sum()
    # Convert Timestamp → string for JSON
    monthly = monthly.rename_axis("Month").reset_index()
    monthly["Month"] = monthly["Month"].dt.strftime("%Y-%m")
    return dict(zip(monthly["Month"], monthly["Amount"]))


def get_category_totals(df: pd.DataFrame) -> dict:
    """
    Returns total spending by category for the entire dataset.
    """
    return df.groupby("Category")["Amount"].sum().to_dict()
