# Client TCP

import socket

target_host = 'localhost'
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(bytes('Teste envio socket', "utf-8"))
response = client.recv(4096)
response = response.decode("utf-8")
print(f'Response: {response}')
