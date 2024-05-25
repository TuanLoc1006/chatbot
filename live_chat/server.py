import socket
import threading
import signal
import sys

def close_server(signum, frame):
    print('Shutting down the server...')
    srvsocket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, close_server)

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')

try:
    srvsocket.bind(('localhost', 9999))
    print('Bind to the local port')
except OSError as e:
    print(f'Error binding socket: {e}')
    sys.exit(1)

srvsocket.listen(5)
print('Started listening...')

def NewClientSocketHandler(cli, ip):
    print('The new client has socket id:', cli)
    cli.send(b'CONNECT_SUCCESSFUL')
    while True:
        print('The message got for client socket:', cli)
        try:
            message = cli.recv(256).decode()
            if not message:
                break
            print(f'Received message from {ip}: {message}')
            response = f'Server received: {message}'
            cli.send(response.encode('utf-8'))
        except ConnectionResetError:
            break
    cli.close()
    print(f'Client {ip} disconnected')

while True:
    print('Waiting for the incoming connections')
    try:
        cli, ip = srvsocket.accept()
        threading.Thread(target=NewClientSocketHandler, args=(cli, ip)).start()
    except Exception as e:
        print(f'Error accepting connections: {e}')
        break
