import wx

from config import colors

from src.templates.SideBarPrimary import SideBarPrimary
from src.templates.SideBarSecondary import SideBarSecondary

class SideBar(wx.Panel):    
	def __init__(self, parent, state, plugins, commands, onGridUpdate, onExitClick, onSaveIconButton, onSyncButtonClick):
		super().__init__(parent=parent)
		
		self.state = state
		self.plugins = plugins
		self.commands = commands
		
		self.onExitClick = onExitClick
		self.onSaveIconButton = onSaveIconButton
		self.onSyncButtonClick = onSyncButtonClick
		self.onGridUpdate = onGridUpdate
		
		self.SetBackgroundColour(colors.primary)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
	
	def render(self, page, rowIndex, colIndex):
		try:
			self.element.Destroy()
		except:
			pass
		if page:
			self.element = SideBarSecondary(
				parent=self,
				page=page,
				rowIndex=rowIndex,
				colIndex=colIndex,
				onExitClick=self.onExitClick,
				onSaveIconButton=self.onSaveIconButton,
				plugins=self.plugins,
				defaultValues=self.commands[page+"-"+rowIndex+"-"+colIndex] if page+"-"+rowIndex+"-"+colIndex in self.commands else None
			)
		else:
			self.element = SideBarPrimary(
				parent=self,
				onSyncButtonClick=self.onSyncButtonClick,
				plugins=self.plugins,
				onGridUpdate=self.onGridUpdate,
				state=self.state
			)
		self.GetSizer().Add(self.element, wx.SizerFlags(1).Expand())
		self.GetSizer().Layout()