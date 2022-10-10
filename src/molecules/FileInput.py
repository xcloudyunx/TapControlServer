import wx
import os

from src.molecules.CustomBaseInput import CustomBaseInput

class FileInput(CustomBaseInput):    
	def makeCtrl(self, settings):
		# print(imageFilePicker.GetPath())
		#imageFilePicker.SetInitialDirectory() # asset directory from plugins?
		return wx.FilePickerCtrl(
			parent=self,
			wildcard=settings,
			size=wx.Size(1, 1),
			validator=Validator(settings)
		)
	
	def setDefault(self, default):
		self.ctrl.SetPath(default)
	
	def getValue(self):
		return self.ctrl.GetPath()
		
	def getEvent(self):
		return wx.EVT_FILEPICKER_CHANGED
	
	def reset(self):
		self.ctrl.SetPath("")

class Validator(wx.Validator):
	def __init__(self, settings):
		super().__init__()
		self.settings = settings

	def Clone(self):
		return Validator(self.settings)

	def Validate(self, _=None):
		item = self.GetWindow()
		path = item.GetPath()
		if os.path.exists(path):
			return True
		return False