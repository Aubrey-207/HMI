from PyQt5.Qt import *
from resource.TcpServer_ui import Ui_Form


class TcpServer_Panel(QWidget, Ui_Form):

    send_signal = pyqtSignal(str, )
    listen_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.btn_Send.clicked.connect(self.on_clicked_btnSend)
        self.btn_Listen.clicked.connect(self.on_clicked_btnListen)
        self.lineEdit_IP.setText("192.168.2.128")
        self.lineEdit_Port.setText("7890")

    def on_clicked_btnSend(self):
        self.send_signal.emit(self.textEdit_Send.toPlainText())

    def on_clicked_btnListen(self):
        self.listen_signal.emit(self.lineEdit_IP.text(), self.lineEdit_Port.text())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = TcpServer_Panel()
    window.show()

    sys.exit(app.exec_())