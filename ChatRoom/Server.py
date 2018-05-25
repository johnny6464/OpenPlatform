# -*- encoding: utf-8 -*-
import socket
import threading
from time import gmtime, strftime


class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()

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
                connection.send(b'Welcome to chat room!')
            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay, name):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(name.encode() + b': ' + whatToSay.encode() + b'      people: ' + str(len(self.mylist)).encode())
                except:
                    pass

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        myconnection.send(b'1')
        name = myconnection.recv(1024).decode()
        myconnection.send(b'Now Lets Chat, ' + name.encode())
        self.tellOthers(connNumber, 'SYSTEM: ' + name + ' in the chat room',name)
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    self.tellOthers(connNumber, recvedMsg, name)
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                    self.tellOthers(connNumber, name + ' is out',name)
                except:
                    pass

                myconnection.close()
                return


def main():
    s = Server('localhost', 5550)
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

