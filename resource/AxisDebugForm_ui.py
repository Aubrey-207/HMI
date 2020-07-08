# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AxisDebugForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2006, 962)
        Form.setStyleSheet("QComboBox{\n"
"     background:#FFFFFF;\n"
"     selection-background-color: #4197FF;\n"
"     border: 1px solid #8D8D91;\n"
"     padding: 0 1px;\n"
"     min-height: 40px;\n"
"     border-radius:5px;\n"
"     padding:2px;\n"
"}\n"
"QComboBox:editable{\n"
"     border-style: solid;\n"
"     border-radius:5px;\n"
"     padding:2px;\n"
"}\n"
"QComboBox:hover{\n"
"     border-color: #4197FF;\n"
"     border:2px solid #7EA3D9;\n"
"     border-radius:5px;\n"
"}\n"
" QComboBox:focus{\n"
"     border-color: #7EA3D9;\n"
"     border:1px solid #7EA3D9;\n"
"     border-radius:5px;\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"     padding-top: 2px;\n"
"     padding-left: 2px;\n"
"     border-radius:5px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"     image:url(drop_down.png);\n"
"}\n"
" \n"
"QComboBox::drop-down { /* shift the text when the popup opens */\n"
"     background:#4197FF;\n"
"     width:15px;\n"
"     padding-right:2px;\n"
"     border-top-right-radius: 3px;\n"
"     border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"     background:#FFFFFF;\n"
"     border: 1px solid #8D8D91;\n"
"     border-radius:3px;\n"
"     selection-background-color: #4197FF;\n"
"}\n"
"QComboBox QAbstractItemView::item{\n"
"     height:50px;\n"
"}\n"
"QLineEdit {\n"
"     background:#FFFFFF;\n"
"     selection-background-color: #4197FF;\n"
"     border: 1px solid #8D8D91;\n"
"     padding: 2px;\n"
"     min-height: 40px;\n"
"     border-radius:5px;\n"
"}\n"
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
"     border-radius: 5px;\n"
"     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, \n"
"         stop: 0 #FEFEFE, stop: 0.05 #FBFBFB,stop: 0.4 #FBFBFB, \n"
"         stop: 0.9 #F5F5F5, stop: 1 #F5F5F5);\n"
"     padding: 2px;\n"
"     min-height: 60px;\n"
"     min-width:60px;\n"
"}\n"
"QPushButton:default {\n"
"     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, \n"
"         stop: 0 #68B1FA, stop: 0.05 #3C9AFC,stop: 0.4 #3C9AFC, \n"
"         stop: 0.9 #0A81FF, stop: 1 #0A81FF);\n"
"} \n"
"QPushButton:hover{\n"
"     border: 2px solid #B4B4D0F5;\n"
"     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, \n"
"         stop: 0 #68B1FA, stop: 0.05 #3C9AFC,stop: 0.4 #3C9AFC, \n"
"         stop: 0.9 #0A81FF, stop: 1 #0A81FF);  \n"
"}\n"
"QPushButton:pressed{\n"
"     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, \n"
"         stop: 0 #68B1FA, stop: 0.05 #0A81FF,stop: 0.4 #0A81FF, \n"
"         stop: 0.9 #3C9AFC, stop: 1 #3C9AFC);\n"
"     \n"
"}\n"
"QPushButton:disabled{ \n"
"     border:1px solid #CDCDCD;\n"
"     color:#C7C7C7;\n"
"     background:#EFEFEF;\n"
"}")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_Axis = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_Axis.setObjectName("comboBox_Axis")
        self.gridLayout.addWidget(self.comboBox_Axis, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_Point = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_Point.setObjectName("comboBox_Point")
        self.gridLayout.addWidget(self.comboBox_Point, 1, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_SavedPoint = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_SavedPoint.setObjectName("lineEdit_SavedPoint")
        self.gridLayout.addWidget(self.lineEdit_SavedPoint, 2, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_CurrentPoint = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_CurrentPoint.setObjectName("lineEdit_CurrentPoint")
        self.gridLayout.addWidget(self.lineEdit_CurrentPoint, 3, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.comboBox_Distance = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_Distance.setObjectName("comboBox_Distance")
        self.comboBox_Distance.addItem("")
        self.comboBox_Distance.addItem("")
        self.comboBox_Distance.addItem("")
        self.comboBox_Distance.addItem("")
        self.gridLayout.addWidget(self.comboBox_Distance, 4, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 3, 1, 1)
        self.btn_Backward = QtWidgets.QPushButton(self.widget_2)
        self.btn_Backward.setObjectName("btn_Backward")
        self.gridLayout.addWidget(self.btn_Backward, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.btn_Forward = QtWidgets.QPushButton(self.widget_2)
        self.btn_Forward.setObjectName("btn_Forward")
        self.gridLayout.addWidget(self.btn_Forward, 5, 2, 1, 2)
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 3, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_Origion = QtWidgets.QPushButton(self.widget_3)
        self.btn_Origion.setObjectName("btn_Origion")
        self.gridLayout_2.addWidget(self.btn_Origion, 0, 0, 1, 1)
        self.btn_ServoOn = QtWidgets.QPushButton(self.widget_3)
        self.btn_ServoOn.setObjectName("btn_ServoOn")
        self.gridLayout_2.addWidget(self.btn_ServoOn, 1, 0, 1, 1)
        self.btn_ClearAlarm = QtWidgets.QPushButton(self.widget_3)
        self.btn_ClearAlarm.setObjectName("btn_ClearAlarm")
        self.gridLayout_2.addWidget(self.btn_ClearAlarm, 2, 0, 1, 1)
        self.btn_Stop = QtWidgets.QPushButton(self.widget_3)
        self.btn_Stop.setObjectName("btn_Stop")
        self.gridLayout_2.addWidget(self.btn_Stop, 3, 0, 1, 1)
        self.btn_SavePoint = QtWidgets.QPushButton(self.widget_3)
        self.btn_SavePoint.setObjectName("btn_SavePoint")
        self.gridLayout_2.addWidget(self.btn_SavePoint, 4, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 0, 2, 3, 2)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(900, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 1, 5, 4, 2)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 371, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 371, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 3, 2, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QLabel[notice_level=\'OK\']{\n"
"    background-color: yellow;\n"
"    min-width:     40px;     \n"
"    min-height:    40px;     \n"
"    max-width:     40px;     \n"
"    max-height:    40px;    \n"
"    border-radius: 20px;      \n"
"    border:1px solid black; \n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_ServoOn = QtWidgets.QLabel(self.widget)
        self.label_ServoOn.setStyleSheet("")
        self.label_ServoOn.setText("")
        self.label_ServoOn.setObjectName("label_ServoOn")
        self.gridLayout_3.addWidget(self.label_ServoOn, 1, 0, 1, 1)
        self.label_Alarm = QtWidgets.QLabel(self.widget)
        self.label_Alarm.setStyleSheet("")
        self.label_Alarm.setText("")
        self.label_Alarm.setObjectName("label_Alarm")
        self.gridLayout_3.addWidget(self.label_Alarm, 1, 1, 1, 1)
        self.label_PositiveLimit = QtWidgets.QLabel(self.widget)
        self.label_PositiveLimit.setStyleSheet("")
        self.label_PositiveLimit.setText("")
        self.label_PositiveLimit.setObjectName("label_PositiveLimit")
        self.gridLayout_3.addWidget(self.label_PositiveLimit, 1, 2, 1, 1)
        self.label_NegtiveLimit = QtWidgets.QLabel(self.widget)
        self.label_NegtiveLimit.setStyleSheet("")
        self.label_NegtiveLimit.setText("")
        self.label_NegtiveLimit.setObjectName("label_NegtiveLimit")
        self.gridLayout_3.addWidget(self.label_NegtiveLimit, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 4, 0, 2, 2)
        spacerItem6 = QtWidgets.QSpacerItem(273, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 5, 3, 1, 1)
        self.btn_Refresh = QtWidgets.QPushButton(Form)
        self.btn_Refresh.setObjectName("btn_Refresh")
        self.gridLayout_4.addWidget(self.btn_Refresh, 5, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(741, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 5, 6, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "轴调试"))
        self.label.setText(_translate("Form", "当前轴: "))
        self.label_2.setText(_translate("Form", "点位:"))
        self.label_8.setText(_translate("Form", "当前点位值："))
        self.label_3.setText(_translate("Form", "当前位置："))
        self.label_9.setText(_translate("Form", "移动刻度："))
        self.comboBox_Distance.setItemText(0, _translate("Form", "0.01"))
        self.comboBox_Distance.setItemText(1, _translate("Form", "0.1"))
        self.comboBox_Distance.setItemText(2, _translate("Form", "1"))
        self.comboBox_Distance.setItemText(3, _translate("Form", "10"))
        self.btn_Backward.setText(_translate("Form", "向前"))
        self.btn_Forward.setText(_translate("Form", "向后"))
        self.btn_Origion.setText(_translate("Form", "回原点"))
        self.btn_ServoOn.setText(_translate("Form", "轴使能"))
        self.btn_ClearAlarm.setText(_translate("Form", "清除报警"))
        self.btn_Stop.setText(_translate("Form", "停止"))
        self.btn_SavePoint.setText(_translate("Form", "保存"))
        self.label_10.setText(_translate("Form", "所有点位信息"))
        self.label_4.setText(_translate("Form", "轴使能"))
        self.label_5.setText(_translate("Form", "报警"))
        self.label_6.setText(_translate("Form", "正极限"))
        self.label_7.setText(_translate("Form", "负极限"))
        self.label_ServoOn.setProperty("notice_level", _translate("Form", "OK"))
        self.label_Alarm.setProperty("notice_level", _translate("Form", "OK"))
        self.label_PositiveLimit.setProperty("notice_level", _translate("Form", "OK"))
        self.label_NegtiveLimit.setProperty("notice_level", _translate("Form", "OK"))
        self.btn_Refresh.setText(_translate("Form", "刷新"))

