import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load NAV history
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Select first fund
fund_code = nav['amfi_code'].iloc[0]

fund = nav[nav['amfi_code'] == fund_code].copy()

# Sort by date
fund['date'] = pd.to_datetime(fund['date'])
fund = fund.sort_values('date')

# Calculate daily returns
fund['daily_return'] = fund['nav'].pct_change()

returns = fund['daily_return'].dropna()

# Mean and standard deviation
mu = returns.mean()
sigma = returns.std()

# Simulation settings
simulations = 1000
days = 252 * 5

current_nav = fund['nav'].iloc[-1]

paths = np.zeros((days, simulations))
paths[0] = current_nav

# Run simulation
for s in range(simulations):
    for t in range(1, days):
        paths[t, s] = paths[t-1, s] * (
            1 + np.random.normal(mu, sigma)
        )

# Plot
plt.figure(figsize=(12,6))
plt.plot(paths[:, :50])

plt.title("Monte Carlo Simulation - 5 Year NAV Projection")
plt.xlabel("Trading Days")
plt.ylabel("Projected NAV")

plt.savefig("bonus/monte_carlo_simulation.png")

plt.show()

print("Monte Carlo simulation completed successfully.")