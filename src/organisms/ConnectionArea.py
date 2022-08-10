import wx
import qrcode

from config import colors
from config import constants

from src.atoms.TextElement import TextElement
from src.atoms.CustomButton import CustomButton
from src.pages.PluginManager import PluginManager

class ConnectionArea(wx.Panel):
	def __init__(self, parent, onSyncButtonClick, plugins):
		super().__init__(parent=parent)
		
		self.plugins = plugins
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		# title = TextElement(parent=self, value="ConnectionArea")
		# sizer.Add(title, wx.SizerFlags(2).Expand())
		
		# add a sizer to make button one row
		
		pluginManagerButton = CustomButton(
			parent=self,
			value="Plugin Manager",
			onClick=lambda evt : self.managePluginManager()
		)
		sizer.Add(pluginManagerButton, wx.SizerFlags(0).Centre())
		
		syncButton = CustomButton(
			parent=self,
			value="Sync",
			onClick=lambda evt : onSyncButtonClick()
		)
		sizer.Add(syncButton, wx.SizerFlags(0).Centre())
		
		qr = qrcode.QRCode()
		qr.add_data(constants.IP)
		qr.make()
		img = qr.make_image(fill_color=colors.white, back_color=colors.primary)
		img.save("assets/ip.png")
		bmp = wx.Bitmap("assets/ip.png", wx.BITMAP_TYPE_ANY)
		auto = wx.StaticBitmap(parent=self, bitmap=bmp)
		sizer.Add(auto, wx.SizerFlags(20).Expand())
		
		# change text element? or maybe just this one
		manual = TextElement(parent=self, value=constants.IP)
		sizer.Add(manual, wx.SizerFlags(2).Expand())
		
		
		sizer.Add(0, 0, wx.SizerFlags(1))
	
	def managePluginManager(self):
		with PluginManager(self, self.plugins) as dlg:
			if dlg.ShowModal() == wx.ID_OK:
				dlg.downloadPlugins()