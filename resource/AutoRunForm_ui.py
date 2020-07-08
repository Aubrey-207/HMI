# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoRunForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2006, 962)
        font = QtGui.QFont()
        font.setFamily("宋体")
        Form.setFont(font)
        Form.setStyleSheet("QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center;\n"
"     border:1px solid #8D8D91;\n"
"     border-radius:3px;\n"
"     min-width:150px;\n"
"     min-height:30px;\n"
"     margin-bottom:10px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.2 #F5F5F5, stop: 0.8 #FEFEFE);\n"
"}\n"
"QGroupBox {\n"
"     border:1px solid #8D8D91;\n"
"     border-radius:8px;\n"
"}\n"
"QLabel {\n"
"     border: 0px solid #8D8D91;\n"
"     padding: 1px;\n"
"     background:transparent;\n"
"}\n"
"QLineEdit {\n"
"     background:#FFFFFF;\n"
"     selection-background-color: #4197FF;\n"
"     border: 1px solid #8D8D91;\n"
"     padding: 2px;\n"
"     min-height: 35px;\n"
"     border-radius:5px;\n"
"}\n"
" /*\n"
"     border也可以加入渐变\n"
"     border-top-color:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(206, 210, 255, 255));\n"
"     border-left-color:qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(206, 210, 255, 255));\n"
"     border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(206, 210, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(206, 210, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     \n"
" */\n"
"QLineEdit:hover{\n"
"     border:2px solid #B4B4D0F5;\n"
"     border-radius:5px;\n"
"     }\n"
" \n"
"QLineEdit:focus{\n"
"     border:2px solid #7EA3D9;\n"
"}\n"
" \n"
"QLineEdit:read-only {\n"
"     border: 1px solid #DCDCDC;\n"
"     color: lightgray;\n"
"}\n"
"QLineEdit:disabled {\n"
"     border: 1px solid #DCDCDC;\n"
"     color: lightgray;\n"
"}\n"
"QPushButton {\n"
"     border: 1px solid #8D8D91;\n"
"     border-radius: 10px;\n"
"     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, \n"
"         stop: 0 #FEFEFE, stop: 0.05 #FBFBFB,stop: 0.4 #FBFBFB, \n"
"         stop: 0.9 #F5F5F5, stop: 1 #F5F5F5);\n"
"     padding: 2px;\n"
"     min-height: 80px;\n"
"     min-width:180px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Start = QtWidgets.QPushButton(Form)
        self.btn_Start.setMinimumSize(QtCore.QSize(186, 86))
        self.btn_Start.setObjectName("btn_Start")
        self.gridLayout.addWidget(self.btn_Start, 1, 2, 1, 1)
        self.btn_Clear = QtWidgets.QPushButton(Form)
        self.btn_Clear.setMinimumSize(QtCore.QSize(186, 86))
        self.btn_Clear.setObjectName("btn_Clear")
        self.gridLayout.addWidget(self.btn_Clear, 4, 2, 1, 1)
        self.btn_Origion = QtWidgets.QPushButton(Form)
        self.btn_Origion.setMinimumSize(QtCore.QSize(186, 86))
        self.btn_Origion.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_Origion.setObjectName("btn_Origion")
        self.gridLayout.addWidget(self.btn_Origion, 0, 2, 1, 1)
        self.btn_Stop = QtWidgets.QPushButton(Form)
        self.btn_Stop.setMinimumSize(QtCore.QSize(186, 86))
        self.btn_Stop.setObjectName("btn_Stop")
        self.gridLayout.addWidget(self.btn_Stop, 3, 2, 1, 1)
        self.btn_Pause = QtWidgets.QPushButton(Form)
        self.btn_Pause.setMinimumSize(QtCore.QSize(186, 86))
        self.btn_Pause.setObjectName("btn_Pause")
        self.gridLayout.addWidget(self.btn_Pause, 2, 2, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setMinimumSize(QtCore.QSize(711, 411))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout.addWidget(self.groupBox_4, 8, 1, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(711, 411))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 8, 0, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setMinimumSize(QtCore.QSize(711, 411))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(10, 30, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_Alarm = QtWidgets.QTextEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_Alarm.sizePolicy().hasHeightForWidth())
        self.textEdit_Alarm.setSizePolicy(sizePolicy)
        self.textEdit_Alarm.setObjectName("textEdit_Alarm")
        self.gridLayout_2.addWidget(self.textEdit_Alarm, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 6, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(711, 411))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_TotalCount = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_TotalCount.setEnabled(True)
        self.lineEdit_TotalCount.setObjectName("lineEdit_TotalCount")
        self.horizontalLayout.addWidget(self.lineEdit_TotalCount)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_OKCount = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_OKCount.setObjectName("lineEdit_OKCount")
        self.horizontalLayout_3.addWidget(self.lineEdit_OKCount)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_NGCount = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_NGCount.setObjectName("lineEdit_NGCount")
        self.horizontalLayout_2.addWidget(self.lineEdit_NGCount)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 167, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 6, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_Start.setText(_translate("Form", "启动"))
        self.btn_Clear.setText(_translate("Form", "清料"))
        self.btn_Origion.setText(_translate("Form", "回原点"))
        self.btn_Stop.setText(_translate("Form", "停止"))
        self.btn_Pause.setText(_translate("Form", "暂停"))
        self.groupBox_4.setTitle(_translate("Form", "实时信息"))
        self.groupBox_2.setTitle(_translate("Form", "状态显示"))
        self.groupBox_3.setTitle(_translate("Form", "报警信息"))
        self.groupBox.setTitle(_translate("Form", "生产数据统计"))
        self.label.setText(_translate("Form", "生产总数:"))
        self.label_3.setText(_translate("Form", "OK数:    "))
        self.label_2.setText(_translate("Form", "NG数:    "))
        self.label_4.setText(_translate("Form", "比率:    "))

import image_rc
