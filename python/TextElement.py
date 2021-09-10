import wx

import colors
			
class TextElement(wx.Panel):    
	def __init__(self, parent, value=""):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.SetBackgroundColour(colors.white)
		
		self.value = wx.StaticText(parent=self, label=value, style=wx.ALIGN_CENTRE_HORIZONTAL)
		self.value.SetForegroundColour(colors.black)
		sizer.Add(self.value, wx.SizerFlags(1).Centre())
		
	def render(self, value=None):
		if value:
			self.value.SetLabel(str(value))
			self.GetSizer().Layout()