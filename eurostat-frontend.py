from FileReadingPanel import FileReadingPanel
from DisplayChart import DisplayChart
from FirstWindow import FirstWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from LoadFile import LoadFile
import sys

def main():
    FRP = FileReadingPanel("")
    DC = DisplayChart()
    FW = FirstWindow()


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_first_window = FirstWindow()
    ui_first_window.setupUi(MainWindow)
    MainWindow.show()

    filename = ui_first_window.ChooseFileButton.clicked.connect(lambda: FRP.file_reading())
    print("dupa")
    print(filename)

    # LF = LoadFile(filename)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()