import socket

rowMax = 10
colMax = 5
pageMax = 10
IP = socket.gethostbyname(socket.gethostname())
PORT = 5321
MSGSIZE = 4096
ADDRESS = (IP, PORT)