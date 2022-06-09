from matplotlib import pyplot as plt
from copy import deepcopy
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DisplayChart:
    def __init__(self, dates=None, countries=None, country_colors=None):
        self.__dates = dates
        self.__countries = countries
        self.__country_colors = country_colors

    def get_countries(self):
        return self.__countries

    def get_dates(self):
        return self.__dates

    def set_countries(self, cnt):
        self.__countries = cnt

    def set_dates(self, dts):
        self.__dates = dts

    def get_country_colors(self):
        return self.__country_colors

    def set_country_colors(self, cc, element):
        self.__country_colors[element] = cc

    def generate_colors(self):
        self.__country_colors = deepcopy(self.countries)

        for el in self.__country_colors:
            r = random.randint(0, 100) / 100
            g = random.randint(0, 100) / 100
            b = random.randint(0, 100) / 100
            some_color = [r, g, b]
            self.set_country_colors(some_color, el)

    def prepare_and_show_plot(self):
        fig = plt.figure()
        plt.title("Ceny prądu w europejskich krajach na przestrzeni czasu")

        for country in self.__countries.keys():
            list_of_country_values = self.__countries[country]
            plt.plot(self.__dates, list_of_country_values, label=country)
            plt.xticks(rotation=50)
        # plt.legend()
        plt.savefig("chart.png")
        return fig
