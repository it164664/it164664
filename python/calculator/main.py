import sys
# import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi


class Calculator(QDialog):
    number = "0"
    number1 = 0
    number2 = 0
    praksi=""


    def __init__(self):
        super().__init__()
        loadUi("Calculator.ui", self)
        self.show()
        self.b0.clicked.connect(self.b0Button)
        self.b1.clicked.connect(self.b1Button)
        self.b2.clicked.connect(self.b2Button)
        self.b3.clicked.connect(self.b3Button)
        self.b4.clicked.connect(self.b4Button)
        self.b5.clicked.connect(self.b5Button)
        self.b6.clicked.connect(self.b6Button)
        self.b7.clicked.connect(self.b7Button)
        self.b8.clicked.connect(self.b8Button)
        self.b9.clicked.connect(self.b9Button)
        self.dot.clicked.connect(self.dotButton)
        self.equals.clicked.connect(self.equalsButton)
        self.divide.clicked.connect(self.divideButton)
        self.sub.clicked.connect(self.subButton)
        self.add.clicked.connect(self.addButton)
        self.multiplication.clicked.connect(self.multiplicationButton)
        self.empty.clicked.connect(self.emptyButton)

    def b0Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"0")
            self.number=self.calcLabel.text()

            self.number1 = int(self.number)
        else:
            if self.number2== 0:
                self.calcLabel.setText("0")
                self.number = self.calcLabel.text()
                self.number2=0
            else:
                b=self.calcLabel.text()
                self.calcLabel.setText(b + "0")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b1Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"1")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("1")
                self.number = self.calcLabel.text()
                self.number2 = 1
            else:
                b=self.calcLabel.text()
                self.calcLabel.setText(b + "1")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b2Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"2")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("2")
                self.number = self.calcLabel.text()
                self.number2 = 2
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "2")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b3Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"3")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("3")
                self.number = self.calcLabel.text()
                self.number2 = 3
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "3")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b4Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"4")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("4")
                self.number = self.calcLabel.text()
                self.number2 = 4
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "4")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b5Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"5")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("5")
                self.number = self.calcLabel.text()
                self.number2 = 5
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "5")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b6Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"6")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("6")
                self.number = self.calcLabel.text()
                self.number2 = 6
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "6")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b7Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"7")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("7")
                self.number = self.calcLabel.text()
                self.number2 = 7
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "7")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b8Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"8")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)
        else:
            if self.number2 == 0:
                self.calcLabel.setText("8")
                self.number = self.calcLabel.text()
                self.number2 = 8
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "8")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def b9Button(self):
        if self.praksi == "":
            a = self.calcLabel.text()
            self.calcLabel.setText(a+"9")
            self.number = self.calcLabel.text()
            self.number1 = int(self.number)

        else:
            if self.number2 == 0:
                self.calcLabel.setText("9")
                self.number = self.calcLabel.text()
                self.number2 = 9
            else:
                b = self.calcLabel.text()
                self.calcLabel.setText(b + "9")
                self.number = self.calcLabel.text()
                self.number2 = int(self.number)

    def dotButton(self):
        a = self.calcLabel.text()
        self.calcLabel.setText(a + ".")

    def equalsButton(self):
        a = self.calcLabel.text()
        if self.praksi == "+":
            solution=self.number1 + self.number2
            print(solution)
            convertedSolution = str(solution)
            self.calcLabel.setText(convertedSolution)
        elif self.praksi == "-":
            solution = self.number1 - self.number2
            print(solution)
            convertedSolution = str(solution)
            self.calcLabel.setText(convertedSolution)
        elif self.praksi == "/":
            solution = self.number1 / self.number2
            print(solution)
            convertedSolution = str(solution)
            self.calcLabel.setText(convertedSolution)
        elif self.praksi == "*":
            solution = self.number1 * self.number2
            print(solution)
            convertedSolution = str(solution)
            self.calcLabel.setText(convertedSolution)

    def divideButton(self):
        a = self.calcLabel.text()
        #self.calcLabel.setText(a + "/")
        self.praksi="/"
        self.miniCalcLabel.setText(self.number + self.praksi)
        print(self.number + self.praksi)

    def multiplicationButton(self):
        a = self.calcLabel.text()
        #self.calcLabel.setText(a + "*")
        self.praksi="*"
        self.miniCalcLabel.setText(self.number + self.praksi)
        print(self.number + self.praksi)

    def subButton(self):
        a = self.calcLabel.text()
        #self.calcLabel.setText(a + "-")
        self.praksi="-"
        self.miniCalcLabel.setText(self.number + self.praksi)
        print(self.number + self.praksi)

    def addButton(self):
        a = self.calcLabel.text()
        #self.calcLabel.setText(a + "+")
        self.praksi = "+"
        self.miniCalcLabel.setText(self.number + self.praksi)
        print(self.number + self.praksi)

    def emptyButton(self):
        self.miniCalcLabel.setText("")
        self.calcLabel.setText("")
        self.praksi = ""
        self.number = "0"
        self.number1 = 0
        self.number2 = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    CalculatorWindow = Calculator()
    # loginWindow.show()
    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
