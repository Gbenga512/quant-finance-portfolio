import numpy as np
from scipy.stats import norm

# Black-Scholes option pricing formula

def black_scholes_call(S, K, T, r, sigma):
    
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    
    d2 = d1 - sigma*np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    
    return call_price


# Example values

S = 100      # stock price
K = 100      # strike price
T = 1        # time to maturity
r = 0.05     # risk free rate
sigma = 0.2  # volatility


price = black_scholes_call(S,K,T,r,sigma)

print("Call Option Price:", price)
