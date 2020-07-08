# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IODebugForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2006, 962)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mdiArea = QtWidgets.QMdiArea(Form)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_2.addWidget(self.mdiArea, 0, 0, 2, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_IO1 = QtWidgets.QPushButton(self.widget)
        self.btn_IO1.setObjectName("btn_IO1")
        self.gridLayout.addWidget(self.btn_IO1, 0, 0, 1, 1)
        self.btn_IO2 = QtWidgets.QPushButton(self.widget)
        self.btn_IO2.setObjectName("btn_IO2")
        self.gridLayout.addWidget(self.btn_IO2, 1, 0, 1, 1)
        self.btn_IO3 = QtWidgets.QPushButton(self.widget)
        self.btn_IO3.setObjectName("btn_IO3")
        self.gridLayout.addWidget(self.btn_IO3, 2, 0, 1, 1)
        self.btn_IO4 = QtWidgets.QPushButton(self.widget)
        self.btn_IO4.setObjectName("btn_IO4")
        self.gridLayout.addWidget(self.btn_IO4, 3, 0, 1, 1)
        self.btn_IO1_5 = QtWidgets.QPushButton(self.widget)
        self.btn_IO1_5.setObjectName("btn_IO1_5")
        self.gridLayout.addWidget(self.btn_IO1_5, 4, 0, 1, 1)
        self.btn_IO1_6 = QtWidgets.QPushButton(self.widget)
        self.btn_IO1_6.setObjectName("btn_IO1_6")
        self.gridLayout.addWidget(self.btn_IO1_6, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 539, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_IO1.setText(_translate("Form", "IO1"))
        self.btn_IO2.setText(_translate("Form", "IO2"))
        self.btn_IO3.setText(_translate("Form", "IO3"))
        self.btn_IO4.setText(_translate("Form", "IO4"))
        self.btn_IO1_5.setText(_translate("Form", "IO5"))
        self.btn_IO1_6.setText(_translate("Form", "IO6"))

