-- 1. Top 5 funds by NAV
SELECT amfi_code, MAX(nav)
FROM fact_nav
GROUP BY amfi_code
ORDER BY MAX(nav) DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 3. SIP inflow trend
SELECT transaction_date, SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY transaction_date;

-- 4. Transactions by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5. High performing funds (5Y return)
SELECT amfi_code, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 6. Low expense ratio funds
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7. Redemption vs SIP comparison
SELECT transaction_type, SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Monthly investment trend
SELECT strftime('%Y-%m', transaction_date) AS month,
SUM(amount_inr)
FROM fact_transactions
GROUP BY month;

-- 9. Fund count by category (needs dim_fund later)
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- 10. High volatility funds
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC;