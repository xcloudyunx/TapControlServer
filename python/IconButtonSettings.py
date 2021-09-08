import wx, wx.adv

from CustomButton import CustomButton
from TextElement import TextElement

class IconButtonSettings(wx.Panel):    
	def __init__(self, parent, className, id, onClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		exitBtn = CustomButton(
			parent=self,
			value="X",
			onClick=lambda evt : onClick()
		)
		sizer.Add(exitBtn, wx.SizerFlags(1).Expand())
		
		txt = TextElement(parent=self, value="IconButtonSettings"+str(className)+str(id))
		sizer.Add(txt, wx.SizerFlags(1).Expand())
	
	def render(self):
		pass