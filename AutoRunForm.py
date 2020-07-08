from PyQt5.Qt import *
from resource.AutoRunForm_ui import Ui_Form

class AutoRunForm(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        #self.setWindowFlags(Qt.CustomizeWindowHint)
        #Qt.Qt.CustomizeWindowHint
        self.setupUi(self)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = AutoRunForm()
    window.show()

    sys.exit(app.exec_())