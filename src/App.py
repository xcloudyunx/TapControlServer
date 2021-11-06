import wx.lib.inspection
import wx

from src.pages.MainFrame import MainFrame

def startApp(plugins, commands, state, onSyncState, onSyncImage, onSyncAll):
	app = wx.App()
	frame = MainFrame(
		plugins=plugins,
		commands=commands,
		state=state,
		onSyncState=onSyncState,
		onSyncImage=onSyncImage,
		onSyncAll=onSyncAll
	)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()