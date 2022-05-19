from LoadFile import LoadFile


class DisplayChart(LoadFile):
    def __init__(self, width, height, dpi, position_x, position_y, color, label, filename, field_width, field_height):
        super().__init__(width, height, position_x, position_y, color, label, filename, field_width, field_height)
        self.width = width
        self.height = height
        self.dpi = dpi

    def add_new_plot(self):
        pass

    def set_bottom_boundary(self):
        pass

    def set_top_boundary(self):
        pass
