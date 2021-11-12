import socket
import json
import datetime

# getting server up
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Server = (socket.gethostbyname(socket.gethostname()), int(input('PORT:')))
listener.bind(Server)
listener.listen(1)

while True:
    data = listener.accept()
    my_data = data[0].recv(400).decode('utf-8')
    if my_data:
        my_data = json.JSONDecoder().decode(my_data)
        print(my_data)
        data[0].sendall(json.dumps({'code': 'success'}).encode("utf-8"))
