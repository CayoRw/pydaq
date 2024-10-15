import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    # ----------------------------
    # 1. Configurações do Controlador PID
    # ----------------------------
    Kp = 2.0  # Ganho proporcional
    Ki = 0.5  # Ganho integr5
    Kd = 0.1  # Ganho derivativo

    # ----------------------------
    # 2. Configurações do Sistema Discreto
    # ----------------------------
    T = 0.1  # Intervalo de amostragem em segundos
    a = 2     # Denominador do sistema (s+2)

    # Função de transferência discreta do sistema (utilizando Euler para discretizar)
    def system_output(u, y_prev):
        # Discretização por Euler
        return (T * u + y_prev) / (1 + T * a)

    # Implementação do PID em tempo discreto
    def pid_controller(setpoint, y, Kp, Ki, Kd, integral_prev, error_prev, T):
        error = setpoint - y
        integral = integral_prev + error * T
        derivative = (error - error_prev) / T
        output = Kp * error + Ki * integral + Kd * derivative
        return output, integral, error

    # ----------------------------
    # 3. Entrada do Usuário
    # ----------------------------
    try:
        setpoint = float(input("Digite o valor do setpoint desejado: "))
    except ValueError:
        print("Entrada inválida para o setpoint. Usando setpoint padrão = 1.0")
        setpoint = 1.0

    try:
        sim_time = float(input("Digite o tempo de simulação em segundos: "))
        if sim_time <= 0:
            raise ValueError
    except ValueError:
        print("Entrada inválida para o tempo de simulação. Usando tempo padrão = 10 segundos")
        sim_time = 10.0

    # ----------------------------
    # 4. Parâmetros de Simulação
    # ----------------------------
    time_steps = int(sim_time / T)  # Número total de iterações
    time_array = np.arange(0, sim_time, T)  # Vetor de tempo

    y = 0.0                     # Saída inicial do sistema
    integral = 0.0              # Valor inicial da integral
    error_prev = 0.0            # Erro anterior

    # Armazenar dados para plotar
    output_data = []
    setpoint_data = []

    # Configuração inicial do gráfico
    plt.ion()  # Ativa o modo interativo
    fig, ax = plt.subplots()
    line1, = ax.plot([], [], label="Saída do sistema")
    line2, = ax.plot([], [], '--', label="Setpoint", color='red')
    ax.set_xlim(0, sim_time)
    ax.set_ylim(0, max(setpoint*1.2, 1.2))  # Ajusta o limite y com base no setpoint
    ax.set_title('Resposta do sistema controlado por PID')
    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('Saída')
    ax.legend()
    ax.grid(True)

    # ----------------------------
    # 5. Loop de Simulação em Tempo Real
    # ----------------------------
    start_time = time.time()
    for k in range(time_steps):
        current_time = k * T

        # Controlador PID
        u, integral, error_prev = pid_controller(setpoint, y, Kp, Ki, Kd, integral, error_prev, T)

        # Resposta do sistema discreto
        y = system_output(u, y)

        # Armazenar dados
        output_data.append(y)
        setpoint_data.append(setpoint)

        # Atualizar gráfico
        line1.set_data(time_array[:k+1], output_data)
        line2.set_data(time_array[:k+1], setpoint_data)
        ax.relim()
        ax.autoscale_view()
        plt.pause(0.001)  # Pequena pausa para atualizar o gráfico

        # Esperar até o próximo intervalo de amostragem
        elapsed_time = time.time() - start_time
        expected_time = (k + 1) * T
        sleep_time = expected_time - elapsed_time
        if sleep_time > 0:
            time.sleep(sleep_time)

    # Desativar o modo interativo e mostrar o gráfico final
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()