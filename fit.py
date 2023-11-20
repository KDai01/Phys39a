import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the decaying exponential function
def decay_function(x, T, q):
    return T * np.exp(-q * x) 

# Generate example data
x_data = np.array([0,0.0127,0.0254,0.0381,0.0508])
y_data = np.array([50.5, 49.5, 47.7, 46.7, 44.1])
y_data = y_data - 25

# Use curve_fit to fit the data to the decaying exponential function
params, covariance = curve_fit(decay_function, x_data, y_data)

# Extract the parameters
a_fit, b_fit = params
print(a_fit)
print(b_fit)

# Generate fitted curve using the fitted parameters
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = decay_function(x_fit, a_fit, b_fit)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_fit, y_fit, label='Fitted Curve', color='red')
plt.legend()
plt.xlabel('Height (m)')
plt.ylabel('Temperature over ambient (C)')
plt.title('Temperature vs Height on Rod')
plt.show()