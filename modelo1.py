import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Slot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Interface Principal')

        self.button = QPushButton('Ver Gráficos')
        self.button.clicked.connect(self.show_graph_window)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.graph_window = None

    @Slot()
    def show_graph_window(self):
        if self.graph_window is None:
            self.graph_window = GraphWindow()
        self.graph_window.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
