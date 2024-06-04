import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PYDAQ - Step Response (Arduino)")  # window name
        self.setFixedSize(773, 345)  # fixed value of the screen

        self.central_frame = QFrame()  # create the central widget

        self.main_layout = QVBoxLayout(self.central_frame)  # create the main layout
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # create content frame
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #404040")

        self.content_layout = QHBoxLayout(self.content)
        self.content_layout.setContentsMargins(20, 0, 10, 0)
        self.content_layout.setSpacing(0)

        # create the left frame
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #404040")
        self.left_menu.setMinimumWidth(250)
        self.left_menu.setMaximumWidth(250)

        # create the left frame layout
        self.left_menu_layout = QGridLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(10)

        self.label1 = QLabel("Choose your arduino:")
        self.label1.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label1, 0, 0, Qt.AlignLeft)

        self.label2 = QLabel("Sample period (s):")
        self.label2.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label2, 1, 0, Qt.AlignLeft)

        self.label3 = QLabel("Session duration (s)")
        self.label3.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label3, 2, 0, Qt.AlignLeft)
        
        self.label4 = QLabel("Get PID Parametres?")
        self.label4.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label4, 3, 0, Qt.AlignLeft)

        self.label5 = QLabel("Plot Data?")
        self.label5.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label5, 4, 0, Qt.AlignLeft)

        self.label6 = QLabel("Save Data?")
        self.label6.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label6, 5, 0, Qt.AlignLeft)

        self.label7 = QLabel("Path")
        self.label7.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.left_menu_layout.addWidget(self.label7, 6, 0, Qt.AlignLeft)

        # create the right frame
        self.right_menu = QFrame()
        self.right_menu.setStyleSheet("background-color: #404040")
        self.right_menu.setMinimumWidth(386.5)
        self.right_menu.setMaximumWidth(386.5)

        # create the right frame layout
        self.right_menu_layout = QGridLayout(self.right_menu)
        self.right_menu_layout.setContentsMargins(30, 0, 0, 0)
        self.right_menu_layout.setSpacing(0)

        self.labelr1 = QComboBox()
        self.labelr1.setStyleSheet("background-color: white")
        self.labelr1.setMinimumSize(200,25)
        self.right_menu_layout.addWidget(self.labelr1, 0, 0, Qt.AlignLeft)

        self.labelr2 = QLineEdit()
        self.labelr2.setStyleSheet("background-color: white")
        self.right_menu_layout.addWidget(self.labelr2, 1, 0, Qt.AlignLeft)

        self.labelr3 = QLineEdit()
        self.labelr3.setStyleSheet("background-color: white")
        self.right_menu_layout.addWidget(self.labelr3, 2, 0, Qt.AlignLeft)
        
        # Creating QButtonGroup for PID control
        self.digital_group = QButtonGroup()
        self.digital_group.setExclusive(True)
        
        self.labelr4 = QCheckBox("Yes")
        self.labelr4.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.digital_group.addButton(self.labelr4)
        self.right_menu_layout.addWidget(self.labelr4, 3, 0, Qt.AlignLeft)
        
        self.labelr5 = QCheckBox("No")
        self.labelr5.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.digital_group.addButton(self.labelr5)
        self.right_menu_layout.addWidget(self.labelr5, 3, 1, Qt.AlignLeft)
        
        # Creating QButtonGroup for Plotar
        self.plot_group = QButtonGroup()
        self.plot_group.setExclusive(True)

        self.labelr6 = QCheckBox("Yes")
        self.labelr6.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.plot_group.addButton(self.labelr6)
        self.right_menu_layout.addWidget(self.labelr6, 4, 0, Qt.AlignLeft)

        self.labelr7 = QCheckBox("No")
        self.labelr7.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.plot_group.addButton(self.labelr7)
        self.right_menu_layout.addWidget(self.labelr7, 4, 1, Qt.AlignLeft)

        # Creating QButtonGroup for Salvar
        self.save_group = QButtonGroup()
        self.save_group.setExclusive(True)

        self.labelr8 = QCheckBox("Yes")
        self.labelr8.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.save_group.addButton(self.labelr8)
        self.right_menu_layout.addWidget(self.labelr8, 5, 0, Qt.AlignLeft)

        self.labelr9 = QCheckBox("No")
        self.labelr9.setStyleSheet("font: 100 15pt 'Helvetica'; color: white")
        self.save_group.addButton(self.labelr9)
        self.right_menu_layout.addWidget(self.labelr9, 5, 1, Qt.AlignLeft)

        self.labelr10 = QComboBox()
        self.labelr10.setStyleSheet("background-color: white")
        self.labelr10.setMinimumSize(200,23)
        self.right_menu_layout.addWidget(self.labelr10, 6, 0, Qt.AlignLeft)

        # create a vertical line as separator between left and right side
        self.vertical_line = QFrame()
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)
        self.vertical_line.setStyleSheet("background-color: white")

        self.content_layout.addWidget(self.left_menu)
        self.content_layout.addWidget(self.vertical_line)
        self.content_layout.addWidget(self.right_menu)

        # create the bottom frame
        self.bottom_menu = QFrame()
        self.bottom_menu.setStyleSheet("background-color: #404040")
        self.bottom_menu.setMinimumHeight(60)
        self.bottom_menu.setMaximumHeight(60)

        # create the bottom frame layout
        self.bottom_menu_layout = QHBoxLayout(self.bottom_menu)
        self.bottom_menu_layout.setContentsMargins(10, 0, 10, 0)

        # create STEP RESPONSE Button
        self.get_data_button = QPushButton("STEP RESPONSE")
        self.get_data_button.setStyleSheet("background-color: green; color: white")
        self.get_data_button.setMinimumWidth(120)
        self.get_data_button.setMaximumWidth(120)

        # add get data button in bottom menu
        self.bottom_menu_layout.addWidget(self.get_data_button)

        # create the bottom line separator
        self.horizontal_line = QFrame()
        self.horizontal_line.setFrameShape(QFrame.HLine)
        self.horizontal_line.setFrameShadow(QFrame.Sunken)
        self.horizontal_line.setStyleSheet("background-color: white")

        # Add the content in layout
        self.main_layout.addWidget(self.content)
        self.main_layout.addWidget(self.horizontal_line)
        self.main_layout.addWidget(self.bottom_menu)

        self.setCentralWidget(self.central_frame)
     
    

def create_and_show_window():
    app = QApplication(sys.argv)  # Create app
    window = MainWindow()  # Create window
    window.show()  # show window
    sys.exit(app.exec())  # loop
 
def start_application():
    create_and_show_window()

if __name__ == "__main__":
    start_application()