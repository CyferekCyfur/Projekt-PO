from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(self.__padding_x, self.__padding_y, self.__width, self.__height)

        self.setWindowTitle("Program z mapkom i wykresikiem")

        self.show()

    def __init_default_value(self):

        self.__padding_x = 300
        self.__padding_y = 300
        self.__width = 800
        self.__height = 600

    def __init_view(self):