import wx
import requests

from src.atoms.Plugin import Plugin

class PluginManager(wx.MultiChoiceDialog):
	def __init__(self, parent, plugins):
		super().__init__(
			parent=parent,
			caption="Plugin Manager",
			message="Select the plugins you want",
			choices=self.getAllPlugins()
		)
		
		self.installedPlugins = plugins
		
		# need to keep track of what plugins are already installed for setselections
		# probably need to linear search?
		# change to available, updates, installed?
		# need to show description of plugin when selected
		self.SetSelections(self.getInstalledPlugins())
	
	def getAllPlugins(self):
		r = requests.get("https://api.github.com/repos/xcloudyunx/TapControlPlugins/git/trees/main")
		res = r.json()
		
		self.allPlugins = []
		
		for file in res["tree"]:
			if file["type"] == "tree":
				self.allPlugins.append(file["path"])
			
		return self.allPlugins
	
	def getInstalledPlugins(self):
		self.selectedPlugins = []
		for plugin in self.installedPlugins:
			for i in range(len(self.allPlugins)):
				if plugin == self.allPlugins[i]:
					self.selectedPlugins.append(i)
					break
		return self.selectedPlugins
	
	def downloadPlugin(self, pluginName):
		r = requests.get("https://raw.githubusercontent.com/xcloudyunx/TapControlPlugins/main/"+pluginName+"/plugin.py")
		#r.content gives bytes, r.text gives string
		with open("plugins/"+pluginName+".py", "wb") as file:
			file.write(r.content)
		# need to update plugins list
		plugin = Plugin(pluginName+".py")
		self.installedPlugins[plugin.getName()] = plugin
	
	def downloadPlugins(self):
		for i in self.GetSelections():
			if i not in self.selectedPlugins:
				self.downloadPlugin(self.allPlugins[i])