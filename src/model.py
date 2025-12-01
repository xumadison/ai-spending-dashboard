import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_total_next_month(summary_df: pd.DataFrame) -> float:
    monthly = summary_df.groupby("Month", as_index=False)["Amount"].sum().sort_values("Month")

    if len(monthly) < 2:
        return float(monthly["Amount"].iloc[-1]) if len(monthly) == 1 else 0.0

    monthly["MonthIndex"] = np.arange(len(monthly))
    X = monthly[["MonthIndex"]].values
    y = monthly["Amount"].values

    model = LinearRegression().fit(X, y)

    next_idx = np.array([[len(monthly)]])
    return float(model.predict(next_idx)[0])
