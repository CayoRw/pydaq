# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_PID_Control_widgetXIWxEI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Arduino_PID_Control(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(533, 432)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 50, 395, 339))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 5, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 6, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 6, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 7, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 7, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 8, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 8, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 9, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 9, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(393, 16777215))

        self.verticalLayout_2.addWidget(self.widget)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choose your device:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Setpoint:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Unit:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Equation (x^2 + x + 1):", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Sampling frequency:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Controler type:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kp:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ki:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Kd:", None))
        self.label_10.setText("")
        self.pushButton.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Voltage (V)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Temperatue (C\u00b0)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Other", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"P", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"PI", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"PD", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"PID", None))

        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

