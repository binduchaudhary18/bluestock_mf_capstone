import pandas as pd

# Load fund scorecard
scorecard = pd.read_csv("data/processed/fund_scorecard.csv")

# Get top 5 funds
top_funds = scorecard.sort_values(
    scorecard.columns[-1],
    ascending=False
).head(5)

# Create HTML report
html = f"""
<html>

<head>
<title>Weekly Mutual Fund Report</title>
</head>

<body>

<h1>Bluestock Weekly Mutual Fund Performance Report</h1>

<h2>Top 5 Funds</h2>

{top_funds.to_html(index=False)}

<p>
This report was automatically generated using Python.
</p>

</body>

</html>
"""

# Save report
with open(
    "bonus/weekly_report.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("HTML report generated successfully.")