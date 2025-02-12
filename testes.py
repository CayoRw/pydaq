import numpy as np
import matplotlib.pyplot as plt

class PIDTuning:
    def get_parameters(self, time, system_value, step_time, type_sintony, min_val, max_val):
        # Estimativa do ganho estático k
        delta = (min_val - max_val)
        if delta == 0 or min_val == 0:
            k = (system_value[-1] - system_value[0]) / (max_val - 0)
        else:
            k = (system_value[-1] - system_value[0]) / (max_val - min_val)

        # Cálculo da derivada
        derivative = np.gradient(system_value, time)

        # Encontrando o índice do máximo valor absoluto da derivada
        max_derivative_idx = np.argmax(np.abs(derivative))

        # Obtendo os valores correspondentes
        time_inflection = time[max_derivative_idx]
        sys_inflection = system_value[max_derivative_idx]

        # Ajustando reta tangente na inflexão
        slope = derivative[max_derivative_idx]
        intercept = sys_inflection - slope * time_inflection
        tangent_line = slope * time + intercept  # Equação da reta tangente

        # Encontrando L e T
        L = (step_time - (-intercept / slope)) if step_time > 0 else (-intercept / slope)
        T = (k - intercept) / slope - step_time - L  # Ajuste para `step_time`

        # Definição dos ganhos do controlador
        if type_sintony == 0:  # P Controler
            Kp = (T / L)
            Ki = 0
            Kd = 0
        elif type_sintony == 1:  # PI Controler
            Kp = 0.9 * (T / L)
            Ti = L / 0.3
            Ki = Kp / Ti
            Kd = 0
        elif type_sintony == 2:  # PID Controler
            Kp = 1.2 * (T / L)
            Ti = 2 * L
            Ki = Kp / Ti
            Td = 0.5 * L
            Kd = Kp * Td

        return Kp, Ki, Kd, time_inflection, sys_inflection, tangent_line

# Simulação de dados (exemplo)
time = np.linspace(0, 10, 100)  # Tempo de 0 a 10 segundos
system_value = 1 - np.exp(-time / 2)  # Sistema de primeira ordem simulado

# Criando o objeto e obtendo os parâmetros
pid_tuner = PIDTuning()
step_time = 0
type_sintony = 2  # PID
min_val = 0
max_val = 1
Kp, Ki, Kd, time_inflection, sys_inflection, tangent_line = pid_tuner.get_parameters(
    time, system_value, step_time, type_sintony, min_val, max_val
)

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(time, system_value, label="Resposta do sistema", linewidth=2)
plt.plot(time, tangent_line, '--', label="Reta tangente", linewidth=2, color='r')
plt.scatter(time_inflection, sys_inflection, color='black', zorder=3, label="Ponto de inflexão")

plt.xlabel("Tempo (s)")
plt.ylabel("Valor do sistema")
plt.legend()
plt.grid(True)
plt.title("Curva do sistema e reta tangente na inflexão")
plt.show()

# Exibindo os parâmetros calculados
print(f"Kp: {Kp:.4f}, Ki: {Ki:.4f}, Kd: {Kd:.4f}")
