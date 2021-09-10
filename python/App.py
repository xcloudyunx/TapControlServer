import wx.lib.inspection
import wx
from MainFrame import MainFrame

def startApp():
	app = wx.App()
	frame = MainFrame()
	# wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()