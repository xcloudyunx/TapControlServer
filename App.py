import wx.lib.inspection
import wx

from screens.MainFrame import MainFrame

def startApp(plugins, onSyncGrid, onSyncImage):
	app = wx.App()
	frame = MainFrame(
		plugins=plugins,
		onSyncGrid=onSyncGrid,
		onSyncImage=onSyncImage
	)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()