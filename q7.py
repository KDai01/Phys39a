import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Select period
period = 60 #60, 120, 180, 240

# Load data from the text file
file_path = f'Tset45_{period}secPeriod_q7_data.txt'
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
p0 = (37.8, 2.9, 2*np.pi/period, 3)  # Omega = 0.0525 for 120 sec, 0.026 for 240 sec, 0.035 for 180 sec, 0.105 for 60 sec

params_list = []


plt.figure(figsize=(12, 8))

#print('Parameters:')
for i in range(num_thermistors):
    thermistor_i_data = thermistor_data[:, i]
    
    params_i, _ = curve_fit(oscillating_temperature, time, thermistor_i_data, p0=p0)
    params_list.append(params_i)


    # Plot the data and fits for each thermistor
    plt.subplot(2, 3, i + 1)
    plt.scatter(time, thermistor_i_data, marker='o', color='red', label=f'Thermistor {i + 1} Data')
    plt.plot(time, oscillating_temperature(time, *params_i), 'b--',label='Fit')
    plt.title(f'Thermistor {i + 1}, A={params_i[0]:0.2f}, B={params_i[1]:0.2f}, omega={params_i[2]:0.2f}, epsilon={params_i[3]:0.2f}', fontsize=10)
    plt.legend()

    #print(f'A{i+1} = {params_i[0]:0.3f}, B{i+1} = {params_i[1]:0.3f}, omega{i+1} = {params_i[2]:0.3f}, epsilon{i+1} = {params_i[3]:0.3f}')

plt.tight_layout()
plt.show()

# Extract parameters for each thermistor
params_array = np.array(params_list)
#print (params_array)

# Calculate q, q', and epsilon
room_temp = 25.0
thermistor_locations = np.array([0,0.0127,0.0254,0.0381,0.0508])

def paramA(x, ql, T, delta):
    return (T-room_temp) * np.exp(-ql * x + delta)

def paramB(x, q, amp_T, delta):
    return amp_T* np.exp(-q * x + delta)

def paramEps(x, eps, qprime):
    return eps - qprime * x

a_fit, _ = curve_fit(paramA, thermistor_locations, params_array[:, 0], p0=(1, 39.2, 0))
b_fit, _ = curve_fit(paramB, thermistor_locations, params_array[:, 1], p0=(1, 4.23, 0))
eps_fit, _ = curve_fit(paramEps, thermistor_locations, params_array[:, 3], p0=(3.68, 16))

ql = a_fit[0]
q = b_fit[0]
qprime = eps_fit[1]

print("Parameters:")
print(f'ql = {ql:0.3f}, q = {q:0.3f}, qprime = {qprime:0.3f}, q*qprime = {q*qprime:0.3f}')

omega_average = np.average(params_array[:, 2])

kappa = omega_average / (2 * q * qprime)
nu = kappa * ql**2

print(f'kappa = {kappa:0.2E}, nu = {nu:0.2E}')

"""
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