## Flask - ChatApp implement with SocketIO

This is example code for implement SocketIO with Flask-SocketIO

## 🚀 Quickstart

**Requirements**

- Make sure you has been install **git**, **pip**, and **python** in your device

**Project setup**

- Clone this Project

    ```sh
    git clone https://github.com/antheiz/flask-chatapp.git
    cd flask-chatapp/
    ```
    
- Create and activated development environment
  
  ```sh
  pip install pipenv
  pipenv install -r requirements.txt
  pipenv shell
  ```

**Run Project**

  ```
    gunicorn --worker-class eventlet -w 1 run:app
  ```

## License
Licensed under [MIT](LICENSE)
