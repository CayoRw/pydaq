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
        self.setMinimumSize(1000, 750)

#Calling the functions
        self.pushButton_startstop.clicked.connect(self.stopstart)
        self.pushButton_close.clicked.connect(self.go_back)
        self.pushButton_apply.clicked.connect(self.apply_parameters)
        self.comboBox_TypeDialog.currentIndexChanged.connect(self.on_type_combo_changed)
        self.paused = False
        self.pid = None
#to save the data path
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop") # Defining default path

#Starting the canvas
        self.figure = plt.figure(figsize =(6.4,4.8), facecolor='#404040')
        self.ax = self.figure.add_subplot(111, facecolor='#505050')  # Output graph
        self.canvas = FigureCanvas(self.figure)
        self.image_layout.addWidget(self.canvas)

#Defining the fuctions
    def set_parameters(self, kp, ki, kd, index, com_port, setpoint, unit, equation, period, path, save, board):
        self.kp = kp if kp else 1
        self.ki = ki if ki else 0
        self.kd = kd if kd else 0
        self.index = index if index else 0
        self.com_port = com_port
        self.setpoint = setpoint if setpoint else 0.0
        self.unit = unit if unit else 'Voltage (V)'
        self.calibration_equation = equation
        self.period = period if period else 1 
        self.path = path if path else os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        self.save = save
        self.board = board if board else 'arduino'
        self._check_path()
        print('kp ', self.kp)
        print('ki ', self.ki)
        print('kd ', self.kd)
        print('Index ', self.index)
        print('Com Port ', self.com_port)
        print('Setpoint ', self.setpoint)
        print('Unit ', self.unit)
        print('Equation ', self.calibration_equation)
        print('Period ', self.period)
        print ('Path ', self.path)
        print ('Save ', self.save)
        self.start_control(self.kp, self.ki, self.kd, self.setpoint, self.calibration_equation, self.unit, self.period)

#stop/start the event and change the button text
    def stopstart (self):
        self.paused = not self.paused
        if self.paused:
            self.ani.event_source.stop()
            self.pushButton_startstop.setText("Start")
        else:
            self.ani.event_source.start()
            self.pushButton_startstop.setText("Stop")

#def to save and go back
    def go_back(self):
#save if wanted
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.system_values, "output.dat")
            self._save_data(self.errors, "error.dat")
            self._save_data(self.setpoints, "setpoint.dat")
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
        if self.board == 'arduino':
            # Turning off the output at the end
            self.pid.ser.write(b"0")
            # Closing port
            self.pid.ser.close()
        self.ani.event_source.stop()
        self.close()

#apply all pid parameters while the event goes on
    def apply_parameters(self):
        try:
            self.setpoint = self.doubleSpinBox_SetpointDialog.value()
            print ('The new setpoint is ', self.setpoint)
            if self.pid:
                self.pid.setpoint = self.setpoint
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
            self.pid.integral = 0
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
        print ('The new kp is ', self.kp)
        print ('The new ki is ', self.ki)
        print ('The new kd is ', self.kd)
        self.disturbe = self.doubleSpinBox_DisturbeDialog.value()
        self.pid.disturbe = self.disturbe
        print ('The new disturbe is ', self.disturbe)

#stating the control and inicializating variables
    def start_control(self, Kp, Ki, Kd, setpoint, calibration_equation, unit, period):
        try:
            self.set_text()
            self.on_type_combo_changed(self.index)
            self.pid = PIDControl(Kp, Ki, Kd, setpoint, calibration_equation, unit, period, self.com_port)
            self.check_board()
            self.ani = animation.FuncAnimation(
                self.figure, 
                self.update_plot, 
                frames=range(100), 
                init_func=self.init_plot, 
                blit=True, 
                interval=self.period*1000
                )
            plt.suptitle('PID Control', color='white')
            self.canvas.draw()
        except ValueError:
            print("Error")

# Changing the text of the pid parameters inputs
    def set_text(self):
        self.comboBox_TypeDialog.setCurrentIndex(self.index)
        self.doubleSpinBox_KpDialog.setValue(self.kp)
        self.doubleSpinBox_KiDialog.setValue(self.ki)
        self.doubleSpinBox_KdDialog.setValue(self.kd)
        self.doubleSpinBox_SetpointDialog.setValue(self.setpoint)
        self.comboBox_TypeDialog.setCurrentIndex(self.index)
        if self.save == True:
            self.pushButton_close.setText("Save and Close")
            self.pushButton_close.setMinimumWidth(150)
        else:
            self.pushButton_close.setText("Close")
            self.pushButton_close.setMinimumWidth(60)

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

    def check_board(self):
        if self.board == 'arduino':
            self.pid.pid_control_arduino()
            self.pid.com_port = self.com_port
        elif self.board == 'nidaq':
            self.pid.pid_control_nidaq()

    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.doubleSpinBox_KpDialog.setEnabled(kp_enabled)
        self.doubleSpinBox_KiDialog.setEnabled(ki_enabled)
        self.doubleSpinBox_KdDialog.setEnabled(kd_enabled)
        if ki_enabled == False:
            self.doubleSpinBox_KiDialog.setValue(0)
        if kd_enabled == False:
            self.doubleSpinBox_KdDialog.setValue(0)

# Init the plot with variables axes 
    def init_plot(self):

        self.line1, = self.ax.plot([], [], 'x', label='System Output', color = 'cyan')  
        self.line2, = self.ax.plot([], [], '-', label='Setpoint', color = 'lime')  
        self.line3, = self.ax.plot([], [], '--', label='Error', color = 'red')  
        if not hasattr(self, 'ax2'):
            self.ax2 = self.ax.twinx()  # Create the error axe the first time

        self.ax.set_xlim(0, self.period*10)
        self.ax.set_ylim(-1.1*self.setpoint,1.1*self.setpoint)
        self.ax2.set_ylim(-1.1 *self.setpoint, 1.1 * self.setpoint)

        self.ax.set_xlabel('Sample (s)', color = 'white')
        self.ax.set_ylabel(self.unit, color = 'white')
        self.ax2.set_ylabel('Error', color = 'white')

# Set the axes colors to white
        for spine in ['bottom', 'top', 'left', 'right']:
            self.ax.spines[spine].set_color('white')

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax2.tick_params(axis='y', colors='white')
        
        self.ax.title.set_color('white')
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
        self.ax.legend(['System Output', 'Setpoint', 'Error'])
        
        #self.figure.tight_layout()
        
        return self.line1, self.line2, self.line3

    def update_plot(self, frame):

        if self.pid is None:
            print ('self.pid is none')
            return self.line1, self.line2, self.line3

        if self.board == 'arduino':
            self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed = self.pid.update_plot_arduino()
        elif self.board == 'nidaq':
            self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed = self.pid.update_plot_nidaq()
        self.system_value = self.system_values[-1]

        # Change the color when the system value reaches 95% of setpoint
        if abs(self.system_value - self.setpoint) <= 0.05 * self.setpoint:
            self.line1.set_color('yellow')  
        else:
            self.line1.set_color('cyan')  
# Updating
        self.ax.set_xlim(0, self.time_elapsed)
        self.line1.set_data(np.arange(len(self.system_values)) * self.period, self.system_values)
        self.line2.set_data(np.arange(len(self.setpoints)) * self.period, self.setpoints)
        self.line3.set_data(np.arange(len(self.setpoints)) * self.period, self.errors)  
# Reloading the axes
        if (min(self.setpoints + self.system_values + self.errors)<0):
            xmin = min(self.setpoints + self.system_values + self.errors) * 1.1
        elif(min(self.setpoints + self.system_values + self.errors)>0):
            xmin = min(self.setpoints + self.system_values + self.errors) * 0.9
        else:
            xmin = max(self.setpoints + self.system_values + self.errors) * -0.1
        self.ax.set_ylim(xmin, max(self.setpoints + self.system_values + self.errors) *1.1)
# Reload the error axe
        self.ax2.set_ylim(xmin, max(self.setpoints + self.system_values + self.errors) *1.1)
# Reload the X axe after 30 datas
        if len(self.system_values) > 30:
            self.ax.set_xlim((len(self.system_values) - 30) * self.period, len(self.system_values) * self.period)
        else:
            self.ax.set_xlim(0, self.time_elapsed)
        self.canvas.draw()
        
        return self.line1, self.line2, self.line3