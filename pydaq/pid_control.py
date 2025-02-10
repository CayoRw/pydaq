import os
import time
import numpy as np
import sympy as sp
from scipy.signal import dlti, dlsim
import scipy.signal as signal
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import warnings
import nidaqmx
from sympy import symbols, parse_expr
from nidaqmx.constants import TerminalConfiguration

class PIDControl(Base):
    def __init__(
        self, 
        Kp, 
        Ki, 
        Kd, 
        setpoint=0.0, 
        numerator = '1',
        denominator = 's+0.2',
        calibration_equation_vu = None, 
        calibration_equation_uv = None,
        unit='Voltage (V)', 
        period=1
        ):
        super().__init__() #Inicializating the matematical control
        self.Kp = float(Kp)
        self.Ki = float(Ki)
        self.Kd = float(Kd)
        self.disturbe = 0
        self.setpoint = float(setpoint)
        self.numerator = numerator
        self.denominator = denominator
        self.calibration_equation_vu = calibration_equation_vu
        self.calibration_equation_uv = calibration_equation_uv
        self.integral = 0.0
        self.previous_error = 0.0
        self.previous_output = 0.0
        self.period = period
        self.device = "Dev1" # To nidaq
        self.ao_channel="ao0"
        self.ai_channel="ai0"
        self.terminal="Diff"
        self.com_port = 'COM1' # To arduino  # Default COM port
        self.a = 0.2 # To simulated

    def update(self, feedback_value):
        self.setpoint_calibrated = self.calibrationvu(self.setpoint)
        error = self.setpoint_calibrated - feedback_value
        self.integral = self.integral + error * self.period
        derivative = (error - self.previous_error) / self.period
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        #print('Output = ', self.Kp,' * ', error, ' + ', self.Kd , ' * ', derivative, ' = ', output)
        self.previous_error = error
        self.previous_output = output
        return output, error

    def pid_control_arduino(self):
        self.setpoints = []
        self.system_values = []
        self.errors = []
        self.controls = []
        self.time_var = [] 
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = self.setpoint
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()] # COM ports
        self._open_serial() # Oppening ports
        self.arduino_ai_bits = 10 # Arduino ADC resolution (in bits)
        self.ard_ao_max, self.ard_ao_min = 5, 0 # Arduino analog input max and min
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min) / ((2 ** self.arduino_ai_bits)-1) # Value per bit - Arduino
        self.ser.reset_input_buffer()
        time.sleep(1)  # Wait for Arduino and Serial to start up
        self.title = f"PYDAQ - Step Response (Arduino), Port: {self.com_port}" # Start updatable plot

# Updating the Datas to plot
    def update_plot_arduino(self):
        if self.ser.in_waiting > 64:  # If there's more than 64 bits accumulated
            self.ser.reset_input_buffer()
        self.time_elapsed += self.period # Clock
        data = self.ser.read(14).decode("UTF-8") # Get the feedback sensor value
        try:
            self.feedback_value =  int(data.split()[-2]) * self.ard_vpb
        except (IndexError, ValueError):
            print('using the last data value ',self.feedback_value)
            self.feedback_value = self.feedback_value # Use the last valid value
        self.control_no_calibrated, error = self.update(self.feedback_value) # Get the control value
        self.control = self.calibrated_control(self.control_no_calibrated)
        if(self.control <= 0):
            self.control = 0
        elif (self.control >=5):
            self.control = 5
        self.duty_cycle_control = int((self.control/self.ard_ao_max) *255) # Change to a duty cicle
        self.ser.write(f"{self.duty_cycle_control}\n".encode("utf-8")) # Send data to arduino 
        print(f"Control (V): {self.control:.2f}, Duty Cycle (0-255): {self.duty_cycle_control}, Feedback: {self.feedback_value:.2f}")
        self.feedback_calibrated = self.calibrationuv(self.feedback_value)
        self.error_calibrated = self.calibrationuv(error)
        self.errors.append(self.error_calibrated) # Queue data in a list
        self.system_values.append(self.feedback_calibrated)
        self.setpoints.append(self.setpoint)
        self.controls.append(self.control)
        self.time_var.append(self.time_elapsed)
        return self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed, self.controls

    def pid_control_nidaq(self): #Inicializating the updating nidaq values
        terminal_config = self.terminal # Terminal configuration
        self._nidaq_info() # Gathering nidaq info
        self.task_ai = nidaqmx.Task()
        self.task_ao = nidaqmx.Task()   
        self.task_ai.ai_channels.add_ai_voltage_chan(
            self.device + "/" + self.ai_channel, terminal_config=terminal_config
        )
        self.task_ao.ao_channels.add_ao_voltage_chan(
            self.device + "/" + self.ao_channel,
            min_val=0.0,  # Max value to usb 6009
            max_val=5.0   # Max value to usb 6009
        )
        self.setpoints = []
        self.system_values = []
        self.errors = []
        self.controls = []
        self.time_var = [] 
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = 0

    def update_plot_nidaq(self):
        self.time_elapsed += self.period # Clock
        self.feedback_value = self.task_ai.read()
        self.control, error = self.update(self.feedback_value) # Get the control value
        if(self.control <= 0):
            self.control = 0
        elif (self.control >=5):
            self.control = 5
        self.task_ao.write(self.control)
        print ('Time = ',self.time_elapsed,'Control: ', self.control, '; Feedback: ',self.feedback_value)
        self.feedback_calibrated = self.calibrationuv(self.feedback_value)
        self.error_calibrated = self.calibrationuv(error)
        self.controls.append(self.control) # Att the datas
        self.errors.append(self.error_calibrated)
        self.system_values.append(self.feedback_calibrated)
        self.setpoints.append(self.setpoint)
        self.time_var.append(self.time_elapsed)
        return self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed, self.controls

    def simulate_system(self):
        self.setpoints = []
        self.system_values = []
        self.feedback_list = []
        self.errors = []
        self.controls = []
        self.time_var = [] 
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = 0

        numerator_cont = self.parse_polynomial(self.numerator)
        denominator_cont = self.parse_polynomial(self.denominator)
        
        print(f"Coeficientes do numerador: {numerator_cont}")
        print(f"Coeficientes do denominador: {denominator_cont}")

        self.system_cont = signal.TransferFunction(numerator_cont, denominator_cont)

    def update_simulated_system(self):
        ordem = max(len(self.feedback_list), len(self.controls))  # Estimativa da ordem do sistema
        while len(self.feedback_list) < ordem:
            self.feedback_list.insert(0, 0.0)  # Preenche com zeros
        while len(self.controls) < ordem:
            self.controls.insert(0, 0.0)

        _, self.system_value = self.get_value_simulate_system(self.system_cont, self.period, self.control, self.feedback_value)  # Get the system response value by euler descritization of system
        # Print ('System value = ', self.system_value )
        self.feedback_value = self.system_value         # Get the feedback sensor value
        self.time_elapsed += self.period # Clock
        self.controls.append(self.control)         # Att the datas
        self.control, error = self.update(self.feedback_value)         # Get control value
        self.control = self.control - self.disturbe
        self.feedback_calibrated = self.calibrationuv(self.feedback_value)
        self.error_calibrated = self.calibrationuv(error)
        self.errors.append(self.error_calibrated)
        #print('self.feedback_calibrated after self.calibration(self.feedback_value) -> ', self.feedback_calibrated, ' do tipo ', type(self.feedback_calibrated))
        self.feedback_list.append(self.feedback_value)
        self.system_values.append(self.feedback_calibrated)
        self.setpoints.append(self.setpoint)
        self.time_var.append(self.time_elapsed)
        return self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed, self.controls

    #def system_output(self, y_prev, control): # System type 1/s+a
    #    return (self.period * control + y_prev) / (1 + self.period * self.a) # Discretization by euler

    def calibrationvu(self, output):
        #print('A funcao foi chamada com ', output, 'e com a equacao ', self.calibration_equation_vu, 'do tipo ', type(output), ', ', type(self.calibration_equation))
        if not self.calibration_equation_vu.strip():
            #print ('self.calibration_equation is ', self.calibration_equation_vu)
            return output
        else:
            equation = parse_expr(self.calibration_equation_vu)
            #print('equation after parse_expr -> ', equation)
            output_calibrated = equation.subs('x', output) # X is the variable used
            #print('output_calibrated after equation.subs -> ', output_calibrated, ' do tipo ', type(output_calibrated))
            output_calibrated = float(output_calibrated)
            return output_calibrated

    def calibrationuv(self, output):
        #print('A funcao foi chamada com ', output, 'e com a equacao ', self.calibration_equation_uv, 'do tipo ', type(output), ', ', type(self.calibration_equation_uv))
        if not self.calibration_equation_uv.strip():
            #print ('self.calibration_equation is ', self.calibration_equation_uv)
            return output
        else:
            equation = parse_expr(self.calibration_equation_uv)
            #print('equation after parse_expr -> ', equation)
            output_calibrated = equation.subs('x', output) # X is the variable used
            #print('output_calibrated after equation.subs -> ', output_calibrated, ' do tipo ', type(output_calibrated))
            output_calibrated = float(output_calibrated)
            return output_calibrated

    def parse_polynomial(self,poly_str):
        s = sp.symbols('s')
        poly_expr = sp.sympify(poly_str)
        coeffs = sp.Poly(poly_expr, s).all_coeffs()
        return [float(c) for c in coeffs]

    def get_value_simulate_system(self, system, period, control, x0):
        
        time_control = np.linspace(0, period, 100)  
        input_control_signal = np.full_like(time_control, control)
        time_array_output, system_output, _ = signal.lsim(system, input_control_signal, time_control,x0)
        last_time = time_array_output[-1]
        last_output = system_output[-1]
        print('Control: ', input_control_signal[1], 'System value: ', last_output, 'Time: ', last_time)
        return last_time, last_output

    def control_no_calibrated(self, control):
        return 3.4157*control^2 + -12.7914*control + 11.8828
