from LoadFile import LoadFile


class SideButtonsPanel(LoadFile):
    def __init__(self, field_width, field_height, button_height, button_width, width, height, position_x, position_y,
                 color, label, filename):
        super().__init__(width, height, position_x, position_y, color, label, filename, field_width, field_height)

        self.field_width = field_width
        self.field_height = field_height
        self.button_height = button_height
        self.button_width = button_width

    def prepare_buttons_grid(self):
        pass

    def create_button(self):
        pass

    def assign_color(self):
        pass

    def assign_state(self):
        pass

    def position_buttons(self):
        pass
