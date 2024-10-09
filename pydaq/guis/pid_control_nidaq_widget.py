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
        self.pushButton_reload.clicked.connect(self.locate_arduino)

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

#Calling the functions