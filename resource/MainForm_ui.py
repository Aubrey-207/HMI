# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2044, 1150)
        font = QtGui.QFont()
        font.setFamily("宋体")
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/SAA.png"))
        self.label_logo.setObjectName("label_logo")
        self.gridLayout.addWidget(self.label_logo, 0, 0, 1, 1)
        self.label_FixtureName = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_FixtureName.setFont(font)
        self.label_FixtureName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FixtureName.setObjectName("label_FixtureName")
        self.gridLayout.addWidget(self.label_FixtureName, 0, 3, 1, 1)
        self.label_Date = QtWidgets.QLabel(Form)
        self.label_Date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Date.setObjectName("label_Date")
        self.gridLayout.addWidget(self.label_Date, 0, 6, 1, 1)
        self.mdiArea = QtWidgets.QMdiArea(Form)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 1, 0, 1, 7)
        self.btn_AutoRun = QtWidgets.QPushButton(Form)
        self.btn_AutoRun.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_AutoRun.setObjectName("btn_AutoRun")
        self.gridLayout.addWidget(self.btn_AutoRun, 2, 0, 1, 1)
        self.btn_AxisDebug = QtWidgets.QPushButton(Form)
        self.btn_AxisDebug.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_AxisDebug.setObjectName("btn_AxisDebug")
        self.gridLayout.addWidget(self.btn_AxisDebug, 2, 1, 1, 1)
        self.btn_FunctionTest = QtWidgets.QPushButton(Form)
        self.btn_FunctionTest.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_FunctionTest.setObjectName("btn_FunctionTest")
        self.gridLayout.addWidget(self.btn_FunctionTest, 2, 2, 1, 1)
        self.btn_IODebug = QtWidgets.QPushButton(Form)
        self.btn_IODebug.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_IODebug.setObjectName("btn_IODebug")
        self.gridLayout.addWidget(self.btn_IODebug, 2, 3, 1, 1)
        self.btn_Parameter = QtWidgets.QPushButton(Form)
        self.btn_Parameter.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_Parameter.setObjectName("btn_Parameter")
        self.gridLayout.addWidget(self.btn_Parameter, 2, 4, 1, 1)
        self.btn_Alarm = QtWidgets.QPushButton(Form)
        self.btn_Alarm.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_Alarm.setObjectName("btn_Alarm")
        self.gridLayout.addWidget(self.btn_Alarm, 2, 5, 1, 1)
        self.btn_UserChange = QtWidgets.QPushButton(Form)
        self.btn_UserChange.setMinimumSize(QtCore.QSize(150, 80))
        self.btn_UserChange.setObjectName("btn_UserChange")
        self.gridLayout.addWidget(self.btn_UserChange, 2, 6, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_FixtureName.setText(_translate("Form", "TextLabel"))
        self.label_Date.setText(_translate("Form", "TextLabel"))
        self.btn_AutoRun.setText(_translate("Form", "自动运行"))
        self.btn_AxisDebug.setText(_translate("Form", "轴调试"))
        self.btn_FunctionTest.setText(_translate("Form", "功能测试"))
        self.btn_IODebug.setText(_translate("Form", "IO调试"))
        self.btn_Parameter.setText(_translate("Form", "参数设置"))
        self.btn_Alarm.setText(_translate("Form", "报警记录"))
        self.btn_UserChange.setText(_translate("Form", "用户切换"))

import image_rc
