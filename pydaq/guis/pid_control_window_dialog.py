import sys, os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import *
from ..uis.ui_PyDAQ_pid_control_window_dialog import Ui_Dialog_Plot_PID_Window


class PID_Control_Window_Dialog(QDialog, Ui_Dialog_Plot_PID_Window):
    def __init__(self, *args):
        super(PID_Control_Window_Dialog, self).__init__()
        self.setupUi(self)