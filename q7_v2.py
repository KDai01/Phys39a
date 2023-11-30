import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

pers = [60, 120, 180, 240]
qls = []
qs = []
qprimes = []
kappas = []
nus = []

for period in pers:
    #print(f'Period: {period} seconds')

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
        plt.scatter(time, thermistor_i_data, marker='.', color='red', label=f'Data')
        plt.plot(time, oscillating_temperature(time, *params_i), 'b--', linewidth=1, label=f'Fit')
        plt.title(f'Thermistor {i + 1}, A={params_i[0]:0.2f}, B={params_i[1]:0.2f}, omega={params_i[2]:0.2f}, epsilon={params_i[3]:0.2f}',fontsize=10)
        plt.legend()

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

    #print("Parameters:")
    #print(f'ql = {ql:0.3f}, q = {q:0.3f}, qprime = {qprime:0.3f}, q*qprime = {q*qprime:0.3f}')

    omega_average = np.average(params_array[:, 2])

    kappa = omega_average / (2 * q * qprime)
    nu = kappa * ql**2

    qls.append(ql)
    qs.append(q)
    qprimes.append(qprime)
    kappas.append(kappa)
    nus.append(nu)

    #print(f'kappa = {kappa:0.2E}, nu = {nu:0.2E}')
    #print('')

print('Summary:')
np.set_printoptions(formatter={'float_kind':"{:0.3f}".format})
print(f'period:\t{np.array(pers).astype(np.float64)}')
print(f'ql:\t{np.array(qls)}')
print(f'q:\t{np.array(qs)}')
print(f'qprime:\t{np.array(qprimes)}')
np.set_printoptions(formatter={'float_kind':"{:0.1E}".format})
print(f'kappa:\t{np.array(kappas)}')
print(f'nu:\t{np.array(nus)}')

prod = np.array(qs) * np.array(qprimes)
quot = np.array(qprimes) / np.array(qs)
omegas = 2 * np.pi / np.array(pers)

def product(omega, kappa):
    return omega / (2 * kappa)

prod_fit, _ = curve_fit(product, omegas, prod, p0=(0.00009))

plt.subplot(1, 2, 1)
plt.scatter(omegas, prod, marker='o', color='red', label='Data')
plt.plot(np.linspace(0,0.2), product(np.linspace(0,0.2), prod_fit[0]), 'b--', label=f'Fit')
plt.title(f'q*qprime vs omega, kappa fit = {prod_fit[0]:0.2E}')
plt.xlabel('omega')
plt.ylabel('q*qprime')
plt.legend()

def quotient(omega, nu):
    return (np.sqrt(nu**2 + omega**2) - nu) / omega

quot_fit, _ = curve_fit(quotient, omegas, quot, p0=(0.0002))

plt.subplot(1, 2, 2)
plt.scatter(omegas, quot, marker='o', color='red', label='Data')
plt.plot((np.linspace(0.001,0.2)), quotient(np.linspace(0.001,0.2), quot_fit[0]), 'b--', label=f'Fit')
plt.title(f'qprime/q vs omega, nu fit = {quot_fit[0]:0.2E}')
plt.xlabel('omega')
plt.ylabel('qprime/q')
plt.legend()

plt.tight_layout()
plt.show()
