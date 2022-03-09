from argparse import Namespace
from crypt import methods
import time
from app import app, socketio
from flask import render_template, request, redirect, url_for, session
from flask_socketio import emit, join_room, leave_room


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET','POST'])
def chat():
    if(request.method == 'POST'):
        username = request.form['username']
        room = request.form['room']
        # Store data in session
        session['username'] = username
        session['room'] = room
        return render_template('chat.html', session=session)
    else:
        if(session.get('username') is not None):
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for('index'))

@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    username = session.get('username')
    join_room(room)
    emit('status', {'msg': str(username) + ': bergabung ke room'}, room=room)


@socketio.on('messages', namespace='/chat')
def messages(message):
    room = session.get('room')
    username = session.get('username')
    emit('message', {'msg': str(username) + ' : ' + message['msg']}, room=room)


@socketio.on('leave', namespace='/chat')
def leave(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': str(username) + ': keluar dari room'}, room=room)

