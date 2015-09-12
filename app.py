async_mode = 'threading'

if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None

roll = 28
pitch = 10
yaw = 39


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(1)
        count += 1
        socketio.emit('my response',
                      {'roll': roll + count,
                       'pitch': pitch + count,
                       'yaw': yaw + count},
                      namespace='/test')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')


@socketio.on('disconnect request', namespace='/test')
def disconnect_request():
    emit('my response',
         {'roll': '(sin dato)',
          'pitch': '(sin dato)',
          'yaw': '(sin dato)'})
    disconnect()


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response',
         {'roll': roll,
          'pitch': pitch,
          'yaw': yaw})


if __name__ == '__main__':
    socketio.run(app)
