import threading
import socket
import json
import hashlib

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
			self.conn, address = self.server.accept()
			c = True
			print("accepted")
			
			self.handleSync()

			while c:
				data = self.receiveMessage()
				print(data)
				
	def handleSync(self):
		print("syncing")
		with open("assets/state.json", "r") as file:
			self.state = json.loads(file.read())
		print(self.hash(self.state))
		self.sendMessage('{"hash":"'+self.hash(self.state)+'"}')
		print("syncing complete")
		
	def receiveMessage(self):
		return self.conn.recv(constants.MSGSIZE).decode()
		
	def sendMessage(self, msg):
		self.conn.send(msg.encode())
	
	def hash(self, obj):
		return hashlib.sha256(json.dumps(obj).encode()).hexdigest()