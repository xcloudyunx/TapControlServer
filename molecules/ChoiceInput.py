import wx

from atoms.Label import Label

class ChoiceInput(wx.Panel):    
	def __init__(self, parent, title, choices, onChangeChoice, default=None, required=False):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=("*" if required else "")+title+":"
		)
		sizer.Add(label, wx.SizerFlags(6).Expand())
		
		choice = wx.Choice(
			parent=self,
			choices=choices
		)
		sizer.Add(choice, wx.SizerFlags(8).Expand())
		if default:
			choice.SetSelection(choices.index(default))
			onChangeChoice(title, default, True)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		choice.Bind(wx.EVT_CHOICE, lambda evt : onChangeChoice(title, choices[choice.GetSelection()]))