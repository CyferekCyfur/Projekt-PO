from PyQt5 import QtCore, QtGui, QtWidgets
from CreatePDF import CreatePDF
from DisplayChart import DisplayChart


class MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MapButton = QtWidgets.QPushButton(self.centralwidget)
        self.MapButton.setGeometry(QtCore.QRect(60, 480, 100, 50))
        self.MapButton.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.MapButton.setObjectName("MapButton")
        self.ChartButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChartButton.setGeometry(QtCore.QRect(180, 480, 100, 50))
        self.ChartButton.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.ChartButton.setObjectName("ChartButton")
        self.GeneratePDFButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.generate_pdf())
        self.GeneratePDFButton.setGeometry(QtCore.QRect(300, 480, 100, 50))
        self.GeneratePDFButton.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.GeneratePDFButton.setObjectName("GeneratePDFButton")
        # self.widget = DisplayChart(self.centralwidget)
        # self.widget.setGeometry(QtCore.QRect(10, 10, 550, 450))
        # self.widget.setObjectName("widget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(420, 480, 200, 20))
        self.horizontalSlider.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(420, 510, 200, 20))
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
