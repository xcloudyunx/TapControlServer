import wx, wx.adv
import qrcode, socket

import colors

from TextElement import TextElement

class ConnectionArea(wx.Panel):    
	def __init__(self, parent):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		title = TextElement(parent=self, value="ConnectionArea")
		sizer.Add(title, wx.SizerFlags(1).Expand())
		
		ip = socket.gethostbyname(socket.gethostname())
		
		manual = TextElement(parent=self, value=ip)
		sizer.Add(manual, wx.SizerFlags(1).Expand())
		
		qr = qrcode.QRCode()
		qr.add_data(ip)
		qr.make()
		img = qr.make_image(fill_color=colors.white, back_color=colors.primary)
		img.save("assets/ip.png")
		bmp = wx.Bitmap("assets/ip.png", wx.BITMAP_TYPE_ANY)
		auto = wx.StaticBitmap(parent=self, bitmap=bmp)
		sizer.Add(auto, wx.SizerFlags(10).Expand())
		
	
	def render(self):
		pass