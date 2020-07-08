from PyQt5.Qt import *
#from PyQt5.QtWidgets import QWidget, QApplication
#from PyQt5 import Qt
from PyQt5.QtCore import QTimer
from QssTool import QssTool
from resource.MainForm_ui import Ui_Form
from AutoRunForm import AutoRunForm
from AxisDebugForm import AxisDebugForm
from IODebugForm import IODebugForm

class MainForm(QWidget, Ui_Form):

    openserver_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        #self.setWindowOpacity(0.9)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupUi(self)
        QssTool.setQssToObj("resource\QSS\Style.qss", self)

        self.autoRunForm = None
        self.axisDebugForm = None
        self.ioDebugForm = None

        # self.label_logo.setText("Amphenol Airwave")
        self.label_FixtureName.setText("HMI")
        self.label_Date.setText("20200706")
        #self.btn_OpenServer.clicked.connect(self.on_clicked_btnOpenServer)
        self.btn_AutoRun.clicked.connect(self.on_clicked_btnAutoRun)
        self.btn_AxisDebug.clicked.connect(self.on_clicked_btnAxisDebug)
        self.btn_IODebug.clicked.connect(self.on_clicked_btnIODebug)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_refresh_date)
        self.timer.start(10)

    def on_clicked_btnOpenServer(self):
        print("open Server")
        self.openserver_signal.emit()

    def timeout_refresh_date(self):
        time = QDateTime.currentDateTime()

        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label_Date.setText(timeDisplay)

    def on_clicked_btnAutoRun(self):
        self.mdiArea.closeActiveSubWindow()
        self.clear_mdi_subwindow()

        autoRunForm = AutoRunForm()
        self.mdiArea.addSubWindow(autoRunForm, Qt.CustomizeWindowHint)

        autoRunForm.showMaximized()
        print(self.mdiArea.subWindowList())

    def on_clicked_btnAxisDebug(self):
        self.mdiArea.closeActiveSubWindow()
        self.clear_mdi_subwindow()


        axisDebugForm = AxisDebugForm()
        self.mdiArea.addSubWindow(axisDebugForm, Qt.CustomizeWindowHint)

        axisDebugForm.showMaximized()
        print(self.mdiArea.subWindowList())

    def on_clicked_btnIODebug(self):
        self.mdiArea.closeActiveSubWindow()
        self.clear_mdi_subwindow()

        ioDebugForm = IODebugForm()
        self.mdiArea.addSubWindow(ioDebugForm, Qt.CustomizeWindowHint)

        ioDebugForm.showMaximized()
        print(self.mdiArea.subWindowList())


    def clear_mdi_subwindow(self):
        for subwindow in self.mdiArea.subWindowList():
            self.mdiArea.removeSubWindow(subwindow)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = MainForm()
    window.show()

    sys.exit(app.exec_())