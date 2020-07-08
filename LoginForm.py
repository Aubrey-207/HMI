import json
from PyQt5.Qt import *
from resource.LoginForm_ui import Ui_Form


class LoginForm(QWidget, Ui_Form):

    check_login_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        #self.setWindowOpacity(0.9)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.btn_Login.clicked.connect(self.check_login)

    def check_login(self):
        account = self.comboBox_Account.currentText()
        password = self.lineEdit_Password.text()
        self.check_login_signal.emit(account, password)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.widget_bottom)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.widget_bottom.pos())
        animation.setKeyValueAt(0.2, self.widget_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.widget_bottom.pos())
        animation.setKeyValueAt(0.7, self.widget_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.widget_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec_())