# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
# import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import *


class AgoraSpitiou(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("AgoraSpitiou.ui", self)
        self.show()
        # self.radioButton()
        self.proti_Photo.toggled.connect(lambda: self.btnstate(self.proti_Photo, "prwtoRadio"))
        self.deuteri_Photo.toggled.connect(lambda: self.btnstate(self.deuteri_Photo, "deuteroRadio"))
        self.triti_Photo.toggled.connect(lambda: self.btnstate(self.triti_Photo, "tritoRadio"))
        self.ipologismos.clicked.connect(self.IpologismosDosis)

        '''self.proti_Photo.setStyleSheet("QRadioButton::hover"
                                       "{"
                                       "image : url(ChatsworthHouse.jpg);"
                                       "}")
        '''

    def IpologismosDosis(self):
        kefalaio = float(self.Kefalaio.text().replace(".", ""))
        epitokio = float(self.Epitokio.text().replace(".", ""))
        diarkeia = float(self.Diarkeia.text().replace(".", ""))
        print(kefalaio)

        Aksia = float(self.timi.text().replace(".", ""))
        print(Aksia)
        Daneio = Aksia - kefalaio
        print(Daneio)
        if Daneio <= 0:
            self.denXreiazete.setText("Δεν χρειάζεται Δάνειο")
            # print("5")
        else:
            self.denXreiazete.setText("")
            tokos = (Daneio * epitokio) / 100
            daneiometoko = Daneio + tokos
            if diarkeia <= 0:
                self.DosiTimi.setText("lathos diarkeia")
            else:
                dosi = daneiometoko / diarkeia
                Dosi = str(dosi)
                self.DosiTimi.setText(Dosi)

    def btnstate(self, b, choosenRadio):
        if choosenRadio == "prwtoRadio":

            if b.isChecked():
                self.proti_Photo.setIcon(QIcon("ChatsworthHousePressed.jpg"))
                self.timi.setText("3.000.000")
                # a=self.timi.text().replace("." , "")
                # a=self.timi.text()
                # print(a)
            else:
                self.proti_Photo.setIcon(QIcon("ChatsworthHouse.jpg"))

        elif choosenRadio == "deuteroRadio":
            if b.isChecked():
                self.deuteri_Photo.setIcon(QIcon("queen_housePressed.jpg"))
                self.timi.setText("4.000.000")
            else:
                self.deuteri_Photo.setIcon(QIcon("queen_house.jpg"))

        else:
            if b.isChecked():
                self.triti_Photo.setIcon(QIcon("white_housePressed.jpg"))
                self.timi.setText("5.000.000")
            else:
                self.triti_Photo.setIcon(QIcon("white_house.jpg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    CalculatorWindow = AgoraSpitiou()
    # loginWindow.show()
    app.exec_()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
