import wx, wx.adv
import sys

class SystemTrayIcon(wx.adv.TaskBarIcon):
	def __init__(self, frame):
		super().__init__()
		
		# stores the actual app
		self.frame = frame
 
		# create tray icon
		bmp = wx.Bitmap("assets/default.png", wx.BITMAP_TYPE_ANY)
		self.icon = wx.Icon(bmp)
		self.SetIcon(self.icon, "Remote")
		
		# actions for left and right click
		self.Bind(wx.adv.EVT_TASKBAR_LEFT_UP, self.open)
		self.Bind(wx.adv.EVT_TASKBAR_RIGHT_UP, self.showMenu)
		
		# create menu
		self.menu = self.createMenu()
 
	def createMenu(self):
		# menu has two options, restore and exit
		# may add more options in the future
		# add "Top Secret Control Panel" like discord?
		menu = wx.Menu("Remote")
		menu.Append(0, "Open")
		menu.Append(1, "Exit")
		self.Bind(wx.EVT_MENU, self.open, menu.FindItemById(0))
		self.Bind(wx.EVT_MENU, self.exit, menu.FindItemById(1))
		return menu
		
	def showMenu(self, evt):
		self.PopupMenu(self.menu)
		
	def open(self, evt):
		self.frame.Show()
 
	def exit(self, evt):
		self.frame.Destroy()
		self.Destroy()
		sys.exit()