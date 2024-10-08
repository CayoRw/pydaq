import sys, os

from PySide6 import QtWidgets
from ..uis.ui_PyDAQ_PID_Control_widget import Ui_Arduino_PID_Control

class PID_Control_Arduino_Widget(QtWidgets.QMainWindow, Ui_Arduino_PID_Control):
    def __init__(self):
        super(PID_Control_Arduino_Widget, self).__init__()
        self.setupUi(self)
		

app = QtWidgets.QApplication(sys.argv)
window = PID_Control_Arduino_Widget()
window.show()
sys.exit(app.exec())