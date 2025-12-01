
from flask import Flask, request, jsonify
import pandas as pd
from io import TextIOWrapper
from src.pipeline import process_transactions, get_monthly_totals, get_category_totals
from src.model import forecast_total_next_month
from src.insights import generate_insight


app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded. Use form key 'file'."}), 400

    file = request.files["file"]

    # Read the uploaded CSV
    try:
        df = pd.read_csv(TextIOWrapper(file, encoding="utf-8"))
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV: {e}"}), 400

    # Validate columns
    required = {"Date", "Merchant", "Category", "Amount"}
    if not required.issubset(df.columns):
        return jsonify({"error": f"CSV must contain: {sorted(required)}"}), 400

    # PROCESS DATA
    summary_df = process_transactions(df)

    # METRICS
    by_category = get_category_totals(df)
    by_month = get_monthly_totals(summary_df)
    forecast_next = forecast_total_next_month(summary_df)
    insight_text = generate_insight(by_month, by_category, forecast_next)


   # Determine top category
    top_category = max(by_category, key=by_category.get) if by_category else None

    result = {
        "total_spend": float(df["Amount"].sum()),
        "by_category": by_category,
        "by_month": by_month,
        "forecast_next_month": forecast_next,
        "insight_text": insight_text,
        "top_category": top_category
    }


    return jsonify(result), 200

@app.after_request
def add_cors_headers(response):
    # Echo back whatever origin the browser sends (for local dev)
    origin = request.headers.get("Origin")
    if origin:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Vary"] = "Origin"
    else:
        # Fallback for non-browser clients like curl
        response.headers["Access-Control-Allow-Origin"] = "*"

    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

