def generate_insight(by_month: dict, by_category: dict, forecast: float) -> str:
    # Sort months
    months = sorted(by_month.keys())
    if len(months) < 2:
        return "You spent ${:.2f} this period.".format(sum(by_month.values()))

    # Month-over-month change
    m1, m2, *rest = months
    last_month = months[-1]
    prev_month = months[-2]

    last_val = by_month[last_month]
    prev_val = by_month[prev_month]

    change_pct = ((last_val - prev_val) / prev_val) * 100 if prev_val > 0 else 0

    # Top category
    top_category = max(by_category, key=by_category.get)

    # Build the message
    message = (
        f"Your spending increased by {change_pct:.1f}% from {prev_month} to {last_month}, "
        f"driven mainly by {top_category.lower()}. "
        f"Based on recent trends, you're on track to spend about ${forecast:.2f} next month."
    )

    return message
