import json
import socket

# getting server up
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Server = (socket.gethostbyname(socket.gethostname()), int(input('PORT:')))
listener.bind(Server)
listener.listen(1)


def get_connection():
    while True:
        data = listener.accept()
        if data:
            yield data


# {'name':'', 'time':'%d.%m.%Y %H:%M:%S', 'message':''}
def add_to_base(data) -> str:
    pass


def get_base() -> list:
    pass


def check_base():
    pass


for connection in get_connection():
    data = json.JSONDecoder.decode(connection[0].recv(500).decode('utf-8'))
    check_base()
    if data['command'] == 'send':
        data = data['data']
        # check data for sql injections
        # add try catch
        connection[0].send(json.dumps({'code': add_to_base(data)}).encode("utf-8"))
    elif data['command'] == 'get':
        connection[0].send(json.dumps(get_base()).encode("utf-8"))
    elif data['command'] == 'latency':
        pass
    elif data['command'] == 'info':
        pass