import wx.lib.inspection
import wx

from pages.MainFrame import MainFrame

def startApp(plugins, onSync, onIconButtonUpdate):
	app = wx.App()
	frame = MainFrame(
		plugins=plugins,
		onSync=onSync,
		onIconButtonUpdate=onIconButtonUpdate
	)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()