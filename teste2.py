import numpy as np
import matplotlib.pyplot as plt

def get_parameters(time, voltage, system_value, step_time,type_sintony):
    # Estimativa do ganho estático k
    k = (system_value[-1] - system_value[0]) / (voltage[-1] - 0)

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
    
    # Encontrando L e T
    L = (step_time - (-intercept / slope)) if step_time > 0 else (-intercept / slope)
    T = (k - intercept) / slope - step_time - L  # Ajuste para `step_time`
    print(f"L: {L}, T: {T}")

    if type_sintony == 0:  # P Controler
        Kp = (T / L)
        Ki = 0
        Kd = 0
    elif type_sintony == 1: # PI Controler
        Kp = 0.9 * (T / L)
        Ti = L / 0.3 
        Ki = Kp / Ti
        Kd = 0
    elif type_sintony == 2: # PID Controler
        Kp = 1.2 * (T / L)
        Ti = 2 * L
        Ki = Kp / Ti
        Td = 0.5 * L
        Kd = Kp * Td

    return Kp, Ki, Kd, slope, intercept, time_inflection, sys_inflection


pid_parameters = True

# Lista corrigida para o tempo (time)
time = [
    1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
    11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0,
    21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30, 31, 32, 33
]

# Lista corrigida para a voltagem (voltage)
voltage = [10.0] * len(time)  # Criando uma lista de 10.0 com o mesmo tamanho de `time`

# Lista corrigida para os valores do sistema (system_value)
system_value = [
    0.0, 0, 0, 0, 0, 2.4000000000000004, 3.8240000000000003, 5.0022400000000005, 5.954662400000001,
    6.725633024, 7.3496675942400005, 7.8547726925824, 8.263613950132223, 8.594537509803786,
    8.862393065456166, 9.079200230138838, 9.254687897523764, 9.396730811323613,
    9.511702932506896, 9.604763461158186, 9.680088347780497, 9.741057682759505,
    9.790407372808446, 9.830351910644799, 9.862683747002384, 9.888853724147603,
    9.910036180232275, 9.927181645942433, 9.94105949812554, 9.952292484413107,
    9.961384668078983, 9.968744047116552, 9.974700862531739
]

# Definição de valores adicionais
step_time = 5
type_sintony = 0

# Verifica se deve calcular os parâmetros do PIDs
if pid_parameters:
    # A função `get_parameters` precisa ser implementada!
    try:
        Kp, Ki, Kd, slope, intercept, time_inflection, sys_inflection = get_parameters(time, voltage, system_value, step_time, type_sintony)
        parameters = [Kp, Ki, Kd]
        print (parameters)
    except NameError:
        print("Erro: A função get_parameters não foi definida.")
        parameters = None
else:
    parameters = 0

setpoint = voltage[0]

# Tangent Line (y = mx + b)
tangent_line = [slope * t + intercept for t in time]

# Plotting
plt.plot(time, system_value, 'o', label="System Response")
plt.plot(time, tangent_line, label="Tangent Line at Inflexion", linestyle='--')
plt.axhline(y=setpoint, color='r', linestyle='-', label=f"Setpoint ({setpoint})")
plt.xlabel('Time (s)')
plt.ylabel('System Value')
plt.title(f'System Response vs PID Model (Kp={Kp:.2f}, Ki={Ki:.2f}, Kd={Kd:.2f})')
plt.legend()
plt.grid(True)
plt.show()