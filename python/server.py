import wx.lib.inspection
import wx, wx.adv
from MainFrame import MainFrame

def main():
	app = wx.App()
	frame = MainFrame()
	wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()	

if __name__ == "__main__":
	main()