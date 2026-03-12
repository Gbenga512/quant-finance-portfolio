import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example stock return data
returns = pd.DataFrame({
    "StockA":[0.12,0.10,0.15,0.11,0.13],
    "StockB":[0.08,0.09,0.07,0.10,0.09],
    "StockC":[0.15,0.16,0.14,0.17,0.18]
})

# Calculate mean returns
mean_returns = returns.mean()

# Covariance matrix
cov_matrix = returns.cov()

# Number of portfolios
num_portfolios = 5000

results = np.zeros((3,num_portfolios))

for i in range(num_portfolios):

    weights = np.random.random(3)
    weights /= np.sum(weights)

    portfolio_return = np.sum(mean_returns * weights)

    portfolio_std = np.sqrt(
        np.dot(weights.T,np.dot(cov_matrix,weights))
    )

    results[0,i] = portfolio_return
    results[1,i] = portfolio_std
    results[2,i] = portfolio_return/portfolio_std

# Plot Efficient Frontier
plt.scatter(results[1,:],results[0,:],c=results[2,:])

plt.xlabel("Risk (Standard Deviation)")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier - Portfolio Optimization")

plt.colorbar(label="Sharpe Ratio")

plt.show()
