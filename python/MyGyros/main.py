# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functools import partial
import numpy as np
import sys
# import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import *


class Gyros(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("MyGyros.ui", self)
        self.show()

        self.foodIcon.setPixmap(QPixmap("gyros.jpg"))
        self.drinkIcon.setPixmap(QPixmap("fanta.jpg"))
        foods2 = np.array([["Γύρος", "Σουτζουκάκι", "Σουβλάκι", "Χωριάτικη", "Πράσινη", "Γεμιστά"], [3, 3.5, 4, 4.5, 4, 5]])
        drinks2 = np.array([["Πορτοκαλάδα", "Λεμονάδα", "Νερό", "κοκακόλα"], [1, 1, 0.5, 1.5]])
        self.listItems(foods2, drinks2)
        self.addCart.clicked.connect(partial(self.addtoCart, foods2))
        self.addCart2.clicked.connect(partial(self.addtoCart2, drinks2))

    def listItems(self, foods2, drinks2):

        for row in foods2[0]:
            self.foodlist.addItem(row)
        self.foodlist.currentTextChanged.connect(self.showfoodIcon)

        for row in drinks2[0]:
            self.drinklist.addItem(row)
        self.drinklist.currentTextChanged.connect(self.showdrinkIcon)

    def showfoodIcon(self):

        dokimi = self.foodlist.currentText()
        if dokimi == "Γύρος":
            self.foodIcon.setPixmap(QPixmap("gyros.jpg"))
        elif dokimi == "Σουτζουκάκι":
            self.foodIcon.setPixmap(QPixmap("soutsoukaki.jpg"))
        elif dokimi == "Χωριάτικη":
            self.foodIcon.setPixmap(QPixmap("xoriatiki.jpg"))
        elif dokimi == "Σουβλάκι":
            self.foodIcon.setPixmap(QPixmap("souvlaki.jpg"))
        elif dokimi == "Πράσινη":
            self.foodIcon.setPixmap(QPixmap("prasini.jpg"))
        elif dokimi == "Γεμιστά":
            self.foodIcon.setPixmap(QPixmap("gemista.jpg"))

    def showdrinkIcon(self):
        dokimi2 = self.drinklist.currentText()
        if dokimi2 == "Πορτοκαλάδα":
            self.drinkIcon.setPixmap(QPixmap("fanta.jpg"))
        elif dokimi2 == "κοκακόλα":
            self.drinkIcon.setPixmap(QPixmap("kokakola.jpg"))
        elif dokimi2 == "Λεμονάδα":
            self.drinkIcon.setPixmap(QPixmap("lemonada.jpg"))
        elif dokimi2 == "Νερό":
            self.drinkIcon.setPixmap(QPixmap("nero.jpg"))

    def addtoCart(self, foods2):
        order = self.foodlist.currentText()
        quantity = self.spinBoxFood.value()
        rowPosition = self.table.rowCount()

        voithitiki_timi = 0
        for row in foods2[0]:
            if row == order:
                print(row)
                break
            voithitiki_timi = voithitiki_timi + 1
        timi_monadas = foods2[1][voithitiki_timi]

        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QTableWidgetItem(order))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(quantity)))
        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(timi_monadas)))

        self.ipologismos()

    def addtoCart2(self, drinks2):
        order = self.drinklist.currentText()
        quantity = self.spinBoxDrink.value()
        rowPosition = self.table.rowCount()

        voithitiki_timi = 0
        for row in drinks2[0]:
            if row == order:
                print(row)
                break
            voithitiki_timi = voithitiki_timi + 1
        timi_monadas = drinks2[1][voithitiki_timi]

        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QTableWidgetItem(order))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(quantity)))
        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(timi_monadas)))

        self.ipologismos()

    def ipologismos(self):
        athroismatimis = 0
        for row in range(self.table.rowCount()):
            # for column in range(self.table.columnCount()):
            # print("A")
            posotita = self.table.item(row, 1)
            timi = self.table.item(row, 2)
            name = float(posotita.text())
            name2 = float(timi.text())
            timiproiontos = name * name2
            athroismatimis = athroismatimis + timiproiontos
            print("loupa", name, name2, timiproiontos, athroismatimis)
        self.Lefta.setText(str(athroismatimis))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    holidays = Gyros()
    # loginWindow.show()
    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
