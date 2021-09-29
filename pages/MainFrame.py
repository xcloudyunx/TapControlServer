import wx
import json

from config import colors
from config import constants

from templates.MainBar import MainBar
from templates.SideBar import SideBar
from atoms.SystemTrayIcon import SystemTrayIcon

class MainFrame(wx.Frame):    
	def __init__(self, plugins, commands, state, onSync):
		super().__init__(
			parent=None,
			title="Tap Control",
			size=(600, 600),
			style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		
		self.SetIcon(wx.Icon("assets/default.png"))
		
		self.plugins = plugins
		self.onSync = onSync
		
		# commands 
		self.commands = commands
		
		# states
		self.state = state
		
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
			plugins=self.plugins,
			commands=self.commands
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
	
	def handleExitClick(self):
		self.buttonClassName = 0
		self.renderSideBar()
	
	def handleCloseButton(self, evt):
		self.Hide()
		
	def handleGridSettingsSave(self, numOfRows, numOfCols, numOfPages):
		self.state["numOfRows"] = numOfRows
		self.state["numOfCols"] = numOfCols
		if self.state["numOfPages"] != numOfPages:
			for i in range(self.state["numOfPages"], numOfPages+1):
				self.commands[str(i)] = {}
			for i in range(numOfPages+1, self.state["numOfPages"]+1):
				del self.commands[str(i)]
			with open("config/commands.json", "w") as file:
				file.write(json.dumps(self.commands))
			self.state["numOfPages"] = numOfPages
		if (self.currentPage > numOfPages):
			self.currentPage = numOfPages
		self.renderMainBar()
		with open("config/state.json", "w") as file:
			file.write(json.dumps(self.state))
			
	def handleSyncButtonClick(self):
		self.onSync()
		
	def handleSaveIconButton(self, info):
		self.buttonClassName = 0
		self.render()
		page = info.pop("page")
		id = info.pop("id")
		plugin = info.pop("name", None)
		if plugin:
			self.commands[page][id] = [plugin, info]
		else:
			self.commands[page].pop(id, None)
		with open("config/commands.json", "w") as file:
			file.write(json.dumps(self.commands))