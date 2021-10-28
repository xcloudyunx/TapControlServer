import wx

from config import colors

from src.organisms.ConnectionArea import ConnectionArea
from src.organisms.IconButtonSettingsContainer import IconButtonSettingsContainer
from src.organisms.GridSettings import GridSettings

class SideBar(wx.Panel):    
	def __init__(self, parent, state, plugins, commands, onGridSettingsSave, onExitClick, onSaveIconButton, onSyncButtonClick):
		super().__init__(parent=parent)
		
		self.state = state
		self.plugins = plugins
		self.commands = commands
		
		self.onExitClick = onExitClick
		self.onSaveIconButton = onSaveIconButton
		self.onSyncButtonClick = onSyncButtonClick
		
		self.SetBackgroundColour(colors.primary)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.gridSettings = GridSettings(
			parent=self,
			state=state,
			onGridSettingsSave=onGridSettingsSave
		)
		sizer.Add(self.gridSettings, wx.SizerFlags(1).Expand())
	
	def render(self, page, rowIndex, colIndex):
		try:
			self.element.Destroy()
		except:
			pass
		if page:
			self.element = IconButtonSettingsContainer(
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
			self.element = ConnectionArea(
				parent=self,
				onSyncButtonClick=self.onSyncButtonClick
			)
		self.GetSizer().Insert(0, self.element, wx.SizerFlags(3).Expand())
		self.GetSizer().Layout()