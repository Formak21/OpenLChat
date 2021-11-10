import socket

# getting server up
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Server = (socket.gethostbyname(socket.gethostname()), int(input('PORT:')))
listener.bind(Server)
listener.listen(1)

while True:
    data = listener.accept()
    text = data[0].recv(1024).decode("utf-8")
    if text:
        print(text)
        data[0].sendall('SERVER_ANSWER'.encode("utf-8"))
