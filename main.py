from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMessageBox, QWidget

import uii
from createUser import Ui_CreateUser
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

CreateUser = QtWidgets.QMainWindow()
ui_createUser = Ui_CreateUser()
ui_createUser.setupUi(CreateUser)


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
                fillTable(work.table)
            else:
                MainWindow_ws.show()
                fillTable(workspace.table)
        MainWindow.close()

def fillTable(table:QtWidgets.QTableWidget):
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels(['id', 'имя','пол','роль','пароль',''])
    users = printUsers()
    table.setRowCount(len(users))
    row = 0
    for user in users:
        checkbox = QtWidgets.QCheckBox()
        checkbox.setChecked(user['sex'])
        removeButton = QtWidgets.QPushButton("Удалить")
        print(row)
        removeButton.setObjectName(str(user['id']))
        removeButton.clicked.connect(lambda: delete_user(table.sender().objectName()))


        table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['id']))
        table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['name']))
        table.setCellWidget(row, 2, checkbox)
        table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['role']))
        table.setItem(row, 4, QtWidgets.QTableWidgetItem(user['password']))
        table.setCellWidget(row, 5, removeButton)
        row += 1

def delete_user(id):
    print(id)
    remove_user(id)
    fillTable(work.table)

def createUser():
    CreateUser.show()
    name = ui_createUser.nameField.text()
    sex = ui_createUser.sexCheckBox.isChecked()
    role = ui_createUser.roleField.text()
    password = ui_createUser.passwordField.text()
    res = create_new_user(name, sex, role, password)
    if res:
        CreateUser.close()
    else:
        QMessageBox.critical(QWidget(), 'Ошибка!', "Пользователь с таким именем уже существует!")

    fillTable(work.table)


ui.loginButton.clicked.connect(login)
work.pushButton.clicked.connect(CreateUser.show)
ui_createUser.createUserButton.clicked.connect(createUser)





MainWindow.show()
sys.exit(app.exec_())
