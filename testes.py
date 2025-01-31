import sympy as sp

def discrete_euler(numerador: str, denominador: str, period: float, y_prev: float, control: float) -> float:
    s = sp.symbols('s')

    # Criar função de transferência
    num_expr = sp.sympify(numerador)
    den_expr = sp.sympify(denominador)

    H_s = num_expr / den_expr  # Função de transferência H(s)

    # Aproximação de Euler: s ≈ (y[k] - y[k-1]) / T
    H_s_discrete = H_s.subs(s, (1 - sp.exp(-period)) / period)  

    # Multiplicar pelo controle (entrada do sistema)
    output_expr = H_s_discrete * control

    # Avaliar a expressão numérica para obter a saída
    output = float(output_expr.evalf()) + y_prev  # Aproximação da resposta

    return output

# Definição dos parâmetros
setpoint = 5
numerador = 's+3'   
denominador = 's**2+10*s+20'
period = 0.05
saida = 0
y_prev = 0
Kp = 10
Kd = 1
error = setpoint - saida
control = error * Kp + (saida - y_prev) * Kd
count = 0

while count <= 100:    
    # Cálculo da saída
    saida = discrete_euler(numerador, denominador, period, y_prev, control)
    error = setpoint - saida
    control = error * Kp + (saida - y_prev) * Kd
    print(saida)
    y_prev = saida
    count += 1