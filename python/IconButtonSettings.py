import wx, wx.adv

from TextElement import TextElement

class IconButtonSettings(wx.Panel):    
	def __init__(self, parent, className, id, onClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		txt = TextElement(parent=self, value="IconButtonSettings"+str(className)+str(id))
		sizer.Add(txt, wx.SizerFlags(1).Expand())
	
	def render(self):
		pass