import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi

class Decoder(QDialog):  # it has to be dialog

    def __init__(self):
        super().__init__()

        loadUi("encode_decode_reset.ui", self)
        self.show()
        self.EncodeButton.clicked.connect(self.EncodeMethod)
        self.DecodeButton.clicked.connect(self.DecodeMethod)
        self.ResetButton.clicked.connect(self.ResetMethod)

    def EncodeMethod(self):
        ch = self.FirstLineEdit.text()

        encode=''
        for i in ch:
            x=chr(ord(i)+1)
            print(x)
            encode = encode+x

        print(encode)
        self.SecondLineEdit.setText(encode)
        #print("The incremented character value is : ", end="")
        #print(x)
    def DecodeMethod(self):
        ch = self.SecondLineEdit.text()

        decode=''
        for i in ch:
            x=chr(ord(i)-1)
            print(x)
            decode = decode+x

        print(decode)
        self.FirstLineEdit.setText(decode)

    def ResetMethod(self):
        self.FirstLineEdit.setText("")
        self.SecondLineEdit.setText("")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    DecoderWindow = Decoder()
    app.exec_()