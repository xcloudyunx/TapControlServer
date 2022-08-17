import wx

from src.atoms.CustomButton import CustomButton

class SearchBar(wx.Panel):
	def __init__(self, parent, onSearch):
		super().__init__(
			parent=parent,
		)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		searchLabel = wx.StaticText(
			parent=self,
			label="Search: "
		)
		sizer.Add(searchLabel, wx.SizerFlags().Centre())
		searchBox = wx.TextCtrl(
			parent=self,
		)
		sizer.Add(searchBox, wx.SizerFlags(1).Centre())
		searchButton = CustomButton(
			parent=self,
			value="Next",
			onClick=lambda evt: onSearch(searchBox.GetValue())
		)
		sizer.Add(searchButton, wx.SizerFlags().Centre())
		
		self.Bind(wx.EVT_TEXT, lambda evt: onSearch(searchBox.GetValue()))