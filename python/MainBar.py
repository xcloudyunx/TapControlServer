import wx

import colors

from Grid import Grid

class MainBar(wx.Panel):    
	def __init__(self, parent):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
	
	def render(self, numOfRows, numOfCols, numOfPages, currentPage, iconButtons, onIconButtonClick):
		try:
			self.grid.Destroy()
		except:
			pass
		self.grid = Grid(
			parent=self,
			className=currentPage,
			numOfRows=numOfRows,
			numOfCols=numOfCols,
			page=iconButtons[currentPage],
			onClick=onIconButtonClick
		)
		self.GetSizer().Add(self.grid, wx.SizerFlags(1).Expand())
		self.GetSizer().Layout()