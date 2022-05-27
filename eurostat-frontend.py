from DisplayChart import DisplayChart
from FirstWindow import FirstWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from LoadFile import LoadFile
import sys

def main():
    DC = DisplayChart()
    FW = FirstWindow("")


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    FW.setupUi(MainWindow)
    MainWindow.show()

    filename = FW.ChooseFileButton.clicked.connect(lambda: FW.file_reading())
    print(filename)

    # LF = LoadFile(filename)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()