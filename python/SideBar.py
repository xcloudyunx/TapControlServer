import wx

import colors

from ConnectionArea import ConnectionArea
from IconButtonSettings import IconButtonSettings
from GridSettings import GridSettings

class SideBar(wx.Panel):    
	def __init__(self, parent, onGridSettingsClick, onGridSettingsSave):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.primary)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.gridSettings = GridSettings(
			parent=self,
			onGridSettingsClick=onGridSettingsClick,
			onGridSettingsSave=onGridSettingsSave
		)
		sizer.Add(self.gridSettings, wx.SizerFlags(1).Expand())
	
	def render(self, className, id, onExitClick, onSyncButtonClick, numOfRows, numOfCols, numOfPages):
		try:
			self.element.Destroy()
		except:
			pass
		if className:
			self.element = IconButtonSettings(
				parent=self,
				className=className,
				id=id,
				onClick=onExitClick
			)
		else:
			self.element = ConnectionArea(
				parent=self,
				onSyncButtonClick=onSyncButtonClick
			)
		self.GetSizer().Insert(0, self.element, wx.SizerFlags(3).Expand())
		self.GetSizer().Layout()
	
		self.gridSettings.render(
			numOfRows=numOfRows,
			numOfCols=numOfCols,
			numOfPages=numOfPages
		)