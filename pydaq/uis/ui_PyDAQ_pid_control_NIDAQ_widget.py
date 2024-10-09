# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_pid_control_NIDAQ_widgetjxloYd.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_NIDAQ_PID_Control(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(643, 795)
        Form.setStyleSheet(u"QWidget{\n"
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
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(120, 30))
        self.pushButton_start.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.pushButton_start, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_top = QWidget(Form)
        self.widget_top.setObjectName(u"widget_top")
        self.gridLayout_2 = QGridLayout(self.widget_top)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_kp = QLabel(self.widget_top)
        self.label_kp.setObjectName(u"label_kp")
        self.label_kp.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_kp, 9, 0, 1, 1)

        self.widget_setpoint = QWidget(self.widget_top)
        self.widget_setpoint.setObjectName(u"widget_setpoint")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_setpoint)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_setpoint = QLineEdit(self.widget_setpoint)
        self.lineEdit_setpoint.setObjectName(u"lineEdit_setpoint")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_setpoint.sizePolicy().hasHeightForWidth())
        self.lineEdit_setpoint.setSizePolicy(sizePolicy)
        self.lineEdit_setpoint.setMinimumSize(QSize(100, 25))
        self.lineEdit_setpoint.setMaximumSize(QSize(90, 22))

        self.horizontalLayout_3.addWidget(self.lineEdit_setpoint)

        self.comboBox_setpoint = QComboBox(self.widget_setpoint)
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.setObjectName(u"comboBox_setpoint")
        self.comboBox_setpoint.setMinimumSize(QSize(190, 0))
        self.comboBox_setpoint.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_setpoint)


        self.gridLayout_2.addWidget(self.widget_setpoint, 4, 2, 1, 1)

        self.label_setpoint = QLabel(self.widget_top)
        self.label_setpoint.setObjectName(u"label_setpoint")
        self.label_setpoint.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_setpoint, 4, 0, 1, 1)

        self.widget_equation = QWidget(self.widget_top)
        self.widget_equation.setObjectName(u"widget_equation")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_equation)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_equation = QLineEdit(self.widget_equation)
        self.lineEdit_equation.setObjectName(u"lineEdit_equation")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_equation.sizePolicy().hasHeightForWidth())
        self.lineEdit_equation.setSizePolicy(sizePolicy1)
        self.lineEdit_equation.setMinimumSize(QSize(150, 0))
        self.lineEdit_equation.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_9.addWidget(self.lineEdit_equation)


        self.gridLayout_2.addWidget(self.widget_equation, 6, 2, 1, 1)

        self.widget_ki = QWidget(self.widget_top)
        self.widget_ki.setObjectName(u"widget_ki")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_ki)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_kd = QLineEdit(self.widget_ki)
        self.lineEdit_kd.setObjectName(u"lineEdit_kd")
        self.lineEdit_kd.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_kd)


        self.gridLayout_2.addWidget(self.widget_ki, 10, 2, 1, 1)

        self.label_kd = QLabel(self.widget_top)
        self.label_kd.setObjectName(u"label_kd")
        self.label_kd.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_kd, 11, 0, 1, 1)

        self.label_equation = QLabel(self.widget_top)
        self.label_equation.setObjectName(u"label_equation")
        self.label_equation.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_equation, 6, 0, 1, 1)

        self.widget_kp = QWidget(self.widget_top)
        self.widget_kp.setObjectName(u"widget_kp")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_kp)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_kp = QLineEdit(self.widget_kp)
        self.lineEdit_kp.setObjectName(u"lineEdit_kp")
        self.lineEdit_kp.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_kp)


        self.gridLayout_2.addWidget(self.widget_kp, 9, 2, 1, 1)

        self.label_path = QLabel(self.widget_top)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_2.addWidget(self.label_path, 12, 0, 1, 1)

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


        self.gridLayout_2.addWidget(self.widget_type, 8, 2, 1, 1)

        self.pushButton_confirm = QPushButton(self.widget_top)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setMinimumSize(QSize(80, 30))
        self.pushButton_confirm.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_confirm, 13, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_arduino = QLabel(self.widget_top)
        self.label_arduino.setObjectName(u"label_arduino")
        self.label_arduino.setMinimumSize(QSize(154, 30))
        self.label_arduino.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_2.addWidget(self.label_arduino, 1, 0, 1, 1)

        self.label_ki = QLabel(self.widget_top)
        self.label_ki.setObjectName(u"label_ki")
        self.label_ki.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_ki, 10, 0, 1, 1)

        self.label = QLabel(self.widget_top)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.widget_path = QWidget(self.widget_top)
        self.widget_path.setObjectName(u"widget_path")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_path)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_path = QLineEdit(self.widget_path)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_10.addWidget(self.lineEdit_path)

        self.pushButton_browse = QPushButton(self.widget_path)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setMinimumSize(QSize(70, 30))

        self.horizontalLayout_10.addWidget(self.pushButton_browse)


        self.gridLayout_2.addWidget(self.widget_path, 12, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_periody = QLabel(self.widget_top)
        self.label_periody.setObjectName(u"label_periody")
        self.label_periody.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_periody, 7, 0, 1, 1)

        self.line = QFrame(self.widget_top)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 1, 15, 1)

        self.widget_period = QWidget(self.widget_top)
        self.widget_period.setObjectName(u"widget_period")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_period)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_period = QLineEdit(self.widget_period)
        self.lineEdit_period.setObjectName(u"lineEdit_period")
        self.lineEdit_period.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_period)


        self.gridLayout_2.addWidget(self.widget_period, 7, 2, 1, 1)

        self.widget_unit = QWidget(self.widget_top)
        self.widget_unit.setObjectName(u"widget_unit")
        self.horizontalLayout = QHBoxLayout(self.widget_unit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_unit = QLineEdit(self.widget_unit)
        self.lineEdit_unit.setObjectName(u"lineEdit_unit")
        sizePolicy1.setHeightForWidth(self.lineEdit_unit.sizePolicy().hasHeightForWidth())
        self.lineEdit_unit.setSizePolicy(sizePolicy1)
        self.lineEdit_unit.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_unit)


        self.gridLayout_2.addWidget(self.widget_unit, 5, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.widget_kd = QWidget(self.widget_top)
        self.widget_kd.setObjectName(u"widget_kd")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_kd)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_ki = QLineEdit(self.widget_kd)
        self.lineEdit_ki.setObjectName(u"lineEdit_ki")
        self.lineEdit_ki.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_ki)


        self.gridLayout_2.addWidget(self.widget_kd, 11, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.widget_arduino = QWidget(self.widget_top)
        self.widget_arduino.setObjectName(u"widget_arduino")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_arduino)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_arduino = QComboBox(self.widget_arduino)
        self.comboBox_arduino.setObjectName(u"comboBox_arduino")
        self.comboBox_arduino.setMinimumSize(QSize(0, 0))
        self.comboBox_arduino.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_2.addWidget(self.comboBox_arduino)

        self.pushButton_reload = QPushButton(self.widget_arduino)
        self.pushButton_reload.setObjectName(u"pushButton_reload")
        self.pushButton_reload.setMinimumSize(QSize(22, 22))
        self.pushButton_reload.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.pushButton_reload)


        self.gridLayout_2.addWidget(self.widget_arduino, 1, 2, 1, 1)

        self.label_type = QLabel(self.widget_top)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_type, 8, 0, 1, 1)

        self.label_unit = QLabel(self.widget_top)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_unit, 5, 0, 1, 1)

        self.label_2 = QLabel(self.widget_top)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.widget = QWidget(self.widget_top)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)


        self.gridLayout_2.addWidget(self.widget, 2, 2, 1, 1)

        self.widget_2 = QWidget(self.widget_top)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_11.addWidget(self.comboBox_2)


        self.gridLayout_2.addWidget(self.widget_2, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_top, 2, 0, 1, 1)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 1)

        self.frame_equation = QFrame(Form)
        self.frame_equation.setObjectName(u"frame_equation")
        self.frame_equation.setMinimumSize(QSize(400, 70))
        self.frame_equation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_equation.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_equation)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_pidequation = QLabel(self.frame_equation)
        self.label_pidequation.setObjectName(u"label_pidequation")

        self.gridLayout_5.addWidget(self.label_pidequation, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.frame_equation, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"PID CONTROL", None))
        self.label_kp.setText(QCoreApplication.translate("Form", u"Kp", None))
        self.comboBox_setpoint.setItemText(0, QCoreApplication.translate("Form", u"Voltage (V)", None))
        self.comboBox_setpoint.setItemText(1, QCoreApplication.translate("Form", u"Temperature (C\u00b0)", None))
        self.comboBox_setpoint.setItemText(2, QCoreApplication.translate("Form", u"Others", None))

        self.label_setpoint.setText(QCoreApplication.translate("Form", u"Setpoint:", None))
        self.label_kd.setText(QCoreApplication.translate("Form", u"Kd", None))
        self.label_equation.setText(QCoreApplication.translate("Form", u"Equation (?)", None))
        self.label_path.setText(QCoreApplication.translate("Form", u"Data path", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("Form", u"P", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("Form", u"PI", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("Form", u"PD", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("Form", u"PID", None))

        self.pushButton_confirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.label_arduino.setText(QCoreApplication.translate("Form", u"Choose your device:", None))
        self.label_ki.setText(QCoreApplication.translate("Form", u"Ki", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choose channel:", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_periody.setText(QCoreApplication.translate("Form", u"Sampling period (s)", None))
        self.pushButton_reload.setText("")
        self.label_type.setText(QCoreApplication.translate("Form", u"Controler type?", None))
        self.label_unit.setText(QCoreApplication.translate("Form", u"Unit:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Terminal config.", None))
        self.label_pidequation.setText(QCoreApplication.translate("Form", u"Equacao", None))
    # retranslateUi

