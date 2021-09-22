import wx.lib.inspection
import wx
from screens.MainFrame import MainFrame

def startApp(onSyncGrid, onSyncImage):
	app = wx.App()
	frame = MainFrame(onSyncGrid, onSyncImage)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()