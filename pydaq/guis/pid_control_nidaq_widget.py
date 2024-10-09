import sys, os
import serial
import serial.tools.list_ports

from PySide6.QtWidgets import QFileDialog, QWidget
from ..uis.ui_PyDAQ_pid_control_NIDAQ_widget import Ui_NIDAQ_PID_Control



class PID_Control_NIDAQ_Widget(QWidget, Ui_NIDAQ_PID_Control):
    def __init__(self, *args):
        super(PID_Control_NIDAQ_Widget, self).__init__()
        self.setupUi(self)

        #Calling the functions
        self.locate_arduino()
        self.reload_devices.clicked.connect(self.locate_arduino)

        #Calling the functions
        self.locate_arduino()
        self.reload_devices.clicked.connect(self.locate_arduino)
        self.on_unit_change()
        self.comboBox_setpoint.currentIndexChanged.connect(self.on_unit_change)
        self.on_type_combo_changed(0)
        self.comboBox_type.currentIndexChanged.connect(self.on_type_combo_changed)
    
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