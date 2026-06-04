-- DIM TABLES

CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date TEXT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

-- FACT TABLES

CREATE TABLE fact_nav (
    amfi_code TEXT,
    date TEXT,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (transaction_date) REFERENCES dim_date(date)
);

CREATE TABLE fact_performance (
    amfi_code TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);