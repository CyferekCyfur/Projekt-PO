from BottomButtonsPanel import BottomButtonsPanel


class ShowChart(BottomButtonsPanel):
    def __init__(self, width, height, position_x, position_y, color, label, button_state, field_width, field_height):
        super().__init__(field_width, field_height)

        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.label = label
        self.button_state = button_state

    def load_files_to_chart(self):
        pass

    def show_chart(self):
        pass