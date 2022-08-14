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
		
		self.readyPluginLists()
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.availablePluginsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.availablePluginsInfo
		)
		# self.availablePluginsCheckListBox.Show()
		sizer.Add(self.availablePluginsCheckListBox, wx.SizerFlags(1).Expand())
		
		self.updatesPlguinsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.updatesPluginsInfo
		)
		# self.updatesPlguinsCheckListBox.Show()
		sizer.Add(self.updatesPlguinsCheckListBox, wx.SizerFlags(1).Expand())
		
		self.installedPluginsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.installedPluginsInfo
		)
		# self.updatesPlguinsCheckListBox.Show()
		sizer.Add(self.installedPluginsCheckListBox, wx.SizerFlags(1).Expand())
		
	
	def readyPluginLists(self):
		self.readyAllPlugins()
		self.readyInstalledPlugins()
		
		self.availablePluginsInfo = []
		self.updatesPluginsInfo = []
		
		for ap in self.allPluginsInfo:
			for ip in self.installedPluginsInfo:
				if ap[0] == ip[0]:
					if ap[1] != ip[1]:
						self.updatesPluginsInfo.append(ap)
					break
			else:
				self.availablePluginsInfo.append(ap)
	
	def readyAllPlugins(self):
		r = requests.get("https://raw.githubusercontent.com/xcloudyunx/TapControlPlugins/main/pluginList.json")
		res = r.json()
		
		self.allPluginsInfo = []
		
		for plugin in res["plugins"]:
			self.allPluginsInfo.append([plugin["name"], plugin["version"], plugin["description"], plugin["author"], plugin["homepage"]])
				
	def readyInstalledPlugins(self):
		self.installedPluginsInfo = []
		
		for pluginName, plugin in self.plugins.items():
			self.installedPluginsInfo.append([pluginName, plugin.getVersion(), plugin.getDescription(), plugin.getAuthor(), plugin.getHomepage()])
	
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