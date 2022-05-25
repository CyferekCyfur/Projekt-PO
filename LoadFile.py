class LoadFile:
    def __init__(self, filename):
        self.filename = filename

    def getFilename(self):
        return self.filename

    def load_file(self):
        countries = {}
        dates = []

        # wyciaganie krajow z pliku oraz ich danych kt
        with open(self.getFilename(), 'r') as fp:
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
            return dates, countries


lf = LoadFile("Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv")
