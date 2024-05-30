# pid_control.py

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyGUI(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Exemplo de Interface Gráfica')
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Clique aqui', self)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.information(self, 'Mensagem', 'Você clicou no botão!')

def create_application():
    return QApplication([])

