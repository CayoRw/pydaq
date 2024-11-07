# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_pid_control_window_dialogdenNiD.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_Plot_PID_Window(object):
    def setupUi(self, Dialog_Plot_PID_Window):
        if not Dialog_Plot_PID_Window.objectName():
            Dialog_Plot_PID_Window.setObjectName(u"Dialog_Plot_PID_Window")
        Dialog_Plot_PID_Window.resize(455, 502)
        Dialog_Plot_PID_Window.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout = QVBoxLayout(Dialog_Plot_PID_Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog_Plot_PID_Window)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 4, 2, 2, 1)

        self.doubleSpinBox_SetpointDialog = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_SetpointDialog.setObjectName(u"doubleSpinBox_SetpointDialog")
        self.doubleSpinBox_SetpointDialog.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.doubleSpinBox_SetpointDialog, 4, 3, 1, 1)

        self.doubleSpinBox_DisturbeDialog = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_DisturbeDialog.setObjectName(u"doubleSpinBox_DisturbeDialog")

        self.gridLayout.addWidget(self.doubleSpinBox_DisturbeDialog, 5, 3, 1, 1)

        self.doubleSpinBox_KiDialog = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_KiDialog.setObjectName(u"doubleSpinBox_KiDialog")

        self.gridLayout.addWidget(self.doubleSpinBox_KiDialog, 2, 3, 1, 1)

        self.comboBox_TypeDialog = QComboBox(self.widget_2)
        self.comboBox_TypeDialog.setObjectName(u"comboBox_TypeDialog")

        self.gridLayout.addWidget(self.comboBox_TypeDialog, 0, 3, 1, 1)

        self.label_Kp = QLabel(self.widget_2)
        self.label_Kp.setObjectName(u"label_Kp")

        self.gridLayout.addWidget(self.label_Kp, 1, 1, 1, 1)

        self.label_Ki = QLabel(self.widget_2)
        self.label_Ki.setObjectName(u"label_Ki")

        self.gridLayout.addWidget(self.label_Ki, 2, 1, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_Disturbe = QLabel(self.widget_2)
        self.label_Disturbe.setObjectName(u"label_Disturbe")

        self.gridLayout.addWidget(self.label_Disturbe, 5, 1, 1, 1)

        self.doubleSpinBox_KpDialog = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_KpDialog.setObjectName(u"doubleSpinBox_KpDialog")

        self.gridLayout.addWidget(self.doubleSpinBox_KpDialog, 1, 3, 1, 1)

        self.label_Setpoint = QLabel(self.widget_2)
        self.label_Setpoint.setObjectName(u"label_Setpoint")
        self.label_Setpoint.setMinimumSize(QSize(100, 30))
        self.label_Setpoint.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label_Setpoint, 4, 1, 1, 1)

        self.label_Kd = QLabel(self.widget_2)
        self.label_Kd.setObjectName(u"label_Kd")

        self.gridLayout.addWidget(self.label_Kd, 3, 1, 1, 1)

        self.doubleSpinBox_KdDialog = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_KdDialog.setObjectName(u"doubleSpinBox_KdDialog")

        self.gridLayout.addWidget(self.doubleSpinBox_KdDialog, 3, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.pushButton_apply = QPushButton(self.widget)
        self.pushButton_apply.setObjectName(u"pushButton_apply")
        self.pushButton_apply.setMinimumSize(QSize(100, 0))
        self.pushButton_apply.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.pushButton_apply, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_image = QFrame(self.widget)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_image)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_image = QWidget(self.frame_image)
        self.widget_image.setObjectName(u"widget_image")
        self.image_layout = QHBoxLayout(self.widget_image)
        self.image_layout.setObjectName(u"image_layout")

        self.verticalLayout_2.addWidget(self.widget_image)


        self.verticalLayout_3.addWidget(self.frame_image)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_startstop = QPushButton(self.widget_3)
        self.pushButton_startstop.setObjectName(u"pushButton_startstop")
        self.pushButton_startstop.setMinimumSize(QSize(0, 0))
        self.pushButton_startstop.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_startstop)

        self.pushButton_close = QPushButton(self.widget_3)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(60, 0))
        self.pushButton_close.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_close)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog_Plot_PID_Window)

        QMetaObject.connectSlotsByName(Dialog_Plot_PID_Window)
    # setupUi

    def retranslateUi(self, Dialog_Plot_PID_Window):
        Dialog_Plot_PID_Window.setWindowTitle(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Dialog", None))
        self.label_Kp.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Kp:", None))
        self.label_Ki.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Ki:", None))
        self.label.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Controler type?", None))
        self.label_Disturbe.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Disturbe (?):", None))
        self.label_Setpoint.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Setpoint:", None))
        self.label_Kd.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Kd:", None))
        self.pushButton_apply.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Apply", None))
        self.pushButton_startstop.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Stop", None))
        self.pushButton_close.setText(QCoreApplication.translate("Dialog_Plot_PID_Window", u"Close", None))
    # retranslateUi

