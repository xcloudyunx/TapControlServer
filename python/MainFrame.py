import wx

import colors, constants

from MainBar import MainBar
from SideBar import SideBar
from SystemTrayIcon import SystemTrayIcon

class MainFrame(wx.Frame):    
	def __init__(self, onSync):
		super().__init__(
			parent=None,
			title="Remote Server",
			size=(600, 600),
			style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		
		self.onSync = onSync
		
		# states
		self.numOfRows = 4
		self.numOfCols = 2
		self.numOfPages = 2
		self.currentPage = 1
		self.iconButtons = [[]]
		self.buttonClassName = None
		self.buttonID = None
		
		# style
		self.SetBackgroundColour(colors.black)
		
		# children
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.mainBar = MainBar(
			parent=self,
			onChangePageButtonClick=self.handlePageChange
		)
		sizer.Add(self.mainBar, wx.SizerFlags(1).Expand())
		
		self.sideBar = SideBar(
			parent=self,
			onGridSettingsClick=self.handleGridSettingsClick,
			onSync=self.handleSync
		)
		sizer.Add(self.sideBar, wx.SizerFlags(1).Expand())
		
		# create system tray icon
		SystemTrayIcon(self)
		
		# shrink to system tray when hitting the close button
		self.Bind(wx.EVT_CLOSE, self.handleCloseButton)
		
		# show app
		self.Show()
		
		# render after positioning set up
		wx.CallAfter(self.updateIconButtons)
		wx.CallAfter(self.render)
	
	def render(self):
		self.renderMainBar()
		self.renderSideBar()
		
	def renderMainBar(self):
		self.updateIconButtons()
		self.mainBar.render(
			numOfRows=self.numOfRows,
			numOfCols=self.numOfCols,
			numOfPages=self.numOfPages,
			currentPage=self.currentPage,
			iconButtons=self.iconButtons,
			onIconButtonClick=self.handleIconButtonClick
		)
		
	def renderSideBar(self):
		self.sideBar.render(
			className=self.buttonClassName,
			id=self.buttonID,
			onExitClick=self.handleExitClick,
			numOfRows=self.numOfRows,
			numOfCols=self.numOfCols,
			numOfPages=self.numOfPages
		)

	def updateIconButtons(self):
		self.iconButtons = self.iconButtons[0:self.numOfPages+1]
		for k in range(1, self.numOfPages+1):
			if k >= len(self.iconButtons):
				self.iconButtons.append([])
			else:
				self.iconButtons[k] = self.iconButtons[k][0:self.numOfRows]
			for i in range(self.numOfRows):
				if i >= len(self.iconButtons[k]):
					self.iconButtons[k].append([])
				else:
					self.iconButtons[k] = self.iconButtons[k][0:self.numOfCols]
				for j in range(self.numOfCols):
					if j >= len(self.iconButtons[k][i]):
						self.iconButtons[k][i].append("assets/default.png")
		
	def handleIconButtonClick(self, page, id):
		self.buttonClassName = page;
		self.buttonID = id;
		self.render()
		
	def handlePageChange(self, pageNum):
		self.currentPage = pageNum%self.numOfPages
		if self.currentPage == 0:
			self.currentPage = self.numOfPages
		self.renderMainBar()
	
	def handleGridSettingsClick(self, type, val):
		val = max(val, 1);
		if type == "row":
			self.numOfRows = min(constants.rowMax, val)
		elif type == "col":
			self.numOfCols = min(constants.colMax, val)
		elif type == "page":
			x = min(constants.pageMax, val)
			self.numOfPages = x
			if (self.currentPage > x):
				self.currentPage = x;
		self.updateIconButtons()
		self.render()
	
	def handleExitClick(self):
		self.buttonClassName = 0
		self.renderSideBar()
	
	def handleCloseButton(self, evt):
		self.Hide()
		
	def handleSync(self):
		print("saving")
		self.onSync()