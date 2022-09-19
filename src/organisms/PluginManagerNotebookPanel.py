import wx

from src.molecules.PluginCheckListBox import PluginCheckListBox
from src.molecules.SearchBar import SearchBar
from src.atoms.CustomButton import CustomButton

class PluginManagerNotebookPanel(wx.Panel):
	def __init__(self, parent, type, plugins, onPluginFocus, handleActionButtonClick):
		super().__init__(
			parent=parent
		)
		
		self.type = type
		self.handleActionButtonClick = handleActionButtonClick
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		topLayer = wx.BoxSizer()
		sizer.Add(topLayer, wx.SizerFlags(1).Expand())
		
		topLayer.Add(0, 0, 1)
		
		searchBar = SearchBar(
			parent=self,
			handleSearch=self.handleSearch
		)
		topLayer.Add(searchBar, wx.SizerFlags(1).Expand())
		
		topLayer.Add(0, 0, 3)
		
		actionButton = CustomButton(
			parent=self,
			value=type,
			onClick=self.onActionButtonClick
		)
		topLayer.Add(actionButton, wx.SizerFlags(1).Centre())
		
		topLayer.Add(0, 0, 1)
		
		self.checkListBox = PluginCheckListBox(
			parent=self,
			plugins=plugins,
			onPluginFocus=onPluginFocus
		)
		sizer.Add(self.checkListBox, wx.SizerFlags(4).Expand())
	
	def onActionButtonClick(self, evt):
		item = self.checkListBox.GetNextItem(-1)
		while item != -1:
			if self.checkListBox.IsItemChecked(item):
				self.handleActionButtonClick(item)
				self.checkListBox.DeleteItem(item)
				item -= 1
			item = self.checkListBox.GetNextItem(item)
	
	def addPluginToList(self, pluginInfo):
		self.checkListBox.Append(pluginInfo)
		
	def removePluginFromList(self, pluginName):
		item = self.checkListBox.GetNextItem(-1)
		while item != -1:
			if self.checkListBox.GetItem(item).GetText() == pluginName:
				self.checkListBox.DeleteItem(item)
				break
			item = self.checkListBox.GetNextItem(item)
	
	def handleSearch(self, text):
		index = self.checkListBox.FindItem(
			start=self.checkListBox.GetFocusedItem(),
			str=text,
			partial=True
		)
		if index != -1:
			self.checkListBox.Select(index)
			self.checkListBox.Focus(index)