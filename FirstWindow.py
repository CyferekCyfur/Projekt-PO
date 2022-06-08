from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from MainWindow import MainWindow
from DisplayChart import DisplayChart
from LoadFile import LoadFile
from tkinter.filedialog import askopenfilename
from easygui import msgbox
import threading


class FirstWindow:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirstWindow, cls).__new__(cls)
        return cls._instance

    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextPlace = QtWidgets.QLineEdit(self.centralwidget)
        self.TextPlace.setGeometry(QtCore.QRect(100, 265, 500, 35))
        self.TextPlace.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.TextPlace.setObjectName("TextPlace")
        self.ChooseFileButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: threading.Thread(target=self.file_reading()).start)
        self.ChooseFileButton.setGeometry(QtCore.QRect(625, 260, 100, 50))
        self.ChooseFileButton.setStyleSheet(
            "background-color: rgb(119, 118, 123)")
        self.ChooseFileButton.setObjectName("ChooseFileButton")
        self.ReadyButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: threading.Thread(target=self.open_main_window()).start)
        self.ReadyButton.setGeometry(QtCore.QRect(300, 325, 100, 50))
        self.ReadyButton.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.ReadyButton.setObjectName("ReadyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Załaduj plik")
        self.ChooseFileButton.setText("Wybierz plik")
        self.ReadyButton.setText("Gotowe")

    DC = DisplayChart()
    LF = LoadFile()
    MW = MainWindow()

    def file_reading(self):
        filename = askopenfilename()
        if filename[-4:] != ".csv":
            msgbox("Proszę załadować poprawny plik z rozszerzeniem .csv", "Błąd")
            return

        self.LF.set_filename(filename)
        dates, countries = self.LF.load_file()
        self.DC.set_dates(dates)
        self.DC.set_countries(countries)

    def open_main_window(self):
        if self.DC.get_countries() == None and self.DC.get_dates() == None:
            msgbox("Proszę najpierw wybrać plik z rozszerzeniem .csv", "Błąd")
            return
        self.mainwindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
