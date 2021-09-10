import wx

import colors

class CustomButton(wx.Button):    
	def __init__(self, parent, value, onClick):
		super().__init__(parent=parent, label=value, style=wx.BU_EXACTFIT)
		
		self.Bind(wx.EVT_BUTTON, onClick)