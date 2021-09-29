import sys
import json

__name = "template"
__properties = {
	# reserved property names
	# page
	# id
	# name
	# image
	"property1":[
		"choice",
		["option1", "option2"]
	],
	"property2":[
		"file",
		"(*.png)|*.png"
		# "filetypename (*.extension1,*.extension2,...)|*.extension1;*.extension2;..."
	]
}
# user typing???
# recording macro????

def getName():
	return __name
	
def getProperties():
	return json.dumps(__properties)

for i in range(1, len(sys.argv)):
	if sys.argv[i] == "--setup":
		print(getName())
		print(getProperties())
	else:
		