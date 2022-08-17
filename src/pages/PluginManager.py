import wx
import requests
import webbrowser

from src.templates.PluginManagerNotebook import PluginManagerNotebook
from src.atoms.Plugin import Plugin

class PluginManager(wx.Dialog):
	def __init__(self, parent, plugins):
		super().__init__(
			parent=parent,
			title="Plugin Manager"
		)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.pluginManagerNotebook = PluginManagerNotebook(
			parent=self,
			plugins=plugins,
			onPluginFocus=self.updateDescription
		)
		sizer.Add(self.pluginManagerNotebook, wx.SizerFlags(1).Expand())
		
		self.description = wx.TextCtrl(
			parent=self,
			style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL
		)
		sizer.Add(self.description, wx.SizerFlags(1).Expand())
		
		self.description.Bind(wx.EVT_TEXT_URL, self.visitURL)
	
	def updateDescription(self, evt):
		for plugin in self.allPluginsInfo:
			if plugin[0] == evt.GetItem().GetText():
				self.description.write(plugin[2]+"\r\n")
				self.description.write("Author: "+plugin[3]+"\r\n")
				self.description.write("Homepage: "+plugin[4])
				
	def visitURL(self, evt):
		# currently triggers mutiple times for some reason???
		webbrowser.open(self.description.GetValue()[evt.GetURLStart():evt.GetURLEnd()])