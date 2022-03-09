# Realtime Chat - Dikembangkan menggunakan SocketIO + Flask

## Demo Realtime Chat
Lihat Demo pada link berikut ini : https://lumintu-chatapp.herokuapp.com/

<br>

## Syarat Menjalankan Project

- Pastikan telah menginstall **git** pada perangkat anda. periksa dengan mengetik di teriminal/command prompt "*git --version*"
- Pastikan telah menginstall **python** pada perangkat anda. periksa dengan mengetik di teriminal/command prompt "*python -V*"
- Pastikan telah menginstall package manager **pip** pada perangkat anda. periksa dengan mengetik di teriminal/command prompt "*pip -V*"

## Panduan Menjalan Project

*Buka Terminal/Command Prompt pada komputer anda dan ketik*
<br>

- Clone Repository ini :

  ```
    $ git clone https://github.com/antheiz/flask-chatapp.git
  ```

- Masuk ke directory Project
  ```
    $ cd flask-chatapp
  ```

- Buat environment & Install package yang dibutuhkan

  ```
    $ pip install pipenv
    $ pipenv install -r requirements.txt
  ```

- Aktivasi/Masuk ke environments:

  ```
    $ pipenv shell
  ```

- Jalankan Project

  ```
    $ gunicorn --worker-class eventlet -w 1 run:app
  ```
