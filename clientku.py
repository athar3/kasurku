#YANG CLIENT

import socket
from socket import timeout
import time
from threading import Thread

error = (ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, socket.gaierror, TimeoutError, EOFError, KeyboardInterrupt)
user = socket.gethostname()

print("===========Simple Chat Pc to Server in Private LAN=================\n")

while True:
    try:
        host = input("Berapa IP Address Private tujuan Anda?: ")
        port = int(input("Berapa port dari tujuan Anda?: "))
        break
    except error:
        print("\nHost/Port tidak valid, masukkan lagi")

s = socket.socket()
a = True

def Connecting():
    try:
        s.connect((host,port))
    except error:
        print("-> Error tidak dapat menyambungkan, mohon dicek kembali host dan port tujuan")
        time.sleep(1)
        return "error"

def msg():
        try:
            global a
            message = input("")
            while a is True:
                try:
                    s.send((user + ': ' + message).encode())
                    message = input("")
                except EOFError:
                    s.close()
                    a = False
        except KeyboardInterrupt or EOFError:
            s.close()
            a = False

def recv():
    global a
    while a is True:
        time.sleep(0.1)
        try:
            s.settimeout(1)
            print(s.recv(1024).decode())
        except timeout:
            pass

if _name_ == '_main_':
    try:
        print("\nMasuk sebagai: ", user)
        if Connecting() == 'error':
            print("-> Program akan ditutup...")
            time.sleep(1)
        else:
            print("Koneksi Berhasil")
            threadmsg=Thread(target=msg, args=())
            threadrecv=Thread(target=recv, args=())
            threadmsg.start()
            threadrecv.start()
    except error:
        print("Keluar...")
        a = False
        threadmsg.join()
        threadrecv.join()
        s.close()
