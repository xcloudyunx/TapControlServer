import wx

from src.molecules.CustomBaseInput import CustomBaseInput

class TextInput(CustomBaseInput):    
	def makeCtrl(self, _):
		return wx.TextCtrl(
			parent=self
		)
	
	def setDefault(self, default):
		self.ctrl.SetValue(default)
	
	def getValue(self):
		return self.ctrl.GetValue()
	
	def getEvent(self):
		return wx.EVT_TEXT