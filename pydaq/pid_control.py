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
    def __init__(self, Kp, Ki, Kd, setpoint=0.0, calibration_equation=None, unit='Voltage (V)', period=1):
        self.Kp = float(Kp)
        self.Ki = float(Ki)
        self.Kd = float(Kd)
        self.setpoint = float(setpoint)
        self.integral = 0.0
        self.previous_error = 0.0
        self.previous_output = 0.0
        self.T = period
        self.hold_time = period
#need to review
    def update(self, feedback_value, current_time):
        error = self.setpoint - feedback_value
        self.integral += error * self.T
        derivative = (error - self.previous_error) / self.T
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        #output = self.zero_order_hold(current_time, self.hold_time)
        self.previous_error = error
        self.previous_output = output
        
        return output

'''
    def zero_order_hold(self, current_time_step, hold_time):
        if current_time_step % hold_time == 0:
            return self.previous_output
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