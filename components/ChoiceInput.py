import wx

from config import colors

from components.Label import Label

class ChoiceInput(wx.Panel):    
	def __init__(self, parent, title, choices, onChangeChoice):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=title+":"
		)
		sizer.Add(label, wx.SizerFlags(6).Expand())
		
		choice = wx.Choice(
			parent=self,
			choices=choices
		)
		sizer.Add(choice, wx.SizerFlags(8).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		choice.Bind(wx.EVT_CHOICE, lambda evt : onChangeChoice(title, choices[choice.GetSelection()]))