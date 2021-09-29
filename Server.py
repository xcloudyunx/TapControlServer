import threading
import socket
import json
import hashlib

from config import constants

class Server(threading.Thread):
	def __init__(self, plugins):
		super().__init__(daemon=True)
		
		self.plugins = plugins
		with open("config/commands.json", "r") as file:
			self.commands = json.loads(file.read())
			
		with open("config/state.json", "r") as file:
			self.state = json.loads(file.read())
		
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
			
			# self.checkSync()

			while c:
				data = self.receiveMessage()
				thread = threading.Thread(target=self.handleData, args=(data,))
				
	def checkSync(self):
		self.sendMessage('{"hash":"'+self.hash(self.state)+'"}')
		synced = bool(self.receiveMessage())
		if not synced:
			handleSyncGrid(self.state)
			
	def handleSync(self):
		# sync
		pass
				
	def syncGrid(self, state):
		self.state = state
		if self.conn:
			self.sendMessage(json.dumps(self.state))
		
	def syncImage(self):
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
		
	def handleData(self, data):
		print(data)
		splitData = data.split()
		page = splitData[0]
		id = splitData[1]
		self.run(page, id)
		
	def run(self, page, id):
		if id in self.commands[page]:
			self.plugins.run(self.commands[page][id])