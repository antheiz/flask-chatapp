from distutils.log import debug
from app import app, socketio


if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, debug=True, host='0.0.0.0')