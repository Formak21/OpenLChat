import socket
import sqlite3

# getting server up
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Server = (socket.gethostbyname(socket.gethostname()), int(input('PORT:')))
listener.bind(Server)
listener.listen(1)
database = sqlite3.connect("messages_db.sqlite")


def get_connection():
    while True:
        data = listener.accept()
        if data:
            yield data