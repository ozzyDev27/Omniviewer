import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from new_gui import Ui_MainWindow


class Omniviewer(QtWidgets.QMainWindow):
    def __init__(self):
        super(Omniviewer, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.pick_file)

    def test_activation(self):
        print("ohio")
        
    def pick_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Pick File", "~/", "Anything (*.*)"
        )[0]

        self.setWindowTitle(f"Omniviewer | {os.path.basename(fileName)}")
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("kvantum-dark")
    omniviewer = Omniviewer()
    omniviewer.show()
    sys.exit(app.exec_())