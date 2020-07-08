import json
from PyQt5.Qt import *
from resource.AxisDebugForm_ui import Ui_Form

class AxisDebugForm(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['轴','点位','值','地址'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 加载点位
        self.read_points()
        self.fill_table()

        # 信号与槽的连接
        # 轴combobox索引选择变化时连接的槽函数
        self.comboBox_Axis.currentIndexChanged.connect(lambda: self.slot_combobox_axis_change())
        self.btn_Stop.clicked.connect(self.on_clicked_btn_Stop)

    '''
    加载点位
    从Points.json文件中读取点位信息，并更新到对应的combobox中
    '''
    def read_points(self):
        with open("Points.json", "r") as f:
            self.points_dict = json.load(f)

        self.axis_name = list()
        for dict in self.points_dict["axis"]:
            self.axis_name.append(dict["axis_name"])
            self.comboBox_Axis.addItem(dict["axis_name"])

        for dict in self.points_dict["axis"][0]["axis_points"]:
            # print(dict)
            self.comboBox_Point.addItem(dict["point_name"])

    def fill_table(self):
        for dict in self.points_dict["axis"]:
            for tmp in dict["axis_points"]:
                row_cnt = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_cnt)

                item = QTableWidgetItem(str(dict["axis_name"]))
                self.tableWidget.setItem(row_cnt, 0, item)

                item1 = QTableWidgetItem(str(tmp["point_name"]))
                self.tableWidget.setItem(row_cnt, 1, item1)

                item2 = QTableWidgetItem(str(tmp["address"]))
                self.tableWidget.setItem(row_cnt, 3, item2)


    def slot_combobox_axis_change(self):
        self.comboBox_Point.clear()
        current_index = self.comboBox_Axis.currentIndex()
        print(current_index)
        #print(self.points_dict["axis"][current_index]["axis_points"])
        #self.points_dict["axis"](current_index)
        for dict in self.points_dict["axis"][current_index]["axis_points"]:
            #print(dict)
            self.comboBox_Point.addItem(dict["point_name"])

    def on_clicked_btn_Stop(self):
        self.label_Alarm.setStyleSheet("background-color:gold")
        print("Stop")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = AxisDebugForm()
    #window.read_points()
    #window.get_axis_name()
    window.show()

    sys.exit(app.exec_())