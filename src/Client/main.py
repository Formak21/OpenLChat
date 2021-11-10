import socket

Server = ("192.168.88.246", int(input('PORT:'))
Message = input()
while True:
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect(Server)
    con.sendall(Message.encode('utf-8'))
    print(con.recv(1024).decode(utf-8))
    Message = input()
    con.close()