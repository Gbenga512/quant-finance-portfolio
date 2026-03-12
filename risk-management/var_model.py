import numpy as np
import matplotlib.pyplot as plt

# Simulated portfolio returns
np.random.seed(42)
returns = np.random.normal(0.001, 0.02, 1000)

# Confidence level
confidence_level = 0.95

# Calculate Value at Risk (VaR)
VaR = np.percentile(returns, (1 - confidence_level) * 100)

print("Value at Risk (95% confidence):", VaR)

# Plot distribution of returns
plt.hist(returns, bins=50)

# VaR line
plt.axvline(VaR, color='red', linestyle='dashed', linewidth=2)

plt.title("Value at Risk (VaR)")
plt.xlabel("Returns")
plt.ylabel("Frequency")

plt.show()
