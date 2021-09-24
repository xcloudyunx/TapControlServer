import sys

__name = "template"
__properties = {}

def getName():
	return __name
	
def getProperties():
	return __properties

for i in range(1, len(sys.argv)):
	if sys.argv[i] == "--setup":
		print(getName())
		print(getProperties())