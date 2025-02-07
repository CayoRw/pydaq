import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sympy as sp

# Função para calcular a resposta do sistema à entrada
def get_system_value(entrada_signal, tempo, sistema):
    # Calculando a resposta do sistema à entrada
    tempo_resposta, resposta, _ = signal.lsim(sistema, entrada_signal, tempo)
    
    # Retornando o último tempo e a última resposta
    tempo_resposta1 = tempo_resposta[-1]
    resposta1 = resposta[-1]
    return tempo_resposta1, resposta1

def parse_polynomial(poly_str):
    s = sp.symbols('s')
    poly_expr = sp.sympify(poly_str)
    coeffs = sp.Poly(poly_expr, s).all_coeffs()
    return [float(c) for c in coeffs]


# Definindo a função de transferência G(s) = 1 / (s + 1)
numerador_str = '10'
denominador_str = '1*s^2 + 10'

numerador = parse_polynomial(numerador_str)
denominador = parse_polynomial(denominador_str)

sistema = signal.TransferFunction(numerador, denominador)



# Inicializando a entrada no valor 0
entrada1 = 0
# Listas para armazenar os tempos e respostas
tempo_resposta2 = []
resposta2 = []
entrada_total = []  # Lista para armazenar os valores de entrada em cada ciclo
periodo = 1
tempo_resposta = 0
tempo = np.linspace(0, 0.2, 1000)
# Laço de repetição para variar a entrada a cada ciclo
for i in range(10):
    periodo = 1
    # Definindo o tempo de simulação
    # Criando a entrada degrau variável (um degrau por 1 segundo)
    entrada_signal = np.full_like(tempo, entrada1)
    print(len(entrada_signal), entrada_signal[1], entrada_signal[-1])
    # Calculando a resposta do sistema à entrada
    inutil, resposta = get_system_value(entrada_signal, tempo, sistema)
    tempo_resposta = tempo_resposta + periodo
    # Armazenando o último tempo e resposta
    tempo_resposta2.append(tempo_resposta)
    resposta2.append(resposta)
    
    # Armazenando a entrada no total
    entrada_total.extend([entrada1] * len(tempo))  # Estendendo a entrada total

    # Atualizando a entrada para o próximo valor
    if entrada1 < 6:
        entrada1 = entrada1 +2   # Incrementando a entrada por 1 a cada ciclo
    else:
        entrada1 = 0

# Plotando a resposta final
plt.plot(tempo_resposta2, resposta2, label='Resposta do Sistema')

# Plotando os valores de resposta1 como 'x'
plt.scatter(tempo_resposta2, resposta2, color='r', marker='x', label='Valores de Resposta')

# Exibindo a entrada (degraus variáveis)
plt.step(np.linspace(0, 10, len(entrada_total)), entrada_total, where='post', label='Entrada (Degrau)', linestyle='--', color='b')

plt.xlabel('Tempo (segundos)')
plt.ylabel('Saída')
plt.title('Resposta de um Sistema Contínuo a Entrada Degrau Variada')
plt.legend()
plt.grid(True)
plt.show()