import wx
import requests

class PluginManager(wx.MultiChoiceDialog):
	def __init__(self, parent):
		super().__init__(
			parent=parent,
			caption="Plugin Manager",
			message="Select the plugins you want",
			choices=self.getPlugins()
		)
		
		# need to keep track of what plugins are already installed for setselections
		# probably need to linear search?
		# self.SetSelections([1])
		
		self.ShowModal()
	
	def getPlugins(self):
		r = requests.get("https://api.github.com/repos/xcloudyunx/TapControlPlugins/git/trees/main")
		res = r.json()
		
		plugins = []
		
		for file in res["tree"]:
			if file["type"] == "tree":
				plugins.append(file["path"])
			
		return plugins