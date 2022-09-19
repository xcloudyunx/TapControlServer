import wx

from src.molecules.CustomBaseInput import CustomBaseInput

class FileInput(CustomBaseInput):    
	def makeCtrl(self, settings):
		# print(imageFilePicker.GetPath())
		#imageFilePicker.SetInitialDirectory() # asset directory from plugins?
		return wx.FilePickerCtrl(
			parent=self,
			wildcard=settings,
			size=wx.Size(1, 1)
		)
	
	def setDefault(self, default):
		self.ctrl.SetPath(default)
	
	def getValue(self):
		return self.ctrl.GetPath()
		
	def getEvent(self):
		return wx.EVT_FILEPICKER_CHANGED
	
	def reset(self):
		self.ctrl.SetPath("")