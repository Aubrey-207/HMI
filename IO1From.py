from PyQt5.Qt import *
from resource.IO1Form_ui import Ui_Form

class IO1Form(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = IO1Form()
    #window.read_points()
    #window.get_axis_name()
    window.show()

    sys.exit(app.exec_())