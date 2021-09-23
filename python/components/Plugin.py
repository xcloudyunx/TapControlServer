import subprocess
import os

class Plugin():
	def __init__(self, file):
		# remove the python when compiling as it will be exe
		process = subprocess.Popen(["python", "./plugins/"+file, "--setup"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		outSplit = out.split()
		
		self.name = outSplit[0]
		self.properties = outSplit[1:]
		
	def getName(self):
		return self.name
		
	def getProperties(self):
		return self.properties
			