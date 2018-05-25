import socket
import threading
import datetime
import mainwindow
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Client:
    def __init__(self, host, port, name):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.sock.recv(1024).decode()
        self.sock.send(name.encode())
        myname = self.sock.recv(1024).decode()
        Main.txtBrowser.append(myname)
        Main.txtBrowser.update()

    def sendThreadFunc(self):
        x = datetime.datetime.now()
        while True:
            try:
                myword = input() + "                             [" + str(x.hour) + ":" + str(x.minute) + ":" + str(x.second) + "]"
                self.sock.send(myword.encode())
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024).decode() # socket.recv(recv_size)
                print(otherword)
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

class Main(QMainWindow,  mainwindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.btnSend.clicked.connect(self.send)
        self.btnLogin.clicked.connect(self.start)

    def send(self):
        text = self.txtInput.text()
        self.txtBrowser.append(text)
        self.txtBrowser.update()
        self.txtInput.setText("")
        self.txtInput.setFocus()

    def start(self):
        # myname = self.txtName.text()
        self.btnLogin.setEnabled(False)
        self.txtName.setEnabled(False)
        self.btnSend.setEnabled(True)
        self.txtInput.setEnabled(True)
        # c = Client('localhost', 5550, name)
        # th1 = threading.Thread(target=c.sendThreadFunc)
        # th2 = threading.Thread(target=c.recvThreadFunc)
        # threads = [th1, th2]
        # for t in threads:
        #     t.setDaemon(True)
        #     t.start()
        # t.join()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow=Main()
    MainWindow.show()
    sys.exit(app.exec_())
