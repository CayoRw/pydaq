import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PIDController:
    def __init__(self, kp, ki, kd, setpoint, a, period, duration):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.a = a  # Parâmetro do sistema contínuo
        self.period = period  # Período de amostragem (T)
        self.duration = duration  # Tempo total de controle
        
        # Discretizando o sistema 1/(s + a)
        self.e_at = np.exp(-a * period)  # e^(-aT)
        self.b0 = 1 - self.e_at
        self.a1 = -self.e_at
        
        # Variáveis do PID discreto
        self.integral = 0
        self.prev_error = 0
        self.prev_time = time.time()

        # Estado anterior do sistema (para modelo discreto)
        self.prev_output = 0  # Saída anterior do sistema discreto

    def system_response(self, u):
        # Implementa a equação da diferença do sistema discreto 1/(s+a)
        # G(z) = (1 - e^(-aT)) / (z - e^(-aT))
        output = self.b0 * u + self.a1 * self.prev_output
        self.prev_output = output  # Atualiza o estado anterior
        return output

    def compute(self, feedback):
        current_time = time.time()
        error = self.setpoint - feedback
        dt = current_time - self.prev_time

        if dt >= self.period:
            # Ação proporcional
            proportional = self.kp * error
            
            # Ação integral
            self.integral += error * dt
            integral = self.ki * self.integral
            
            # Ação derivativa
            derivative = self.kd * (error - self.prev_error) / dt
            
            # Controle final (PID)
            u = proportional + integral + derivative
            
            # Atualiza estados
            self.prev_error = error
            self.prev_time = current_time
            
            return u
        else:
            return None

# Configuração do controlador PID
kp = 1.0
ki = 0.5
kd = 0.1
setpoint = 1.0  # Valor desejado
a = 5  # Coeficiente do sistema 1/(s + a)
period = 0.1  # Tempo de amostragem (100 ms)
duration = 10  # Tempo de controle (10 segundos)

# Inicialização
controller = PIDController(kp, ki, kd, setpoint, a, period, duration)
start_time = time.time()
current_time = start_time
feedback = 0  # Valor inicial de saída do sistema

# Para armazenar dados do gráfico
times = []
feedbacks = []
controls = []

# Função de atualização do gráfico em tempo real
def update_plot(frame):
    global current_time, feedback
    
    control_signal = controller.compute(feedback)
    
    if control_signal is not None:
        # Aplica o controle ao sistema e obtém a nova resposta
        feedback = controller.system_response(control_signal)
        current_time = time.time()
        
        # Armazena dados para o gráfico
        times.append(current_time - start_time)
        feedbacks.append(feedback)
        controls.append(control_signal)
        
        # Limita o número de pontos para manter o gráfico mais leve
        if len(times) > 200:
            times.pop(0)
            feedbacks.pop(0)
            controls.pop(0)
        
        # Atualiza o gráfico
        ax1.cla()
        ax2.cla()
        
        ax1.set_title('Sistema: Resposta do Feedback')
        ax1.plot(times, feedbacks, label='Feedback')
        ax1.axhline(setpoint, color='r', linestyle='--', label='Setpoint')
        ax1.legend()
        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Feedback')
        
        ax2.set_title('Ação de Controle')
        ax2.plot(times, controls, label='Controle', color='g')
        ax2.legend()
        ax2.set_xlabel('Tempo (s)')
        ax2.set_ylabel('Controle')
    
    if current_time - start_time >= duration:
        print("Controle finalizado.")
        anim.event_source.stop()  # Para a animação quando o controle terminar

# Configurando o gráfico com Matplotlib
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Animação para atualizar o gráfico
anim = FuncAnimation(fig, update_plot, interval=int(period * 1000))

plt.tight_layout()
plt.show()
