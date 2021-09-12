import wx.lib.inspection
import wx
from MainFrame import MainFrame

def startApp(onSync):
	app = wx.App()
	frame = MainFrame(onSync)
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()