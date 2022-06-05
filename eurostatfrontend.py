from DisplayChart import DisplayChart
from FirstWindow import FirstWindow
from MainWindow import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from LoadFile import LoadFile
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    FW.setupUi(mainwindow)

    mainwindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    FW = FirstWindow()

    main()
