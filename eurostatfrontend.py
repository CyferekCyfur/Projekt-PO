from DisplayChart import DisplayChart
from FirstWindow import FirstWindow
from MainWindow import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from LoadFile import LoadFile
from tkinter.filedialog import askopenfilename
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    FW.setupUi(mainwindow)

    mainwindow.show()

    FW.ReadyButton.clicked.connect(lambda: FW.close_first_window())
    # FW.ChooseFileButton.clicked.connect(lambda: FW.file_reading())

    sys.exit(app.exec_())


if __name__ == "__main__":
    FW = FirstWindow()

    main()
