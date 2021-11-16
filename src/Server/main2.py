import net
import json

# {'name':'', 'time':'%d.%m.%Y %H:%M:%S', 'message':''}
def add_to_base(data) -> str:
    cur = self.con.cursor()
    cur.execute("SELECT * FROM films WHERE id=?",
                         (item_id := self.spinBox.text(),)).fetchall()


def get_base() -> list:
    pass


def check_base():
    pass


for connection in get_connection():
    data = json.JSONDecoder.decode(connection[0].recv(500).decode('utf-8'))
    check_base()
    if data['command'] == 'send':
        data = data['data']
        connection[0].send(json.dumps({'code': add_to_base(data)}).encode("utf-8"))
    elif data['command'] == 'get':
        connection[0].send(json.dumps(get_base()).encode("utf-8"))
    else:
        connection[0].send(json.dumps({'code': 'incorrect command'}).encode("utf-8"))
    connection.close()