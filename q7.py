import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load data from the text file
file_path = 'Tset45_120secPeriod_q7_data.txt'
data = np.loadtxt(file_path, delimiter='\t')

# Extracting relevant columns
time = data[:, 2]  # Assuming the time column is at index 2
thermistor_data = data[:, 4:]  # Assuming the thermistor columns start from index 4
#print(thermistor_data[0])

# Function for fitting the oscillating temperature
def oscillating_temperature(t, A, B, omega, epsilon):
    return A + B * np.cos(omega * t + epsilon)

# Fit the data for each thermistor
num_thermistors = thermistor_data.shape[1]
p0 = (45, 11, .0525, 1.5)  # Initial guess for parameters (A, B, omega, epsilon)

params_list = []


plt.figure(figsize=(12, 8))

for i in range(num_thermistors):
    thermistor_i_data = thermistor_data[:, i]
    
    params_i, _ = curve_fit(oscillating_temperature, time, thermistor_i_data, p0=p0)
    params_list.append(params_i)

    # Plot the data and fits for each thermistor
    plt.subplot(2, 3, i + 1)
    plt.scatter(time, thermistor_i_data, marker='o', color='red', label=f'Thermistor {i + 1} Data')
    plt.plot(time, oscillating_temperature(time, *params_i), 'b--',label='Fit')
    plt.title(f'Thermistor {i + 1}')
    plt.legend()

    print(f'Thermistor {i + 1} parameters: {params_i}')

plt.tight_layout()
plt.show()

# Extract parameters for each thermistor
params_array = np.array(params_list)

"""
# Calculate q, q', and epsilon
# Replace the formulas below with your actual expressions
q = np.sqrt(1.0 / 2.0)  # Placeholder value, replace with your formula
q_prime = np.sqrt(1.0 / 2.0)  # Placeholder value, replace with your formula
epsilon = 0.0  # Placeholder value, replace with your formula

# Calculate kappa and nu
# Replace the formulas below with your actual expressions
kappa = 1.0  # Placeholder value, replace with your formula
nu = 1.0  # Placeholder value, replace with your formula

# Repeat as a function of frequency omega
# Replace the formulas below with your actual expressions
omega_values = np.linspace(1, 10, 100)  # Adjust the range and number of points as needed
q_q_prime_values = omega_values / (2 * kappa)  # Adjust the formula as needed

# Plot q q' vs omega
plt.figure(figsize=(8, 6))
plt.plot(omega_values, q_q_prime_values, label='q q\' vs. omega')
plt.xlabel('Omega')
plt.ylabel('q q\'')
plt.legend()
plt.show()

# Deduce kappa from the plot and extract nu from measurements of q(omega) and q'(omega)
# Replace the formulas below with your actual calculations

# Plot and fit q'/q vs omega to obtain nu
q_over_q_prime_values = np.sqrt(omega_values / (2 * kappa))  # Adjust the formula as needed

plt.figure(figsize=(8, 6))
plt.plot(omega_values, q_over_q_prime_values, label='q\'/q vs. omega')
plt.xlabel('Omega')
plt.ylabel('q\'/q')
plt.legend()
plt.show()

"""