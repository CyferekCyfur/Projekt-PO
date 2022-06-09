from FirstWindow import FirstWindow
from PyQt5 import QtCore, QtGui, QtWidgets
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
