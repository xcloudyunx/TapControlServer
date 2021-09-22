import wx.lib.inspection
import wx

from screens.MainFrame import MainFrame

def startApp(pluginList, onSyncGrid, onSyncImage):
	app = wx.App()
	frame = MainFrame(
		pluginList=pluginList,
		onSyncGrid=onSyncGrid,
		onSyncImage=onSyncImage
	)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()