import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.stats import linregress

# Dados

#Primeira coleta de dados decrescente
C1 = np.array([92,91,89,88,86,81,80,76,69,66,62])
Vout1 = np.array([3.86,3.81,3.75,3.66,3.585,3.375,3.34,3.21,3.105,2.89,2.71])
Vin1 = np.array([5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0])
#Segunda coleta de dados crescente
C2 = np.array([64,67,74,77,80,83,86]) #,87,92,95,90])
Vout2 = np.array([2.7, 2.88, 2.865, 3, 3.08, 3.165, 3.27]) #,2.94,3.09,3.12,3.17])
Vin2 = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5]) #,4, 4.5, 5, 4.5])
#Terceira coleta de dados decrescente
C3 = np.array([97,96,92,89,87,82,81,78,74,70,66])
Vout3 = np.array([3.97,3.87,3.75,3.645,3.57,3.39,3.35,3.238,3.125,2.954,2.821])
Vin3 = np.array([5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0])
#Quarta coleta de dados crescente
C4 = np.array([69,72,76,79,82,86,87,90,93,96])
Vout4 = np.array([2.65,2.754,2.852,2.961,3.061,3.19,3.248,3.364,3.457,3.568])
Vin4 = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
print('Lens Vout: ',len(Vout1),'  ',len(Vout2),' ',len(Vout2),'')
print('Lens Vin: ',len(Vin1),'  ',len(Vin2),' ',len(Vin3),'')
print('Lens C: ',len(C1),'  ',len(C2),' ',len(C3),'')

Vin = np.concatenate([Vin1, Vin2, Vin3, Vin4])
Vout = np.concatenate([Vout1,Vout2, Vout3, Vout4])
C = np.concatenate([C1,C2, C3,C4])

#Decrescente
#Vin = np.concatenate([Vin1, Vin3])
#Vout = np.concatenate([Vout1,Vout3])
#C = np.concatenate([C1,C3])

#Crescente
#Vin = np.concatenate([Vin2, Vin4])
#Vout = np.concatenate([Vout2, Vout4])
#C = np.concatenate([C2, C4])

#Uma de cada
Vin = np.concatenate([Vin3, Vin4])
Vout = np.concatenate([Vout3, Vout4])
C = np.concatenate([C3, C4])

print(type(C), C.shape, C)
print(type(Vin), Vin.shape, Vin)

# Ajuste de uma equação de primeiro grau para Vout(C)
coef_vinC = np.polyfit(C, Vin, 1)
poly_vout = np.poly1d(coef_vinC)
VinC_fit = poly_vout(C)

# Ajuste de uma equação de primeiro grau para C(Vout)
coef_c = np.polyfit(Vout, C, 1)
poly_c = np.poly1d(coef_c)
C_fit = poly_c(Vout)

# Ajuste de uma equação de segundo grau para Vin(Vout)
coef_vout_vin = np.polyfit(Vin, Vout, 2)
poly_vin = np.poly1d(coef_vout_vin)
Vou_vin_fit = poly_vin(Vin)

# Estatísticas de ajuste
r2_vinC = linregress(C, Vin).rvalue ** 2
r2_vout_vin = linregress(Vin, Vout).rvalue ** 2
r2_c = linregress(Vout, C).rvalue ** 2

print(f"Equação linear para Vin(C): {coef_vinC[0]:.4f}*x + {coef_vinC[1]:.4f}, R² = {r2_vinC:.4f}")
print(f"Equação quadrática para Vin(Vout): {coef_vout_vin[0]:.4f}*x^2 + {coef_vout_vin[1]:.4f}*x + {coef_vout_vin[2]:.4f}, R² = {r2_vout_vin:.4f}")
print(f"Equação linear para C(Vout): {coef_c[0]:.4f}*x + {coef_c[1]:.4f}, R² = {r2_c:.4f}")

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
plt.plot(Vin, Vout, 'o', label='Vin (V) - Dados')
plt.plot(Vin, Vou_vin_fit, '-', label='Ajuste Quadrático')
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
