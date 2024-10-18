import sys, os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import *
from ..guis.pid_control_arduino_widget import PID_Control_Arduino_Widget
from ..uis.ui_PyDAQ_pid_control_window_dialog import Ui_Dialog_Plot_PID_Window
from ..pid_control import PIDControl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PID_Control_Window_Dialog(QDialog, Ui_Dialog_Plot_PID_Window):
    def __init__(self, *args):
        super(PID_Control_Window_Dialog, self).__init__()
        self.setupUi(self)

#Starting the canvas
        self.figure = plt.figure(facecolor='#434544')
        self.canvas = FigureCanvas(self.figure)
        self.image_layout.addWidget(self.canvas)

#Calling the functions
        self.pushButton_close.clicked.connect(self.go_back)
    
    def set_parameters(self, kp, ki, kd, setpoint, unit, equation, period, duration,):
        self.kp = kp
        self.ki = ki
        self.kd = kd

#Defining the fuctions
    def go_back(self):
        self.close()
    
    def update_setpoint(self):
        try:
            new_setpoint = float(self.setpoint_input.text())
            if self.pid:
                self.pid.setpoint = new_setpoint
        except ValueError:
            pass  # Ignore invalid input

    def start_control(self,  Kp, Ki, Kd, setpoint, calibration_equation, unit, frequency):
        try:
            setpoint = float(setpoint)
            Kp = float(Kp)
            Ki = float(Ki)
            Kd = float(Kd)
            self.unit = unit
            self.pid = PID(Kp, Ki, Kd, setpoint, calibration_equation, self.unit)
            self.setpoints = []
            self.system_values = []
            self.errors = []
            self.period = 1/float(frequency)
            self.time_elapsed = 0.0
            self.ani = animation.FuncAnimation(self.figure, self.update_plot, frames=range(100), init_func=self.init_plot, blit=True, interval=self.period*1000)
            self.ax.set_xlabel('Time (s)')
            self.ax.set_ylabel(self.unit)
            self.ax.legend(['System Output', 'Setpoint'])
            plt.suptitle('PID Control')
            self.canvas.draw()
        except ValueError:
            print("Error")

    def init_plot(self):
        self.line1, = self.ax.plot([], [], 'o', label='System Output')  # Usar 'o' para pontos
        self.line2, = self.ax.plot([], [], '-', label='Setpoint')  # Usar 'o' para pontos
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-10, 10)
        return self.line1, self.line2

    def update_plot(self, frame):
        if self.pid is None:
            return self.line1, self.line2
        control, error = self.pid.update(self.system_value)
        self.system_value += control * 0.1
        self.system_values.append(self.system_value)
        self.errors.append(error)
#clock
        self.time_elapsed += self.period
        self.ax.set_xlim(0, self.time_elapsed)
        self.line1.set_data(np.arange(len(self.system_values)) * self.period, self.system_values)
        self.line2.set_data(np.arange(len(self.setpoints)) * self.period, self.setpoints)
#reloading the axes 
        self.ax.set_ylim(min(self.setpoints + self.system_values) - 1, max(self.setpoints + self.system_values) + 1)
        self.canvas.draw()
        return self.line1, self.line2