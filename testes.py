import numpy as np

def simple_discrete_control(period: float, y_prev: list, u_prev: list, control: float) -> float:
    # Simples modelo discreto de controle: y[k+1] = a * y[k] + b * u[k]
    a = 0.5  # Coeficiente de amortecimento (pode ser ajustado)
    b = 1.0  # Coeficiente de ganho do controle (pode ser ajustado)
    
    # Calcular a saída y[k+1] com base na entrada control (u[k])
    y_new = a * y_prev[-1] + b * control  # Saída dependente da entrada de controle
    
    return y_new

# Exemplo de teste
period = 1.0
y_prev = [0.0]
u_prev = [0.0]
controls = [0, 1, 2, 3, 4, 5]
outputs = []

for control in controls:
    y_k = simple_discrete_control(period, y_prev, u_prev, control)
    y_prev.append(y_k)
    y_prev = y_prev[-1:]  # Mantém apenas o último valor de y
    u_prev.append(control)
    u_prev = u_prev[-1:]  # Mantém apenas o último valor de u
    outputs.append(y_k)

print("\nOutputs finais:", outputs)