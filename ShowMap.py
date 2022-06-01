from itertools import count
from LoadFile import LoadFile
import geopandas as gpd


class ShowMap:
    def __init__(self, width, height, position_x, position_y, color, label, button_state, field_width, field_height):
        super().__init__(field_width, field_height)

        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.label = label
        self.button_state = button_state

    def load_files_to_map(self):
        pass

    def show_map(self):
        pass


def main():
    LF = LoadFile(None)
    LF.set_filename(
        "Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
    dates, countries = LF.load_file()
    average_price_of_electricity_in_country = {}
    for key in countries:
        average_price_of_electricity_in_country[key] = [
            round(sum(countries[key])/len(dates), 3)]
    print(average_price_of_electricity_in_country)


if __name__ == "__main__":
    main()
