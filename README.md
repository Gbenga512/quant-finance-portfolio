import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulated stock price data
np.random.seed(42)
price = np.cumsum(np.random.normal(0,1,200)) + 100

data = pd.DataFrame({"Price":price})

# Moving averages
data["MA_short"] = data["Price"].rolling(window=10).mean()
data["MA_long"] = data["Price"].rolling(window=30).mean()

# Trading signals
data["Signal"] = 0
data.loc[data["MA_short"] > data["MA_long"], "Signal"] = 1
data.loc[data["MA_short"] < data["MA_long"], "Signal"] = -1

# Plot strategy
plt.plot(data["Price"], label="Price")
plt.plot(data["MA_short"], label="Short MA")
plt.plot(data["MA_long"], label="Long MA")

plt.title("Moving Average Trading Strategy")
plt.legend()

plt.show()
