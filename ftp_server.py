from socket import *
from threading import Thread
import os
from time import sleep

FTP = "/home/tarena/FTP/"

class Handle:
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        files = os.listdir(FTP)
        if files:
            self.connfd.send(b"ok")
            sleep(0.1)

            data= "\n".join(files)
            self.connfd.send(data.encode())
        else:
            self.connfd.send(b"FAIL")
