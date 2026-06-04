import pandas as pd

df = pd.read_csv("../data/raw/07_scheme_performance.csv")

print("Original Rows:", len(df))
print(df.columns)

# Convert return columns to numeric
return_cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Validate expense ratio
df["expense_ratio_pct"] = pd.to_numeric(df["expense_ratio_pct"], errors="coerce")

df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Remove missing critical values
df = df.dropna(subset=["amfi_code"])

print("Cleaned Rows:", len(df))

df.to_csv(
    "../data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Saved Successfully")