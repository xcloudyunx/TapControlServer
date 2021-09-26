import subprocess
import json

class Plugin():
	def __init__(self, file):
		# remove the python when compiling as it will be exe
		process = subprocess.Popen(["python", "./plugins/"+file, "--setup"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		outSplit = out.decode().splitlines()
		
		self.name = outSplit[0]
		self.properties = json.loads(outSplit[1])
		
	def getName(self):
		return self.name
		
	def getProperties(self):
		return self.properties
	
	def getPropertyType(self, property):
		return self.properties[property][0]
		
	def getPropertySettings(self, property):
		return self.properties[property][1]