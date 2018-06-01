# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 61, 31))
        self.label_2.setObjectName("label_2")
        self.add_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_Button.setGeometry(QtCore.QRect(10, 70, 341, 41))
        self.add_Button.setObjectName("add_Button")
        self.member_list = QtWidgets.QListView(self.centralwidget)
        self.member_list.setGeometry(QtCore.QRect(10, 120, 341, 211))
        self.member_list.setObjectName("member_list")
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(10, 340, 341, 31))
        self.del_button.setObjectName("del_button")
        self.nickname_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nickname_lineEdit.setGeometry(QtCore.QRect(70, 30, 113, 20))
        self.nickname_lineEdit.setObjectName("nickname_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(240, 30, 113, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nickname : "))
        self.label_2.setText(_translate("MainWindow", "Password : "))
        self.add_Button.setText(_translate("MainWindow", "Add"))
        self.del_button.setText(_translate("MainWindow", "Del"))

