#Exercise 12.1 Change the socket program socket1.py to prompt the user for the
#URL so it can read any web page. You can use split(/) to break the URL into
#its component parts so you can extract the host name for the socket connect call.
#Add error checking using try and except to handle the condition where the user
#enters an improperly formatted or non-existent URL.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

website = raw_input("Enter URL: ")

url = website.split('/')

try:
    main = url[2]
    mysock.connect((main, 80))
    print "adf"
    mysock.send('GET website HTTP/1.0\n\n')
    print "here"
except:
    print "Error bad address"
    exit()

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data

mysock.close()
