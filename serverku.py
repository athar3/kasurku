#YANG SERVER

from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

host = '192.168.56.103'
port = 6969
s = socket(AF_INET, SOCK_STREAM)

def Connecting():
    s.bind((host, port))
    print("Koneksi berhasil dibuka")

def listen():
    try:
        s.listen()
        global c
        c, addr = s.accept()
        print("Tersambung", addr)
        while True:
            data = c.recv(1024).decode()
            print(data)
            if not data:
                c.close()
                break
    except ConnectionResetError or OSError:
        c.close()

def msg():
    while True:
        try:
            reply = input('')
            reply2 = "SERVER: " + reply
            try:
                c.send(reply2.encode())
            except OSError:
                print("Tidak ada lagi client yang tersambung")
                c.close()
                break
        except KeyboardInterrupt or OSError:
            c.close()

if _name_ == '_main_':
    print("Memulai koneksi")
    Connecting()
    try:
        threadmsg=Thread(target=msg, args=())
        threadlisten=Thread(target=listen, args=())
        threadmsg.start()
        threadlisten.start()
        threadmsg.join()
        threadlisten.join()
    except KeyboardInterrupt:
        print=("Keluar...")
        c.close()
