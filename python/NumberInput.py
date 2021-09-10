import wx

import colors

from TextElement import TextElement
from CustomButton import CustomButton

class NumberInput(wx.Panel):    
	def __init__(self, parent, title, onClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = wx.StaticText(
			parent=self,
			label=title+":"
		)
		label.SetForegroundColour(colors.white)
		font = label.GetFont()
		font.SetPointSize(12)
		label.SetFont(font)
		sizer.Add(label, wx.SizerFlags(8).Expand())
		
		btnLeft = CustomButton(
			parent=self,
			value="-",
			onClick=lambda evt : onClick(self.value-1)
		)
		sizer.Add(btnLeft, wx.SizerFlags(1).Expand())
		
		self.txt = TextElement(
			parent=self
		)
		sizer.Add(self.txt, wx.SizerFlags(2).Expand())
		
		btnRight = CustomButton(
			parent=self,
			value="+",
			onClick=lambda evt : onClick(self.value+1)
		)
		sizer.Add(btnRight, wx.SizerFlags(1).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
	
	def render(self, value):
		self.value = value
		self.txt.render(value)