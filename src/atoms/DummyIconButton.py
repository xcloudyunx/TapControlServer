import wx
import os
import json

from config import constants

class DummyIconButton(wx.Panel):
	def __init__(self, parent, id, buttonDim):
		super().__init__(parent=parent)
		
		self.source = None
		self.id = id
		self.buttonDim = buttonDim
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		source = "assets/"+self.id+".png"
		if os.path.exists(source):
			bmp = self.createScaledImage(source, buttonDim)
		else:
			bmp = wx.Bitmap()
		self.btn = wx.BitmapButton(parent=self, bitmap=bmp, size=wx.Size(buttonDim, buttonDim))
		self.GetSizer().Add(self.btn, wx.SizerFlags(0).Centre())
		
	def update(self, source):
		self.source = source
		if source:
			bmp = self.createScaledImage(source, self.buttonDim)
		else:
			bmp = wx.Bitmap()
		self.btn.SetBitmap(bmp)
		self.btn.Refresh()
		
	def createScaledImage(self, source, containerSize):
		img = wx.Image(source, wx.BITMAP_TYPE_ANY)
		scaleFactor = constants.iconButtonPadding/(max(img.GetWidth(), img.GetHeight())/containerSize)
		img.Rescale(img.GetWidth()*scaleFactor, img.GetHeight()*scaleFactor)
		bmp = wx.Bitmap(img)
		return bmp
		
	def saveImage(self):
		# with open("settings/updates.json", "r") as file:
			# data = json.loads(file.read())
		source = "assets/"+self.id+".png"
		if self.source:
			bmp = self.createScaledImage(self.source, constants.iconButtonSize)
			bmp.SaveFile(source, wx.BITMAP_TYPE_PNG)
			# data[self.id] = True
		elif not self.btn.GetBitmap():
			if os.path.exists(source):
				os.remove(source)
				# data[self.id] = False
		# with open("settings/updates.json", "w") as file:
			# file.write(json.dumps(data))