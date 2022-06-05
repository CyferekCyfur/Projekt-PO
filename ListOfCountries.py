from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from LoadFile import LoadFile
import sys


class ListOfCountries(QMainWindow):
    def __init__(self, countries, dates):
        super(ListOfCountries, self).__init__()
        self.__countries = countries
        self.dates = dates

    def get_countries(self):
        return self.__countries

    def get_dates(self):
        return self.dates

    def set_countries(self, cnt):
        self.__countries = cnt

    def set_dates(self, dts):
        self.dates = dts

    def show_countries_list(self):
        listWidget = QListWidget()
        listWidget.resize(300, 120)

        for country in self.__countries.keys():
            listWidget.addItem(country)

        listWidget.itemClicked.connect(self.Clicked)

        self.setCentralWidget(listWidget)

        self.show()

    def Clicked(self, item):
        QMessageBox.information(
            self, "ListWidget", "You clicked: "+item.text())


def main():
    app = QApplication(sys.argv)
    w = ListOfCountries(countries, dates)

    w.show_countries_list()
    sys.exit(app.exec_())


if __name__ == '__main__':
    LF = LoadFile(
        "Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
    dates, countries = LF.load_file()
    main()
