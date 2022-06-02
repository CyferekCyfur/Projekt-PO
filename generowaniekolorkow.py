from itertools import count
from matplotlib import pyplot as plt
import random
from copy import deepcopy
from ListOfCountries import ListOfCountries

countries = {}
dates = []

with open("Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv", 'r') as fp:
    lines = fp.readlines()
    lines_to_be_processed = lines[4:]

    for line in lines_to_be_processed:
        country = ''
        comma = False
        counter = False
        number = ''
        list_of_strings = []
        for character in line:
            if character == '\n':
                break
            if character != ',' and not comma:
                country += character
                continue
            else:
                comma = True
            if character == ':':
                list_of_strings.append('0.0')
                continue
            if character == '"' and not counter:
                counter = True
                continue
            if character == '"' and counter:
                counter = False
                list_of_strings.append(number)
                number = ''
                continue
            if character == ',' and counter:
                number += '.'
                continue
            if counter:
                number += character
        list_of_values = []
        for number in list_of_strings:
            list_of_values.append(float(number))
        countries[country] = list_of_values
    # wyciaganie poszczegolnych dat
    line_0 = lines[0]
    formatted_line_0 = line_0.strip().split(",")
    for element in formatted_line_0:
        if element == "TIME":
            pass
        else:
            dates.append(element)

# plotting cus
bottom_boundary_default = 0
top_boundary_default = len(dates)
country_colors = deepcopy(countries)

# generate colors
for el in country_colors:
    r = random.randint(0, 100) / 100
    g = random.randint(0, 100) / 100
    b = random.randint(0, 100) / 100
    some_color = [r, g, b]
    country_colors[el] = some_color


for country in countries.keys():
    new_color = tuple(country_colors[country])

    formatted_dates = dates[bottom_boundary_default: top_boundary_default]

    plot = plt.plot(formatted_dates,
                    countries[country], color=new_color, label=country)
    plt.xlabel("Dates")
    plt.ylabel("Energy price")
    plt.xticks(rotation=60)
    plt.legend()

plt.show()
