from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:8080'])

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('A user connected')

@socketio.on('disconnect')
def on_disconnect():
    print('A user disconnected')

@socketio.on('send message')
def on_send_message(message):
    print(f'Received message: {message}')

    # Send message back to the client that initiated the event
    print(request.sid)
    emit('new message', message+"!")
    # send('new message', message+"!", room=request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)
