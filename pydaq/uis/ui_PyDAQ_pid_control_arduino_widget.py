# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_pid_control_Arduino_widgetlcJVCN.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Arduino_PID_Control(object):
    def setupUi(self, Arduino_PID_Control):
        if not Arduino_PID_Control.objectName():
            Arduino_PID_Control.setObjectName(u"Arduino_PID_Control")
        Arduino_PID_Control.resize(519, 840)
        Arduino_PID_Control.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QTabWidget::pane { \n"
"   border: 1px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  	background-color: rgb(77, 77, 77);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  	background-color: rgb(140, 140, 140);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:selected:hover {\n"
"  	background-color: rgb(140, 140, 140);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:hover {\n"
"  	background-color: rgb(109, 109, 109);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:middle {\n"
"	border-right: 1px dashed rgb(166, 166, 166);\n"
"	border-left: 1px dashed rgb(166, 166, 166);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar:"
                        ":tab:last {\n"
"	border-top-right-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:first {\n"
"	border-top-left-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:focus{\n"
"    background-color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	background-color: rgb(77, 77, 77);\n"
"	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"    image: url(:/imgs/imgs/drop_up_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px sol"
                        "id rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"    image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(77, "
                        "77, 77);\n"
"	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 2px solid rgb(127, 167, 127);\n"
"	border-left: 2px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 2px solid rgb(0, 0, 0);\n"
"	border-right: 2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 79, 0);\n"
"\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	\n"
"	font: 12pt \"Helve"
                        "tica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QWidget{\n"
"	font: 12pt \"Helvetica\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(77, 77, 77);\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	border-radius: 6px;\n"
"	border-top: 1.5px solid rgb(0, 0, 0);\n"
"	border-left: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	border-bottom: 1.5px solid rgb(160, 160, 160);\n"
"	border-right: 1.5px solid rgb(160, 160, 160);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:hover{\n"
"	background-color: #9F9F9F;\n"
"}\n"
"\n"
"QRadioButton::indicator::pressed{\n"
"	border: 1.5px solid #505050\n"
"}\n"
""
                        "\n"
"QPushButton#reload_devices{\n"
"	image: url(:/imgs/imgs/reload.png);\n"
"	width: 11px;\n"
"	background-color: rgb(0, 79, 0);\n"
"\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	\n"
"	font: 12pt \"Helvetica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton#reload_devices:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QPushButton#reload_devices:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	background-color: rgb(77, 77, 77);\n"
"	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"    background-color: rgb(50, 50, 50);\n"
"    \n"
"    border-top: 1.5px solid rgb(30, 30, 30);\n"
"    border-left: 1.5px s"
                        "olid rgb(30, 30, 30);\n"
"    \n"
"    border-bottom: 1.5px solid rgb(100, 100, 100);\n"
"    border-right: 1.5px solid rgb(100, 100, 100);\n"
"    \n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"    image: url(:/imgs/imgs/drop_up_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"    image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	"
                        "border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Arduino_PID_Control)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(Arduino_PID_Control)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.pushButton_start = QPushButton(Arduino_PID_Control)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(120, 30))
        self.pushButton_start.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.pushButton_start, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_top = QWidget(Arduino_PID_Control)
        self.widget_top.setObjectName(u"widget_top")
        self.gridLayout_2 = QGridLayout(self.widget_top)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_unit = QWidget(self.widget_top)
        self.widget_unit.setObjectName(u"widget_unit")
        self.horizontalLayout = QHBoxLayout(self.widget_unit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_unit = QLineEdit(self.widget_unit)
        self.lineEdit_unit.setObjectName(u"lineEdit_unit")

        self.horizontalLayout.addWidget(self.lineEdit_unit)


        self.gridLayout_2.addWidget(self.widget_unit, 3, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.widget_kp = QWidget(self.widget_top)
        self.widget_kp.setObjectName(u"widget_kp")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_kp)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.doubleSpinBox_kp = QDoubleSpinBox(self.widget_kp)
        self.doubleSpinBox_kp.setObjectName(u"doubleSpinBox_kp")
        self.doubleSpinBox_kp.setSingleStep(0.100000000000000)
        self.doubleSpinBox_kp.setValue(1.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_kp)


        self.gridLayout_2.addWidget(self.widget_kp, 7, 2, 1, 1)

        self.label = QLabel(self.widget_top)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 10, 0, 1, 1)

        self.widget_period = QWidget(self.widget_top)
        self.widget_period.setObjectName(u"widget_period")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_period)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.doubleSpinBox_period = QDoubleSpinBox(self.widget_period)
        self.doubleSpinBox_period.setObjectName(u"doubleSpinBox_period")
        self.doubleSpinBox_period.setMaximum(9999999.000000000000000)
        self.doubleSpinBox_period.setSingleStep(0.100000000000000)
        self.doubleSpinBox_period.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_period)


        self.gridLayout_2.addWidget(self.widget_period, 5, 2, 1, 1)

        self.label_unit = QLabel(self.widget_top)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_unit, 3, 0, 1, 1)

        self.widget_equation = QWidget(self.widget_top)
        self.widget_equation.setObjectName(u"widget_equation")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_equation)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_equation = QLineEdit(self.widget_equation)
        self.lineEdit_equation.setObjectName(u"lineEdit_equation")

        self.horizontalLayout_9.addWidget(self.lineEdit_equation)


        self.gridLayout_2.addWidget(self.widget_equation, 4, 2, 1, 1)

        self.label_path = QLabel(self.widget_top)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_2.addWidget(self.label_path, 11, 0, 1, 1)

        self.widget_arduino = QWidget(self.widget_top)
        self.widget_arduino.setObjectName(u"widget_arduino")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_arduino)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_arduino = QComboBox(self.widget_arduino)
        self.comboBox_arduino.setObjectName(u"comboBox_arduino")
        self.comboBox_arduino.setMinimumSize(QSize(0, 0))
        self.comboBox_arduino.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_2.addWidget(self.comboBox_arduino)

        self.reload_devices = QPushButton(self.widget_arduino)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMinimumSize(QSize(22, 22))
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.reload_devices)


        self.gridLayout_2.addWidget(self.widget_arduino, 1, 2, 1, 1)

        self.label_equation = QLabel(self.widget_top)
        self.label_equation.setObjectName(u"label_equation")
        self.label_equation.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_equation, 4, 0, 1, 1)

        self.label_type = QLabel(self.widget_top)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_type, 6, 0, 1, 1)

        self.widget = QWidget(self.widget_top)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_12 = QHBoxLayout(self.widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.yes_save_radio = QRadioButton(self.widget)
        self.save_radio_group = QButtonGroup(Arduino_PID_Control)
        self.save_radio_group.setObjectName(u"save_radio_group")
        self.save_radio_group.addButton(self.yes_save_radio)
        self.yes_save_radio.setObjectName(u"yes_save_radio")
        self.yes_save_radio.setChecked(True)

        self.horizontalLayout_12.addWidget(self.yes_save_radio)

        self.no_save_radio = QRadioButton(self.widget)
        self.save_radio_group.addButton(self.no_save_radio)
        self.no_save_radio.setObjectName(u"no_save_radio")

        self.horizontalLayout_12.addWidget(self.no_save_radio)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.widget, 10, 2, 1, 1)

        self.line = QFrame(self.widget_top)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 1, 14, 1)

        self.widget_ki = QWidget(self.widget_top)
        self.widget_ki.setObjectName(u"widget_ki")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_ki)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.doubleSpinBox_ki = QDoubleSpinBox(self.widget_ki)
        self.doubleSpinBox_ki.setObjectName(u"doubleSpinBox_ki")
        self.doubleSpinBox_ki.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_ki)


        self.gridLayout_2.addWidget(self.widget_ki, 8, 2, 1, 1)

        self.label_kp = QLabel(self.widget_top)
        self.label_kp.setObjectName(u"label_kp")
        self.label_kp.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_kp, 7, 0, 1, 1)

        self.widget_path = QWidget(self.widget_top)
        self.widget_path.setObjectName(u"widget_path")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_path)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.path_line_edit = QLineEdit(self.widget_path)
        self.path_line_edit.setObjectName(u"path_line_edit")
        self.path_line_edit.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_10.addWidget(self.path_line_edit)

        self.path_folder_browse = QPushButton(self.widget_path)
        self.path_folder_browse.setObjectName(u"path_folder_browse")
        self.path_folder_browse.setMinimumSize(QSize(70, 30))

        self.horizontalLayout_10.addWidget(self.path_folder_browse)


        self.gridLayout_2.addWidget(self.widget_path, 11, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_setpoint = QLabel(self.widget_top)
        self.label_setpoint.setObjectName(u"label_setpoint")
        self.label_setpoint.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_setpoint, 2, 0, 1, 1)

        self.label_ki = QLabel(self.widget_top)
        self.label_ki.setObjectName(u"label_ki")
        self.label_ki.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_ki, 8, 0, 1, 1)

        self.label_kd = QLabel(self.widget_top)
        self.label_kd.setObjectName(u"label_kd")
        self.label_kd.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_kd, 9, 0, 1, 1)

        self.widget_type = QWidget(self.widget_top)
        self.widget_type.setObjectName(u"widget_type")
        self.widget_type.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_type)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.comboBox_type = QComboBox(self.widget_type)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setMinimumSize(QSize(0, 25))
        self.comboBox_type.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_7.addWidget(self.comboBox_type)


        self.gridLayout_2.addWidget(self.widget_type, 6, 2, 1, 1)

        self.label_periody = QLabel(self.widget_top)
        self.label_periody.setObjectName(u"label_periody")
        self.label_periody.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_periody, 5, 0, 1, 1)

        self.label_arduino = QLabel(self.widget_top)
        self.label_arduino.setObjectName(u"label_arduino")
        self.label_arduino.setMinimumSize(QSize(154, 30))
        self.label_arduino.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_2.addWidget(self.label_arduino, 1, 0, 1, 1)

        self.widget_setpoint = QWidget(self.widget_top)
        self.widget_setpoint.setObjectName(u"widget_setpoint")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_setpoint)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.doubleSpinBox_setpoint = QDoubleSpinBox(self.widget_setpoint)
        self.doubleSpinBox_setpoint.setObjectName(u"doubleSpinBox_setpoint")
        self.doubleSpinBox_setpoint.setMinimumSize(QSize(100, 0))
        self.doubleSpinBox_setpoint.setMaximumSize(QSize(100, 16777215))
        self.doubleSpinBox_setpoint.setMaximum(9999999.000000000000000)
        self.doubleSpinBox_setpoint.setSingleStep(0.100000000000000)
        self.doubleSpinBox_setpoint.setValue(5.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_setpoint)

        self.comboBox_setpoint = QComboBox(self.widget_setpoint)
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.setObjectName(u"comboBox_setpoint")
        self.comboBox_setpoint.setMinimumSize(QSize(190, 0))
        self.comboBox_setpoint.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_setpoint)


        self.gridLayout_2.addWidget(self.widget_setpoint, 2, 2, 1, 1)

        self.pushButton_confirm = QPushButton(self.widget_top)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setMinimumSize(QSize(80, 30))
        self.pushButton_confirm.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_confirm, 12, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.widget_kd = QWidget(self.widget_top)
        self.widget_kd.setObjectName(u"widget_kd")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_kd)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.doubleSpinBox_kd = QDoubleSpinBox(self.widget_kd)
        self.doubleSpinBox_kd.setObjectName(u"doubleSpinBox_kd")
        self.doubleSpinBox_kd.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_kd)


        self.gridLayout_2.addWidget(self.widget_kd, 9, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.widget_top, 2, 0, 1, 1)

        self.line_3 = QFrame(Arduino_PID_Control)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 1)

        self.frame_equation = QFrame(Arduino_PID_Control)
        self.frame_equation.setObjectName(u"frame_equation")
        self.frame_equation.setMinimumSize(QSize(400, 120))
        self.frame_equation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_equation.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_equation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_image = QWidget(self.frame_equation)
        self.widget_image.setObjectName(u"widget_image")
        self.widget_image.setMinimumSize(QSize(0, 100))
        self.image_layout = QHBoxLayout(self.widget_image)
        self.image_layout.setObjectName(u"image_layout")

        self.verticalLayout.addWidget(self.widget_image)


        self.gridLayout.addWidget(self.frame_equation, 3, 0, 1, 1)


        self.retranslateUi(Arduino_PID_Control)

        QMetaObject.connectSlotsByName(Arduino_PID_Control)
    # setupUi

    def retranslateUi(self, Arduino_PID_Control):
        Arduino_PID_Control.setWindowTitle(QCoreApplication.translate("Arduino_PID_Control", u"Form", None))
        self.pushButton_start.setText(QCoreApplication.translate("Arduino_PID_Control", u"PID CONTROL", None))
        self.label.setText(QCoreApplication.translate("Arduino_PID_Control", u"Save Data?", None))
        self.label_unit.setText(QCoreApplication.translate("Arduino_PID_Control", u"Unit:", None))
        self.label_path.setText(QCoreApplication.translate("Arduino_PID_Control", u"Data path:", None))
        self.reload_devices.setText("")
        self.label_equation.setText(QCoreApplication.translate("Arduino_PID_Control", u"Equation (?):", None))
        self.label_type.setText(QCoreApplication.translate("Arduino_PID_Control", u"Controler type?", None))
        self.yes_save_radio.setText(QCoreApplication.translate("Arduino_PID_Control", u"Yes", None))
        self.no_save_radio.setText(QCoreApplication.translate("Arduino_PID_Control", u"No", None))
        self.label_kp.setText(QCoreApplication.translate("Arduino_PID_Control", u"Kp:", None))
        self.path_folder_browse.setText(QCoreApplication.translate("Arduino_PID_Control", u"Browse", None))
        self.label_setpoint.setText(QCoreApplication.translate("Arduino_PID_Control", u"Setpoint:", None))
        self.label_ki.setText(QCoreApplication.translate("Arduino_PID_Control", u"Ki:", None))
        self.label_kd.setText(QCoreApplication.translate("Arduino_PID_Control", u"Kd:", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("Arduino_PID_Control", u"P", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("Arduino_PID_Control", u"PI", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("Arduino_PID_Control", u"PD", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("Arduino_PID_Control", u"PID", None))

        self.label_periody.setText(QCoreApplication.translate("Arduino_PID_Control", u"Sampling period (s):", None))
        self.label_arduino.setText(QCoreApplication.translate("Arduino_PID_Control", u"Arduino:", None))
        self.comboBox_setpoint.setItemText(0, QCoreApplication.translate("Arduino_PID_Control", u"Voltage (V)", None))
        self.comboBox_setpoint.setItemText(1, QCoreApplication.translate("Arduino_PID_Control", u"Temperature (C\u00b0)", None))
        self.comboBox_setpoint.setItemText(2, QCoreApplication.translate("Arduino_PID_Control", u"Other", None))

        self.pushButton_confirm.setText(QCoreApplication.translate("Arduino_PID_Control", u"Confirm", None))
    # retranslateUi

