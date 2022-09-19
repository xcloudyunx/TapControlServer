import wx
import qrcode

from config import colors
from config import constants

from src.atoms.TextElement import TextElement
from src.atoms.CustomButton import CustomButton
from src.pages.PluginManager import PluginManager
from src.organisms.GridSettings import GridSettings

class SideBarPrimary(wx.Panel):
	def __init__(self, parent, onSyncButtonClick, plugins, onGridUpdate, state):
		super().__init__(parent=parent)
		
		self.plugins = plugins
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		pluginManagerButton = CustomButton(
			parent=self,
			value="Plugin Manager",
			onClick=lambda evt : self.managePluginManager()
		)
		sizer.Add(pluginManagerButton, wx.SizerFlags(1).Expand())
		
		qr = qrcode.QRCode()
		qr.add_data(constants.IP)
		qr.make()
		img = qr.make_image(fill_color=colors.white, back_color=colors.primary)
		img.save("assets/ip.png")
		bmp = wx.Bitmap("assets/ip.png", wx.BITMAP_TYPE_ANY)
		auto = wx.StaticBitmap(parent=self, bitmap=bmp)
		sizer.Add(auto, wx.SizerFlags(8).Expand())
		
		# remove this in final
		# manual = TextElement(parent=self, value=constants.IP)
		# sizer.Add(manual, wx.SizerFlags(2).Expand())
		
		syncButton = CustomButton(
			parent=self,
			value="Sync",
			onClick=lambda evt : onSyncButtonClick()
		)
		sizer.Add(syncButton, wx.SizerFlags(1).Expand())
		
		gridSettings = GridSettings(
			parent=self,
			state=state,
			onGridUpdate=onGridUpdate
		)
		sizer.Add(gridSettings, wx.SizerFlags(4).Expand())
	
	def managePluginManager(self):
		with PluginManager(self, self.plugins) as dlg:
			if dlg.ShowModal() == wx.ID_OK:
				dlg.downloadPlugins()