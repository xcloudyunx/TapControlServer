import wx
import qrcode

import colors, constants

from TextElement import TextElement

class ConnectionArea(wx.Panel):    
	def __init__(self, parent):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		title = TextElement(parent=self, value="ConnectionArea")
		sizer.Add(title, wx.SizerFlags(1).Expand())
		
		manual = TextElement(parent=self, value=constants.IP)
		sizer.Add(manual, wx.SizerFlags(1).Expand())
		
		qr = qrcode.QRCode()
		qr.add_data(constants.IP)
		qr.make()
		img = qr.make_image(fill_color=colors.white, back_color=colors.primary)
		img.save("assets/ip.png")
		bmp = wx.Bitmap("assets/ip.png", wx.BITMAP_TYPE_ANY)
		auto = wx.StaticBitmap(parent=self, bitmap=bmp)
		sizer.Add(auto, wx.SizerFlags(10).Expand())
		
	
	def render(self):
		pass