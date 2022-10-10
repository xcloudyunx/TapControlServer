import wx
import json

from config import colors
from config import constants

from src.atoms.SystemTrayIcon import SystemTrayIcon
from src.templates.MainBar import MainBar
from src.templates.SideBar import SideBar
from src.pages.SyncDialogBox import SyncDialogBox

class MainFrame(wx.Frame):    
	def __init__(self, plugins, commands, state, onSyncState, onSyncImage, onSyncAll):
		super().__init__(
			parent=None,
			title="Tap Control",
			size=(600, 600),
			style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		
		self.SetIcon(wx.Icon("assets/default.png"))
		
		self.plugins = plugins
		self.onSyncState = onSyncState
		self.onSyncImage = onSyncImage
		self.onSyncAll = onSyncAll
		
		# commands 
		self.commands = commands
		
		# states
		self.state = state
		
		self.currentPage = 1
		self.buttonPage = None
		self.buttonRow = None
		self.buttonCol = None
		
		# style
		self.SetBackgroundColour(colors.black)
		
		# children
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.mainBar = MainBar(
			parent=self,
			state=self.state,
			onChangePageButtonClick=self.handlePageChange,
			onIconButtonClick=self.handleIconButtonClick
		)
		sizer.Add(self.mainBar, wx.SizerFlags(1).Expand())
		
		self.sideBar = SideBar(
			parent=self,
			state=self.state,
			plugins=self.plugins,
			commands=self.commands,
			onGridUpdate=self.handleGridUpdate,
			onExitClick=self.handleExitClick,
			onSaveIconButton=self.handleSaveIconButton,
			onSyncButtonClick=self.handleSyncButtonClick
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
			currentPage=self.currentPage
		)
		
	def renderSideBar(self):
		self.sideBar.render(
			page=self.buttonPage,
			rowIndex=self.buttonRow,
			colIndex=self.buttonCol
		)
		
	def handleIconButtonClick(self, page, row, col):
		self.buttonPage = page
		self.buttonRow = row
		self.buttonCol = col
		self.renderSideBar()
		
	def handlePageChange(self, pageNum):
		newPage = min(max(1, pageNum), self.state["numOfPages"])
		if newPage != self.currentPage:
			self.currentPage = newPage
			self.renderMainBar()
	
	def handleExitClick(self):
		self.buttonPage = 0
		self.renderSideBar()
	
	def handleCloseButton(self, evt):
		self.Hide()
		
	def handleGridUpdate(self):
		if (self.currentPage > self.state["numOfPages"]):
			self.currentPage = self.state["numOfPages"]
		self.renderMainBar()
		self.onSyncState()
			
	def handleSyncButtonClick(self):
		# create dialog box saying syncing
		with SyncDialogBox(self.onSyncAll) as syncDialogBox:
			syncDialogBox.Show()
		
	def handleSaveIconButton(self, info):
		self.buttonPage = 0
		self.render()
		id = info.pop("id")
		plugin = info.pop("name", None)
		if plugin:
			self.commands[id] = [plugin, info]
		else:
			self.commands.pop(id, None)
		with open("settings/commands.json", "w") as file:
			file.write(json.dumps(self.commands))
		self.onSyncImage(id)