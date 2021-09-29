import threading
import socket
import json
import hashlib

from config import constants

class Server(threading.Thread):
	def __init__(self, plugins):
		super().__init__(daemon=True)
		
		self.lock = threading.Lock()
		
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
				
	# def checkSync(self):
		# self.sendMessage('{"hash":"'+self.hash(self.state)+'"}')
		# synced = bool(self.receiveMessage())
		# if not synced:
			# handleSyncGrid(self.state)
			
	def handleSync(self):
		if self.conn:
			with self.lock:
				self.syncGrid()
				with open("config/updates.json") as file:
					data = json.loads(file.read())
				for image in data:
					self.syncImage(image if data[image] else None)
			return True
		else:
			return False
				
	def syncGrid(self):
		self.sendMessage(json.dumps(self.state))
		
	def syncImage(self, fileName):
		with open("assets/"+fileName+".png", "rb") as file:
			data = {fileName:file.read()}
		self.sendMessage(json.dumps(data))
		
	def receiveMessage(self):
		return self.conn.recv(constants.MSGSIZE).decode()
		
	def sendMessage(self, msg):
		self.conn.send(msg.encode())
	
	def hash(self, obj):
		return hashlib.sha256(json.dumps(obj).encode()).hexdigest()
		
	def handleData(self, data):
		print(data)
		self.execute(data)
		
	def execute(self, id):
		if id in self.commands:
			self.plugins.run(self.commands[id])