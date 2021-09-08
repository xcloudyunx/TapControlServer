import wx, wx.adv

import colors

class TextElement(wx.Button):    
	def __init__(self, parent, width=0, value=""):
		super().__init__(parent=parent, label=" "*width+value, style=wx.BU_EXACTFIT)
		
		self.Disable()
		
	def render(self, value=None):
		if value:
			self.SetLabel(str(value))