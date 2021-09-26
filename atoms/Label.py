import wx

from config import colors
			
class Label(wx.Panel):    
	def __init__(self, parent, value=""):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.value = wx.StaticText(
			parent=self,
			label=value
		)
		self.value.SetForegroundColour(colors.white)
		font = self.value.GetFont()
		font.SetPointSize(12)
		self.value.SetFont(font)
		sizer.Add(self.value, wx.SizerFlags(1).Expand())
		
	def render(self, value=None):
		if value:
			self.value.SetLabel(str(value))
			self.GetSizer().Layout()