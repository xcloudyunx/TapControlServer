import wx

from config import colors
from config import constants

from atoms.CustomButton import CustomButton
from molecules.NumberInput import NumberInput

class GridSettings(wx.Panel):    
	def __init__(self, parent, state, onGridSettingsSave):
		super().__init__(parent=parent)
		
		self.state = state
		
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
			value=self.state["numOfRows"],
			onClick=lambda val : self.handleGridSettingsClick("numOfRows", val)
		)
		sizer.Add(self.r, wx.SizerFlags(2).Expand())
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# column settings
		self.c = NumberInput(
			parent=self,
			title="Columns",
			value=self.state["numOfCols"],
			onClick=lambda val : self.handleGridSettingsClick("numOfCols", val)
		)
		sizer.Add(self.c, wx.SizerFlags(2).Expand())
		
		# spacer
		sizer.Add(0, 0, wx.SizerFlags(1))
		
		# page settings
		self.p = NumberInput(
			parent=self,
			title="Pages",
			value=self.state["numOfPages"],
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
			self.state["numOfRows"] = min(constants.rowMax, val)
			self.r.render(self.state["numOfRows"])
		elif type == "numOfCols":
			self.state["numOfCols"] = min(constants.colMax, val)
			self.c.render(self.state["numOfCols"])
		elif type == "numOfPages":
			self.state["numOfPages"] = min(constants.pageMax, val)
			self.p.render(self.state["numOfPages"])