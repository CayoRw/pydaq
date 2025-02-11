import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.stats import linregress

# Dados
#C = np.array([37, 43, 45, 48, 49, 50, 51, 53, 54, 55, 56])
#Vout = np.array([2, 2.33, 2.45, 2.53, 2.65, 2.73, 2.85, 2.89, 2.97, 3.02, 3.10])
#Vin = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

#C = np.array([62,66,69,76,80,81,86,88,89,91,92])
C = np.array([92,91,89,88,86,81,80,76,69,66,62,64,67,74,77,80,83,86,87,92,95,90])
Vout = np.array([3.86,3.81,3.75,3.66,3.585,3.375,3.34,3.21,3.105,2.89,2.71, 2.7, 2.88, 2.865, 3, 3.08, 3.165, 3.27,2.94,3.09,3.12,3.17])
#Vout = np.array([2.71,2.89,3.105,3.21,3.34,3.375,3.585,3.66,3.75,3.81,3.86])
Vin = np.array([5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5,4, 4.5, 5, 4.5])

# Ajuste de uma equação de primeiro grau para Vout(C)
coef_vinC = np.polyfit(C, Vin, 1)
poly_vout = np.poly1d(coef_vinC)
VinC_fit = poly_vout(C)

# Ajuste de uma equação de primeiro grau para C(Vout)
coef_c = np.polyfit(Vout, C, 1)
poly_c = np.poly1d(coef_c)
C_fit = poly_c(Vout)

# Ajuste de uma equação de segundo grau para Vin(Vout)
coef_vin = np.polyfit(Vout, Vin, 2)
poly_vin = np.poly1d(coef_vin)
Vin_fit = poly_vin(Vout)

# Estatísticas de ajuste
r2_vinC = linregress(C, Vin).rvalue ** 2
r2_vin = linregress(Vout, Vin).rvalue ** 2
r2_c = linregress(Vout, C).rvalue ** 2

print(f"Equação linear para Vin(C): {coef_vinC[0]:.4f}*C + {coef_vinC[1]:.4f}, R² = {r2_vinC:.4f}")
print(f"Equação quadrática para Vin(Vout): {coef_vin[0]:.4f}*Vout^2 + {coef_vin[1]:.4f}*Vout + {coef_vin[2]:.4f}, R² = {r2_vin:.4f}")
print(f"Equação linear para C(Vout): {coef_c[0]:.4f}*Vout + {coef_c[1]:.4f}, R² = {r2_c:.4f}")

# Criando o primeiro gráfico
plt.figure(figsize=(8, 5))
plt.plot(C, Vout, 'o', label='Vout (V) - Dados')
plt.plot(C, VinC_fit, '-', label='Ajuste Linear')
plt.plot(C, Vin, 's', label='Vin (V) - Dados')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Tensão (V)')
plt.title('Relação entre Temperatura e Tensões Vin/Vout')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Criando o segundo gráfico
plt.figure(figsize=(8, 5))
plt.plot(Vout, Vin, 'o', label='Vin (V) - Dados')
plt.plot(Vout, Vin_fit, '-', label='Ajuste Quadrático')
plt.xlabel('Vout (V)')
plt.ylabel('Vin (V)')
plt.title('Relação entre Vout e Vin')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Criando o terceiro gráfico
plt.figure(figsize=(8, 5))
plt.plot(Vout, C, 'o', label='C (°C) - Dados')
plt.plot(Vout, C_fit, '-', label='Ajuste Linear')
plt.xlabel('Vout (V)')
plt.ylabel('Temperatura (°C)')
plt.title('Relação entre Vout e Temperatura')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
