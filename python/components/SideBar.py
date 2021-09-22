import wx

from config import colors

from components.ConnectionArea import ConnectionArea
from components.IconButtonSettingsContainer import IconButtonSettingsContainer
from components.GridSettings import GridSettings

class SideBar(wx.Panel):    
	def __init__(self, parent, onGridSettingsClick, onGridSettingsSave, numOfRows, numOfCols, numOfPages):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.primary)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.gridSettings = GridSettings(
			parent=self,
			onGridSettingsClick=onGridSettingsClick,
			onGridSettingsSave=onGridSettingsSave,
			numOfRows=numOfRows,
			numOfCols=numOfCols,
			numOfPages=numOfPages
		)
		sizer.Add(self.gridSettings, wx.SizerFlags(1).Expand())
	
	def render(self, className, id, numOfCols, onExitClick, onSaveIconButton, onSyncButtonClick, pluginList):
		try:
			self.element.Destroy()
		except:
			pass
		if className:
			self.element = IconButtonSettingsContainer(
				parent=self,
				className=className,
				id=id,
				numOfCols=numOfCols,
				onExitClick=onExitClick,
				onSaveIconButton=onSaveIconButton,
				pluginList=pluginList
			)
		else:
			self.element = ConnectionArea(
				parent=self,
				onSyncButtonClick=onSyncButtonClick
			)
		self.GetSizer().Insert(0, self.element, wx.SizerFlags(3).Expand())
		self.GetSizer().Layout()