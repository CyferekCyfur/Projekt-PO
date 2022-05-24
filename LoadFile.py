from BottomButtonsPanel import BottomButtonsPanel


class LoadFile(BottomButtonsPanel):
    def __init__(self, width, height, position_x, position_y, color, label, filename, field_width, field_height):
        super().__init__(field_width, field_height)
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.label = label
        self.filename = filename

    def load_file(self, filename):
        countries = []
        with open(filename, 'r', newline="", ) as fhand:
            lines = fhand.readlines()
            lines_to_be_processed = lines[4:]
            for line in lines_to_be_processed:
                words = line.strip().split(sep=",")
                # wyciągane zostają kraje z poszczególnych linijek i zostają ustawiane jako klucze słownika
                countries[words[0]] = 0
                data_in_line_processed = line.strip().split("\"")
                data_per_country = []
                # program przechodzi przez każdą linijkę i tworzy listę z cenami energii
                for el in data_in_line_processed:
                    if el == "":
                        pass
                    elif ":" in el:
                        new_el = el.split(",")
                        for blank_data in new_el:
                            if blank_data == ":":
                                data_per_country.append(0)

                    elif el.startswith("0"):
                        formatted_el = el.replace(",", ".")
                        data_per_country.append(formatted_el)
                countries[words[0]] = data_per_country

            # wyciaganie poszczegolnych dat
            line_0 = lines[0]
            formatted_line_0 = line_0.strip().split(",")
            for el in formatted_line_0:
                if el == "TIME":
                    pass
                else:
                    dates.append(el)




