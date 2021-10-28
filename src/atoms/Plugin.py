import subprocess
import json

class Plugin():
	def __init__(self, file):
		self.file = file
		
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
		return self.properties[property]["type"]
		
	def isPropertyRequired(self, property):
		return self.properties[property]["required"]
		
	def getPropertySettings(self, property):
		return self.properties[property]["settings"]
		
	def run(self, properties):
		# use os.system("whatever")
		# can keep this for now for debugging
		process = subprocess.Popen(["python", "./plugins/"+self.file]+[element for propvalue in [[prop, properties[prop]] for prop in properties] for element in propvalue], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		print(out.decode())