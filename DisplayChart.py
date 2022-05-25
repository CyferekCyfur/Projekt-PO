from LoadFile import LoadFile
from matplotlib import pyplot as plt

class DisplayChart(LoadFile):
    def __init__(self, width, height, dpi, position_x, position_y, color, label, filename, field_width, field_height):
        super().__init__(filename)
        self.width = width
        self.height = height
        self.dpi = dpi

    def add_new_plot(self):
        file = LoadFile("Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
        dates, countries = file.load_file()
        for country in countries.keys():
            list_of_country_values = countries[country]
            plt.plot(dates, list_of_country_values)
            plt.xticks(rotation=60)
            plt.show()
            return 0

        

    def set_bottom_boundary(self):
        pass

    def set_top_boundary(self):
        pass

dc = DisplayChart(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dc.add_new_plot()