import sys
import os
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QTimer
from pydaq.utils.base import Base

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

from ..uis.ui_PyDAQ_pid_control_window_dialog_test import Ui_Dialog_Plot_PID_Window_Test

#python -m pydaq.guis.learning_bokeh

class PlotPIDWindow(QDialog, Ui_Dialog_Plot_PID_Window_Test, Base):
    def __init__(self, *args):
        super(PlotPIDWindow, self).__init__(*args)
        self.setupUi(self)
        self.setMinimumSize(900, 700)

    # Calling the functions
        self.pushButton_startstop.clicked.connect(self.stopstart)

        # Create layout
        self.setWindowTitle("Bokeh and PySide6")
        self.paused = False
        # Create Bokeh plot
        self.x = [0]
        self.y = [0]
        self.plot = figure(title="Dynamic Plot", x_axis_label="Time", y_axis_label="Value")
        self.line = self.plot.line(self.x, self.y, line_width=2)

        # Embed Bokeh plot in QWebEngineView
        self.web_view = QWebEngineView()
        self.update_plot_html()
        self.image_layout.addWidget(self.web_view)

        # Connect buttons to actions
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

#stop/start the event and change the button text
    def stopstart (self):
        self.paused = not self.paused
        if self.paused:
            self.timer.stop()
            self.pushButton_startstop.setText("Start")
        else:
            self.timer.start(1000)
            self.pushButton_startstop.setText("Stop")

    def update_plot_html(self):
        """Generate the Bokeh plot and load it into the QWebEngineView."""
        html = file_html(self.plot, CDN, "Bokeh Plot")
        self.web_view.setHtml(html)

    def update_data(self):
        """Update data for the Bokeh plot dynamically."""
        self.x.append(self.x[-1] + 1)
        self.y.append(self.y[-1] + 1/self.x[-1])  # Example data
        self.line.data_source.data = {'x': self.x, 'y': self.y}
        self.update_plot_html()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = PlotPIDWindow()
    main_win.show()
    sys.exit(app.exec())