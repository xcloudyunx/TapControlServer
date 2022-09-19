import wx
import requests
import os

from src.organisms.PluginManagerNotebookPanel import PluginManagerNotebookPanel
from src.atoms.Plugin import Plugin

class PluginManagerNotebook(wx.Notebook):
	def __init__(self, parent, plugins, onPluginFocus):
		super().__init__(
			parent=parent
		)
		
		self.plugins = plugins
		
		self.readyPluginLists()
		
		self.availablePage = PluginManagerNotebookPanel(
			parent=self,
			type="Install",
			plugins=self.availablePluginsInfo,
			onPluginFocus=onPluginFocus,
			handleActionButtonClick=self.installPlugin
		)
		self.AddPage(self.availablePage, "Available")
		
		self.updatesPage = PluginManagerNotebookPanel(
			parent=self,
			type="Update",
			plugins=self.updatesPluginsInfo,
			onPluginFocus=onPluginFocus,
			handleActionButtonClick=self.updatePlugin
		)
		self.AddPage(self.updatesPage, "Updates")
		
		self.installedPage = PluginManagerNotebookPanel(
			parent=self,
			type="Remove",
			plugins=self.installedPluginsInfo,
			onPluginFocus=onPluginFocus,
			handleActionButtonClick=self.removePlugin
		)
		self.AddPage(self.installedPage, "Installed")
		
	
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
		r = requests.get("https://raw.githubusercontent.com/xcloudyunx/TapControlPlugins/main/pluginList.json", headers={"Cache-Control": "no-store"})
		res = r.json()
		
		self.allPluginsInfo = []
		
		for plugin in res["plugins"]:
			self.allPluginsInfo.append([plugin["name"], plugin["version"], plugin["description"], plugin["author"], plugin["homepage"], plugin["file"]])
				
	def readyInstalledPlugins(self):
		self.installedPluginsInfo = []
		
		for pluginName, plugin in self.plugins.items():
			self.installedPluginsInfo.append([pluginName, plugin.getVersion()])
			
	def getPlugin(self, pluginName):
		for plugin in self.allPluginsInfo:
			if (plugin[0] == pluginName):
				return plugin
	
	def downloadPlugin(self, pluginInfo):
		r = requests.get(pluginInfo[5], headers={"Cache-Control": "no-store"})
		# r.content gives bytes, r.text gives string
		with open("plugins/"+pluginInfo[0]+".py", "wb") as file:
			file.write(r.content)
		# need to update plugins list
		plugin = Plugin(pluginInfo[0]+".py")
		self.plugins[pluginInfo[0]] = plugin
		
		# need to update installedPlugins tab
		self.installedPluginsInfo.append(pluginInfo[0:2])
		self.installedPage.addPluginToList(pluginInfo[0:2])
	
	def installPlugin(self, index):
		self.downloadPlugin(self.getPlugin(self.availablePluginsInfo.pop(index)[0]))
			
	def updatePlugin(self, index):
		pluginName = self.updatesPluginsInfo.pop(index)[0]
		for plugin in self.installedPluginsInfo:
			if plugin[0] == pluginName:
				self.installedPluginsInfo.remove(plugin)
				break
		self.installedPage.removePluginFromList(pluginName)
		self.downloadPlugin(self.getPlugin(pluginName))
			
	def removePlugin(self, index):
		pluginInfo = self.installedPluginsInfo.pop(index)
		self.plugins.pop(pluginInfo[0])
		os.remove("plugins/"+pluginInfo[0]+".py")
		
		# need to update availablePlugins tab
		self.availablePluginsInfo.append(pluginInfo)
		self.availablePage.addPluginToList(pluginInfo)
		