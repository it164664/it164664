# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
# import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import *


class Holidays(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Holidays.ui", self)
        self.show()
        self.proti_Photo.toggled.connect(lambda: self.hotels(self.proti_Photo, "prwtoRadio"))
        self.deuteri_Photo.toggled.connect(lambda: self.hotels(self.deuteri_Photo, "deuteroRadio"))
        self.triti_Photo.toggled.connect(lambda: self.hotels(self.triti_Photo, "tritoRadio"))

        self.dinner.toggled.connect(lambda: self.details(self.dinner))
        self.breakfast.toggled.connect(lambda: self.details(self.Extra))
        self.Extra.toggled.connect(lambda: self.details(self.breakfast))

        self.single.toggled.connect(lambda: self.rooms(self.single, "singleRadio"))
        self.double_2.toggled.connect(lambda: self.rooms(self.double_2, "doubleRadio"))
        self.suite.toggled.connect(lambda: self.rooms(self.suite, "suiteRadio"))

        self.showImage.clicked.connect(self.showIcon)

    def rooms(self, b, radio):
        if radio == "singleRadio":
            if b.isChecked():
                self.roomLabel.setText("Single room")
        elif radio== "doubleRadio":
            if b.isChecked():
                self.roomLabel.setText("Double room")
        else:
            if b.isChecked():
                self.roomLabel.setText("Suite room")
    def showIcon(self):
        print("A")
        if self.deuteri_Photo.isChecked():
            if self.double_2.isChecked():
                pixmap = QPixmap("AlArabDouble.jpg")
                self.picture2.setPixmap(pixmap)
            elif self.single.isChecked():
                pixmap = QPixmap("AlArabRoom.jpg")
                self.picture2.setPixmap(pixmap)
            else:
                pixmap = QPixmap("AlArabSuite.jpg")
                self.picture2.setPixmap(pixmap)
        elif self.triti_Photo.isChecked():
            if self.double_2.isChecked():
                pixmap = QPixmap("IceHotelDouble.jpg")
                self.picture2.setPixmap(pixmap)
            elif self.single.isChecked():
                pixmap = QPixmap("IceHotelSingle.jpg")
                self.picture2.setPixmap(pixmap)
            else:
                pixmap = QPixmap("IceHotelSuite.jpg")
                self.picture2.setPixmap(pixmap)
        elif self.proti_Photo.isChecked():
            if self.double_2.isChecked():
                pixmap = QPixmap("HiltonDouble.jpg")
                self.picture2.setPixmap(pixmap)
            elif self.single.isChecked():
                pixmap = QPixmap("HiltonSingle.jpg")
                self.picture2.setPixmap(pixmap)
            else:
                pixmap = QPixmap("HiltonSuite.jpg")
                self.picture2.setPixmap(pixmap)

    def hotels(self, b, choosenRadio):
        if choosenRadio == "prwtoRadio":

            if b.isChecked():
                self.proti_Photo.setIcon(QIcon("BurjAlArabHotel.jpg"))
                self.HotelLabel.setText("Al Arab Hotel")
            else:
                self.proti_Photo.setIcon(QIcon("BurjAlArabHotelBW.jpg"))

        elif choosenRadio == "deuteroRadio":
            if b.isChecked():
                self.deuteri_Photo.setIcon(QIcon("hiltonhotel.jpg"))
                self.HotelLabel.setText("Hilton Hotel")
            else:
                self.deuteri_Photo.setIcon(QIcon("hiltonhotelBW.jpg"))

        else:
            if b.isChecked():
                self.triti_Photo.setIcon(QIcon("icehotelBW.jpg"))
                self.HotelLabel.setText("Ice Hotel")
            else:
                self.triti_Photo.setIcon(QIcon("icehotelBW.jpg"))

    def details(self, b):

        if self.dinner.isChecked() and self.breakfast.isChecked() and self.Extra.isChecked():
            self.options.setText("Options selected: dinner, breakfast , Extra")
        elif self.dinner.isChecked() and self.breakfast.isChecked():
            self.options.setText("Options selected: dinner, breakfast")
        elif self.dinner.isChecked() and self.Extra.isChecked():
            self.options.setText("Options selected: dinner,Extra")
        elif self.breakfast.isChecked() and self.Extra.isChecked():
            self.options.setText("Options selected: breakfast, Extra")
        elif self.dinner.isChecked():
            self.options.setText("Options selected: dinner")
        elif self.breakfast.isChecked():
            self.options.setText("Options selected: breakfast")
        elif self.Extra.isChecked():
            self.options.setText("Options selected: Extra")
        else:
            self.options.setText("Nothing is chosen")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    holidays = Holidays()
    # loginWindow.show()
    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
