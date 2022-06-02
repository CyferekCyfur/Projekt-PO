from LoadFile import LoadFile
import geopandas
import matplotlib.pyplot as plt
import matplotlib
from shapely.geometry import Polygon


class DisplayMap:
    def __init__(self, dates, countries, europe, min_val, max_val):
        self.dates = dates
        self.countries = countries
        self.europe = europe
        self.min_val = min_val
        self.max_val = max_val

    def get_europe(self):
        return self.europe

    def get_min_val(self):
        return self.min_val

    def get_max_val(self):
        return self.max_val

    def set_countries(self, cnt):
        self.countries = cnt

    def set_dates(self, dts):
        self.dates = dts

    def setup_and_show_map(self, europe, min_val, max_val):
        plt.rcParams["figure.figsize"] = (12, 10)
        plt.rcParams["font.size"] = 12

        fig = europe.plot(color="whitesmoke", edgecolor="black",
                          cmap="Blues_r", vmax=max_val, vmin=min_val)
        fig.xaxis.set_visible(False)
        fig.yaxis.set_visible(False)
        fig.set_title("Ceny prądu w europejskich krajach",
                      fontweight="bold", fontsize=15)

        plt.savefig("map.png")
        plt.show()

    def prepare_data(self):

        average_price_of_electricity_in_country = {}
        for key in self.countries:
            average_price_of_electricity_in_country[key] = [
                round(sum(self.countries[key])/len(self.dates), 3)]

        world = geopandas.read_file(
            geopandas.datasets.get_path("naturalearth_lowres"))

        self.europe = world[world.continent == "Europe"]
        self.europe = self.europe[(self.europe.name != "Russia")]
        polygon = Polygon([(-25, 35), (40, 35), (40, 75), (-25, 75)])

        self.europe = geopandas.clip(self.europe, polygon)

        europe_countries = list(self.europe.name.unique())

        for ec in list(average_price_of_electricity_in_country.keys()):
            if "(" in ec:
                pass
            elif ec not in europe_countries:
                average_price_of_electricity_in_country.pop(ec)

        key_of_minval = min(average_price_of_electricity_in_country.keys(), key=(
            lambda k: average_price_of_electricity_in_country[k]))
        key_of_maxval = max(average_price_of_electricity_in_country.keys(), key=(
            lambda k: average_price_of_electricity_in_country[k]))

        self.min_val = float(
            average_price_of_electricity_in_country[key_of_minval][0])
        self.max_val = float(
            average_price_of_electricity_in_country[key_of_maxval][0])


if __name__ == "__main__":
    LF = LoadFile(
        "Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
    dates, countries = LF.load_file()
    SM = DisplayMap(dates, countries, None, None, None)
    SM.prepare_data()
    SM.setup_and_show_map(SM.get_europe(), SM.get_min_val(), SM.get_max_val())
