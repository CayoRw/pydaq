import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def identificar_parametros(a, b):
    """Identifica K, L e T de um sistema a partir da resposta ao degrau."""
    
    # Determinar K (ganho do sistema)
    K = (b[-1] - b[0])  # Supondo entrada de 1 unidade de amplitude no degrau
    
    # Aproximação da derivada para encontrar o maior crescimento (ponto de inflexão)
    derivada = np.gradient(b, a)
    idx_max_derivada = np.argmax(derivada)

    # Ponto da maior inclinação
    t_inf = a[idx_max_derivada]
    b_inf = b[idx_max_derivada]

    # Ajuste da reta tangente na maior inclinação
    coef_ang = derivada[idx_max_derivada]
    reta_tangente = lambda t: coef_ang * (t - t_inf) + b_inf

    # Encontrar L (tempo de atraso) - interseção da reta tangente com o eixo zero
    L = t_inf - (b_inf / coef_ang)

    # Encontrar T (constante de tempo) - quando a reta tangente atinge 63% de K
    T = (b[0] + 0.632 * K - b_inf) / coef_ang + t_inf

    # Cálculo dos parâmetros PID pelo método de Ziegler-Nichols
    Kp = 1.2 * (T / L) * K
    Ki = Kp / (2 * L)
    Kd = 0.5 * Kp * L

    return K, L, T, Kp, Ki, Kd

# Exemplo de uso
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Vetor de tempo
b = np.array([0, 2, 4, 5, 6, 6.5, 7, 7.4, 7.8, 8])  # Resposta ao degrau

K, L, T, Kp, Ki, Kd = identificar_parametros(a, b)

print(f"K = {K:.4f}")
print(f"L = {L:.4f}")
print(f"T = {T:.4f}")
print(f"Kp = {Kp:.4f}, Ki = {Ki:.4f}, Kd = {Kd:.4f}")

# Plot do gráfico
plt.plot(a, b, label="Resposta ao degrau")
plt.axvline(L, color="r", linestyle="--", label="L (Atraso)")
plt.axvline(T, color="g", linestyle="--", label="T (Constante de tempo)")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.legend()
plt.grid()
plt.show()