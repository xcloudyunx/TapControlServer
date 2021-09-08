import wx, wx.adv

import colors

class IconButton(wx.Panel):    
	def __init__(self, parent, id, source, buttonDim, onClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		bmp = wx.Bitmap(source, wx.BITMAP_TYPE_ANY)
		btn = wx.BitmapButton(parent=self, bitmap=bmp, size=wx.Size(buttonDim, buttonDim))
		self.GetSizer().Add(btn, wx.SizerFlags(0).Centre())
		
		btn.Bind(wx.EVT_BUTTON, lambda evt : onClick(id))