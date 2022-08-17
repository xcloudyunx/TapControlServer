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
		
		# idx = self.FindItem(start=-1, str="searching for this string", partial=True) for searching
		# need to trigger above for each character press and then do 
		# self.Focus(idx) to highlight item
		
		searchBar = SearchBar(
			parent=self,
			onSearch=self.handleSearch
		)
		topLayer.Add(searchBar, wx.SizerFlags().Expand())
		
		actionButton = CustomButton(
			parent=self,
			value=type,
			onClick=self.onActionButtonClick
		)
		topLayer.Add(actionButton, wx.SizerFlags().Centre())
		
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
	
	def handleSearch(self, text):
		index = self.checkListBox.FindItem(
			start=self.checkListBox.GetFocusedItem(),
			str=text,
			partial=True
		)
		if index != -1:
			self.checkListBox.Select(index)
			self.checkListBox.Focus(index)