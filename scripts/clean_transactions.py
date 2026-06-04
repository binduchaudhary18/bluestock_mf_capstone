import pandas as pd

df = pd.read_csv("../data/raw/08_investor_transactions.csv")

print("Original Rows:", len(df))

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# Clean transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.lower()
    .replace({
        "sip": "SIP",
        "lumpsum": "Lumpsum",
        "lump sum": "Lumpsum",
        "redemption": "Redemption"
    })
)

# Clean amount
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")
df = df[df["amount_inr"] > 0]

# Clean KYC
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending", "Rejected"]
df = df[df["kyc_status"].isin(valid_kyc)]

# Remove missing critical values
df = df.dropna(subset=["transaction_date", "amfi_code"])

print("Cleaned Rows:", len(df))

df.to_csv(
    "../data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Saved Successfully")
