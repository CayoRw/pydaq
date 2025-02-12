import os
import time
import numpy as np

import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import warnings
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from scipy.signal import savgol_filter

class StepResponse(Base):
    """
     Class developed to construct Graphical User Interface for step
     response using arduino and NIDAQ boards

    :author: Samir Angelo Milani Martins
          - https://www.samirmartins.com.br
          - https://www.github.com/samirmartins/

     :params:
         device: nidaq default device.
         ao_channel: nidaq default analog output channel
         ai_channel: nidaq default analog input channel
         ts: sample period, in seconds.
         session_duration: session duration, in seconds.
         step_time: time when step will be applied, in seconds
         step_min: minimum step  value
         step_max: maximum step value
         terminal: 'Diff', 'RSE' or 'NRSE': terminal configuration (differential, referenced single ended or non-referenced single ended)
         plot: if True, plot data iteractively as they are sent/acquired
    """

    def __init__(
            self,
            device="Dev1",
            ao_channel="ao0",
            ai_channel="ai0",
            ts=0.5,
            session_duration=10.0,
            step_time=3.0,
            step_min=0,
            step_max=5,
            terminal="Diff",
            com="COM1",
            plot=True,
    ):

        super().__init__()
        self.ts = ts
        self.session_duration = session_duration
        self.plot = plot
        self.step_time = step_time
        self.device = device
        self.ai_channel = ai_channel
        self.ao_channel = ao_channel
        self.step_min = step_min
        self.step_max = step_max
        self.parameters = []
        self.sintony_type = None
        self.pid_parameters = False

        # Terminal configuration
        self.terminal = self.term_map[terminal]

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com  # Default COM port

        # Initializing variables
        self.time_var, self.input, self.output = [], [], []

        # Plot title
        self.title = None

        # Gathering nidaq info
        # self._nidaq_info()

        # Defining default path
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")

        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10

        # Arduino analog input max and min
        self.ard_ao_max, self.ard_ao_min = 5, 0

        # Value per bit - Arduino
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min) / ((2 ** self.arduino_ai_bits)-1)

        # Legends
        self.legend = ["Output", "Input"]

        # Saving data
        self.save = True

    def step_response_arduino(self):
        """
        This method performs the step response using an Arduino board for given parameters.

        :example:
            step_response_arduino()

        """

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Opening ports and serial communication
        self._open_serial()

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Step Response (Arduino), Port: {self.com_port}"
            self._start_updatable_plot()

        # Data to be sent
        sent_data = b"0"

        # Turning off the output before starting
        self.ser.write(b"0")

        # Main loop, where data will be sent/acquired
        for k in range(self.cycles):

            # Sending and acquiring data
            self.ser.write(sent_data)
            self.ser.reset_input_buffer()  # Reseting serial input buffer
            # Get the last complete value
            temp = int(self.ser.read(14).split()[-2].decode("UTF-8")) * self.ard_vpb

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            self.output.append(temp)
            self.input.append(5 * float(sent_data))
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the
                # for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except BaseException:
                    break

                # Updating data values
                self._update_plot(
                    [self.time_var, self.time_var], [self.output, self.input], 2
                )

            print(f"Iteration: {k} of {self.cycles - 1}")

            # Updating sent_data
            if k * self.ts >= float(self.step_time):
                sent_data = b"1"
            else:
                sent_data = b"0"

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Turning off the output at the end
        self.ser.write(b"0")
        # Closing port
        self.ser.close()

        if self.pid_parameters:
            Kp, Ki, Kd, time_inflection, sys_inflection, tangent_line, output_deslocated, gain_normalized = self.get_parameters(self.time_var, self.output,self.step_time,self.sintony_type,self.ard_ao_min,self.ard_ao_max)
            self.parameters = [Kp, Ki, Kd]
            print ('PID Parameters: ', self.parameters)
        # Check if data will or not be saved, and save accordingly
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.input, "input.dat")
            self._save_data(self.output, "output.dat")
            if self.parameters:
                self._save_data(self.parameters, "parameters.dat")
            print("\nData saved ...")
        
        if self.pid_parameters and self.plot:
            # Criando o gráfico
            plt.figure(figsize=(8, 5))
            plt.plot(self.time_var, output_deslocated, label="Output System", linewidth=2)
            plt.plot(self.time_var, tangent_line, '--', label="Tangent Line", linewidth=2, color='r')
            plt.plot(self.time_var, gain_normalized, label="Input System", linewidth=2)
            plt.scatter(time_inflection, sys_inflection, color='black', zorder=3, label="Inflection point")

            plt.xlabel("Time (s)")
            plt.ylabel("System Value")
            plt.legend()
            plt.grid(True)
            plt.title("Inflection curva in system")
            plt.show()
        return

    def step_response_nidaq(self):
        """
        This method performs the step response using a NIDAQ board for given parameters.

        :example:
            step_response_nidaq()

        """

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Initializing device, with channel defined
        task_ao = nidaqmx.Task()
        task_ai = nidaqmx.Task()
        task_ao.ao_channels.add_ao_voltage_chan(
            self.device + "/" + self.ao_channel,
            min_val=float(self.step_min),
            max_val=float(self.step_max),
        )
        task_ai.ai_channels.add_ai_voltage_chan(
            self.device + "/" + self.ai_channel, terminal_config=self.terminal
        )

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Step Response (NIDAQ). {self.device}, {self.ai_channel}, {self.ao_channel}"
            self._start_updatable_plot()

        # Data to be sent
        sent_data = self.step_min

        # Turning off the output before starting
        task_ao.write(sent_data)

        # Main loop, where data will be sent/acquired
        for k in range(self.cycles):

            # Sending and acquiring data
            task_ao.write(sent_data)
            temp = task_ai.read()

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            self.output.append(temp)
            self.input.append(float(sent_data))
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the
                # for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except BaseException:
                    break

                # Updating data values
                self._update_plot(
                    [self.time_var, self.time_var], [self.output, self.input], 2
                )

            print(f"Iteration: {k} of {self.cycles - 1}")

            # Updating sent_data
            if k * self.ts >= float(self.step_time):
                sent_data = self.step_max
            else:
                sent_data = self.step_min

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Turning off the output at the end
        task_ao.write(0)
        # Closing task
        task_ao.close()
        task_ai.close()

        if self.pid_parameters:
            Kp, Ki, Kd, time_inflection, sys_inflection, tangent_line, output_deslocated, gain_normalized = self.get_parameters(self.time_var, self.output,self.step_time,self.sintony_type,self.step_min,self.step_max)
            self.parameters = [Kp, Ki, Kd]
            print ('PID Parameters: ', self.parameters)

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.input, "input.dat")
            self._save_data(self.output, "output.dat")
            print("\nData saved ...")
            if self.parameters:
                self._save_data(self.parameters, "parameters.dat")
                print('PID also saved')

        if self.pid_parameters and self.plot:
            # Criando o gráfico
            plt.figure(figsize=(8, 5))
            plt.plot(self.time_var, output_deslocated, label="Output System", linewidth=2)
            plt.plot(self.time_var, tangent_line, '--', label="Tangent Line", linewidth=2, color='r')
            plt.plot(self.time_var, gain_normalized, label="Input System", linewidth=2)
            plt.scatter(time_inflection, sys_inflection, color='black', zorder=3, label="Inflection point")

            plt.xlabel("Time (s)")
            plt.ylabel("System Value")
            plt.legend()
            plt.grid(True)
            plt.title("Inflection curva in system")
            plt.show()

        return
    
    def get_parameters(self, time, system_value, step_time,type_sintony,min,max):
        
            time = np.array(time)
            # Getting the gain K
            
            system_value = np.array(system_value)  
            system_value = system_value - system_value[1]

            delta = (min - max)
            if delta == 0 or min == 0:
                k = (system_value[-1] - system_value[0]) / (max - 0)
            else:
                k = (system_value[-1] - system_value[0]) / (max - min)

            max_derivative_idx, derivative = self.get_max_derivative_idx(time, system_value, step_time)

            # Obtendo os valores correspondentes
            time_inflection = time[max_derivative_idx]
            sys_inflection = system_value[max_derivative_idx]

            # Ajustando reta tangente na inflexão
            slope = derivative[max_derivative_idx]
            intercept = sys_inflection - slope * time_inflection # Finding b by y(x)=ax+b ->  b = y(x)-ax
            tangent_line = slope * time + intercept  # y=ax+b
            #print('y=ax+b:', tangent_line,' = ',slope,' * x + ',intercept)
            # Encontrando L e T
            L = (-step_time + (-intercept / slope)) # L shoud be 0=ax+b -> x = -b/a. But we also have 
            T =  ((k - intercept) / slope)  - (-intercept / slope) # T here is the time the line hits the gain minus the time the line hit the 0
            #print(f"L: {L}, T: {T}")
            # y = ax+b; 
            # y = k;  { x = (k-b)/a
            # y = 0;  { x = -b/a
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

            # Exibindo os parâmetros calculados
            print(f"Kp: {Kp:.4f}, Ki: {Ki:.4f}, Kd: {Kd:.4f}, T: {T:.4f}, L: {L:.4f}")

            gain_normalized = np.where(time < step_time, 0, k)
            
            return Kp, Ki, Kd, time_inflection, sys_inflection, tangent_line, system_value, gain_normalized

    def get_max_derivative_idx(self, time, system_value, step_time, window_size=11, polyorder=2):
        time = np.array(time)
        system_value = np.array(system_value)

        # Suavização dos dados para evitar picos espúrios
        system_value_smooth = savgol_filter(system_value, window_size, polyorder)
        
        # Cálculo da derivada após suavização
        derivative = np.gradient(system_value_smooth, time)

        # Garantir que buscamos o máximo da derivada apenas para t >= step_time
        valid_indices = time >= step_time  # Máscara booleana para o intervalo válido
        derivative_valid = derivative[valid_indices]  # Aplicando a máscara na derivada
        time_valid = time[valid_indices]  # Aplicando a máscara no tempo
        
        # Encontrar o índice do máximo valor absoluto da derivada no intervalo válido
        max_derivative_local_idx = np.argmax(np.abs(derivative_valid))
        max_derivative_idx = np.where(valid_indices)[0][max_derivative_local_idx]  # Convertendo índice relativo para o original
        
        return max_derivative_idx, derivative
