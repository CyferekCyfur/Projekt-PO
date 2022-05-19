from SideButtonsPanel import SideButtonsPanel


class Slider(SideButtonsPanel):
    def __init__(self, position, top_value, bottom_value, field_width, field_height, button_height, button_width, width,
                 height, position_x, position_y, color, label, filename):
        super().__init__(field_width, field_height, button_height, button_width, width, height, position_x, position_y,
                         color, label, filename)
        self.position = position
        self.top_value = top_value
        self.bottom_value = bottom_value

    def change_position(self):
        pass

    def move_buttons(self):
        pass