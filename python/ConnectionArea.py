import wx, wx.adv

from TextElement import TextElement

class ConnectionArea(wx.Panel):    
	def __init__(self, parent):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		txt = TextElement(parent=self, value="ConnectionArea")
		sizer.Add(txt, wx.SizerFlags(1).Expand())
	
	def render(self):
		pass