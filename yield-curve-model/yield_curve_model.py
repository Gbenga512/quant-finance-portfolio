import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Treasury maturities (years)
maturities = np.array([0.25,0.5,1,2,3,5,7,10,20,30])

# Example yields
yields = np.array([0.02,0.021,0.022,0.023,0.024,0.025,0.026,0.027,0.028,0.029])

# Nelson-Siegel function
def nelson_siegel(params, tau):

    beta0, beta1, beta2, lambd = params

    term1 = (1 - np.exp(-tau/lambd))/(tau/lambd)
    term2 = term1 - np.exp(-tau/lambd)

    return beta0 + beta1*term1 + beta2*term2

# Error function
def objective(params, tau, y):

    model = nelson_siegel(params, tau)
    return np.sum((y-model)**2)

# Initial guess
initial = [0.02,-0.02,0.02,1]

# Optimize parameters
result = minimize(objective, initial, args=(maturities,yields))

# Smooth curve
tau_range = np.linspace(0.25,30,100)
curve = nelson_siegel(result.x, tau_range)

# Plot yield curve
plt.scatter(maturities,yields,label="Observed")
plt.plot(tau_range,curve,label="Nelson-Siegel Fit")

plt.xlabel("Maturity (Years)")
plt.ylabel("Yield")
plt.title("Yield Curve Model")

plt.legend()
plt.show()
