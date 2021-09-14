import wx
import json

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
		with open("assets/state.json", "r") as file:
			self.state = json.loads(file.read())
		
		self.currentPage = 1
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
			onGridSettingsSave=self.handleGridSettingsSave
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
			numOfRows=self.state["numOfRows"],
			numOfCols=self.state["numOfCols"],
			iconButtons=self.state["iconButtons"],
			currentPage=self.currentPage,
			onIconButtonClick=self.handleIconButtonClick
		)
		
	def renderSideBar(self):
		self.sideBar.render(
			className=self.buttonClassName,
			id=self.buttonID,
			onExitClick=self.handleExitClick,
			onSyncButtonClick=self.handleSyncButtonClick,
			numOfRows=self.state["numOfRows"],
			numOfCols=self.state["numOfCols"],
			numOfPages=self.state["numOfPages"]
		)

	def updateIconButtons(self):
		self.state["iconButtons"] = self.state["iconButtons"][0:self.state["numOfPages"]+1]
		for k in range(1, self.state["numOfPages"]+1):
			if k >= len(self.state["iconButtons"]):
				self.state["iconButtons"].append([])
			else:
				self.state["iconButtons"][k] = self.state["iconButtons"][k][0:self.state["numOfRows"]]
			for i in range(self.state["numOfRows"]):
				if i >= len(self.state["iconButtons"][k]):
					self.state["iconButtons"][k].append([])
				else:
					self.state["iconButtons"][k] = self.state["iconButtons"][k][0:self.state["numOfCols"]]
				for j in range(self.state["numOfCols"]):
					if j >= len(self.state["iconButtons"][k][i]):
						self.state["iconButtons"][k][i].append("assets/default.png")
		
	def handleIconButtonClick(self, page, id):
		self.buttonClassName = page;
		self.buttonID = id;
		self.render()
		
	def handlePageChange(self, pageNum):
		self.currentPage = min(max(1, pageNum), self.state["numOfPages"])
		self.renderMainBar()
	
	def handleGridSettingsClick(self, type, val):
		val = max(val, 1);
		if type == "row":
			self.state["numOfRows"] = min(constants.rowMax, val)
		elif type == "col":
			self.state["numOfCols"] = min(constants.colMax, val)
		elif type == "page":
			x = min(constants.pageMax, val)
			self.state["numOfPages"] = x
			if (self.currentPage > x):
				self.currentPage = x;
		self.updateIconButtons()
		self.render()
	
	def handleExitClick(self):
		self.buttonClassName = 0
		self.renderSideBar()
	
	def handleCloseButton(self, evt):
		self.Hide()
		
	def handleGridSettingsSave(self):
		with open("assets/state.json", "w") as file:
			# file.write(json.dumps(self.state, indent=4))
			file.write(json.dumps(self.state))
			
	def handleSyncButtonClick(self):
		self.onSync()