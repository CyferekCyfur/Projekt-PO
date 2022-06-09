from PyQt5 import QtCore, QtGui, QtWidgets
from CreatePDF import CreatePDF
from DisplayChart import DisplayChart
from DisplayMap import DisplayMap
from PyQt5.QtWidgets import QFrame, QGridLayout
from LoadFile import LoadFile
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MainWindow:
    def __init__(self, filename):
        self.__filename = filename

    def get_filename(self):
        return self.__filename

    def set_filename(self, fn):
        self.__filename = fn

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MapButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.show_map())
        self.MapButton.setGeometry(QtCore.QRect(60, 630, 100, 50))
        self.MapButton.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.MapButton.setObjectName("MapButton")
        self.ChartButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.show_chart())
        self.ChartButton.setGeometry(QtCore.QRect(180, 630, 100, 50))
        self.ChartButton.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.ChartButton.setObjectName("ChartButton")
        self.GeneratePDFButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.generate_pdf())
        self.GeneratePDFButton.setGeometry(QtCore.QRect(300, 630, 100, 50))
        self.GeneratePDFButton.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.GeneratePDFButton.setObjectName("GeneratePDFButton")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(420, 630, 200, 20))
        self.horizontalSlider.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(420, 660, 200, 20))
        self.horizontalSlider_2.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("MainWindow")
        self.MapButton.setText("Mapa")
        self.ChartButton.setText("Wykresy")
        self.GeneratePDFButton.setText("Utwórz PDF")

        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 20, 900, 600))
        self.frame_layout = QGridLayout()
        self.frame.setLayout(self.frame_layout)

        self.listframe = QFrame(self.centralwidget)
        self.listframe.setGeometry(QtCore.QRect(1000, 650, 300, 600))
        self.listLayout = QGridLayout()

    def show_chart(self):
        self.LF = LoadFile(self.get_filename())
        dates, countries = self.LF.load_file()
        DC = DisplayChart(dates, countries)
        self.Figure = DC.prepare_and_show_plot()
        self.canvas = FigureCanvasQTAgg(self.Figure)

        self.frame_layout.addWidget(self.canvas)
        self.frame.setLayout(self.frame_layout)

    def show_map(self):
        self.LF = LoadFile(self.get_filename())
        dates, countries = self.LF.load_file()
        DM = DisplayMap(dates, countries)
        self.subplot = DM.setup_and_show_map(
            DM.get_europe(), DM.get_min_val(), DM.get_max_val())
        self.canvas = FigureCanvasQTAgg(self.subplot)

        self.frame_layout.addWidget(self.canvas)
        self.frame.setLayout(self.frame_layout)

    def generate_pdf(self):
        pdf = CreatePDF()
        pdf.AddToPDF("chart.png", "map.png")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MW = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(MW)
    MW.show()
    sys.exit(app.exec_())
