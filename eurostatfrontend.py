from DisplayChart import DisplayChart
from FirstWindow import FirstWindow
from MainWindow import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from LoadFile import LoadFile
from tkinter.filedialog import askopenfilename
import sys


def file_reading():
    filename = askopenfilename()
    LF.set_filename(filename)
    dates, countries = LF.load_file()
    DC.set_dates(dates)
    DC.set_countries(countries)
    print(DC.get_countries())


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    FW.setupUi(mainwindow)
    MW.setupUi(mainwindow)

    mainwindow.show()

    FW.ChooseFileButton.clicked.connect(lambda: file_reading())
    FW.ReadyButton.clicked.connect(lambda: FW.close_first_window())

    sys.exit(app.exec_())


if __name__ == "__main__":
    DC = DisplayChart(None, None)
    FW = FirstWindow()
    LF = LoadFile(None)
    MW = MainWindow()

    main()
