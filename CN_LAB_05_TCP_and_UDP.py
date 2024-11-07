# // TCP
# server:
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)
server_socket.listen(1)

print('TCP Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()

    print('Connection from', client_address)

    data = connection.recv(1024)
    while data:
        print('Received:', data.decode())
        data = connection.recv(1024)

    connection.close()

# TCP
# client:

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
client_socket.connect(server_address)

message = 'Hello, TCP Server!'
print('Sending:', message)
client_socket.sendall(message.encode())

client_socket.close()

# // UDP
# server:

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9090)
server_socket.bind(server_address)

print('UDP Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a message...')
    data, client_address = server_socket.recvfrom(1024)

    print('Received:', data.decode(), 'from', client_address)

# // UDP
# client:

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9090)

message = 'Hello, UDP Server!'
print('Sending:', message)
client_socket.sendto(message.encode(), server_address)

client_socket.close()
