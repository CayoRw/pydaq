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
    
#signal to send back to QWidget the values
    send_values = Signal(float, float, float, int, float)

    def __init__(self, *args):
        super(PID_Control_Window_Dialog, self).__init__()
        self.setupUi(self)
        self.setGeometry(200, 200, 1000, 600)
#Calling the functions
        self.pushButton_startstop.clicked.connect(self.stopstart)
        self.pushButton_close.clicked.connect(self.go_back)
        self.pushButton_apply.clicked.connect(self.apply_parameters)
        self.comboBox_TypeDialog.currentIndexChanged.connect(self.on_type_combo_changed)


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
    def set_parameters(self, kp, ki, kd, index, setpoint, unit, equation, period, path, save):
        self.kp = kp if kp else 1
        self.ki = ki if ki else 0
        self.kd = kd if kd else 0
        self.index = index if index else 0
        self.setpoint = setpoint if setpoint else 0.0
        self.unit = unit if unit else 'Voltage (V)'
        self.calibration_equation = equation
        self.period = period if period else 1 
        self.path = path if path else os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        self.save = save
        self._check_path()
        print('kp ', self.kp)
        print('ki ', self.ki)
        print('kd ', self.kd)
        print('Index ', self.index)
        print('Setpoint ', self.setpoint)
        print('Unit ', self.unit)
        print('Equation ', self.calibration_equation)
        print('Period ', self.period)
        print ('Path ', self.path)
        self.start_control(self.kp, self.ki, self.kd, self.setpoint, self.calibration_equation, self.unit, self.period)

#both function below are to set the comboBox enabled/desabled status
    def on_type_combo_changed(self, index):
        if index == 0:  
            self.enable_pid_parameters(True, False, False)
        elif index == 1:  
            self.enable_pid_parameters(True, True, False)
        elif index == 2: 
            self.enable_pid_parameters(True, False, True)
        elif index == 3:  
            self.enable_pid_parameters(True, True, True)  
        self.index = index  
    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.doubleSpinBox_KpDialog.setEnabled(kp_enabled)
        self.doubleSpinBox_KiDialog.setEnabled(ki_enabled)
        self.doubleSpinBox_KdDialog.setEnabled(kd_enabled)
        if ki_enabled == False:
            self.doubleSpinBox_KiDialog.setValue(0)
        if kd_enabled == False:
            self.doubleSpinBox_KdDialog.setValue(0)

#def to save and go back
    def go_back(self):
#save if wanted
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.data, "data.dat")
            print("\nData saved ...")
#sending the values to QWidget
        self.send_values.emit(
            self.kp,
            self.ki,
            self.kd,
            self.index,
            self.setpoint,
        )
#stop the event and close the dialog
        self.ani.event_source.stop()
        self.close()

#stop/start the event and change the button text
    def stopstart (self):
        self.paused = not self.paused
        if self.paused:
            self.ani.event_source.stop()
            self.pushButton_startstop.setText("Start")
        else:
            self.ani.event_source.start()
            self.pushButton_startstop.setText("Stop")

#apply all pid parameters while the event goes on
    def apply_parameters(self):
        try:
            self.setpoint = self.doubleSpinBox_SetpointDialog.value()
            print ('The new setpoint is ', self.setpoint)
            if self.pid:
                self.pid.setpoint = self.setpoint
                print ('The setpoint has been sended to pid control')
        except ValueError:
            pass  # Ignore invalid input  
#changing Kp Ki and Kd parameters
        if self.doubleSpinBox_KpDialog.isEnabled():
            self.kp = self.doubleSpinBox_KpDialog.value()
            self.pid.Kp = self.kp
        else:
            self.kp = None
            self.pid.Kp = 0
        if self.doubleSpinBox_KiDialog.isEnabled():
            self.ki = self.doubleSpinBox_KiDialog.value()
            self.pid.Ki = self.ki
        else:
            self.ki = None
            self.pid.Ki = 0
        if self.doubleSpinBox_KdDialog.isEnabled():
            self.kd = self.doubleSpinBox_KdDialog.value()
            self.pid.Kd = self.kd
        else:
            self.kd = None
            self.pid.Kd = 0
#changing the disturbe
        self.disturbe = self.doubleSpinBox_DisturbeDialog.value()
        print ('The new disturbe is ', self.disturbe)

#stating the control and inicializating variables
    def start_control(self, Kp, Ki, Kd, setpoint, calibration_equation, unit, period):
        try:
            self.time_elapsed = 0.0
            self.time = []
            self.setpoints = []
            self.disturbe = 0.0
            self.system_values = []
            self.errors = []
            self.data = []
            self.time_var = [] 
            self.set_text()
            self.on_type_combo_changed(self.index)
            self.pid = PIDControl(Kp, Ki, Kd, setpoint, calibration_equation, unit, period)          
            self.ani = animation.FuncAnimation(self.figure, self.update_plot, frames=range(100), init_func=self.init_plot, blit=True, interval=self.period*1000)
            self.ax.set_xlabel('Time (s)')
            self.ax.set_ylabel(self.unit)
            self.ax.legend(['System Output', 'Setpoint'])
            plt.suptitle('PID Control')
            self.canvas.draw()
        except ValueError:
            print("Error")

#changing the text of the pid parameters inputs
    def set_text(self):
        self.comboBox_TypeDialog.setCurrentIndex(self.index)
        self.doubleSpinBox_KpDialog.setValue(self.kp)
        self.doubleSpinBox_KiDialog.setValue(self.ki)
        self.doubleSpinBox_KdDialog.setValue(self.kd)
        self.doubleSpinBox_SetpointDialog.setValue(self.setpoint)
        self.comboBox_TypeDialog.setCurrentIndex(self.index)

#init the plot with variables axes 
    def init_plot(self):
        self.line1, = self.ax.plot([], [], 'x', label='System Output')  # Usar 'o' para pontos
        self.line2, = self.ax.plot([], [], '-', label='Setpoint')  # Usar 'o' para pontos
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-10, 10)
        return self.line1, self.line2

#updating the plot
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

#system type 1/s+a
    def system_output(self, y_prev, control):
#discretization by euler
        return (self.period * control + y_prev) / (1 + self.period * self.a)