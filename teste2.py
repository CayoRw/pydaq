import numpy as np
import scipy.signal as signal
import sympy as sp

def parse_polynomial(poly_str):
    s = sp.symbols('s')
    poly_expr = sp.sympify(poly_str)
    coeffs = sp.Poly(poly_expr, s).all_coeffs()
    return [float(c) for c in coeffs]

# Função para determinar a ordem do polinômio
def get_order(poly_str):
    s = sp.symbols('s')
    poly_expr = sp.sympify(poly_str)
    return sp.degree(poly_expr, s)

# Definição do numerador e denominador
numerador_str = '1'  # Pode ser de qualquer grau, como 2*s**2 + 3*s + 1, etc.
denominador_str = 's + 0.1'  # Também pode ser de qualquer grau, como 3*s**2 + 4*s + 2, etc.

numerador = parse_polynomial(numerador_str)
denominador = parse_polynomial(denominador_str)

# Exibindo os coeficientes do numerador e denominador
print(f"Coeficientes do numerador: {numerador}")
print(f"Coeficientes do denominador: {denominador}")

# Amostragem e transformação bilinear
T = 0.01
numerador_discreto, denominador_discreto = signal.bilinear(numerador, denominador, fs=1/T)

# Exibindo os coeficientes discretizados
print("Numerador discreto:", numerador_discreto)
print("Denominador discreto:", denominador_discreto)

# Inicializando as listas de entrada (u_k) e saída (y_k)
y_k = [0] * 50  # Lista para valores de saída (10 valores)
u_k = [1] * 50  # Lista para valores de entrada (10 valores)

# Laço para calcular os valores de y_k com base em u_k
for k in range(max(len(numerador_discreto), len(denominador_discreto)), len(u_k)):
    # Calculando a saída y_k de forma generalizada
    y_k[k] = sum([numerador_discreto[i] * u_k[k - i - 1] for i in range(len(numerador_discreto))]) - \
              sum([denominador_discreto[i] * y_k[k - i - 1] for i in range(1, len(denominador_discreto))])

    # Exemplo: alterando u_k para uma entrada variável
    u_k[k] = 1  # Você pode mudar isso conforme necessário

# Exibindo os resultados
print("Valores de y_k:", y_k)
print("Valores de u_k:", u_k)

def get_system_value()