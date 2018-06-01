# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtBrowser.setGeometry(QtCore.QRect(0, 90, 450, 280))
        self.txtBrowser.setObjectName("txtBrowser")
        self.txtInput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInput.setGeometry(QtCore.QRect(0, 370, 450, 30))
        self.txtInput.setObjectName("txtInput")
        self.txtInput.setEnabled(False)
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(0, 400, 450, 30))
        self.btnSend.setObjectName("btnSend")
        self.btnSend.setEnabled(False)
        self.btnSend.setStyleSheet("background-color: #FFD700;")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(10, 30, 71, 30))
        self.lblName.setObjectName("lblName")
        self.lblUsers = QtWidgets.QLabel(self.centralwidget)
        self.lblUsers.setGeometry(QtCore.QRect(10, 0, 440, 30))
        self.lblUsers.setObjectName("lblUsers")
        self.lblUsers.setStyleSheet("text-align: center;")
        self.lblCPwd = QtWidgets.QLabel(self.centralwidget)
        self.lblCPwd.setGeometry(QtCore.QRect(10, 60, 90, 30))
        self.lblCPwd.setObjectName("lblCPwd")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(85, 30, 135, 30))
        self.txtName.setObjectName("txtName")
        self.txtPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPwd.setGeometry(QtCore.QRect(220, 30, 130, 30))
        self.txtPwd.setObjectName("txtPwd")
        self.txtPwd.setEchoMode(QLineEdit.Password)
        self.txtCPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCPwd.setGeometry(QtCore.QRect(100, 60, 120, 30))
        self.txtCPwd.setObjectName("txtCPwd")
        self.txtCPwd.setDisabled(True)
        self.txtCPwd.setEchoMode(QLineEdit.Password)
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(350, 30, 100, 30))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setStyleSheet("background-color: #FFD700;")
        self.btnUpwd = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpwd.setGeometry(QtCore.QRect(220, 60, 230, 30))
        self.btnUpwd.setObjectName("btnUpwd")
        self.btnUpwd.setStyleSheet("background-color: #F08080;")
        self.btnUpwd.setDisabled(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 22))
        self.menubar.setObjectName("menubar")
        self.menuChat_Application = QtWidgets.QMenu(self.menubar)
        self.menuChat_Application.setObjectName("menuChat_Application")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuChat_Application.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat  Application"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.btnUpwd.setText(_translate("MainWindow", "Update Password"))
        self.lblName.setText(_translate("MainWindow", "NickName:"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.lblUsers.setText(_translate("MainWindow", "                                                       目前聊天室有0人"))
        self.lblCPwd.setText(_translate("MainWindow", "Change Password:"))

