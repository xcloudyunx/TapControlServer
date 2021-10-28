import wx
import os

from config import constants

class IconButton(wx.Panel):
	def __init__(self, parent, page, rowIndex, colIndex, buttonDim, onClick):
		super().__init__(parent=parent)
		
		self.buttonDim = buttonDim
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		source = "assets/"+page+"-"+rowIndex+"-"+colIndex+".png"
		if os.path.exists(source):
			bmp = self.createScaledImage(source)
		else:
			bmp = wx.Bitmap()
		btn = wx.BitmapButton(parent=self, bitmap=bmp, size=wx.Size(buttonDim, buttonDim))
		self.GetSizer().Add(btn, wx.SizerFlags(0).Centre())
		
		btn.Bind(wx.EVT_BUTTON, lambda evt : onClick(page, rowIndex, colIndex))
	
	def createScaledImage(self, source):
		img = wx.Image(source, wx.BITMAP_TYPE_ANY)
		scaleFactor = constants.iconButtonPadding/(max(img.GetWidth(), img.GetHeight())/self.buttonDim)
		img.Rescale(img.GetWidth()*scaleFactor, img.GetHeight()*scaleFactor)
		bmp = wx.Bitmap(img)
		return bmp