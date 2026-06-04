import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../bluestock_mf.db")

# NAV
nav = pd.read_csv("../data/processed/nav_history_cleaned.csv")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

# TRANSACTIONS
tx = pd.read_csv("../data/processed/investor_transactions_cleaned.csv")
tx.to_sql("fact_transactions", engine, if_exists="replace", index=False)

# PERFORMANCE
perf = pd.read_csv("../data/processed/scheme_performance_cleaned.csv")
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("SQLite DB created successfully")