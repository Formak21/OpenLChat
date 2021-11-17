import welcome
import net
import json
import datetime


# data format - {'name': 'max 16 bytes', 'message': 'max 256 bytes'}
def add_to_base(data) -> str:
    # checking data format
    if sum([int(data[i] != '') for i in data.keys()]) != 2:
        return 'data_err'
    if not (len(bytearray(data['name'], encoding='utf-8')) <= 16 and len(
            bytearray(data['message'], encoding='utf-8')) <= 256):
        return 'len_err'
    # checking size of db
    if len(net.cursor.execute('SELECT * FROM messages_main').fetchall()) >= 64:
        for k in range(48):
            net.cursor.execute('DELETE FROM messages_main WHERE 1')

    # add try catch for errors, and return it with code.

    # adding message to base
    net.cursor.execute("""INSERT INTO messages_main (time, name, message)""" +
                       f""" VALUES ("{datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}", """ +
                       f""""{data['name']}", "{data['message']}")""")
    net.database.commit()
    # returning operation state
    return 'success'


def get_base() -> list:
    return [{'name': k[1], 'message': k[2]} for k in
            net.cursor.execute('SELECT * FROM messages_main').fetchall()]


for connection in net.get_connection():
    data = connection[0].recv(500).decode('utf-8')
    if not data:
        connection[0].close()
        continue
    data = json.loads(data)
    print('LOG:', data)
    if data['command'] == 'send':
        data = data['data']
        answer = {'code': add_to_base(data)}
        print('LOG:', answer)
        connection[0].send(json.dumps(answer).encode("utf-8"))
    elif data['command'] == 'get':
        print('LOG:', 'base sent')
        connection[0].send(json.dumps(get_base()).encode("utf-8"))
    elif data['command'] == 'test':
        answer = {'code': 'we are stable, ver:' + welcome.VERSION}
        print('LOG:', answer)
        connection[0].send(json.dumps(answer).encode("utf-8"))
    else:
        connection[0].send(json.dumps({'code': 'incorrect command'}).encode("utf-8"))
    connection[0].close()
