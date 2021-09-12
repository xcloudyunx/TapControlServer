import threading
import socket

import constants

class Server(threading.Thread):
	def __init__(self):
		super().__init__(daemon=True)
		
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(constants.ADDRESS)
		self.server.listen(1)
		
	def run(self):
		while True:
			conn = None
			print("RESET")
			conn, address = self.server.accept()
			c = True
			print("accepted")

			while c:
				data = conn.recv(constants.MSGSIZE)
				print(data)
				
	def handleSync(self):
		print("syncing")