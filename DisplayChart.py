from matplotlib import pyplot as plt

class DisplayChart:
    def __init__(self, dates, countries):
        self.dates = dates
        self.countries = countries

    def get_countries(self):
        return self.countries

    def get_dates(self):
        return self.dates
    
    def set_countries(self, cnt):
        self.countries = cnt
    
    def set_dates(self, dts):
        self.dates = dts

    def add_new_plot(self):
        for country in self.countries.keys():
            list_of_country_values = self.countries[country]
            plt.plot(self.dates, list_of_country_values)
            plt.xticks(rotation=60)
            plt.show()

        

    def set_bottom_boundary(self):
        pass

    def set_top_boundary(self):
        pass