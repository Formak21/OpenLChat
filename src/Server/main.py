import welcome
import net
import json


# data format - {'name': 'max 16 bytes', 'message': 'max 256 bytes', 'time': '%d.%m.%Y %H:%M:%S'}
def add_to_base(data) -> str:
    # checking data format
    if sum([int(bool(data[i])) for i in data.keys()]) != 3:
        return 'data_err'
    if len(bytearray(data['name'], encoding='utf-8')) <= 16 and len(
            bytearray(data['message'], encoding='utf-8')) <= 256 and len(
            bytearray(data['time'], encoding='utf-8')) <= 20:
        return 'len_err'
    # checking size of db
    if len(net.cursor.execute('SELECT * FROM messages_main').fetchall()) >= 64:
        for k in range(48):
            net.cursor.execute('DELETE FROM messages_main WHERE 1')

    # add try catch for errors, and return it with code.

    # adding message to base
    net.cursor.execute("""INSERT INTO messages_main (time, name, message)""" +
                       f""" VALUES ("{data['time']}", "{data['name']}", "{data['message']}")""")
    net.database.commit()
    # returning operation state
    return 'success'


def get_base() -> list:
    return [{'time': k[0], 'name': k[1], 'message': k[2]} for k in
            net.cursor.execute('SELECT * FROM messages_main').fetchall()]


for connection in net.get_connection():
    data = connection[0].recv(500).decode('utf-8')
    if not data:
        connection[0].close()
        continue
    data = json.loads(data)
    if data['command'] == 'send':
        data = data['data']
        connection[0].send(json.dumps({'code': add_to_base(data)}).encode("utf-8"))
    elif data['command'] == 'get':
        connection[0].send(json.dumps(get_base()).encode("utf-8"))
    else:
        connection[0].send(json.dumps({'code': 'incorrect command'}).encode("utf-8"))
    connection[0].close()
