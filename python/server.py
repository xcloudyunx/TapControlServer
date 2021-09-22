import threading
import socket
import json
import hashlib

from config import constants

class Server(threading.Thread):
	def __init__(self):
		super().__init__(daemon=True)
		
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(constants.ADDRESS)
		self.server.listen(1)
		
	def run(self):
		while True:
			self.conn = None
			print("RESET")
			self.conn, address = self.server.accept()
			c = True
			print("accepted")
			
			self.checkSync()

			while c:
				data = self.receiveMessage()
				print(data)
				
	def checkSync(self):
		with open("assets/state.json", "r") as file:
			self.state = json.loads(file.read())
		self.sendMessage('{"hash":"'+self.hash(self.state)+'"}')
		synced = bool(self.receiveMessage())
		if not synced:
			handleSyncGrid(self.state)
				
	def handleSyncGrid(self, state):
		self.state = state
		if self.conn:
			self.sendMessage(json.dumps(self.state))
		
	def handleSyncImage(self):
		if self.conn:
			# sync the image
			pass
		else:
			# add to sync file
			pass
		
	def receiveMessage(self):
		return self.conn.recv(constants.MSGSIZE).decode()
		
	def sendMessage(self, msg):
		self.conn.send(msg.encode())
	
	def hash(self, obj):
		return hashlib.sha256(json.dumps(obj).encode()).hexdigest()