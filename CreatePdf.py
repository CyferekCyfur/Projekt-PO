from BottomButtonsPanel import BottomButtonsPanel


class CreatePDF(BottomButtonsPanel):
    def __init__(self, width, height, position_x, position_y, color, label, if_file_loaded, field_width, field_height):
        super().__init__(field_width, field_height)

        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.label = label
        self.if_file_loaded = if_file_loaded

    def read_data(self):
        pass

    def sort_data(self):
        pass

    def write_to_file(self):
        pass

    def error_message(self):
        pass