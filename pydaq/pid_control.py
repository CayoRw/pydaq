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
    def __init__(self, Kp, Ki, Kd, setpoint=0, calibration_equation=None, unit='Voltage (V)'):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.unit = unit
        self.calibration_equation = calibration_equation
        self.integral = 0
        self.previous_error = 0

    def update(self, feedback_value):
        error = self.setpoint - feedback_value
        self.integral += error
        derivative = error - self.previous_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output, error