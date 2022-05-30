from DisplayChart import DisplayChart
from FirstWindow import FirstWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from LoadFile import LoadFile
from tkinter.filedialog import askopenfilename
import sys


def file_reading():
    filename = askopenfilename()
    LF.set_filename(filename)
    global dates, countries
    dates, countries = LF.load_file()
    DC.set_dates(dates)
    DC.set_countries(countries)
    print(DC.get_countries())


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    FW.setupUi(MainWindow)
    MainWindow.show()

    FW.ChooseFileButton.clicked.connect(lambda: file_reading())

    FW.ReadyButton.clicked.connect(FW.closeOnReady())

    sys.exit(app.exec_())


if __name__ == "__main__":
    DC = DisplayChart(None, None)
    FW = FirstWindow()
    LF = LoadFile(None)

    main()
