import wx
import requests

from src.organisms.PluginCheckListBox import PluginCheckListBox
from src.atoms.Plugin import Plugin

# change self to be a normal dialog
# have three different panels, one for available, one for updates, one for installed
# can probably reuse code for each of the above panels - one template, use arg to see which i need
# template will contain header to see which tab, search functionality, CheckListBox, description
# figure out how to add an extra column to the checklistbox to display version
# add a select all functionality?

class PluginManager(wx.Dialog):
	def __init__(self, parent, plugins):
		super().__init__(
			parent=parent,
			title="Plugin Manager"
		)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.availablePlugins = PluginCheckListBox(
			parent=self,
			plugins=self.getAllPlugins()
		)
		sizer.Add(self.availablePlugins, wx.SizerFlags(1).Expand().ReserveSpaceEvenIfHidden())
		
		# self.updatesPlguins = PluginCheckListBox(
			# parent=self,
			# plugins=self.getAllPlugins()
		# )
		# sizer.Add(self.updatesPlguins, wx.SizerFlags(1).Expand().ReserveSpaceEvenIfHidden())
		
		# self.installedPlugins = PluginCheckListBox(
			# parent=self,
			# plugins=self.getInstalledPlugins()
		# )
		# sizer.Add(self.installedPlugins, wx.SizerFlags(1).Expand().ReserveSpaceEvenIfHidden())
		
		# self.installedPlugins = plugins
		
		# self.SetSelections(self.getInstalledPlugins())
	
	def getAllPlugins(self):
		r = requests.get("https://api.github.com/repos/xcloudyunx/TapControlPlugins/git/trees/main")
		res = r.json()
		
		self.allPlugins = []
		
		for file in res["tree"]:
			if file["type"] == "tree":
				self.allPlugins.append(file["path"])
			
		return self.allPlugins
		
	def getAvailablePlugins(self):
		return []
	
	def getUpdatesPlugins(self):
		return []
	
	def getInstalledPlugins(self):
		self.selectedPlugins = []
		for plugin in self.installedPlugins:
			for i in range(len(self.allPlugins)):
				if plugin == self.allPlugins[i]:
					self.selectedPlugins.append(i)
					break
		return self.selectedPlugins
	
	# def downloadPlugin(self, pluginName):
		# r = requests.get("https://raw.githubusercontent.com/xcloudyunx/TapControlPlugins/main/"+pluginName+"/plugin.py")
		# r.content gives bytes, r.text gives string
		# with open("plugins/"+pluginName+".py", "wb") as file:
			# file.write(r.content)
		# need to update plugins list
		# plugin = Plugin(pluginName+".py")
		# self.installedPlugins[plugin.getName()] = plugin
	
	# def downloadPlugins(self):
		# for i in self.GetSelections():
			# if i not in self.selectedPlugins:
				# self.downloadPlugin(self.allPlugins[i])