import wx
import os

from config import colors

class IconButton(wx.Panel):
	def __init__(self, parent, id, className, buttonDim, onClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		source = "assets/"+str(+className)+"/"+str(id)+".png"
		if os.path.exists(source):
			bmp = wx.Bitmap(source, wx.BITMAP_TYPE_ANY)
		else:
			bmp = wx.Bitmap()
		btn = wx.BitmapButton(parent=self, bitmap=bmp, size=wx.Size(buttonDim, buttonDim))
		self.GetSizer().Add(btn, wx.SizerFlags(0).Centre())
		
		btn.Bind(wx.EVT_BUTTON, lambda evt : onClick(className, id))