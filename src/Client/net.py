import socket
import json
from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal


class OpenLChatClient:
    def __init__(self, ip_port):
        self.ip_port = ip_port

    def send_message(self, message):
        try:
            con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            con.settimeout(4)
            con.connect(self.ip_port)
            con.send(json.dumps({'command': 'send', 'data': message}).encode('utf-8'))
            return json.loads(con.recv(500).decode('utf-8'))['code']
        except:
            print()
            return 'CONNECTION_LOST_OR_SOMETHING_ELSE'

    def get_base(self):
        try:
            con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            con.settimeout(4)
            con.connect(self.ip_port)
            con.send(json.dumps({'command': 'get'}).encode('utf-8'))
            return json.loads(con.recv(32000).decode('utf-8'))
        except:
            return 'CONNECTION_LOST_OR_SOMETHING_ELSE'

def check_connection(ip_port):
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.settimeout(4)
        con.connect(ip_port)
        con.send(json.dumps({'command': 'test'}).encode('utf-8'))
        return json.loads(con.recv(500).decode('utf-8'))['code'][:13] == 'we are stable'
    except:
        return False
