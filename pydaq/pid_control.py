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

#Main window of pid control
class Pid_Control(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controle PID")
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(800, 250)
        
        #CREATE CENTRAL WIDGET (THE MAIN)
        self.central_frame = QFrame()
        
        #Layout principal
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0) #To remove margins
        self.main_layout.setSpacing(0) #To remove central spacing

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
        
        #Labels setpoint
        self.label0 = QLabel("Setpoint:")
        self.label_unit = QLabel("Unit:")
        self.label_unit.hide()
        self.label_equation = QLabel("Equation (a,b):")
        self.label_equation.hide()
        self.label3 = QLabel("Controller type:")
        self.label4 = QLabel("Parameters:")
        self.labelEmpty1 = QLabel(" ")
        
        self.left_menu_content_layout.addWidget(self.label0, 0, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label_unit, 1, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label_equation, 2, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label3, 3, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.label4, 4, 0, Qt.AlignLeft)
        self.left_menu_content_layout.addWidget(self.labelEmpty1, 5, 0, Qt.AlignLeft)

        #RIGHT LAYOUT
        self.right_menu = QFrame()
        self.right_menu.setObjectName("right_menu")
        self.right_content_layout = QGridLayout(self.right_menu)
        
        # WIDGETS OF THE RIGHT LAYOUT
        self.setpoint_input = QLineEdit()
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Voltage (V)','Temperature (°C)', 'Speed (m/s)', 'Pressure (Pa)', 'Rotation (rad/s)', 'Other'])    
        self.unit_combo.currentIndexChanged.connect(self.on_unit_change)
        self.unit_input = QLineEdit()
        self.unit_input.hide()
        self.equationa_input = QLineEdit()
        self.equationa_input.hide()
        self.equationb_input = QLineEdit()
        self.equationb_input.hide()
        self.controller_type_combo = QComboBox()
        self.controller_type_combo.addItems(["P", "PI", "PD", "PID"])
        self.controller_type_combo.currentIndexChanged.connect(self.on_type_combo_changed)
        self.controller_type_combo.setStyleSheet("background-color: #988782")
        self.controller_type_combo.setMaximumSize(100,25)
        # input of pid parameters
        self.p_label = QLabel("Kp:")
        self.p_input = QLineEdit()
        self.i_label = QLabel("Ki:")
        self.i_input = QLineEdit()
        self.d_label = QLabel("Kd:")
        self.d_input = QLineEdit()
        self.on_type_combo_changed(0)
        self.create_button = QPushButton("Confirm")
        self.create_button.released.connect(self.show_pid_equation)
        
        #ADDING WIDGETS TO THE RIGHT LAYOUT
        self.right_content_layout.addWidget(self.setpoint_input, 0, 1, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.unit_combo, 0, 2, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.unit_input, 1, 1, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.equationa_input, 2, 1, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.equationb_input, 2, 2, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.controller_type_combo, 3, 1, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.p_label, 4, 1, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.p_input, 4, 2, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.i_label, 4, 3, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.i_input, 4, 4, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.d_label, 4, 5, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.d_input, 4, 6, Qt.AlignLeft)
        self.right_content_layout.addWidget(self.create_button, 5, 1,  Qt.AlignLeft)

        # create a vertical line as separator between left and right side
        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)

        #ADD the content to the top layout
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
    
    def on_unit_change(self):
        selected_unit = self.unit_combo.currentText()
        if selected_unit == 'Other':
            self.unit_input.show()
            self.label_unit.show()
            self.label_equation.show()
            self.equationa_input.show()
            self.equationb_input.show()
        elif selected_unit == 'Voltage (V)':
            self.unit_input.hide()
            self.label_unit.hide()
            self.label_equation.hide()
            self.equationa_input.hide()
            self.equationb_input.hide()
        else:
            self.unit_input.hide()
            self.label_unit.hide()
            self.label_equation.show()
            self.equationa_input.show()
            self.equationb_input.show()

    
    def on_type_combo_changed(self, index):
        # Habilita ou desabilita os line edits baseado no tipo de controle selecionado
        if index == 0:  # P
            self.enable_pid_parameters(True, False, False)
        elif index == 1:  # PI
            self.enable_pid_parameters(True, True, False)
        elif index == 2:  # PD
            self.enable_pid_parameters(True, False, True)
        elif index == 3:  # PID
            self.enable_pid_parameters(True, True, True)
    
    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        # Define o estado de habilitação dos line edits
        self.p_input.setEnabled(kp_enabled)
        self.i_input.setEnabled(ki_enabled)
        self.d_input.setEnabled(kd_enabled)
    
    #Function that show the graphic window
    def show_graph_window(self):
        self.graph_window = GraphWindow()
        self.graph_window.show()
        
    def show_pid_equation(self):
        #condição para apenas ler os inputs habilitados e aplicar o None em inputs que não são habilitados
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
        
        
        if kp is not None:
            equation_parts.append(rf"{kp} \cdot e(t)")
        if ki is not None:
            equation_parts.append(rf"{ki} \int_{{0}}^{{t}} e(\tau) \, d\tau")
        if kd is not None:
            equation_parts.append(rf"{kd} \frac{{d}}{{dt}} e(t)")
        if not equation_parts:
            return
        latex = "u(t) = " + " + ".join(equation_parts)
        
        fig = Figure(figsize=(9, 3), facecolor='#434544')
        ax = fig.add_subplot(111, facecolor='#434544')
        ax.text(0.5, 0.5, f"${latex}$", fontsize=15, ha='center', va='center', color='white')
        ax.axis('off')
        canvas = FigureCanvas(fig)

        for i in reversed(range(self.central_content_layout.count())):
            widget_to_remove = self.central_content_layout.itemAt(i).widget()
            self.central_content_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

        self.central_content_layout.addWidget(canvas)
       
class MplCanvas(FigureCanvas):
    def __init__(self, parent=Pid_Control, width=4, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Graphics')
        self.setMinimumSize(1000, 300)
        
        #CREATE CENTRAL WIDGET (THE MAIN)
        self.central_frame = QFrame()
        
        #main layout
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0) #to remove margins
        self.main_layout.setSpacing(0) #to remove central spacing

        #Create the top layout
        self.top_layout = QFrame()
        self.top_layout_content = QHBoxLayout(self.top_layout)
        
        #Create the canvas
        self.exponential_canvas = MplCanvas(self, width=3, height=4, dpi=80)
        self.sine_canvas = MplCanvas(self, width=3, height=4, dpi=80)

        #Add widget to top layouts
        self.top_layout_content.addWidget(self.exponential_canvas)
        self.top_layout_content.addWidget(self.sine_canvas)
        
        #create the bottom line separator
        self.bottom_horizontal_line = QFrame()
        self.bottom_horizontal_line.setFrameShape(QFrame.HLine)
        self.bottom_horizontal_line.setFrameShadow(QFrame.Sunken)
        
        #create the bottom layout
        self.bottom_layout = QFrame()
        self.bottom_layout_content = QHBoxLayout(self.bottom_layout)
        
        #ADD Stop button
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_and_close)
        self.stop_button.setMinimumWidth(150)
        self.stop_button.setMaximumWidth(150)
        
        #ADD widget to bottom layout
        self.bottom_layout_content.addWidget(self.stop_button)

        #ADD to main layout
        self.main_layout.addWidget(self.top_layout)
        self.main_layout.addWidget(self.bottom_layout)
        
        #Add the content to main layout
        self.main_layout.addWidget(self.top_layout)
        self.main_layout.addWidget(self.bottom_horizontal_line)
        self.main_layout.addWidget(self.bottom_layout)

        #Central widget
        self.setCentralWidget(self.central_frame)

        #Data of graphics
        self.time_data = np.linspace(0, 100, 500)
        self.output_data = 1 - np.exp(-self.time_data / 10)  # Output
        self.error_data = np.sin(self.time_data / 10)  # Error

        self.plot_graphs()

    def plot_graphs(self):
        #To Plot the output graph
        self.exponential_canvas.axes.cla()
        self.exponential_canvas.axes.plot(self.time_data, self.output_data, label='Exponential')
        self.exponential_canvas.axes.set_title('Output Graph')
        self.exponential_canvas.axes.set_xlabel('Time (s)')
        self.exponential_canvas.axes.set_ylabel('Voltage (V)')
        self.exponential_canvas.axes.legend()
        self.exponential_canvas.draw()

        #To plot the error graph
        self.sine_canvas.axes.cla()
        self.sine_canvas.axes.plot(self.time_data, self.error_data, label='Sen', color='orange')
        self.sine_canvas.axes.set_title('Error Graph')
        self.sine_canvas.axes.set_xlabel('Time (s)')
        self.sine_canvas.axes.set_ylabel('Voltage (V)')
        self.sine_canvas.axes.legend()
        self.sine_canvas.draw()

    def stop_and_close(self):
        self.close()
        window = Pid_Control()  # Create Windows
        window.show()  # Show Windows

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