# UDP
# client code:
import socket

def send_file(file_path, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            s.sendto(data, (host, port))
            data = file.read(1024)

    print(file_path," sent successfully")
    s.close()

receiver_host = socket.gethostname()
receiver_port = 1255
ch=input("1.Script 2.Audio 3.Video  :")
if ch==1:
    send_file("script.txt", receiver_host, receiver_port)
if ch==2:
    send_file("audio.mp3", receiver_host, receiver_port)
if ch==3:
    send_file("video.ts", receiver_host, receiver_port)


# server code:

import socket

def receive_file(file_path, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((socket.gethostname(), port))

    with open(file_path, 'wb') as file:
        data, _ = s.recvfrom(1024)
        while data:
            file.write(data)
            data, _ = s.recvfrom(1024)
            print(data)

    print(file_path," received successfully")
    s.close()

receiver_port = 1255

receive_file("received_script_last.txt", receiver_port) #if ch==1 in client chi file tr
# receive_file("received_audio_last.mp3", receiver_port)#if ch==2 in client chi file tr
#receive_file("received_video_last.ts", receiver_port)#if ch==3 in client chi file tr