from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 480, 100, 50))
        self.pushButton.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 480, 100, 50))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 480, 100, 50))
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(119, 118, 123);")
        self.pushButton_3.setObjectName("pushButton_3")
        # self.widget = ShowChart(self.centralwidget)
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
        self.pushButton.setText("Mapa")
        self.pushButton_2.setText("Wykresy")
        self.pushButton_3.setText("Utwórz PDF")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MW = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(MW)
    MW.show()
    sys.exit(app.exec_())
