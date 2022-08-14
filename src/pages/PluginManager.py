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
		
		self.plugins = plugins
		self.installedPlugins = plugins.keys()
		
		self.readyPluginLists()
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.availablePluginsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.availablePlugins
		)
		self.availablePluginsCheckListBox.Show()
		sizer.Add(self.availablePluginsCheckListBox, wx.SizerFlags(1).Expand())
		
		self.updatesPlguinsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.updatesPlugins
		)
		sizer.Add(self.updatesPlguinsCheckListBox, wx.SizerFlags(1).Expand())
		
		self.installedPluginsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.installedPlugins
		)
		sizer.Add(self.installedPluginsCheckListBox, wx.SizerFlags(1).Expand())
		
	
	def readyPluginLists(self):
		self.readyAllPlugins()
		
		self.availablePlugins = []
		self.updatesPlugins = []
		
		for plugin in self.allPlugins:
			if plugin not in self.installedPlugins:
				self.availablePlugins.append(plugin)
			# else if self.plugins[plugin].version != :
				# self.updatesPlugins.append(plugin)
	
	def readyAllPlugins(self):
		# need to somehow also get version number
		r = requests.get("https://api.github.com/repos/xcloudyunx/TapControlPlugins/git/trees/main")
		res = r.json()
		
		self.allPlugins = []
		
		for file in res["tree"]:
			if file["type"] == "tree":
				self.allPlugins.append(file["path"])
	
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