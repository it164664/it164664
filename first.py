# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:50:13 2021

@author: Lalik
"""

import sys
#import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi
import tkinter as tk
import sqlite3


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        a = loadUi("login.ui", self)
        self.show()
        a.SignUpButton.clicked.connect(self.SignupButton)
        a.LoginButton.clicked.connect(self.ConnectButton)

    def SignupButton(self):

        self.hide()
        self.second = SecondWindow()
        self.second.exec()  # will wait till you close second window
        # self.show() # show main window again

    def ConnectButton(self):
        # cur.execute('SELECT * from Customers')
        email = self.EmailText.text()
        password = self.PasswordText.text()
        if email == "" or password == "":
            if self.EmailText.text() == "":
                self.EmailError.setText("Dwse Email")
            else:
                self.EmailError.setText("")
            if self.PasswordText.text() == "":
                self.PasswordError.setText("Dwse Password")
            else:
                self.PasswordError.setText("")

        else:
            voithitiki_metavliti=1
            for row in cur.execute('SELECT * FROM Customers'):
                if row[1] == email and row[2] == password:
                    print("sindethikes")
                    print(email + password)
                    self.hide()
                    self.second = ThirdWindow()
                    self.second.exec()
                    voithitiki_metavliti=2
                    break
            if voithitiki_metavliti == 1 :
               print("den sindethikes")
            


class SecondWindow(QDialog):  # it has to be dialog

    def __init__(self):
        super().__init__()

        b = loadUi("register.ui", self)
        b.BackButton.clicked.connect(self.hide_second_window)
        b.Register2Button.clicked.connect(self.RegisterMethod)
        self.show()

    def hide_second_window(self):
        self.close()  # go back to main window
        loginWindow.show()

    def RegisterMethod(self):
        if self.Email2Text.text() == "" or self.Password2Text.text() == "" or self.PhoneText.text() == "":
            if self.Email2Text.text() == "":
                self.ErrorEmail.setText("dwse email")
            else:
                self.ErrorEmail.setText("")
            if self.Password2Text.text() == "":
                self.ErrorPassword.setText("dwse password")
            else:
                self.ErrorPassword.setText("")
            if self.PhoneText.text() == "":
                self.ErrorPhone.setText("dwse tilefono ")
            else:
                self.ErrorPhone.setText("")

        else:
            root = tk.Tk()
            root.title("Registration")
            root.configure(background='#363636')
            root.geometry("300x300")

            w = tk.Label(root, text="Successful registration ,Mr " + self.Email2Text.text(), background="white",
                         foreground="#ff007f")

            w.pack()
            # self.Register2Button.setEnabled(False)
            # self.BackButton.setEnabled(False)
            root.mainloop()
            # if(root.destroy()):
            # self.Register2Button.setEnabled(True)
            # self.BackButton.setEnabled(True)
            self.PerasmaStoixeiwn()

    def PerasmaStoixeiwn(self):

        # cur.execute('SELECT * from Customers')
        id = None
        email = self.Email2Text.text()
        password = self.Password2Text.text()
        phone = self.PhoneText.text()

        # cur.execute("INSERT INTO Customers VALUES (NULL,'iraklistheofanidis@gmail.com','password','6974974316')")
        # cur.execute("INSERT INTO Customers VALUES (?,?,?,?)", (id, email, password, phone))

        for row in cur.execute('SELECT * FROM Customers'):
            print(row)
            # if(row[0]==11):
            # print(row[0])

        conn.commit()
        self.ErrorEmail.setText("")
        self.ErrorPassword.setText("")
        self.ErrorPhone.setText("")


class ThirdWindow(QDialog):  # it has to be dialog

    def __init__(self):
        super().__init__()

        b = loadUi("third.ui", self)
        b.BackButton2.clicked.connect(self.hide_third_window)

    def hide_third_window(self):
        self.close()  # go back to main window
        loginWindow.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = Login()
    conn = sqlite3.connect('GimnastirioLogin.db')
    cur = conn.cursor()
    # loginWindow.show()
    app.exec_()
