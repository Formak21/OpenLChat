import datetime
import socket
import json

Server = (input('IP:'), int(input('PORT:')))
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    con.connect(Server)
    con.send(json.dumps({'command': 'send', 'data': {'name': f'{input("NAME:")}', 'message': f'{input("MESSAGE:")}',
                                                     'time': datetime.datetime.now().strftime(
                                                         '%d.%m.%Y %H:%M:%S')}}).encode('utf-8'))
    print(con.recv(500).decode('utf-8'))
    con.close()
