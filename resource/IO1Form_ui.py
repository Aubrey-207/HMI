# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IO1Form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1772, 926)
        Form.setStyleSheet("QLabel[notice_level=\'OK\']{\n"
"    background-color: yellow;\n"
"    min-width:     40px;     \n"
"    min-height:    40px;     \n"
"    max-width:     40px;     \n"
"    max-height:    40px;    \n"
"    border-radius: 20px;      \n"
"    border:1px solid black; \n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.label_ServoOn = QtWidgets.QLabel(self.widget)
        self.label_ServoOn.setStyleSheet("")
        self.label_ServoOn.setText("")
        self.label_ServoOn.setObjectName("label_ServoOn")
        self.gridLayout.addWidget(self.label_ServoOn, 1, 1, 1, 1)
        self.label_ServoOn_2 = QtWidgets.QLabel(self.widget)
        self.label_ServoOn_2.setStyleSheet("")
        self.label_ServoOn_2.setText("")
        self.label_ServoOn_2.setObjectName("label_ServoOn_2")
        self.gridLayout.addWidget(self.label_ServoOn_2, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.label_ServoOn_3 = QtWidgets.QLabel(self.widget)
        self.label_ServoOn_3.setStyleSheet("")
        self.label_ServoOn_3.setText("")
        self.label_ServoOn_3.setObjectName("label_ServoOn_3")
        self.gridLayout.addWidget(self.label_ServoOn_3, 2, 1, 1, 1)
        self.label_ServoOn_15 = QtWidgets.QLabel(self.widget)
        self.label_ServoOn_15.setStyleSheet("")
        self.label_ServoOn_15.setText("")
        self.label_ServoOn_15.setObjectName("label_ServoOn_15")
        self.gridLayout.addWidget(self.label_ServoOn_15, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.label_ServoOn_14 = QtWidgets.QLabel(self.widget)
        self.label_ServoOn_14.setStyleSheet("")
        self.label_ServoOn_14.setText("")
        self.label_ServoOn_14.setObjectName("label_ServoOn_14")
        self.gridLayout.addWidget(self.label_ServoOn_14, 3, 1, 1, 1)
        self.label_ServoOn_13 = QtWidgets.QLabel(self.widget)
        self.label_ServoOn_13.setStyleSheet("")
        self.label_ServoOn_13.setText("")
        self.label_ServoOn_13.setObjectName("label_ServoOn_13")
        self.gridLayout.addWidget(self.label_ServoOn_13, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(1391, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 641, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "原位"))
        self.label_2.setText(_translate("Form", "工作位"))
        self.pushButton.setText(_translate("Form", "CY1"))
        self.label_ServoOn.setProperty("notice_level", _translate("Form", "OK"))
        self.label_ServoOn_2.setProperty("notice_level", _translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "CY2"))
        self.label_ServoOn_3.setProperty("notice_level", _translate("Form", "OK"))
        self.label_ServoOn_15.setProperty("notice_level", _translate("Form", "OK"))
        self.pushButton_3.setText(_translate("Form", "CY3"))
        self.label_ServoOn_14.setProperty("notice_level", _translate("Form", "OK"))
        self.label_ServoOn_13.setProperty("notice_level", _translate("Form", "OK"))

