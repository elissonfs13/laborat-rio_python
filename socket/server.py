# Server TCP

import socket
import threading

bind_ip = 'localhost'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print(f'Listening on {bind_ip}:{bind_port}')


def handle_client(client_socket):
    request = client_socket.recv(1024)
    request = request.decode("utf-8")
    print(f'Received: {request}')
    client_socket.send(bytes('ACK!', "utf-8"))
    client_socket.close()


while True:
    client, addr = server.accept()
    print(f'Accepted connection from: {addr[0]}:{addr[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
