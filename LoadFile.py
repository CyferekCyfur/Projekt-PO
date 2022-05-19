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

    def load_file(self, filename = "Electricity prices for household consumers - bi-annual data (from 2007 onwards) [NRG_PC_204].csv" ):
        countries = []
        with open(filename) as fhand:
            lines = fhand.readlines()
            for line in lines:



