import wx

import colors

from NumberInput import NumberInput
from CustomButton import CustomButton

class GridSettings(wx.Panel):    
	def __init__(self, parent, onGridSettingsClick, onGridSettingsSave):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.secondary)
		
		# main sizer
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(2))
		
		# row settings
		self.r = NumberInput(
			parent=self,
			title="Rows",
			onClick=lambda val : onGridSettingsClick("row", val)
		)
		sizer.Add(self.r, wx.SizerFlags(2).Expand())
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# column settings
		self.c = NumberInput(
			parent=self,
			title="Columns",
			onClick=lambda val : onGridSettingsClick("col", val)
		)
		sizer.Add(self.c, wx.SizerFlags(2).Expand())
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# page settings
		self.p = NumberInput(
			parent=self,
			title="Pages",
			onClick=lambda val : onGridSettingsClick("page", val)
		)
		sizer.Add(self.p, wx.SizerFlags(2).Expand())
		
		#spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# sync button
		saveButton = CustomButton(
			parent=self,
			value="Save",
			onClick=lambda evt : onGridSettingsSave()
		)
		sizer.Add(saveButton, wx.SizerFlags(0).Centre())
		
		#spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
	
	def render(self, numOfRows, numOfCols, numOfPages):
		self.r.render(numOfRows)
		self.c.render(numOfCols)
		self.p.render(numOfPages)