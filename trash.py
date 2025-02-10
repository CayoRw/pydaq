print('hello')
#    def discrete_euler(self, numerador: str, denominador: str, period: float, y_prev: float, control: float) -> float:
#        s = sp.symbols('s')
#        num_expr = sp.sympify(numerador)
#        den_expr = sp.sympify(denominador)
#        H_s = num_expr / den_expr  
#        H_s_discrete = H_s.subs(s, (1 - sp.exp(-period)) / period)  
#        output_expr = H_s_discrete * control
#        output = float(output_expr.evalf()) 
#        return output
    
#    def discrete_tustin(self, numerador: str, denominador: str, period: float, y_prev: list, u_prev: list, control: float) -> float:
#        s = sp.symbols('s')
#        num_expr = sp.sympify(numerador)
#        den_expr = sp.sympify(denominador)
#        H_s = num_expr / den_expr  # Função de transferência no contínuo
#
#        # Transformada bilinear: s ≈ (2/T) * (z - 1) / (z + 1)
#       s_tustin = (2/period) * (z - 1) / (z + 1)
#        H_z = H_s.subs(s, s_tustin).simplify()  # Discretização
#
#        # Obter coeficientes do numerador e denominador
#        H_z = sp.simplify(H_z)
#        num, den = sp.fraction(H_z)
#        num_coeffs = sp.Poly(num, z).all_coeffs()
#        den_coeffs = sp.Poly(den, z).all_coeffs()#

        # Converter para valores numéricos
#        num_coeffs = [float(c) for c in num_coeffs]
#        den_coeffs = [float(c) for c in den_coeffs]

        # Normalizar os coeficientes pelo primeiro coeficiente do denominador
#        a0 = den_coeffs[0]
#        num_coeffs = [c / a0 for c in num_coeffs]
#        den_coeffs = [c / a0 for c in den_coeffs]

        # Garantir que y_prev e u_prev tenham o tamanho correto
#        ordem = len(den_coeffs) - 1  # Ordem do sistema
#        while len(y_prev) < ordem:
#            y_prev.insert(0, 0.0)  # Preenche com zeros se necessário
#        while len(u_prev) < ordem:
#            u_prev.insert(0, 0.0)

        # Aplicar a equação de diferenças
#        y_k = sum(b * u for b, u in zip(num_coeffs, [control] + u_prev)) - sum(a * y for a, y in zip(den_coeffs[1:], y_prev))

#        return y_k

#   def discrete_dlsim(self, numerador: str, denominador: str, period: float, y_prev: list, y_prev2: float, u_prev: list, control: float) -> float:
        # Criar a variável simbólica para o operador 's'
 #       s = sp.symbols('s')
 #       period = 0.1
 #       # Definir os numeradores e denominadores da função de transferência contínua
 #       num_expr = sp.sympify(numerador)
 #       den_expr = sp.sympify(denominador)
        
        # Função de transferência no contínuo H(s)
#        H_s = num_expr / den_expr
        
        # Transformação bilinear: s ≈ (2/T) * (z - 1) / (z + 1)
#        z = sp.symbols('z')
#        s_tustin = (2 / period) * (z - 1) / (z + 1)
#
        # Substituir s por s_tustin para obter a função de transferência discreta H(z)
 #       H_z = H_s.subs(s, s_tustin).simplify()

        # Obter os coeficientes do numerador e denominador da função de transferência discreta H(z)
  #      num, den = sp.fraction(H_z)
   #     num_coeffs = sp.Poly(num, z).all_coeffs()
    #    den_coeffs = sp.Poly(den, z).all_coeffs()
        
        # Converter para valores numéricos
    #    num_coeffs = [float(c) for c in num_coeffs]
    #    den_coeffs = [float(c) for c in den_coeffs]
        
        # Normalizar os coeficientes pelo primeiro coeficiente do denominador
    #    a0 = den_coeffs[0]
    #    num_coeffs = [c / a0 for c in num_coeffs]
    #    den_coeffs = [c / a0 for c in den_coeffs]
        
        # Garantir que y_prev e u_prev tenham o tamanho correto
     #   ordem = len(den_coeffs) - 1  # Ordem do sistema
     #   while len(y_prev) < ordem:
     #       y_prev.insert(0, 0.0)  # Preenche com zeros se necessário
    #    while len(u_prev) < ordem:
    #        u_prev.insert(0, 0.0)
        
        # Criar o sistema discreto usando o scipy.dlti (com coeficientes do numerador e denominador)
   #     sysd = dlti(num_coeffs, den_coeffs)
        
        # Definir o vetor de tempo para a simulação
   #     t_step = [0, period]  # Passo de tempo para cada atualização
   #     u_step = [u_prev[-1], control]  # Entrada constante durante o intervalo

    #    x0=y_prev2

        # Simular a resposta do sistema utilizando o dlsim
     #   y_step, x = dlsim(sysd, u_step, t_step, x0)  # Simular resposta (x0 é o estado anterior)
        
        # Retornar o valor da saída y[k] após o passo de simulação
     #   return y_step[-1]

'''
    def zero_order_hold(self, current_time_step, hold_time, new_output):
        if current_time_step % hold_time == 0:
            return new_output
        else:
            return self.previous_output
'''


'''Implementação do PID em tempo discreto
    def pid_controller(setpoint, y, Kp, Ki, Kd, integral_prev, error_prev, T):
        error = setpoint - y
        integral = integral_prev + error * T
        derivative = (error - error_prev) / T
        output = Kp * error + Ki * integral + Kd * derivative
        return output, integral, error'''