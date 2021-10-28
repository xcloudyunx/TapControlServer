import wx.lib.inspection
import wx

from src.pages.MainFrame import MainFrame

def startApp(plugins, commands, state, onSync):
	app = wx.App()
	frame = MainFrame(
		plugins=plugins,
		commands=commands,
		state=state,
		onSync=onSync
	)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()