import numpy as np
import matplotlib.pyplot as plt
import time

# Parâmetros do sistema e do controlador PID
a = 1  # Parâmetro do sistema G(s) = 1 / (s + a)
Kp = 1.0  # Ganho proporcional
Ki = 0.5  # Ganho integral
Kd = 0.1  # Ganho derivativo
setpoint = 1.0  # Valor desejado
T = 0.6  # Período de amostragem
total_time = 20  # Tempo total de simulação (segundos)

# Inicializando variáveis do PID
integral = 0.0
prev_error = 0.0
prev_output = 0.0
output = 0.0

# Função do sistema (modelo discreto)
def system_discrete(output_prev, input_signal, a, T):
    # Sistema de primeira ordem discreto: y[n+1] = (1 - a*T)*y[n] + T*u[n]
    return (1 - a*T) * output_prev + T * input_signal

# Variáveis para armazenar resultados
time_steps = np.arange(0, total_time, T)
system_output = []
control_signal = []

# Preparando o gráfico interativo
plt.ion()  # Modo interativo
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))

# Configurando os eixos do gráfico
ax1.set_title("Saída do Sistema e Setpoint")
ax1.set_ylabel("Saída")
ax1.plot(time_steps, [setpoint] * len(time_steps), 'r--', label="Setpoint")
line_output, = ax1.plot([], [], label="Saída do Sistema")
ax1.legend()

ax2.set_title("Sinal de Controle")
ax2.set_xlabel("Tempo (s)")
ax2.set_ylabel("Controle")
line_control, = ax2.plot([], [], label="Sinal de Controle")
ax2.legend()

plt.tight_layout()

# Simulação em tempo real
start_time = time.time()
for t in time_steps:
    # Erro entre o setpoint e a saída do sistema
    error = setpoint - output
    
    # Controle PID (discreto)
    integral += error * T
    derivative = (error - prev_error) / T
    control = Kp * error + Ki * integral + Kd * derivative
    
    # Aplicando o controle no sistema discreto
    output = system_discrete(prev_output, control, a, T)
    
    # Armazenando resultados
    system_output.append(output)
    control_signal.append(control)

    # Atualizando as variáveis
    prev_error = error
    prev_output = output

    # Atualizando os dados no gráfico
    line_output.set_data(time_steps[:len(system_output)], system_output)
    line_control.set_data(time_steps[:len(control_signal)], control_signal)

    # Ajustar os limites do gráfico conforme os dados vão chegando
    ax1.set_xlim(0, total_time)
    ax1.set_ylim(min(system_output) - 0.5, max(system_output) + 0.5)
    ax2.set_xlim(0, total_time)
    ax2.set_ylim(min(control_signal) - 0.5, max(control_signal) + 0.5)

    # Redesenhar o gráfico
    plt.draw()
    plt.pause(0.01)  # Pausa breve para atualização do gráfico

    # Esperar até o próximo instante (tempo real)
    elapsed_time = time.time() - start_time
    sleep_time = T - elapsed_time
    if sleep_time > 0:
        time.sleep(sleep_time)

    start_time = time.time()

# Após a simulação, desativar o modo interativo e mostrar o gráfico final
plt.ioff()
plt.show()