# -*- encoding: utf-8 -*-
import socket
import threading
from time import gmtime, strftime
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import serverwindow
import sys


class Server(QThread):
    def __init__(self, host, port):
        QThread.__init__(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
	
    def run(self):
        while True:
            self.checkConnection()
	
    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())
        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay, name, issystem, onlineusers):
        for c in self.mylist:
            if issystem:
                if c.fileno() != exceptNum:
                    try:
                        c.send(whatToSay.encode() + onlineusers.encode())
                    except:
                        pass
                else:
                    try:
                        c.send(onlineusers.encode())
                    except:
                        pass
            else:
                if c.fileno() != exceptNum:
                    try:
                        c.send(name.encode() + b': ' + whatToSay.encode() + onlineusers.encode())
                    except:
                        pass
                else:
                    pass
    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        name = myconnection.recv(1024).decode()
        self.tellOthers(connNumber, 'SYSTEM: ' + name + ' is in the chat room', name, True, str(len(self.mylist)))
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    self.tellOthers(connNumber, recvedMsg, name, False, str(len(self.mylist)))
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                    self.tellOthers(connNumber, 'SYSTEM: ' + name + ' is out', name, True, str(len(self.mylist)))
                except:
                    pass

                myconnection.close()
                return

class MainWindow(QMainWindow, serverwindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.add_Button.clicked.connect(self.add)
        self.client = Server('localhost',5550)
        self.client.start()
    
    def add(self):
        if self.nickname_lineEdit.text() and self.password_lineEdit.text():
            text = self.nickname_lineEdit.text()
            self.nickname_lineEdit.setText("")
            text2 = self.password_lineEdit.text()
            self.password_lineEdit.setText("")
            self.member_list.append(text)
			


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

