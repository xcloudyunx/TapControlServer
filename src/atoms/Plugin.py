import subprocess
import json

class Plugin():
	def __init__(self, file):
		self.file = file
		
		# remove the python when compiling as it will be exe
		process = subprocess.Popen(["python", "./plugins/"+file, "--name"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		self.name = out.decode().strip()
		
		process = subprocess.Popen(["python", "./plugins/"+file, "--properties"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		self.properties = json.loads(out.decode().strip())
		
	def getName(self):
		return self.name
	
	def getVersion(self):
		process = subprocess.Popen(["python", "./plugins/"+file, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		version = out.decode().strip()
		return version
		
	def getDescription(self):
		process = subprocess.Popen(["python", "./plugins/"+file, "--description"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		description = out.decode()
		return description
		
	def getAuthor(self):
		process = subprocess.Popen(["python", "./plugins/"+file, "--author"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		author = out.decode().strip()
		return author
	
	def getHomepage(self):
		process = subprocess.Popen(["python", "./plugins/"+file, "--homepage"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		homepage = out.decode().strip()
		return homepage
		
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