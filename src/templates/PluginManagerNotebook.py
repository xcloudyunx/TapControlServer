import wx
import requests

from src.organisms.PluginManagerNotebookPanel import PluginManagerNotebookPanel
from src.atoms.Plugin import Plugin

class PluginManagerNotebook(wx.Notebook):
	def __init__(self, parent, plugins, onPluginFocus):
		super().__init__(
			parent=parent
		)
		
		self.plugins = plugins
		
		self.readyPluginLists()
		
		self.AddPage(PluginManagerNotebookPanel(
			parent=self,
			plugins=self.availablePluginsInfo,
			onFocus=onPluginFocus
		), "Available")
		
		self.AddPage(PluginManagerNotebookPanel(
			parent=self,
			plugins=self.updatesPluginsInfo,
			onFocus=onPluginFocus
		), "Updates")
		
		self.AddPage(PluginManagerNotebookPanel(
			parent=self,
			plugins=self.installedPluginsInfo,
			onFocus=onPluginFocus
		), "Installed")
		
	
	def readyPluginLists(self):
		self.readyAllPlugins()
		self.readyInstalledPlugins()
		
		self.availablePluginsInfo = []
		self.updatesPluginsInfo = []
		
		for ap in self.allPluginsInfo:
			for ip in self.installedPluginsInfo:
				if ap[0] == ip[0]:
					if ap[1] != ip[1]:
						self.updatesPluginsInfo.append(ap[0:2])
					break
			else:
				self.availablePluginsInfo.append(ap[0:2])
	
	def readyAllPlugins(self):
		r = requests.get("https://raw.githubusercontent.com/xcloudyunx/TapControlPlugins/main/pluginList.json")
		res = r.json()
		
		self.allPluginsInfo = []
		
		for plugin in res["plugins"]:
			self.allPluginsInfo.append([plugin["name"], plugin["version"], plugin["description"], plugin["author"], plugin["homepage"]])
				
	def readyInstalledPlugins(self):
		self.installedPluginsInfo = []
		
		for pluginName, plugin in self.plugins.items():
			self.installedPluginsInfo.append([pluginName, plugin.getVersion()])
			
	def getAllPluginsInfo(self):
		return self.allPluginsInfo
	
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