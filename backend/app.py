import time
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
# from xo import *
from xo.redis import xoRedis
# import eventlet
# from eventlet import wsgi
# eventlet.monkey_patch()

redis = xoRedis()
port = 5000
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:8080'],async_mode='threading')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    redis.lastSession = request.sid
    print('A user connected', redis.lastSession)

@socketio.on('disconnect')
def on_disconnect():
    print('A user disconnected', request.sid)

@socketio.on('user_msg')
def on_send_message(message):
    print(f'Received message: {message}')

    # Send message back to the client that initiated the event
    # redis.sessions[request.sid].message = message
    print(":::",request.__dir__)
    # emit('server_update', {"data":message+"!","message":message+"@@"}, room = request.sid)
    emit('server_update', {"data":{"_value":message+"@","extra":{"_value":"inner_data","meta":{}}},"message":str(message)+"!"}, room = request.sid)
    print(":::",request.sid)
    # print(xo)
    # redis.lastSession = request.sid

    # send('server_update', message+"!", room=request.sid)

# redis.trigger.on = "off"

# @socketio.on('disconnect')
def manual(*v,**kw):
    print("!!!!!!!!!!!!!!",v, kw)
    redis.trigger.on.value
    print("starting manual", str(redis.tigger.on.value), str(redis.tigger.on) == "on")
    if str(redis.tigger.on.value) == "on":
        print("Running manual",v, kw)
        emit('server_update', {"data":v}, to = redis.lastSession.value)
        print("done emmiting to", redis.lastSession.value )
    else:
        print("....",redis.trigger.on.value, type(redis.trigger.on.value), redis.trigger.on.value == "on")
        if redis.trigger.on.value == "on":
            print("YYYYYY")
            print("Running manual",v, kw)
            room = redis.lastSession.value
            print("xxxxxxxxxxxxxxxxxxxx trying  emmiting to", room , redis.lastSession.value )
            # socketio.emit('server_update', {"data":"aaaaaa"}, room = room)
            
            if True:
                # socketio.emit('server_update', {"data":v[0],"message":str(v[0])+"@@"}, to = room)
                socketio.emit('server_update', {"data":{"_value":v[0],"extra":{"_value":"inner_data","meta":{}}},"message":str(v[0])}, to = room)
                # socketio.emit('server_update', {"data":{"_value":message+"@","extra":{"_value":"inner_data","meta":{}}},"message":str(message)+"@@"}, room = request.sid)

            else:
                c = 0
                while(c<100):
                    socketio.emit('server_update', {"data":f"{v[0]} {c}"}, to = room)
                    time.sleep(redis.settings.delay.value)
                    c+=1
                    print("c....",c)
            # socketio.send('server_update', {"data":"cccccccccc"}, to = room)
            # socketio.call('server_update', {"data":"xxxxxxxxxxxx"}, room = room, namespace='/test')
            # socketio.send({"data":"ooooooo"},json = True, =room)
            print("done emmiting to", redis.lastSession.value )
        else:
            print("XXXXXXXXXX")

redis.trigger @= lambda *v, **kw : manual(*v,**kw)



if __name__ == '__main__':
    socketio.run(app, debug=True)
    # wsgi.server(eventlet.listen(('0.0.0.0', port)), app)
