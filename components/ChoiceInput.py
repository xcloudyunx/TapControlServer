import wx

from config import colors

from components.Label import Label

class ChoiceInput(wx.Panel):    
	def __init__(self, parent, title, choices, onChangeChoice):
		super().__init__(parent=parent)
		
		self.onChangeChoice = onChangeChoice
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=title+":"
		)
		sizer.Add(label, wx.SizerFlags(6).Expand())
		
		self.choice = wx.Choice(
			parent=self,
			choices=choices
		)
		sizer.Add(self.choice, wx.SizerFlags(8).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		self.choice.Bind(wx.EVT_CHOICE, self.handleChangeChoice)
	
	def handleChangeChoice(self, evt):
		self.onChangeChoice(self.choice.GetSelection())