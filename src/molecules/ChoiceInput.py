import wx

from src.molecules.CustomBaseInput import CustomBaseInput

class ChoiceInput(CustomBaseInput):
	def makeCtrl(self, settings):
		return wx.Choice(
			parent=self,
			choices=settings
		)
	
	def setDefault(self, default):
		self.ctrl.SetSelection(self.ctrl.GetItems().index(default))
	
	def getValue(self):
		return self.ctrl.GetString(self.ctrl.GetSelection())
		
	def getEvent(self):
		return wx.EVT_CHOICE