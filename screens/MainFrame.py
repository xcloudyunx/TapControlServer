import wx
import json

from config import colors
from config import constants

from components.MainBar import MainBar
from components.SideBar import SideBar
from components.SystemTrayIcon import SystemTrayIcon

class MainFrame(wx.Frame):    
	def __init__(self, plugins, onSyncGrid, onSyncImage):
		super().__init__(
			parent=None,
			title="Remote Server",
			size=(600, 600),
			style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		
		self.plugins = plugins
		self.onSyncGrid = onSyncGrid
		self.onSyncImage = onSyncImage
		
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
			onGridSettingsSave=self.handleGridSettingsSave,
			numOfRows=self.state["numOfRows"],
			numOfCols=self.state["numOfCols"],
			numOfPages=self.state["numOfPages"]
		)
		sizer.Add(self.sideBar, wx.SizerFlags(1).Expand())
		
		# create system tray icon
		SystemTrayIcon(self)
		
		# shrink to system tray when hitting the close button
		self.Bind(wx.EVT_CLOSE, self.handleCloseButton)
		
		# show app
		self.Show()
		
		# render after positioning set up
		wx.CallAfter(self.render)
	
	def render(self):
		self.renderMainBar()
		self.renderSideBar()
		
	def renderMainBar(self):
		self.mainBar.render(
			numOfRows=self.state["numOfRows"],
			numOfCols=self.state["numOfCols"],
			numOfPages=self.state["numOfPages"],
			currentPage=self.currentPage,
			onIconButtonClick=self.handleIconButtonClick
		)
		
	def renderSideBar(self):
		self.sideBar.render(
			className=self.buttonClassName,
			id=self.buttonID,
			numOfCols=self.state["numOfCols"],
			onExitClick=self.handleExitClick,
			onSaveIconButton=self.handleSaveIconButton,
			onSyncButtonClick=self.handleSyncButtonClick,
			plugins=self.plugins
		)
		
	def handleIconButtonClick(self, page, id):
		self.buttonClassName = page;
		self.buttonID = id;
		self.renderSideBar()
		
	def handlePageChange(self, pageNum):
		newPage = min(max(1, pageNum), self.state["numOfPages"])
		if newPage != self.currentPage:
			self.currentPage = newPage
			self.renderMainBar()
	
	def handleGridSettingsClick(self, type, val):
		self.state[type] = val
		if type == "numOfPages":
			if (self.currentPage > val):
				self.currentPage = val;
		self.renderMainBar()
	
	def handleExitClick(self):
		self.buttonClassName = 0
		self.renderSideBar()
	
	def handleCloseButton(self, evt):
		self.Hide()
		
	def handleGridSettingsSave(self):
		with open("assets/state.json", "w") as file:
			file.write(json.dumps(self.state))
		self.onSyncGrid(self.state)
			
	def handleSyncButtonClick(self):
		self.onSyncImage()
		
	def handleSaveIconButton(self, info):
		print("handle save icon button")
		print(info)