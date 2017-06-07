from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = '781f6267c8cd38eda15fc2306216f08bc0353bbd397cd161'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9999)
