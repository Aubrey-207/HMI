# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 522)
        self.widget_bottom = QtWidgets.QWidget(Form)
        self.widget_bottom.setGeometry(QtCore.QRect(70, 200, 531, 261))
        self.widget_bottom.setStyleSheet("QComboBox {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;    \n"
"    width: 60px;\n"
"    height: 40px;               \n"
"}\n"
"QComboBox::down-arrow {\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color: lightblue;\n"
"}")
        self.widget_bottom.setObjectName("widget_bottom")
        self.comboBox_Account = QtWidgets.QComboBox(self.widget_bottom)
        self.comboBox_Account.setGeometry(QtCore.QRect(180, 40, 271, 41))
        self.comboBox_Account.setStyleSheet("QComboBox {\n"
"    font-size: 30px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;    \n"
"    width: 60px;\n"
"    height: 40px;               \n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/login/login_combobox_icon.png);\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color: lightblue;\n"
"}")
        self.comboBox_Account.setObjectName("comboBox_Account")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.widget_bottom)
        self.lineEdit_Password.setGeometry(QtCore.QRect(180, 130, 271, 41))
        self.lineEdit_Password.setStyleSheet("QLineEdit {\n"
"    font-size: 30px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"")
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.label = QtWidgets.QLabel(self.widget_bottom)
        self.label.setGeometry(QtCore.QRect(50, 60, 108, 24))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_bottom)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 108, 24))
        self.label_2.setObjectName("label_2")
        self.btn_Login = QtWidgets.QPushButton(self.widget_bottom)
        self.btn_Login.setGeometry(QtCore.QRect(190, 190, 181, 46))
        self.btn_Login.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    spacing: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(167, 167, 167);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/login_btn_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Login.setIcon(icon)
        self.btn_Login.setObjectName("btn_Login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密码："))
        self.btn_Login.setText(_translate("Form", "安全登录"))

import image_rc
