import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.stats import linregress

# Dados
C = np.array([37, 43, 45, 48, 49, 50, 51, 53, 54, 55, 56])
Vout = np.array([2, 2.33, 2.45, 2.53, 2.65, 2.73, 2.85, 2.89, 2.97, 3.02, 3.10])
Vin = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

# Ajuste de uma equação de primeiro grau para Vout(C)
coef_vout = np.polyfit(C, Vout, 1)
poly_vout = np.poly1d(coef_vout)
Vout_fit = poly_vout(C)

# Ajuste de uma equação de primeiro grau para C(Vout)
coef_c = np.polyfit(Vout, C, 1)
poly_c = np.poly1d(coef_c)
C_fit = poly_c(Vout)

# Ajuste de uma equação de segundo grau para Vin(Vout)
coef_vin = np.polyfit(Vout, Vin, 2)
poly_vin = np.poly1d(coef_vin)
Vin_fit = poly_vin(Vout)

# Estatísticas de ajuste
r2_vout = linregress(C, Vout).rvalue ** 2
r2_vin = linregress(Vout, Vin).rvalue ** 2
r2_c = linregress(Vout, C).rvalue ** 2

print(f"Equação linear para Vout(C): {coef_vout[0]:.4f}*C + {coef_vout[1]:.4f}, R² = {r2_vout:.4f}")
print(f"Equação quadrática para Vin(Vout): {coef_vin[0]:.4f}*Vout^2 + {coef_vin[1]:.4f}*Vout + {coef_vin[2]:.4f}, R² = {r2_vin:.4f}")
print(f"Equação linear para C(Vout): {coef_c[0]:.4f}*Vout + {coef_c[1]:.4f}, R² = {r2_c:.4f}")

# Criando o primeiro gráfico
plt.figure(figsize=(8, 5))
plt.plot(C, Vout, 'o', label='Vout (V) - Dados')
plt.plot(C, Vout_fit, '-', label='Ajuste Linear')
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
