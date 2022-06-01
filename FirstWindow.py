from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from MainWindow import MainWindow
from DisplayChart import DisplayChart
from LoadFile import LoadFile
from tkinter.filedialog import askopenfilename


class FirstWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        self.__mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextPlace = QtWidgets.QLineEdit(self.centralwidget)
        self.TextPlace.setGeometry(QtCore.QRect(100, 265, 500, 35))
        self.TextPlace.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.TextPlace.setObjectName("TextPlace")
        self.ChooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseFileButton.setGeometry(QtCore.QRect(625, 260, 100, 50))
        self.ChooseFileButton.setStyleSheet(
            "background-color: rgb(119, 118, 123)")
        self.ChooseFileButton.setObjectName("ChooseFileButton")
        self.ReadyButton = QtWidgets.QPushButton(self.centralwidget)
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

        # nie dziala w zaden sposob, lecz gdy to zakomentujemy i usuniemy dziedziczenie po QtWidgets.QMainWindow, a odkomentujemy linijkę 18 w mainie to zaczyna działać, jednakże wolelibyśmy, żeby wywołania akcji przycisków zawierały się w klasie, a nie w mainie
        self.__mainwindow.ChooseFileButton.clicked.connect(
            lambda: self.file_reading())
        # -----------------------------------------------

    def close_first_window(self):
        self.__mainwindow.close()

    DC = DisplayChart(None, None)
    LF = LoadFile(None)
    MW = MainWindow()

    def file_reading(self):
        filename = askopenfilename()
        self.LF.set_filename(filename)
        dates, countries = self.LF.load_file()
        self.DC.set_dates(dates)
        self.DC.set_countries(countries)
        print(self.DC.get_countries())
