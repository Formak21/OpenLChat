import socket
import json

Server = ("IP", int(input('PORT:')))
Message = [input(), input(), input()]
while True:
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect(Server)
    con.sendall(json.dumps(Message).encode('utf-8'))
    print(json.JSONDecoder().decode(con.recv(1024).decode('utf-8')))
    Message = [input(), input(), input()]
    con.close()
