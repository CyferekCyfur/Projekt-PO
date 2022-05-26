from matplotlib import pyplot as plt

class DisplayChart:

    def add_new_plot(self):
        file = LoadFile("Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
        dates, countries = file.load_file()
        for country in countries.keys():
            list_of_country_values = countries[country]
            plt.plot(dates, list_of_country_values)
            plt.xticks(rotation=60)
            plt.show()

        

    def set_bottom_boundary(self):
        pass

    def set_top_boundary(self):
        pass