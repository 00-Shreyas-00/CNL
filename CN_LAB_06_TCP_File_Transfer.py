# client :

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1255
s.connect((host,port))

msg=input("Enter a message :")
s.send(msg.encode())
print("message sent !!")

with open('sample.txt','rb') as file:
    data=file.read(1024)
    while data:
        s.send(data)
        data=file.read(1024)
print("file sent successfully")
s.close()

# server :

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1255
s.bind((host,port))
s.listen(1)
print("Server is listening....")

client_socket,client_address=s.accept()
print("connected with",client_address)
msg=client_socket.recv(1024).decode()
print("Received message :",msg)

with open("received_file.txt",'wb') as file:
    data=client_socket.recv(1024)
    while data:
        file.write(data)
        data = client_socket.recv(1024)
print("file aagayi hai")
s.close()