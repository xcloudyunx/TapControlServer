import wx

from src.atoms.Label import Label
from src.atoms.TextElement import TextElement
from src.atoms.CustomButton import CustomButton

class NumberInput(wx.Panel):    
	def __init__(self, parent, title, value, onClick):
		super().__init__(parent=parent)
		
		self.value = value
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=title+":"
		)
		sizer.Add(label, wx.SizerFlags(8).Expand())
		
		btnLeft = CustomButton(
			parent=self,
			value="-",
			onClick=lambda evt : onClick(self.value-1)
		)
		sizer.Add(btnLeft, wx.SizerFlags(1).Expand())
		
		self.text = TextElement(
			parent=self,
			value=value
		)
		sizer.Add(self.text, wx.SizerFlags(2).Expand())
		
		btnRight = CustomButton(
			parent=self,
			value="+",
			onClick=lambda evt : onClick(self.value+1)
		)
		sizer.Add(btnRight, wx.SizerFlags(1).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
	
	def render(self, value):
		self.value = value
		self.text.render(value)