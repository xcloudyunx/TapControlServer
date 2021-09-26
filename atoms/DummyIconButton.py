import wx
import os

from config import constants

class DummyIconButton(wx.Panel):
	def __init__(self, parent, id, className, buttonDim):
		super().__init__(parent=parent)
		
		self.source = None
		self.id = id
		self.className = className
		self.buttonDim = buttonDim
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		source = "assets/"+str(className)+"-"+str(id)+".png"
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
		if self.source:
			bmp = self.createScaledImage(self.source, constants.iconButtonSize)
			bmp.SaveFile("assets/"+str(self.className)+"-"+str(self.id)+".png", wx.BITMAP_TYPE_PNG)
		elif not self.btn.GetBitmap():
			source = "assets/"+str(self.className)+"-"+str(self.id)+".png"
			if os.path.exists(source):
				os.remove(source)