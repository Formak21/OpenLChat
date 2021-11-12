import socket
import json
import datetime

Server = (input('IP:'), int(input('PORT:')))


def send_message(data) -> dict:
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect(Server)
    con.sendall(json.dumps(data).encode('utf-8'))
    answer = json.JSONDecoder().decode(con.recv(1024).decode('utf-8'))
    con.close()
    return answer

def get_base(data) -> dict:
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect(Server)
    con.sendall(json.dumps(data).encode('utf-8'))
    answer = json.JSONDecoder().decode(con.recv(26000).decode('utf-8'))
    con.close()
    return answer

def menu() -> str:
    print('send <name> <text> - for send message')
    print('get - for get messages')
    print('reload - for reloading saved messages')
    print('save - for saving all messages to the base')
    print('connection - for checking server connection')
    print('reconnect - for reconnect to the other server')
    print('exit - for exit')
    return input()


Messages = []
LastReloadTime = datetime.datetime.now()

while True:
    useranswer = menu().split(' ')

    if useranswer[0] == 'send':
        name = useranswer[1]
        message = ' '.join(useranswer[2:])
        if len(bytearray(name, encoding='utf-8')) <= 16 and len(bytearray(message, encoding='utf-8')) <= 256:
            server_answer = send_message(
                {'command': 'send', 'time': datetime.datetime.now(), 'name': name, 'message': message})
            if server_answer['code'] == 'success':
                print('success')
            else:
                print('fail')
    if useranswer[0] == 'get':
        for i in Messages:
            print(f"[{i['time'].ctime()}] {i['name']} - {i['message']}")
    if useranswer[0] == 'reload' or datetime.datetime.now() - LastReloadTime > datetime.timedelta(seconds=5):
        LastReloadTime = datetime.datetime.now()
        Messages = get_base({'command': 'get'})
    if useranswer[0] == 'save':
        pass
    if useranswer[0] == 'connection':
        send_time = datetime.datetime.now()
        server_time = send_message({'command': 'ping'})['time']
        get_time = datetime.datetime.now()
        print('ping -', ((get_time-server_time)+(server_time-send_time)).seconds)
    if useranswer[0] == 'reconnect':
        Server = (int(input('IP:')), int(input('PORT:')))
    if useranswer[0] == 'exit':
        break
