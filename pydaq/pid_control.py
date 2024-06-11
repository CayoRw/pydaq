# pid_control.py
import sys 
import os 
import numpy as np
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#Load the style.qss    
def apply_stylesheet(app, stylesheet_path):
    with open(stylesheet_path, "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
class Pid_Control(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controle PID")
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(800, 350)
        
        #CREATE CENTRAL WIDGET (THE MAIN)
        self.central_frame = QFrame()
        
        #Layout principal
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0) #Para retirar as bordas
        self.main_layout.setSpacing(0) #Para retirar o espacamento central

        #CREATE TOP LAYOUT FRAME
        self.top_layout = QFrame()

        #CONTENT LAYOUT
        self.content_top_layout = QHBoxLayout(self.top_layout)
        self.content_top_layout.setContentsMargins(0,0,0,0)
        self.content_top_layout.setSpacing(0)

        #LEFT MENU LAYOUT
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #434544")
        self.left_menu.setMaximumWidth(200)
        self.left_menu.setMinimumWidth(200)
        self.left_menu_content_layout = QGridLayout(self.left_menu)
        
        #Label setpoint
        self.label1 = QLabel("Setpoint:")
        self.left_menu_content_layout.addWidget(self.label1, 0, 0, Qt.AlignLeft)
        
        #Label controler type
        self.label2 = QLabel("Controller type:")
        self.left_menu_content_layout.addWidget(self.label2, 1, 0, Qt.AlignLeft)
        
        #Empty Label
        self.label4 = QLabel(" ")
        self.left_menu_content_layout.addWidget(self.label4, 2, 0, Qt.AlignLeft)
        
        #Empty Label
        self.label5 = QLabel(" ")
        self.left_menu_content_layout.addWidget(self.label5, 3, 0, Qt.AlignLeft)

        #RIGHT LAYOUT
        self.right_menu = QFrame()
        self.right_menu.setObjectName("right_menu")
        self.right_content_layout = QGridLayout(self.right_menu)
        
        # WIDGETS OF THE RIGHT LAYOUT
        self.setpoint_input = QLineEdit()
        self.setpoint_input.setMaximumSize(300,25)
        
        # Controller type       
        self.controller_type_combo = QComboBox()
        self.controller_type_combo.addItems(["P", "PI", "PID"])
        self.controller_type_combo.setStyleSheet("background-color: #988782")
        self.controller_type_combo.setMaximumSize(100,25)
        
        #SELECT PARAMETERS BUTTON
        self.open_button = QPushButton("Select Parameters")
        self.open_button.clicked.connect(self.open_controller_interface)
        self.open_button.setMinimumWidth(150)
        self.open_button.setMaximumWidth(150)
        
        # Label to show the select parameters
        self.parameters_label = QLabel("Parameters Selected: None")
        #Label to show the PID equation
        self.label_equation = QLabel("PID Equation: u(t) = Kp * e(t) + Ki * ∫e(t) dt + Kd * de(t)/dt", self)

        #ADDING WIDGETS TO THE RIGHT LAYOUT
        self.right_content_layout.addWidget(self.setpoint_input, 0, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.controller_type_combo, 1, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.open_button, 2, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.parameters_label, 3, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.label_equation, 4, 1, alignment=Qt.AlignLeft)

        # create a vertical line as separator between left and right side
        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)

        #ADD the content to layout
        self.content_top_layout.addWidget(self.left_menu)
        self.content_top_layout.addWidget(self.vertical_line)
        self.content_top_layout.addWidget(self.right_menu)

        # create the central line separator
        self.central_horizontal_line = QFrame()
        self.central_horizontal_line.setFrameShape(QFrame.HLine)
        self.central_horizontal_line.setFrameShadow(QFrame.Sunken)
        
        #create the central layout
        self.central_layout = QFrame()
        self.central_layout.setObjectName("central_layout")

        #create de central layout content
        self.central_content_layout = QHBoxLayout(self.central_layout)
        self.central_content_layout.setContentsMargins(10, 0, 10, 0)
        
        # Output display
        self.output_label = QLabel("Output:")
        self.output_display = QLabel("0.0")
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_display)
        self.central_content_layout.addLayout(output_layout)
        
        # Error display
        self.error_label = QLabel("Error:")
        self.error_display = QLabel("0.0")
        error_layout = QHBoxLayout()
        error_layout.addWidget(self.error_label)
        error_layout.addWidget(self.error_display)
        self.central_content_layout.addLayout(error_layout)

        #create the bottom line separator
        self.bottom_horizontal_line = QFrame()
        self.bottom_horizontal_line.setFrameShape(QFrame.HLine)
        self.bottom_horizontal_line.setFrameShadow(QFrame.Sunken)

        #create bottom layout
        self.bottom_layout = QFrame()

        #create the bottom content layout
        self.bottom_content_layout = QHBoxLayout(self.bottom_layout)
        self.bottom_content_layout.setContentsMargins(10,0,10,0)
        
        #ADD start Button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.show_graph_window)
        self.start_button.setMinimumWidth(150)
        self.start_button.setMaximumWidth(150)

        #ADD Stop button
        self.stop_button = QPushButton("Stop")
        self.stop_button.setMinimumWidth(150)
        self.stop_button.setMaximumWidth(150)

        #Add button to bottom layout
        self.bottom_content_layout.addWidget(self.start_button)
        self.bottom_content_layout.addWidget(self.stop_button)

        #Add the content to main layout
        self.main_layout.addWidget(self.top_layout)
        self.main_layout.addWidget(self.central_horizontal_line)
        self.main_layout.addWidget(self.central_layout)
        self.main_layout.addWidget(self.bottom_horizontal_line)
        self.main_layout.addWidget(self.bottom_layout)

        #Central widget
        self.setCentralWidget(self.central_frame)
        
    def open_controller_interface(self):
        controller_type = self.controller_type_combo.currentText()
        if controller_type == "P":
           self.controller_window = PControllerWindow(self)
        elif controller_type == "PI":
            self.controller_window = PIControllerWindow(self)
        elif controller_type == "PID":
            self.controller_window = PIDControllerWindow(self)
            
        self.controller_window.exec()

    def set_parameters(self, parameters, equation):
        self.parameters_label.setText(f"Parameters selected: {parameters}")
        self.label_equation.setText(f"PID Equation: u(t):{equation}")
        
    def show_graph_window(self):
        self.graph_window = GraphWindow()
        self.graph_window.show()
    
class PControllerWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle('P Controller Configuration ')
        layout = QFormLayout()

        self.kp_input = QLineEdit()
        layout.addRow("Kp:", self.kp_input)

        create_button = QPushButton("Confirm")
        create_button.clicked.connect(self.create_p_controller)

        layout.addWidget(create_button)
        self.setLayout(layout)

    def create_p_controller(self):
        kp = float(self.kp_input.text())
        parameters = f"Kp: {kp}"
        equation = f"{kp} * e(t)"
        self.parent.set_parameters(parameters,equation)
        self.accept()

class PIControllerWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PI Controller Configuration')
        layout = QFormLayout()

        self.kp_input = QLineEdit()
        self.ki_input = QLineEdit()

        layout.addRow("Kp:", self.kp_input)
        layout.addRow("Ki:", self.ki_input)

        create_button = QPushButton("Confirm")
        create_button.clicked.connect(self.create_pi_controller)

        layout.addWidget(create_button)
        self.setLayout(layout)

    def create_pi_controller(self):
        kp = float(self.kp_input.text())
        ki = float(self.ki_input.text())
        parameters = f"Kp: {kp}, Ki: {ki}"
        equation = f"{kp} * e(t) + {ki} * ∫e(t) dt"
        self.parent.set_parameters(parameters,equation)
        self.accept()

class PIDControllerWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PID Controler Configuration')
        layout = QFormLayout()

        self.kp_input = QLineEdit()
        self.ki_input = QLineEdit()
        self.kd_input = QLineEdit()

        layout.addRow("Kp:", self.kp_input)
        layout.addRow("Ki:", self.ki_input)
        layout.addRow("Kd:", self.kd_input)

        create_button = QPushButton("Confirm")
        create_button.clicked.connect(self.create_pid_controller)

        layout.addWidget(create_button)
        self.setLayout(layout)

    def create_pid_controller(self):
        kp = float(self.kp_input.text())
        ki = float(self.ki_input.text())
        kd = float(self.kd_input.text())
        parameters = f"Kp: {kp}, Ki: {ki}, Kd: {kd}"
        equation = f"{kp} * e(t) + {ki} * ∫e(t) dt + {kd} * de(t)/dt"
        self.parent.set_parameters(parameters,equation)
        self.accept()
        

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gráficos Exponencial e Senoide')

        # Criação dos canvases
        self.exponential_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.sine_canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Layouts
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.exponential_canvas)
        main_layout.addWidget(self.sine_canvas)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        # Dados para os gráficos
        self.time_data = np.linspace(0, 100, 500)
        self.exponential_data = np.exp(self.time_data / 10)  # Exponencial
        self.sine_data = np.sin(self.time_data / 10)  # Senoide

        self.plot_graphs()

    def plot_graphs(self):
        # Plotar gráfico exponencial
        self.exponential_canvas.axes.cla()
        self.exponential_canvas.axes.plot(self.time_data, self.exponential_data, label='Exponencial')
        self.exponential_canvas.axes.set_title('Gráfico Exponencial')
        self.exponential_canvas.axes.set_xlabel('Tempo (s)')
        self.exponential_canvas.axes.set_ylabel('Amplitude')
        self.exponential_canvas.axes.legend()
        self.exponential_canvas.draw()

        # Plotar gráfico senoide
        self.sine_canvas.axes.cla()
        self.sine_canvas.axes.plot(self.time_data, self.sine_data, label='Senoide', color='orange')
        self.sine_canvas.axes.set_title('Gráfico Senoide')
        self.sine_canvas.axes.set_xlabel('Tempo (s)')
        self.sine_canvas.axes.set_ylabel('Amplitude')
        self.sine_canvas.axes.legend()
        self.sine_canvas.draw()
        
def create_and_show_window():
    app = QApplication(sys.argv)  # Create Aplicacion
    apply_stylesheet(app,"pydaq/style.qss") #Apply the css
    window = Pid_Control()  # Create Windows
    window.show()  # Show Windows
    sys.exit(app.exec())  # Execute application loop 
    
def start_application():
    create_and_show_window()

if __name__ == "__main__":
    start_application()
    
    