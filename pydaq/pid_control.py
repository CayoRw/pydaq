# pid_control.py
import sys 
import os 

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
    
class Pid_Control(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Controle PID")

        self.setup_ui()

    def setup_ui(self):

        self.setFixedSize(800, 300)

        #CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #434544")

        #Layout principal
        self.main_layout = QVBoxLayout(self.central_frame)
        #Para retirar as bordas
        self.main_layout.setContentsMargins(0,0,0,0)
        #Para retirar o espacamento central
        self.main_layout.setSpacing(0)


        #Pagina inicial
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #434544")

        #CONTENT LAYOUT
        self.content_top_layout = QHBoxLayout(self.content)
        self.content_top_layout.setContentsMargins(0,0,0,0)
        self.content_top_layout.setSpacing(0)

        #LEFT LAYOUT
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #434544")
        self.left_menu.setMaximumWidth(200)
        self.left_menu.setMinimumWidth(200)
        self.left_menu_content_layout = QGridLayout(self.left_menu)
        
        #Label setpoint
        self.label1 = QLabel("Setpoint:")
        self.label1.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_content_layout.addWidget(self.label1, 0, 0, Qt.AlignLeft)
        
        #Label kp
        self.label2 = QLabel("Kp:")
        self.label2.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_content_layout.addWidget(self.label2, 1, 0, Qt.AlignLeft)
        
        #Label ki
        self.label3 = QLabel("Ki:")
        self.label3.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_content_layout.addWidget(self.label3, 2, 0, Qt.AlignLeft)
        
        #Label kd
        self.label4 = QLabel("Kd:")
        self.label4.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_content_layout.addWidget(self.label4, 3, 0, Qt.AlignLeft)
        
        #Label apply parameters
        self.label5 = QLabel(" ")
        self.label5.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_content_layout.addWidget(self.label5, 4, 0, Qt.AlignLeft)

        #RIGHT LAYOUT
        self.right_menu = QFrame()
        self.right_menu.setStyleSheet("background-color: #434544")
        self.right_content_layout = QGridLayout(self.right_menu)
        
        # WIDGETS OF THE RIGHT LAYOUT
        self.setpoint_input = QLineEdit()
        self.setpoint_input.setStyleSheet("background-color: #988782")
        self.setpoint_input.setMaximumSize(300,25)
        self.kp_input = QLineEdit()
        self.kp_input.setStyleSheet("background-color: #988782")
        self.kp_input.setMaximumSize(300, 25)
        self.ki_input = QLineEdit()
        self.ki_input.setStyleSheet("background-color: #988782")
        self.ki_input.setMaximumSize(300, 25)
        self.kd_input = QLineEdit()
        self.kd_input.setStyleSheet("background-color: #988782")
        self.kd_input.setMaximumSize(300, 25)
        self.apply_button = QPushButton("Apply Parameters")
        self.apply_button.setStyleSheet("background-color: green; color: white")
        self.apply_button.setMinimumWidth(150)
        self.apply_button.setMaximumWidth(150)

        #ADDING WIDGETS TO THE RIGHT LAYOUT
        self.right_content_layout.addWidget(self.setpoint_input, 0, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.kp_input, 1, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.ki_input, 2, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.kd_input, 3, 1, alignment=Qt.AlignLeft)
        self.right_content_layout.addWidget(self.apply_button, 4, 1, alignment=Qt.AlignLeft)

        # create a vertical line as separator between left and right side
        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)
        self.vertical_line.setStyleSheet("background-color: white")

        #ADD the content to layout
        self.content_top_layout.addWidget(self.left_menu)
        self.content_top_layout.addWidget(self.vertical_line)
        self.content_top_layout.addWidget(self.right_menu)

        # create the central line separator
        self.central_horizontal_line = QFrame()
        self.central_horizontal_line.setFrameShape(QFrame.HLine)
        self.central_horizontal_line.setFrameShadow(QFrame.Sunken)
        self.central_horizontal_line.setStyleSheet("background-color: white")
        
        #create the central layout
        self.central_layout = QFrame()
        self.central_layout.setStyleSheet("background-color: #434544")

        #create de central layout content
        self.central_content_layout = QHBoxLayout(self.central_layout)
        self.central_content_layout.setContentsMargins(10, 0, 10, 0)
        
        # Output display
        self.output_label = QLabel("Output:")
        self.output_label.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.output_display = QLabel("0.0")
        self.output_display.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_display)
        self.central_content_layout.addLayout(output_layout)
        
        # Error display
        self.error_label = QLabel("Error:")
        self.error_label.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.error_display = QLabel("0.0")
        self.error_display.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        error_layout = QHBoxLayout()
        error_layout.addWidget(self.error_label)
        error_layout.addWidget(self.error_display)
        self.central_content_layout.addLayout(error_layout)

        #create the bottom line separator
        self.bottom_horizontal_line = QFrame()
        self.bottom_horizontal_line.setFrameShape(QFrame.HLine)
        self.bottom_horizontal_line.setFrameShadow(QFrame.Sunken)
        self.bottom_horizontal_line.setStyleSheet("background-color: white")

        #create bottom layout
        self.bottom_layout = QFrame()
        self.bottom_layout.setStyleSheet("background-color: #434544")

        #create the bottom content layout
        self.bottom_content_layout = QHBoxLayout(self.bottom_layout)
        self.bottom_content_layout.setContentsMargins(10,0,10,0)
        
        #ADD start Button
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet("background-color: green; color: white")
        self.start_button.setMinimumWidth(150)
        self.start_button.setMaximumWidth(150)

        #ADD Stop button
        self.stop_button = QPushButton("Stop")
        self.stop_button.setStyleSheet("background-color: green; color: white")
        self.stop_button.setMinimumWidth(150)
        self.stop_button.setMaximumWidth(150)

        #Add button to bottom layout
        self.bottom_content_layout.addWidget(self.start_button)
        self.bottom_content_layout.addWidget(self.stop_button)

        #Add the content to main layout
        self.main_layout.addWidget(self.content)
        self.main_layout.addWidget(self.central_horizontal_line)
        self.main_layout.addWidget(self.central_layout)
        self.main_layout.addWidget(self.bottom_horizontal_line)
        self.main_layout.addWidget(self.bottom_layout)

        #Central widget
        self.setCentralWidget(self.central_frame)
    

def create_and_show_window():
    app = QApplication(sys.argv)  # Criação da aplicação
    window = Pid_Control()  # Criação da janela
    window.show()  # Exibe a janela
    sys.exit(app.exec())  # Execução do loop da aplicação

def start_application():
    create_and_show_window()

if __name__ == "__main__":
    start_application()