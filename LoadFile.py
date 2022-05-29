class LoadFile:
    def __init__(self, filename):
        self.filename = filename

    def get_filename(self):
        return self.filename

    def set_filename(self, fn):
        self.filename = fn

    def load_file(self):
        countries = {}
        dates = []

        with open(self.get_filename(), 'r') as fp:
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

            line_0 = lines[0]
            formatted_line_0 = line_0.strip().split(",")
            for element in formatted_line_0:
                if element == "TIME":
                    pass
                else:
                    dates.append(element)
            return dates, countries
