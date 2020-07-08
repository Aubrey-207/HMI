# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TcpServer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 662)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 10, 51, 24))
        self.label.setObjectName("label")
        self.lineEdit_IP = QtWidgets.QLineEdit(Form)
        self.lineEdit_IP.setGeometry(QtCore.QRect(550, 40, 311, 51))
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 110, 71, 31))
        self.label_2.setObjectName("label_2")
        self.btn_Listen = QtWidgets.QPushButton(Form)
        self.btn_Listen.setGeometry(QtCore.QRect(660, 170, 201, 51))
        self.btn_Listen.setObjectName("btn_Listen")
        self.btn_Send = QtWidgets.QPushButton(Form)
        self.btn_Send.setGeometry(QtCore.QRect(580, 570, 150, 46))
        self.btn_Send.setObjectName("btn_Send")
        self.textEdit_Recv = QtWidgets.QTextEdit(Form)
        self.textEdit_Recv.setGeometry(QtCore.QRect(10, 20, 531, 351))
        self.textEdit_Recv.setObjectName("textEdit_Recv")
        self.textEdit_Send = QtWidgets.QTextEdit(Form)
        self.textEdit_Send.setGeometry(QtCore.QRect(10, 390, 531, 251))
        self.textEdit_Send.setObjectName("textEdit_Send")
        self.lineEdit_Port = QtWidgets.QLineEdit(Form)
        self.lineEdit_Port.setGeometry(QtCore.QRect(730, 100, 131, 51))
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.cmb_Client = QtWidgets.QComboBox(Form)
        self.cmb_Client.setGeometry(QtCore.QRect(550, 250, 311, 41))
        self.cmb_Client.setObjectName("cmb_Client")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "IP:"))
        self.label_2.setText(_translate("Form", "Port:"))
        self.btn_Listen.setText(_translate("Form", "Listen"))
        self.btn_Send.setText(_translate("Form", "Send"))

