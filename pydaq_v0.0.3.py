# pid_control.py
import sys 
import os 
import numpy as np
import time
from sympy import symbols, sympify, lambdify
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import matplotlib.pyplot as plt
from qt_material import apply_stylesheet
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import serial
import serial.tools.list_ports

#Load the style.qss    
def apply_stylesheet(app, stylesheet_path):
    print(f"Attempting to apply stylesheet from: {stylesheet_path}")
    try:
        with open(stylesheet_path, "r") as f:
            stylesheet = f.read()
        app.setStyleSheet(stylesheet)
        print("Stylesheet applied successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{stylesheet_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Main window of pid control
class Pid_Control(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PID Control Interface")
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(500, 650)
        self.setMaximumSize(700, 850)
        
        #CREATE CENTRAL WIDGET (THE MAIN)
        self.central_frame = QFrame()
        #Layout principal
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0) #To remove margins
        self.main_layout.setSpacing(0) #To remove central spacing

        #CREATE TOP LAYOUT FRAME
        self.top_layout = QFrame()
        self.content_top_layout = QHBoxLayout(self.top_layout)
        self.content_top_layout.setContentsMargins(0,0,0,0)
        self.content_top_layout.setSpacing(0)

        #LEFT MENU LAYOUT
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #434544")
        self.left_menu.setMaximumWidth(200)
        self.left_menu.setMinimumWidth(200)
        self.left_menu_content_layout = QGridLayout(self.left_menu)

        #Labels setpoint
        self.label_device = QLabel("Choose your device:")
        self.label0 = QLabel("Setpoint:")
        self.label_unit = QLabel("Unit:")
        self.label_unit.hide()
        self.label_equation = QLabel("Equation (x^2+1*x):")
        self.label_equation.hide()
        self.label_frequence = QLabel("Sampling frequency")
        self.label4 = QLabel("Controller type:")
        self.p_label = QLabel("Kp:")
        self.i_label = QLabel("Ki:")
        self.d_label = QLabel("Kd:")
        self.labelEmpty1 = QLabel(" ")

        #Adding widgets to left menu layout
        self.left_menu_content_layout.addWidget(self.label_device, 0, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label0, 1, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label_unit, 2, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label_equation, 3, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label_frequence, 4, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label4, 5, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.p_label, 6, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.i_label, 7, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.d_label, 8, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.labelEmpty1, 9, 0, Qt.AlignLeft)

        #RIGHT LAYOUT
        self.right_menu = QFrame()
        self.right_menu.setObjectName("right_menu")
        self.right_menu_layout = QVBoxLayout(self.right_menu)

        self.right_menu_line1 = QFrame()
        self.right_menu_line1_layout = QHBoxLayout(self.right_menu_line1)
        self.right_menu_line2 = QFrame()
        self.right_menu_line2_layout = QHBoxLayout(self.right_menu_line2)
        self.right_menu_line3 = QFrame()
        self.right_menu_line3_layout = QHBoxLayout(self.right_menu_line3)
        self.right_menu_line4 = QFrame()
        self.right_menu_line4_layout = QHBoxLayout(self.right_menu_line4)
        self.right_menu_line5 = QFrame()
        self.right_menu_line5_layout = QHBoxLayout(self.right_menu_line5)
        self.right_menu_line6 = QFrame()
        self.right_menu_line6_layout = QHBoxLayout(self.right_menu_line6)
        self.right_menu_line7 = QFrame()
        self.right_menu_line7_layout = QHBoxLayout(self.right_menu_line7)
        self.right_menu_line8 = QFrame()
        self.right_menu_line8_layout = QHBoxLayout(self.right_menu_line8)
        self.right_menu_line9 = QFrame()
        self.right_menu_line9_layout = QHBoxLayout(self.right_menu_line9)
        self.right_menu_line10 = QFrame()
        self.right_menu_line10_layout = QHBoxLayout(self.right_menu_line10)

        # WIDGETS OF THE RIGHT LAYOUT
        self.device_combo = QComboBox()
        self.device_combo.setMinimumWidth(205)
        self.locate_arduino()
        self.button_reload = QPushButton()
        self.button_reload.clicked.connect(self.locate_arduino)
        icon = QIcon("pydaq/imgs/reload.png")
        self.button_reload.setIcon(icon)
        self.setpoint_input = QLineEdit("5")
        self.setpoint_input.setFixedWidth(50)
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Voltage (V)','Temperature (°C)', 'Speed (m/s)', 'Pressure (Pa)', 'Rotation (rad/s)', 'Other'])
        self.unit_combo.currentIndexChanged.connect(self.on_unit_change)
        self.unit_combo.setFixedWidth(150)
        self.unit_input = QLineEdit()
        self.unit_input.setFixedWidth(205)
        self.equation_input = QLineEdit()
        self.equation_input.setMinimumWidth(205)
        self.line_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frequence_input = QLineEdit()
        self.frequence_input.setFixedWidth(50)
        self.controller_type_combo = QComboBox()
        self.controller_type_combo.addItems(["P", "PI", "PD", "PID"])
        self.controller_type_combo.setFixedWidth(60)
        self.controller_type_combo.currentIndexChanged.connect(self.on_type_combo_changed)
        # input of pid parameters
        self.labelEmpty2 = QLabel(" ")
        self.p_input = QLineEdit()
        self.p_input.setFixedWidth(100)
        self.i_input = QLineEdit()
        self.i_input.setFixedWidth(100)
        self.d_input = QLineEdit()
        self.d_input.setFixedWidth(100)
        self.on_type_combo_changed(0)
        self.create_button = QPushButton("Confirm")
        self.create_button.released.connect(self.show_pid_equation)
        
        #ADDING WIDGETS TO THE RIGHT LAYOUT
        self.right_menu_line1_layout.addWidget(self.device_combo, alignment= Qt.AlignLeft)
        self.right_menu_line1_layout.addWidget(self.button_reload, alignment= Qt.AlignLeft)
        self.right_menu_line1_layout.addItem(self.line_spacer)
        self.right_menu_line2_layout.addWidget(self.setpoint_input, alignment= Qt.AlignLeft)
        self.right_menu_line2_layout.addWidget(self.unit_combo, alignment= Qt.AlignLeft)
        self.right_menu_line2_layout.addItem(self.line_spacer)
        self.right_menu_line3_layout.addWidget(self.unit_input, alignment= Qt.AlignLeft)
        self.right_menu_line3.hide()
        self.right_menu_line4_layout.addWidget(self.equation_input)
        self.right_menu_line4_layout.addItem(self.line_spacer)
        self.right_menu_line4.hide()
        self.right_menu_line5_layout.addWidget(self.frequence_input, alignment= Qt.AlignLeft)
        self.right_menu_line6_layout.addWidget(self.controller_type_combo, alignment= Qt.AlignLeft)
        self.right_menu_line7_layout.addWidget(self.p_input, alignment= Qt.AlignLeft)
        self.right_menu_line8_layout.addWidget(self.i_input, alignment= Qt.AlignLeft)
        self.right_menu_line9_layout.addWidget(self.d_input, alignment= Qt.AlignLeft)
        self.right_menu_line10_layout.addWidget(self.create_button, alignment= Qt.AlignLeft)

        self.right_menu_layout.addWidget(self.right_menu_line1)
        self.right_menu_layout.addWidget(self.right_menu_line2)
        self.right_menu_layout.addWidget(self.right_menu_line3)
        self.right_menu_layout.addWidget(self.right_menu_line4)
        self.right_menu_layout.addWidget(self.right_menu_line5)
        self.right_menu_layout.addWidget(self.right_menu_line6)
        self.right_menu_layout.addWidget(self.right_menu_line7)
        self.right_menu_layout.addWidget(self.right_menu_line8)
        self.right_menu_layout.addWidget(self.right_menu_line9)
        self.right_menu_layout.addWidget(self.right_menu_line10)

        # create a vertical line as separator between left and right side
        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)

        #ADD all the content to the top layout
        self.content_top_layout.addWidget(self.left_menu)
        self.content_top_layout.addWidget(self.vertical_line)
        self.content_top_layout.addWidget(self.right_menu)
        
        #create the central QFrame to be changed for the equation
        self.central_layout = QFrame(self)
        self.central_content_layout = QHBoxLayout(self.central_layout)
       
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

        #Add button to bottom layout
        self.bottom_content_layout.addWidget(self.start_button)

        #Add the content to main layout
        self.main_layout.addWidget(self.top_layout)
        self.main_layout.addWidget(self.central_layout)
        self.main_layout.addWidget(self.bottom_horizontal_line)
        self.main_layout.addWidget(self.bottom_layout)

        #Central widget
        self.setCentralWidget(self.central_frame)
    
    #get arduino device
    def locate_arduino(self):  # function that locate arduino 
        current_selection = self.device_combo.currentText()
        self.device_combo.clear()
        ports = serial.tools.list_ports.comports()

        for port in ports:
            self.device_combo.addItem(f"{port.device} - {port.description}")
        
        if current_selection:
            index = self.device_combo.findText(current_selection)
            if index != -1:
                self.device_combo.setCurrentIndex(index)
    
    #Condiction to show the labels when necessary
    def on_unit_change(self):
        selected_unit = self.unit_combo.currentText()
        if selected_unit == 'Other':
            self.right_menu_line3.show()
            self.label_unit.show()
            self.label_equation.show()
            self.right_menu_line4.show()
        elif selected_unit == 'Voltage (V)':
            self.right_menu_line3.hide()
            self.label_unit.hide()
            self.label_equation.hide()
            self.right_menu_line4.hide()
        else:
            self.right_menu_line3.hide()
            self.label_unit.hide()
            self.label_equation.show()
            self.right_menu_line4.show()

    #call the 'enable pid parameters' and set the 'enable or disable' setup
    def on_type_combo_changed(self, index):
        if index == 0:  
            self.enable_pid_parameters(True, False, False)
        elif index == 1:  
            self.enable_pid_parameters(True, True, False)
        elif index == 2: 
            self.enable_pid_parameters(True, False, True)
        elif index == 3:  
            self.enable_pid_parameters(True, True, True)

    #Enable the pid parameters inputs 
    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.p_input.setEnabled(kp_enabled)
        self.i_input.setEnabled(ki_enabled)
        self.d_input.setEnabled(kd_enabled)

    #Method who create a image and show the pid equation
    def show_pid_equation(self):
        #Condiction who read only the inputs enable and set 'None' at desable inputs
        if self.p_input.isEnabled():
            kp_text = self.p_input.text()
            kp = float(kp_text) if kp_text else None
        else:
            kp = None
        if self.i_input.isEnabled():
            ki_text = self.i_input.text()
            ki = float(ki_text) if ki_text else None
        else:
            ki = None
        if self.d_input.isEnabled():
            kd_text = self.d_input.text()
            kd = float(kd_text) if kd_text else None
        else:
            kd = None
        equation_parts = []
        
        #Create a pid equation based on parameters readed
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
        fig = Figure(figsize=(9, 3), facecolor='#434544')
        ax = fig.add_subplot(111, facecolor='#434544')
        ax.text(0.5, 0.5, f"${latex}$", fontsize=15, ha='center', va='center', color='white')
        ax.axis('off')
        canvas = FigureCanvas(fig)

        #Remove the widgets from central content layout in reverse and reset the widget from parents too        
        for i in reversed(range(self.central_content_layout.count())):
            widget_to_remove = self.central_content_layout.itemAt(i).widget()
            self.central_content_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

        self.central_content_layout.addWidget(canvas)

    def get_selected_unit(self):
        return self.unit_combo.currentText()
    def get_calibration_equation(self):
        return self.equation_input.text()
    
    #Method who call the graph window
    def show_graph_window(self):
        kp_text = self.p_input.text()
        ki_text = self.i_input.text()
        kd_text = self.d_input.text()
        frequency_text = self.frequence_input.text()
        setpoint_text = self.setpoint_input.text()

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
class PID:
    def __init__(self, Kp, Ki, Kd, setpoint=0, calibration_equation=None, unit='Voltage (V)'):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.unit = unit
        self.calibration_equation = calibration_equation
        self.integral = 0
        self.previous_error = 0

    def update(self, feedback_value):
        error = self.setpoint - feedback_value
        self.integral += error
        derivative = error - self.previous_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output

class PlotWindow(QDialog):
    def __init__(self, unit, calibration_equation, parent=None):
        super().__init__(parent)
        self.unit = unit
        self.calibration_equation = calibration_equation
        self.setWindowTitle("PID Control Plot")
        self.setGeometry(200, 200, 1000, 600)
        self.paused = False
        self.start_time = time.time()
        self.central_layout = QVBoxLayout(self)

        #create a top_layout frame
        self.top_layout = QFrame ()
        self.top_layout_content = QHBoxLayout(self.top_layout)
        # Create a sublayout for setpoint control
        self.label0 = QLabel("Setpoint:")
        self.setpoint_input = QLineEdit()
        self.setpoint_input.setText("5")
        self.update_button = QPushButton("Update Setpoint")
        self.update_button.clicked.connect(self.update_setpoint)
        #Add widgets to top layout
        self.top_layout_content.addWidget(self.label0)
        self.top_layout_content.addWidget(self.setpoint_input)
        self.top_layout_content.addWidget(self.update_button)

        #create a mid_layout frame for the images
        self.mid_layout = QFrame()
        self.mid_layout_content = QHBoxLayout(self.mid_layout)
        self.figure = plt.figure(facecolor='#434544')
        self.ax = self.figure.add_subplot(111, facecolor='#434544')  # Output graph
        self.canvas = FigureCanvas(self.figure)
        #Add widget to layout
        self.mid_layout_content.addWidget(self.canvas)

        #create a bottom layout
        self.botton_layout = QFrame()
        self.bottom_layout_content = QHBoxLayout(self.botton_layout)
        #botton layout content
        self.stopstart_button = QPushButton("Stop / Start")
        self.stopstart_button.clicked.connect(self.stopstart)
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        #add widget
        self.bottom_layout_content.addWidget(self.stopstart_button)
        self.bottom_layout_content.addWidget(self.back_button)

        self.central_layout.addWidget(self.top_layout)
        self.central_layout.addWidget(self.mid_layout)
        self.central_layout.addWidget(self.botton_layout)

        #variable for control
        self.system_value = 0
        self.setpoints = []
        self.system_values = []
        self.errors = []
        self.pid = None

    def update_setpoint(self):
        try:
            new_setpoint = float(self.setpoint_input.text())
            self.setpoint = new_setpoint
            if self.pid:
                self.pid.setpoint = new_setpoint
        except ValueError:
            pass  # Ignore invalid input

    def start_control(self,  Kp, Ki, Kd, setpoint, calibration_equation, unit, frequency):
        try:
            setpoint = float(setpoint)
            self.setpoint = setpoint
            Kp = float(Kp)
            Ki = float(Ki)
            Kd = float(Kd)
            self.unit = unit
            self.pid = PID(Kp, Ki, Kd, setpoint, calibration_equation, self.unit)
            self.setpoints = []
            self.system_values = []

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

    # Função de transferência discreta do sistema (utilizando Euler para discretizar)
    def system_output(u, y_prev):
        # Discretização por Euler
        return (1 * u + y_prev) / (1 + 1 * 2)

    def update_plot(self, frame):
        if self.pid is None:
            return self.line1, self.line2
        self.time_elapsed += self.period
        
        control = self.pid.update(self.system_value)
        y = self.system_output(control)
        self.system_value += y
        self.system_values.append(self.system_value)
        self.setpoints.append(self.setpoint)
        
        # Atualizar o tempo
        self.ax.set_xlim(0, self.time_elapsed)
        self.line1.set_data(np.arange(len(self.system_values)) * self.period, self.system_values)
        self.line2.set_data(np.arange(len(self.setpoints)) * self.period, self.setpoints)
        # Atualizar os limites dos eixos dinamicamente
        self.ax.set_ylim(min(self.setpoints + self.system_values) - 1, max(self.setpoints + self.system_values) + 1)
        
        self.canvas.draw()
        return self.line1, self.line2

    def stopstart (self):
        self.paused = not self.paused
        if self.paused:
            self.ani.event_source.stop()
            self.stopstart_button.setText("Start")
        else:
            self.ani.event_source.start()
            self.stopstart_button.setText("Stop")

    def go_back(self):
        self.close()

def create_and_show_window():
    app = QApplication(sys.argv)  # Create Aplicacion
    apply_stylesheet(app,"pydaq/pydaq/style.qss") #Apply the css
    window = Pid_Control()  # Create Windows
    window.show()  # Show Windows
    sys.exit(app.exec())  # Execute application loop 

def start_application():
    create_and_show_window()

if __name__ == "__main__":
    start_application()