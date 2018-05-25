# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtBrowser.setGeometry(QtCore.QRect(0, 61, 391, 181))
        self.txtBrowser.setObjectName("txtBrowser")
        self.txtInput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInput.setGeometry(QtCore.QRect(0, 250, 391, 31))
        self.txtInput.setObjectName("txtInput")
        self.txtInput.setEnabled(False)
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(0, 280, 391, 31))
        self.btnSend.setObjectName("btnSend")
        self.btnSend.setEnabled(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(70, 0, 181, 61))
        self.txtName.setObjectName("txtName")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(250, 0, 141, 61))
        self.btnLogin.setCheckable(False)
        self.btnLogin.setChecked(False)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>NickName:</p></body></html>"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))

