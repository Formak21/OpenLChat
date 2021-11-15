import socket

Server = (input('IP:'), int(input('PORT:')))
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect(Server)
con.send(input().encode('utf-8'))
con.send(input().encode('utf-8'))
con.send(input().encode('utf-8'))
con.close()