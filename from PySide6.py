from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QDoubleSpinBox, QPushButton

class PID_Control_Window_Dialog(QDialog):
    # Sinal personalizado para enviar o valor ao fechar o diálogo
    value_chosen = Signal(float)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog")

        # QDoubleSpinBox no Dialog
        self.double_spin_box2 = QDoubleSpinBox()
        self.double_spin_box2.setRange(0, 100)

        # Layout do Dialog
        layout = QVBoxLayout()
        layout.addWidget(self.double_spin_box2)

        # Botão para chamar go_back
        button_ok = QPushButton("OK")
        button_ok.clicked.connect(self.go_back)
        layout.addWidget(button_ok)

        self.setLayout(layout)

    def go_back(self):
        # Emite o valor do QDoubleSpinBox2 antes de fechar
        self.value_chosen.emit(self.double_spin_box2.value())
        # Interrompe a animação e fecha o diálogo
        self.ani.event_source.stop()
        self.close()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Widget")

        # QDoubleSpinBox no Widget principal
        self.double_spin_box = QDoubleSpinBox()
        self.double_spin_box.setRange(0, 100)

        # Botão para abrir o Dialog
        self.button_open_dialog = QPushButton("Open Dialog")
        self.button_open_dialog.clicked.connect(self.show_graph_window)

        # Layout do Widget principal
        layout = QVBoxLayout()
        layout.addWidget(self.double_spin_box)
        layout.addWidget(self.button_open_dialog)

        self.setLayout(layout)

    def show_graph_window(self):
        # Cria a instância do diálogo
        plot_window = PID_Control_Window_Dialog()

        # Conecta o sinal value_chosen para atualizar o QDoubleSpinBox no QWidget
        plot_window.value_chosen.connect(self.double_spin_box.setValue)

        # Executa o diálogo
        plot_window.exec()


# Execução da aplicação
if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
