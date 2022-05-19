from CreatePdf import CreatePDF


class PDFMenu(CreatePDF):
    def __init__(self, if_map, if_chart, file_title, width, height, position_x, position_y, color, label, if_file_loaded, field_width, field_height):
        super().__init__(width, height, position_x, position_y, color, label, if_file_loaded, field_width, field_height)

        self.if_map = if_map
        self.if_chart = if_chart
        self.file_title = file_title

    def make_title(self):
        pass

    def add_map_to_file(self):
        pass

    def add_chart_to_file(self):
        pass

    def add_legend(self):
        pass
