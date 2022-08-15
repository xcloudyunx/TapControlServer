import wx
import requests
import webbrowser

from src.organisms.PluginCheckListBox import PluginCheckListBox
from src.atoms.Plugin import Plugin

class PluginManager(wx.Dialog):
	def __init__(self, parent, plugins):
		super().__init__(
			parent=parent,
			title="Plugin Manager"
		)
		
		self.plugins = plugins
		
		self.readyPluginLists()
		
		self.currentTab = "available"
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.availablePluginsCheckListBox = PluginCheckListBox(
			parent=self,
			plugins=self.availablePluginsInfo,
			onFocus=self.updateDescription
		)
		self.availablePluginsCheckListBox.Show()
		sizer.Add(self.availablePluginsCheckListBox, wx.SizerFlags(1).Expand())
		
		# self.updatesPlguinsCheckListBox = PluginCheckListBox(
			# parent=self,
			# plugins=self.updatesPluginsInfo,
			# onFocus=self.updateDescription
		# )
		# self.updatesPlguinsCheckListBox.Show()
		# sizer.Add(self.updatesPlguinsCheckListBox, wx.SizerFlags(1).Expand())
		
		# self.installedPluginsCheckListBox = PluginCheckListBox(
			# parent=self,
			# plugins=self.installedPluginsInfo,
			# onFocus=self.updateDescription
		# )
		# self.installedPluginsCheckListBox.Show()
		# sizer.Add(self.installedPluginsCheckListBox, wx.SizerFlags(1).Expand())
		
		self.description = wx.TextCtrl(
			parent=self,
			style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL
		)
		sizer.Add(self.description, wx.SizerFlags(1).Expand())
		
		self.description.Bind(wx.EVT_TEXT_URL, self.visitURL)
		
	
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
	
	def updateDescription(self, evt):
		for plugin in self.allPluginsInfo:
			if plugin[0] == evt.GetItem().GetText():
				self.description.write(plugin[2]+"\r\n")
				self.description.write("Author: "+plugin[3]+"\r\n")
				self.description.write("Homepage: "+plugin[4])
				
	def visitURL(self, evt):
		# currently triggers mutiple times for some reason???
		webbrowser.open(self.description.GetValue()[evt.GetURLStart():evt.GetURLEnd()])
	
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