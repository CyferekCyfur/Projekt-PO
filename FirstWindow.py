from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from MainWindow import MainWindow
from eurostatfrontend import FW, DC, LF
from tkinter.filedialog import askopenfilename


class FirstWindow():

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

        MainWindow.setWindowTitle("MainWindow")
        self.ChooseFileButton.setText("Wybierz plik")
        self.ReadyButton.setText("Gotowe")

    def close_first_window(self):
        self.__mainwindow.close()
