from matplotlib import pyplot as plt
from copy import deepcopy
import random
from ListOfCountries import ListOfCountries
from LoadFile import LoadFile
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class DisplayChart:
    def __init__(self, dates, countries, country_colors):
        self.dates = dates
        self.countries = countries
        self.country_colors = country_colors

    def get_countries(self):
        return self.countries

    def get_dates(self):
        return self.dates

    def set_countries(self, cnt):
        self.countries = cnt

    def set_dates(self, dts):
        self.dates = dts

    def get_country_colors(self):
        return self.country_colors

    def set_country_colors(self, cc, element):
        self.country_colors[element] = cc

    def generate_colors(self):
        self.country_colors = deepcopy(self.countries)

        for el in self.country_colors:
            r = random.randint(0, 100) / 100
            g = random.randint(0, 100) / 100
            b = random.randint(0, 100) / 100
            some_color = [r, g, b]
            self.set_country_colors(some_color, el)

    def prepare_and_show_plot(self):
        plt.rcParams["figure.figsize"] = (12, 10)
        plt.rcParams["font.size"] = 12

        for country in self.countries.keys():
            list_of_country_values = self.countries[country]
            plt.plot(self.dates, list_of_country_values, label=country)
            plt.xticks(rotation=60)
        plt.show()
        plt.legend()


if __name__ == "__main__":
    LF = LoadFile(
        "Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
    dates, countries = LF.load_file()
    DC = DisplayChart(dates, countries, None)
    DC.prepare_and_show_plot()
