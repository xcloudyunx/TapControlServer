import wx, wx.adv

import colors

from NumberInput import NumberInput

class GridSettings(wx.Panel):    
	def __init__(self, parent, onClick):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.secondary)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		self.r = NumberInput(
			parent=self,
			title="Rows",
			onClick=lambda val : onClick("row", val)
		)
		sizer.Add(self.r, wx.SizerFlags(1).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		self.c = NumberInput(
			parent=self,
			title="Columns",
			onClick=lambda val : onClick("col", val)
		)
		sizer.Add(self.c, wx.SizerFlags(1).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		self.p = NumberInput(
			parent=self,
			title="Pages",
			onClick=lambda val : onClick("page", val)
		)
		sizer.Add(self.p, wx.SizerFlags(1).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
	
	def render(self, numOfRows, numOfCols, numOfPages):
		self.r.render(numOfRows)
		self.c.render(numOfCols)
		self.p.render(numOfPages)