from PyQt5.Qt import *
from resource.IODebugForm_ui import Ui_Form
from IO1From import IO1Form

class IODebugForm(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.btn_IO1.clicked.connect(self.on_clicked_btnIO1)

    def on_clicked_btnIO1(self):
        self.mdiArea.closeActiveSubWindow()
        self.clear_mdi_subwindow()

        io1Form = IO1Form()
        self.mdiArea.addSubWindow(io1Form, Qt.CustomizeWindowHint)

        io1Form.showMaximized()
        print(self.mdiArea.subWindowList())

    def clear_mdi_subwindow(self):
        for subwindow in self.mdiArea.subWindowList():
            self.mdiArea.removeSubWindow(subwindow)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = IODebugForm()
    #window.read_points()
    #window.get_axis_name()
    window.show()

    sys.exit(app.exec_())