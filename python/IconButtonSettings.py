import wx

import colors

from CustomButton import CustomButton
from TextElement import TextElement
from Heading import Heading

class IconButtonSettings(wx.ScrolledWindow):    
	def __init__(self, parent):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.secondary)
		
		# main sizer
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
	
	def render(self):
		pass