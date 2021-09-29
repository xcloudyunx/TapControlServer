import wx

from config import colors

from organisms.ConnectionArea import ConnectionArea
from organisms.IconButtonSettingsContainer import IconButtonSettingsContainer
from organisms.GridSettings import GridSettings

class SideBar(wx.Panel):    
	def __init__(self, parent, state, onGridSettingsSave, onExitClick, onSaveIconButton, onSyncButtonClick):
		super().__init__(parent=parent)
		
		self.state = state
		
		self.onExitClick = onExitClick
		self.onSaveIconButton = onSaveIconButton
		self.onSyncButtonClick = onSaveIconButton
		
		self.SetBackgroundColour(colors.primary)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.gridSettings = GridSettings(
			parent=self,
			state=state,
			onGridSettingsSave=onGridSettingsSave
		)
		sizer.Add(self.gridSettings, wx.SizerFlags(1).Expand())
	
	def render(self, className, id, plugins, commands):
		try:
			self.element.Destroy()
		except:
			pass
		if className:
			self.element = IconButtonSettingsContainer(
				parent=self,
				className=className,
				id=id,
				numOfCols=self.state["numOfCols"],
				onExitClick=self.onExitClick,
				onSaveIconButton=self.onSaveIconButton,
				plugins=plugins,
				defaultValues=commands[str(className)][str(id)] if str(id) in commands[str(className)] else None if str(className) in commands else None
			)
		else:
			self.element = ConnectionArea(
				parent=self,
				onSyncButtonClick=self.onSyncButtonClick
			)
		self.GetSizer().Insert(0, self.element, wx.SizerFlags(3).Expand())
		self.GetSizer().Layout()