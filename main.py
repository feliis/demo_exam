from PyQt5.QtWidgets import QMessageBox, QWidget

from login import Ui_MainWindow
from ui import Ui_Workspace
from PyQt5 import QtCore, QtGui, QtWidgets
from db import *
import sys

from uii import Ui_Main

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow_ws = QtWidgets.QMainWindow()
workspace = Ui_Workspace()
workspace.setupUi(MainWindow_ws)

Main = QtWidgets.QMainWindow()
work = Ui_Main()
work.setupUi(Main)


def login() :
    name = ui.nameField.text()
    password = ui.passwordField.text()
    user = getUser(name)
    if not user:
        QMessageBox.critical(QWidget(), 'Ошибка!', "Не верный логин!")
    else:
        if password != user['password']:
            QMessageBox.critical(QWidget(), 'Ошибка!', "Не верный пароль!")
        else:
            print("Logged in")
            if user['role'] == 'admin':
                Main.show()
            else:
                MainWindow_ws.show()
        MainWindow.close()



ui.loginButton.clicked.connect(login)







MainWindow.show()
sys.exit(app.exec_())
