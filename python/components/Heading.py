import wx

from config import colors
			
class Heading(wx.Panel):    
	def __init__(self, parent, value=""):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.value = wx.StaticText(parent=self, label=str(value), style=wx.ALIGN_CENTRE_HORIZONTAL)
		self.value.SetForegroundColour(colors.white)
		font = self.value.GetFont()
		font.SetWeight(wx.FONTWEIGHT_BOLD)
		font.SetSymbolicSize(wx.FONTSIZE_LARGE)
		self.value.SetFont(font)
		sizer.Add(self.value, wx.SizerFlags(1).Centre())
		
	def render(self, value=None):
		if value:
			self.value.SetLabel(str(value))
			self.GetSizer().Layout()