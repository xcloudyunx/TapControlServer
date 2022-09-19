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
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=title+("*" if required else "")+":"
		)
		sizer.Add(label, wx.SizerFlags(6).Expand())
		
		self.ctrl = self.makeCtrl(settings)
		sizer.Add(self.ctrl, wx.SizerFlags(8).Expand())
		if default:
			self.setDefault(default)
			onChange(title, default, True)
		self.ctrl.Bind(self.getEvent(), lambda evt : onChange(title, self.getValue()))
		
		sizer.Add(0, 0, 1)
	
	def makeCtrl(self, _):
		pass
	
	def setDefault(self, _):
		pass
	
	def getValue(self):
		pass
	
	def getEvent(self):
		pass