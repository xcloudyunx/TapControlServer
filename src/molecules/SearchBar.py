import wx

from src.atoms.CustomButton import CustomButton

class SearchBar(wx.Panel):
	def __init__(self, parent, handleSearch):
		super().__init__(
			parent=parent,
		)
		
		self.handleSearch = handleSearch
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		searchLabel = wx.StaticText(
			parent=self,
			label="Search: "
		)
		sizer.Add(searchLabel, wx.SizerFlags().Centre())
		self.searchBox = wx.TextCtrl(
			parent=self,
			style=wx.TE_PROCESS_ENTER
		)
		sizer.Add(self.searchBox, wx.SizerFlags(1).Centre())
		searchButton = CustomButton(
			parent=self,
			value="Next",
			onClick=self.onSearch
		)
		sizer.Add(searchButton, wx.SizerFlags().Centre())
		
		self.searchBox.Bind(wx.EVT_TEXT, self.onSearch)
		self.searchBox.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
		
	def onSearch(self, evt):
		self.handleSearch(self.searchBox.GetValue())