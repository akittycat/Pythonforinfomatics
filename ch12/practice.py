import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET  https://www.youtube.com/watch?v=PJlAnR3asGQ HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print data
mysock.close()