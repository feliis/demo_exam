from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMessageBox, QWidget, QComboBox

import uii
from createUser import Ui_CreateUserWindow
from editUser import Ui_editUser
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

CreateUserWindow = QtWidgets.QMainWindow()
ui_createUser = Ui_CreateUserWindow()
ui_createUser.setupUi(CreateUserWindow)

editUser = QtWidgets.QMainWindow()
ui_editUser = Ui_editUser()
ui_editUser.setupUi(editUser)


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
            print(user['role'])
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
        editButton = QtWidgets.QPushButton("Редактировать")
        editButton.setObjectName(str(user['id']))
        editButton.clicked.connect(lambda: edit_user(table.sender().objectName()))

        roles = get_roles()
        combobox = QComboBox()
        r = []
        for i in roles:
            r.append(i['name'])
        combobox.addItems(r)

        combobox.setCurrentIndex(r.index(user['role']))

        table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['id']))
        table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['name']))
        table.setCellWidget(row, 2, checkbox)
        table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['role']))
        table.setItem(row, 4, QtWidgets.QTableWidgetItem(user['password']))
        table.setCellWidget(row, 5, editButton)
        row += 1
def edit_user(id):
    editUser.show()
    ui_editUser.removeButton.clicked.connect(lambda: delete_user(id))
    fill_profile(id)



def delete_user(id):
    print(id)
    remove_user(id)
    fillTable(work.table)
    editUser.close()

# def edit_user()


def fill_profile(id):
    ui = ui_editUser

    roles = get_roles()
    r = []
    for i in roles:
        r.append(i['name'])
    ui.rolesComboBox.addItems(r)

    user = get_info_user(id)
    ui.nameField.setText(user['name'])
    ui.sexCheckBox.setChecked(user['sex'])
    ui.rolesComboBox.setCurrentIndex(r.index(user['role']))
    ui.passwordField.setText(user['password'])


def createUser():
    CreateUserWindow.show()
    name = ui_createUser.nameField.text()
    sex = ui_createUser.sexCheckBox.isChecked()
    role = str(ui_createUser.rolesComboBox.currentText())
    print(role)
    password = ui_createUser.passwordField.text()
    res = create_new_user(name, sex, role, password)
    if res:
        CreateUserWindow.close()
    else:
        QMessageBox.critical(QWidget(), 'Ошибка!', "Пользователь с таким именем уже существует!")

    fillTable(work.table)


ui.loginButton.clicked.connect(login)
work.pushButton.clicked.connect(CreateUserWindow.show)
ui_createUser.saveButton.clicked.connect(createUser)



MainWindow.show()
sys.exit(app.exec_())
