import wx

from src.molecules.CustomBaseInput import CustomBaseInput

class TextInput(CustomBaseInput):
# https://docs.wxpython.org/wx.lib.masked.numctrl.html
# https://github.com/wxWidgets/Phoenix/blob/master/demo/Validator.py
	def makeCtrl(self, settings):
		return wx.TextCtrl(
			parent=self,
			validator=Validator(settings)
		)
	
	def setDefault(self, default):
		self.ctrl.SetValue(default)
	
	def getValue(self):
		return self.ctrl.GetValue()
	
	def getEvent(self):
		return wx.EVT_TEXT
	
class Validator(wx.Validator):
	def __init__(self, settings):
		super().__init__()
		self.settings = settings
		self.string = ""
		self.Bind(wx.EVT_TEXT, self.OnChange)

	def Clone(self):
		return Validator(self.settings)

	def Validate(self, _=None):
		item = self.GetWindow()
		value = item.GetValue()
		print(self.settings, value)
		if not value:
			return True
		if self.settings == "integer":
			try:
				int(value)
			except:
				return False
		if self.settings == "decimal":
			try:
				float(value)
			except:
				return False
		return True
		
	def IsValidCurrently(self, value):
		if value == "-":
			return True
		return self.Validate()

	def OnChange(self, event):
		item = self.GetWindow()
		
		if self.IsValidCurrently(item.GetValue()):
			event.Skip()
			self.string = item.GetValue()
		else:
			item.ChangeValue(self.string)
			item.SetInsertionPointEnd()