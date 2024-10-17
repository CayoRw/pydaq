import sys, os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import *
from ..uis.ui_PyDAQ_pid_control_Arduino_widget import Ui_Arduino_PID_Control
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ..guis.pid_control_window_dialog import PID_Control_Window_Dialog


class PID_Control_Arduino_Widget(QWidget, Ui_Arduino_PID_Control):
    def __init__(self, *args):
        super(PID_Control_Arduino_Widget, self).__init__()
        self.setupUi(self)

#Calling the functions
        self.locate_arduino()
        self.reload_devices.clicked.connect(self.locate_arduino)
        self.on_unit_change()
        self.comboBox_setpoint.currentIndexChanged.connect(self.on_unit_change)
        self.on_type_combo_changed(0)
        self.comboBox_type.currentIndexChanged.connect(self.on_type_combo_changed)
        self.pushButton_confirm.released.connect(self.show_pid_equation)
        self.pushButton_start.clicked.connect(self.show_graph_window)

#Fuctions
    def locate_arduino(self):
        current_selection = self.comboBox_arduino.currentText()
        self.comboBox_arduino.clear()
        ports = serial.tools.list_ports.comports()

        for port in ports:
            self.comboBox_arduino.addItem(f"{port.device} - {port.description}")
        
        if current_selection:
            index = self.comboBox_arduino.findText(current_selection)
            if index != -1:
                self.comboBox_arduino.setCurrentIndex(index)

#Condiction to show the line edit equation and unit
    def on_unit_change(self):
        selected_unit = self.comboBox_setpoint.currentText()
        if selected_unit == 'Other':
            self.widget_unit.show()
            self.label_unit.show()
            self.label_equation.show()
            self.widget_equation.show()
        elif selected_unit == 'Voltage (V)':
            self.widget_unit.hide()
            self.label_unit.hide()
            self.label_equation.hide()
            self.widget_equation.hide()
        else:
            self.widget_unit.hide()
            self.label_unit.hide()
            self.label_equation.show()
            self.widget_equation.show()

#Enable the pid parameters inputs 
    def on_type_combo_changed(self, index):
        if index == 0:  
            self.enable_pid_parameters(True, False, False)
        elif index == 1:  
            self.enable_pid_parameters(True, True, False)
        elif index == 2: 
            self.enable_pid_parameters(True, False, True)
        elif index == 3:  
            self.enable_pid_parameters(True, True, True)

    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.doubleSpinBox_kp.setEnabled(kp_enabled)
        self.doubleSpinBox_ki.setEnabled(ki_enabled)
        self.doubleSpinBox_kd.setEnabled(kd_enabled)
        if ki_enabled == False:
            self.doubleSpinBox_ki.setValue(0)
        if kd_enabled == False:
            self.doubleSpinBox_kd.setValue(0)

#Method to create a image and show the pid equation
    def show_pid_equation(self):
#Condiction to read only the inputs enable and set 'None' on desable inputs
        if self.doubleSpinBox_kp.isEnabled():
            kp = self.doubleSpinBox_kp.value()
        else:
            kp = None
        if self.doubleSpinBox_ki.isEnabled():
            ki = self.doubleSpinBox_ki.value()
        else:
            ki = None
        if self.doubleSpinBox_kd.isEnabled():
            kd = self.doubleSpinBox_kd.value()
        else:
            kd = None
        equation_parts = []
#Create a pid equation
        if kp is not None:
            kp_display = f"{kp:.2f}"
            equation_parts.append(rf"{kp_display} \cdot e(t)")
        if ki is not None:
            ki_display = f"{ki:.2f}"
            equation_parts.append(rf"{ki_display} \int_{{0}}^{{t}} e(\tau) \, d\tau")
        if kd is not None:
            kd_display = f"{kd:.2f}"
            equation_parts.append(rf"{kd_display} \frac{{d}}{{dt}} e(t)")
        if not equation_parts:
            return
        #Equation on latex
        latex = "u(t) = " + " + ".join(equation_parts)
        #Figure created showing the equation, without axes
        fig = Figure(figsize=(9, 3), facecolor='#404040')
        ax = fig.add_subplot(111, facecolor='#404040')
        ax.text(0.5, 0.5, f"${latex}$", fontsize=15, ha='center', va='center', color='white')
        ax.axis('off')
        canvas = FigureCanvas(fig)
#Remove the widgets from central content layout in reverse and reset the widget from parents too        
        for i in reversed(range(self.image_layout.count())):
            widget_to_remove = self.image_layout.itemAt(i).widget()
            self.image_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)
            
        self.image_layout.addWidget(canvas)

    def show_graph_window(self):
        # Criar uma nova instância da janela para a segunda interface
        plot_window = PID_Control_Window_Dialog()
        plot_window.exec()

'''#Method who call the graph window
    def show_graph_window(self):
        try:
            kp = float(kp_text) if kp_text else 0.0
            ki = float(ki_text) if ki_text else 0.0
            kd = float(kd_text) if kd_text else 0.0
            setpoint = float(setpoint_text) if setpoint_text else 0.0
            frequency = float(frequency_text) if frequency_text else 1.0  # Default to 1 Hz if empty
            unit = self.get_selected_unit()
            calibration_equation = self.get_calibration_equation()
            plot_window = PlotWindow(unit, calibration_equation)
            plot_window.start_control(kp, ki, kd, setpoint, calibration_equation, unit, frequency)
            plot_window.exec()
            
        except ValueError:
            print("Please enter valid numbers for Kp, Ki, and Kd.")
'''


'''app = QtWidgets.QApplication(sys.argv)
window = PID_Control_Arduino_Widget()
window.show()
sys.exit(app.exec())'''