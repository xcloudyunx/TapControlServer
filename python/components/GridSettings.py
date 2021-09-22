import wx

from config import colors
from config import constants

from components.NumberInput import NumberInput
from components.CustomButton import CustomButton

class GridSettings(wx.Panel):    
	def __init__(self, parent, onGridSettingsClick, onGridSettingsSave, numOfRows, numOfCols, numOfPages):
		super().__init__(parent=parent)
		
		self.onGridSettingsClick = onGridSettingsClick
		
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
			value=numOfRows,
			onClick=lambda val : self.handleGridSettingsClick("numOfRows", val)
		)
		sizer.Add(self.r, wx.SizerFlags(2).Expand())
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# column settings
		self.c = NumberInput(
			parent=self,
			title="Columns",
			value=numOfCols,
			onClick=lambda val : self.handleGridSettingsClick("numOfCols", val)
		)
		sizer.Add(self.c, wx.SizerFlags(2).Expand())
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# page settings
		self.p = NumberInput(
			parent=self,
			title="Pages",
			value=numOfPages,
			onClick=lambda val : self.handleGridSettingsClick("numOfPages", val)
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
		
	def handleGridSettingsClick(self, type, val):
		val = max(val, 1);
		if type == "numOfRows":
			val = min(constants.rowMax, val)
			self.r.render(val)
		elif type == "numOfCols":
			val = min(constants.colMax, val)
			self.c.render(val)
		elif type == "numOfPages":
			val = min(constants.pageMax, val)
			self.p.render(val)
		self.onGridSettingsClick(type, val)