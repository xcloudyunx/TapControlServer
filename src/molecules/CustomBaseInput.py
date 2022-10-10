import wx

from src.atoms.Label import Label

class CustomBaseInput(wx.Panel):
	def __init__(self, parent=None, title=None, settings=None, onChange=None, default=None, required=False):
		if parent:
			self.Create(parent, title, settings, onChange, default, required)
		else:
			super().__init__()
		
	def Create(self, parent, title, settings, onChange, default, required):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, 1)
		
		label = Label(
			parent=self,
			value=title+("*" if required else "")+":"
		)
		
		self.ctrl = self.makeCtrl(settings)
		
		multiLineSizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(multiLineSizer, wx.SizerFlags(14).Expand())
		
		multiLineSizer.Add(label, wx.SizerFlags(1).Expand())
		multiLineSizer.Add(self.ctrl, wx.SizerFlags(1).Expand())
		
		if default:
			self.setDefault(default)
			onChange(title, default, True)
		self.ctrl.Bind(self.getEvent(), lambda evt : self.handleChange(onChange, title))
		
		sizer.Add(0, 0, 1)
		
	def handleChange(self, onChange, title):
		if self.Validate():
			onChange(title, self.getValue())
	
	def makeCtrl(self, _):
		pass
	
	def setDefault(self, _):
		pass
	
	def getValue(self):
		pass
	
	def getEvent(self):
		pass