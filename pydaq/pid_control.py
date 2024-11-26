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

class PIDControl(Base):
    def __init__(
        self, 
        Kp, 
        Ki, 
        Kd, 
        setpoint=0.0, 
        calibration_equation=None, 
        unit='Voltage (V)', 
        period=1,
        com="COM1",
        ):
        super().__init__()

#Inicializating the matematical control
        self.Kp = float(Kp)
        self.Ki = float(Ki)
        self.Kd = float(Kd)
        self.disturbe = 0
        self.setpoint = float(setpoint)
        self.integral = 0.0
        self.previous_error = 0.0
        self.previous_output = 0.0
        self.period = period
        
        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com  # Default COM port
        
#       self.hold_time = period
#defining the a in "H(s) = 1/s+a"
        self.a = 0.1
#Inicializating the updating plot

#need to review
    def update(self, feedback_value):
        #self.setpoint_update = self.setpoint - self.disturbe
        error = self.setpoint - feedback_value
        self.integral = self.integral + error * self.period
        derivative = (error - self.previous_error) / self.period
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        #print('Output = ', self.Kp,'*', error)
        #output = self.zero_order_hold(current_time, self.hold_time, output)
        self.previous_error = error
        self.previous_output = output
        
        return output, error

# Updating the datas to plot
    def update_plot_arduino(self):

        # Counting time to append data and update interface
        st = time.time()

        self.ser.reset_input_buffer()

        # Get the feedback sensor value
        self.time_elapsed += self.period # Clock
        
        # Get the control value
        self.control, error = self.update(self.feedback_value)
        self.control = self.control - self.disturbe

        # Sending and acquiring data
        self.ser.write(f"{self.control:.2f}\n".encode("utf-8"))

        data = self.ser.read(14).decode("UTF-8").strip()
        try:
            self.feedback_value = int(data.split()[-2]) * self.ard_vpb
        except (IndexError, ValueError):
            self.feedback_value = self.feedback_value # Use o último valor válido

        # Queue data in a list
        self.output.append(self.feedback_value)
        self.input.append(5 * float(self.control))

        # Att the datas
        self.errors.append(error)
        self.system_values.append(self.feedback_value)
        self.setpoints.append(self.setpoint)
        self.time_var.append(self.time_elapsed)

        # Getting end time
        et = time.time()
        next_time = st + self.period
        while time.time() < next_time:
            pass

        # Wait for (period - delta_time) seconds
        try:
            time.sleep(self.period + (st - et))
        except BaseException:
            warnings.warn(
                "Time spent to append data and update interface was greater than ts. "
                "You CANNOT trust time.dat"
            )

        return self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed
    
    def pid_control_arduino(self):
        self.setpoints = []
        self.system_values = []
        self.errors = []
        self.datas = []
        self.time_var = [] 
        self.output = []
        self.input = []
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = 0

        # Oppening ports
        self._open_serial()
        
        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = self.com  # Default COM port
        
        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10
        # Arduino analog input max and min
        self.ard_ao_max, self.ard_ao_min = 5, 0
        # Value per bit - Arduino
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min) / ((2 ** self.arduino_ai_bits)-1)
        
        # Turning off the output before starting
        self.ser.write(b"0")
        
        time.sleep(2)  # Wait for Arduino and Serial to start up
        # Start updatable plot
        self.title = f"PYDAQ - Step Response (Arduino), Port: {self.com_port}"

        
    def pid_control_nidaq(self):
        self.setpoints = []
        self.system_values = []
        self.errors = []
        self.datas = []
        self.time_var = [] 
        self.output = []
        self.input = []
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = 0

    def update_plot_nidaq(self):
        
        # Get the system response value
        self.system_value = self.system_output(self.feedback_value, self.control)
        # Print ('System value = ', self.system_value )
        # Get the feedback sensor value
        self.feedback_value = self.system_value
        self.time_elapsed += self.period # Clock
        # Get the control value
        self.control, error = self.update(self.feedback_value)
        self.control = self.control - self.disturbe

        # Att the datas
        self.errors.append(error)
        self.system_values.append(self.feedback_value)
        self.setpoints.append(self.setpoint)
        self.time_var.append(self.time_elapsed)

        return self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed

# System type 1/s+a
    def system_output(self, y_prev, control):
# Discretization by euler
        return (self.period * control + y_prev) / (1 + self.period * self.a)
'''
        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10

        # Arduino analog input max and min
        self.ard_ai_max, self.ard_ai_min = 5, 0

        # Value per bit - Arduino
        self.ard_vpb = (self.ard_ai_max - self.ard_ai_min) / ((2 ** self.arduino_ai_bits)-1)
'''
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