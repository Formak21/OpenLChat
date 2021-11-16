import datetime
import socket
import json

Server = (input('IP:'), int(input('PORT:')))
while True:
    command = input('COMMAND:')
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect(Server)
    if command == 'send':
        con.send(
            json.dumps({'command': command, 'data': {'name': f'{input("NAME:")}', 'message': f'{input("MESSAGE:")}',
                                                     'time': datetime.datetime.now().strftime(
                                                         '%d.%m.%Y %H:%M:%S')}}).encode('utf-8'))
        print(json.loads(con.recv(500).decode('utf-8'))['code'])
    elif command == 'get':
        con.send(json.dumps({'command': command}).encode('utf-8'))
        for i in json.loads(con.recv(26000).decode('utf-8')):
            print(f"[{i['time']}] [{i['name']}] - {i['message']}")
    con.close()
