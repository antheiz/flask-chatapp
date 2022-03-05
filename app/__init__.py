from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rahasia'
app.config['SESSION_TYPE'] = 'filesystem'
socketio = SocketIO(app, manage_session=False)

from app import routes