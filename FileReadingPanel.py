from tkinter.filedialog import askopenfilename
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        if not FirstWindow.objectName():
            FirstWindow.setObjectName(u"FirstWindow")
        FirstWindow.resize(650, 450)
        self.pushButton = QPushButton(FirstWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 300, 100, 50))
        self.lineEdit = QLineEdit(FirstWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(75, 200, 500, 35))
        self.pushButton_2 = QPushButton(FirstWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 300, 100, 50))

        self.retranslateUi(FirstWindow)

        QMetaObject.connectSlotsByName(FirstWindow)
    # setupUi

    def retranslateUi(self, FirstWindow):
        FirstWindow.setWindowTitle(QCoreApplication.translate("FirstWindow", u"Eurostat-frontend", None))
        self.pushButton.setText(QCoreApplication.translate("FirstWindow", u"Wybierz plik", None))
        self.pushButton_2.setText(QCoreApplication.translate("FirstWindow", u"Gotowe", None))
    # retranslateUi

class FileReadingPanel:
    def file_reading(self):
        filename = askopenfilename()
        print(filename)
        return filename



    
FRP = FileReadingPanel()
FRP.file_reading()