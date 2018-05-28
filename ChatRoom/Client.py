import socket
import threading
import datetime
import mainwindow
import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal


class ClientRecv(QThread):
    recvmsg = pyqtSignal(str)

    def __init__(self, host, port, name):
        QThread.__init__(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        time.sleep(1)
        self.sock.send(name.encode())

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            otherword = self.sock.recv(1024).decode()
            self.recvmsg.emit(otherword)

    def send(self, myword):
        try:
            self.sock.send(myword.encode())
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')


class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.name = None
        self.client = None
        self.time = None
        self.btnLogin.clicked.connect(self.login)
        self.btnSend.clicked.connect(self.send)
        self.txtName.setFocus()

    def login(self):
        self.txtName.setFocus()
        if self.txtName.text():
            self.name = self.txtName.text()
            self.btnLogin.setEnabled(False)
            self.txtName.setEnabled(False)
            self.btnSend.setEnabled(True)
            self.txtInput.setEnabled(True)
            self.txtInput.setFocus()
            self.txtBrowser.append("Welcome to chat room! " + self.name)
            self.txtBrowser.append("Now Lets Chat,  " + self.name)
            self.client = ClientRecv('localhost', 5550, self.name)
            self.client.recvmsg.connect(self.printMsg)
            self.client.start()

    def send(self):
        self.txtInput.setFocus()
        if self.txtInput.text():
            text = self.txtInput.text()
            self.time = datetime.datetime.now()
            self.time = self.time.strftime("%H:%M:%S")
            self.txtBrowser.append("                  " + self.name + ": " + text + "[" + self.time + "]")
            self.txtInput.setText("")
            self.client.send(text)

    def printMsg(self, data):
        self.time = datetime.datetime.now()
        self.time = self.time.strftime("%H:%M:%S")
        self.txtBrowser.append(data + "[" + str(self.time) + "]")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
