import threading
import socket
import json
import hashlib
import base64
import time
import os

from config import constants

class Server(threading.Thread):
	def __init__(self, plugins):
		super().__init__(daemon=True)
		
		self.lock = threading.Lock()
		
		self.readBuffer = ""
		
		self.plugins = plugins
		with open("settings/commands.json", "r") as file:
			self.commands = json.loads(file.read())
			
		with open("settings/state.json", "r") as file:
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
			
			self.checkSync()
			
			try:
				while c:
					data = self.receiveMessage()
					if not data:
						break
					thread = threading.Thread(target=self.handleData, args=(data,))
					thread.start()
			except:
				continue
				
	def checkSync(self):
		data = {"lastUpdateTime":self.state["lastUpdate"]}
		self.sendMessage(json.dumps(data))
		synced = bool(int(self.receiveMessage()))
		if synced:
			self.syncUpdated()
		else:
			self.syncAll()
			
	# def handleSync(self, syncDialogBox):
	def syncUpdated(self):
		self.handleSyncState()
		with self.lock:
			if self.conn:
				with open("settings/updates.json", "r") as file:
					data = json.loads(file.read())["updates"]
				for image in data:
					self.syncImage(image)
				with open("settings/updates.json", "w") as file:
					file.write(json.dumps({"updates":[]}))
	
	def syncAll(self, syncDialogBox=None):
		self.handleSyncState()
		with self.lock:
			if self.conn:
				if syncDialogBox:
					percentageGain = 100/(self.state["numOfPages"]*self.state["numOfRows"]*self.state["numOfCols"]+1)
					currentPercent = percentageGain
					syncDialogBox.Update(currentPercent, "Syncing grid...")
					currentPercent += percentageGain
				for p in range(1, self.state["numOfPages"]+1):
					for r in range(self.state["numOfRows"]):
						for c in range(self.state["numOfCols"]):
							id = str(p)+"-"+str(r)+"-"+str(c)
							self.syncImage(id)
							if syncDialogBox:
								syncDialogBox.Update(currentPercent, "Syncing icons..." if currentPercent<100 else "Syncing complete")
								currentPercent += percentageGain
				with open("settings/updates.json", "w") as file:
					file.write(json.dumps({"updates":[]}))
				return True
			else:
				return False
			
	def handleSyncState(self):
		self.state["lastUpdate"] = time.time()
		with open("settings/state.json", "w") as file:
			file.write(json.dumps(self.state))
		with self.lock:
			if self.conn:
				self.syncState()
	
	def syncState(self):
		data = {"state":self.state}
		self.sendMessage(json.dumps(data))
		
	def handleSyncImage(self, id):
		self.handleSyncState()
		with self.lock:
			if self.conn:
				self.syncImage(id)
			else:
				with open("settings/updates.json", "r") as file:
					data = json.loads(file.read())
				data["updates"].append(id)
				with open("settings/updates.json", "w") as file:
					file.write(json.dumps(data))
		
	def syncImage(self, id):
		data = {"imageName":id}
		if os.path.exists("assets/"+id+".png"):
			with open("assets/"+id+".png", "rb") as file:
				data["imageData"] = base64.b64encode(file.read()).decode()
		else:
			data["imageData"] = None
		self.sendMessage(json.dumps(data))
		
	def receiveMessage(self):
		return self.conn.recv(constants.MSGSIZE).decode()
		
	def sendMessage(self, msg):
		self.conn.send((msg+constants.EOF).encode())
	
	def hash(self, obj):
		return hashlib.sha256(json.dumps(obj).encode()).hexdigest()
		
	def handleData(self, data):
		print(data)
		self.execute(data)
		
	def execute(self, id):
		if id in self.commands:
			command = self.commands[id]
			self.plugins[command[0]].run(command[1])