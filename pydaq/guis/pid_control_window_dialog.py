import sys, os
import serial
import serial.tools.list_ports
import numpy as np
import time
from pydaq.utils.base import Base
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import *
from ..uis.ui_PyDAQ_pid_control_window_dialog import Ui_Dialog_Plot_PID_Window
from ..pid_control import PIDControl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PID_Control_Window_Dialog(QDialog, Ui_Dialog_Plot_PID_Window, Base):
    def __init__(self, *args):
        super(PID_Control_Window_Dialog, self).__init__()
        self.setupUi(self)
        self.setGeometry(200, 200, 1000, 600)
#Calling the functions
        self.pushButton_startstop.clicked.connect(self.stopstart)
        self.pushButton_close.clicked.connect(self.go_back)
        self.pushButton_apply.clicked.connect(self.apply_parameters)

#variable for control
        self.system_value = 0.0
        self.paused = False
        self.setpoints = []
        self.system_values = []
        self.start_time = time.time()
        self.pid = None
#defining the a in H(s) = 1/s+a
        self.a = 0.1

#to save the data path
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop") # Defining default path
        self._check_path()

#Starting the canvas
        self.figure = plt.figure(facecolor='#404040')
        self.ax = self.figure.add_subplot(111, facecolor='#404040')  # Output graph
        self.canvas = FigureCanvas(self.figure)
        self.image_layout.addWidget(self.canvas)

#Defining the fuctions
    def set_parameters(self, kp, ki, kd, setpoint, unit, equation, period, duration):
        self.kp = kp if kp else 1
        self.ki = ki if ki else 0
        self.kd = kd if kd else 0
        self.setpoint = setpoint if setpoint else 0.0
        self.unit = unit if unit else 'Voltage (V)'
        self.calibration_equation = equation
        self.period = period if period else 1 
        self.duration = duration if duration else 10
        print('kp ', self.kp)
        print('ki ', self.ki)
        print('kd ', self.kd)
        print('Setpoint ', self.setpoint)
        print('unit ', self.unit)
        print('equation ', self.calibration_equation)
        print('period ', self.period)
        print('Duration ', self.duration)
        self.start_control(self.kp, self.ki, self.kd, self.setpoint, self.calibration_equation, self.unit, self.period)

    def go_back(self):
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.data, "data.dat")
            print("\nData saved ...")
        self.ani.event_source.stop()
        self.close()

    def stopstart (self):
        self.paused = not self.paused
        if self.paused:
            self.ani.event_source.stop()
            self.pushButton_startstop.setText("Start")
        else:
            self.ani.event_source.start()
            self.pushButton_startstop.setText("Stop")

    def apply_parameters(self):
        try:
            new_setpoint = self.doubleSpinBox_SetpointDialog.value()
            self.setpoint = new_setpoint
            print ('The new setpoint is ', new_setpoint)
            if self.pid:
                self.pid.setpoint = new_setpoint
                print ('The setpoint has been sended to pid control')
        except ValueError:
            pass  # Ignore invalid input  
        self.disturbe = self.doubleSpinBox_DisturbeDialog.value()
        print ('The new disturbe is ', self.disturbe)

    def start_control(self, Kp, Ki, Kd, setpoint, calibration_equation, unit, period):
        try:
            self.time_elapsed = 0.0
            self.setpoint = setpoint
            self.unit = unit
            self.period = period
            self.time = []
            self.setpoints = []
            self.disturbe = 0.0
            self.system_values = []
            self.errors = []
            self.save = True
            self.data = []
            self.time_var = [] 
            self.set_text()
            self.pid = PIDControl(Kp, Ki, Kd, setpoint, calibration_equation, self.unit, self.period, self.save)          
            self.ani = animation.FuncAnimation(self.figure, self.update_plot, frames=range(100), init_func=self.init_plot, blit=True, interval=self.period*1000)
            self.ax.set_xlabel('Time (s)')
            self.ax.set_ylabel(self.unit)
            self.ax.legend(['System Output', 'Setpoint'])
            plt.suptitle('PID Control')
            self.canvas.draw()
        except ValueError:
            print("Error")

    def set_text(self):
        self.doubleSpinBox_SetpointDialog.setValue(self.setpoint)

    def init_plot(self):
        self.line1, = self.ax.plot([], [], 'x', label='System Output')  # Usar 'o' para pontos
        self.line2, = self.ax.plot([], [], '-', label='Setpoint')  # Usar 'o' para pontos
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-10, 10)
        return self.line1, self.line2

    def update_plot(self, frame):
        if self.pid is None:
            print ('self.pid is none')
            return self.line1, self.line2
#clock
        self.time_elapsed += self.period
        control = self.pid.update(self.system_value, self.time_elapsed)
#print(f" self.system_value type: {type(self.system_value)}")
#self.system_value += control * 0.1
        self.system_value = self.system_output(self.system_value,control)
        self.system_value = self.system_value - self.disturbe
        self.system_values.append(self.system_value)
        self.setpoints.append(self.setpoint)
        
        self.data.append(self.system_value)
        self.time_var.append(self.time_elapsed)
#updating
        self.ax.set_xlim(0, self.time_elapsed)
        self.line1.set_data(np.arange(len(self.system_values)) * self.period, self.system_values)
        self.line2.set_data(np.arange(len(self.setpoints)) * self.period, self.setpoints)
#reloading the axes
        self.ax.set_ylim(min(self.setpoints + self.system_values) - 1, max(self.setpoints + self.system_values) + 1)
        self.canvas.draw()
        return self.line1, self.line2

    def system_output(self, y_prev, control):
#discretization by euler
        return (self.period * control + y_prev) / (1 + self.period * self.a)