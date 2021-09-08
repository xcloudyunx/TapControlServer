import wx, wx.adv

import colors, constants

from MainBarOverlay import MainBarOverlay
from SideBar import SideBar

class MainFrame(wx.Frame):    
	def __init__(self):
		super().__init__(
			parent=None,
			title="Remote Server",
			size=(600, 600),
			style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		
		self.numOfRows = 4
		self.numOfCols = 2
		self.numOfPages = 2
		self.currentPage = 1
		self.iconButtons = [[]]
		self.buttonClassName = None
		self.buttonID = None
		
		self.SetBackgroundColour(colors.black)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.mainBarOverlay = MainBarOverlay(
			parent=self,
			onChangePageButtonClick=self.handlePageChange
		)
		sizer.Add(self.mainBarOverlay, wx.SizerFlags(1).Expand())
		
		self.sideBar = SideBar(
			parent=self,
			onGridSettingsClick=self.handleGridSettingsClick
		)
		sizer.Add(self.sideBar, wx.SizerFlags(1).Expand())
		
		self.Show()
		
		wx.CallAfter(self.updateIconButtons)
	
	def render(self):
		self.mainBarOverlay.render(
			numOfRows=self.numOfRows,
			numOfCols=self.numOfCols,
			numOfPages=self.numOfPages,
			currentPage=self.currentPage,
			iconButtons=self.iconButtons,
			onIconButtonClick=self.handleIconButtonClick
		)
		
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
		
		self.render()
		
	def handleIconButtonClick(self, page, id):
		self.buttonClassName = page;
		self.buttonID = id;
		self.render()
		
	def handlePageChange(self, pageNum):
		self.currentPage = pageNum%self.numOfPages
		if self.currentPage == 0:
			self.currentPage = self.numOfPages
		self.render()
	
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
	
	def handleExitClick(self):
		self.buttonClassName = 0
		self.render()