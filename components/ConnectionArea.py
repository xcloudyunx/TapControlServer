import wx
import qrcode

from config import colors
from config import constants

from components.TextElement import TextElement
from components.CustomButton import CustomButton

class ConnectionArea(wx.Panel):
	def __init__(self, parent, onSyncButtonClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		title = TextElement(parent=self, value="ConnectionArea")
		sizer.Add(title, wx.SizerFlags(2).Expand())
		
		manual = TextElement(parent=self, value=constants.IP)
		sizer.Add(manual, wx.SizerFlags(2).Expand())
		
		qr = qrcode.QRCode()
		qr.add_data(constants.IP)
		qr.make()
		img = qr.make_image(fill_color=colors.white, back_color=colors.primary)
		img.save("assets/ip.png")
		bmp = wx.Bitmap("assets/ip.png", wx.BITMAP_TYPE_ANY)
		auto = wx.StaticBitmap(parent=self, bitmap=bmp)
		sizer.Add(auto, wx.SizerFlags(20).Expand())
		
		syncButton = CustomButton(
			parent=self,
			value="Sync",
			onClick=lambda evt : onSyncButtonClick()
		)
		sizer.Add(syncButton, wx.SizerFlags(0).Centre())
		
		sizer.Add(0, 0, wx.SizerFlags(1))
	
	def render(self):
		pass