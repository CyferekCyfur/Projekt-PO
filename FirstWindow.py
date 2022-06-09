from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MainWindow
from tkinter.filedialog import askopenfilename
from easygui import msgbox
import threading


class FirstWindow:
    def __init__(self, filename=None):
        self.__filename = filename

    def get_filename(self):
        return self.__filename

    def set_filename(self, fn):
        self.__filename = fn

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

    def file_reading(self):
        filename = askopenfilename()
        if filename[-4:] != ".csv":
            msgbox("Proszę załadować poprawny plik z rozszerzeniem .csv", "Błąd")
            return
        self.set_filename(filename)

    def open_main_window(self):
        if self.get_filename() == None:
            msgbox("Proszę najpierw wybrać plik z rozszerzeniem .csv", "Błąd")
            return
        self.mainwindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = MainWindow(self.get_filename())
        self.ui.setupUi(self.window)
        self.window.show()
