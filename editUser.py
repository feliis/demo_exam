# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editUser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.nameField = QtWidgets.QLineEdit(self.centralwidget)
        self.nameField.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.nameField.setObjectName("nameField")
        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(110, 180, 113, 20))
        self.passwordField.setObjectName("passwordField")
        self.sexCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sexCheckBox.setGeometry(QtCore.QRect(110, 100, 70, 17))
        self.sexCheckBox.setText("")
        self.sexCheckBox.setObjectName("sexCheckBox")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(200, 230, 161, 23))
        self.saveButton.setObjectName("saveButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(60, 230, 91, 23))
        self.removeButton.setObjectName("removeButton")
        self.rolesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.rolesComboBox.setGeometry(QtCore.QRect(110, 130, 69, 22))
        self.rolesComboBox.setObjectName("rolesComboBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактирование пользователя"))
        self.label.setText(_translate("MainWindow", "Имя:"))
        self.label_2.setText(_translate("MainWindow", "Пол:"))
        self.label_3.setText(_translate("MainWindow", "Роль:"))
        self.label_4.setText(_translate("MainWindow", "Пароль:"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить изменения"))
        self.removeButton.setText(_translate("MainWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editUser = QtWidgets.QMainWindow()
    ui_editUser = Ui_editUser()
    ui_editUser.setupUi(editUser)
    editUser.show()
    sys.exit(app.exec_())