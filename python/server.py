import socket

import constants
	
def startServer():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(constants.ADDRESS)
	server.listen(1)
	
	while True:
		conn = None
		print("RESET")
		conn, address = server.accept()
		c = True
		print("accepted")

		while c:
			data = self.conn.recv(constants.MSGSIZE)
			print(data)