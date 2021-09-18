import wx

import colors

from CustomButton import CustomButton
from TextElement import TextElement
from Grid import Grid

class MainBar(wx.Panel):    
	def __init__(self, parent, onChangePageButtonClick):
		super().__init__(parent=parent)
		
		# main sizer that contains everything
		mainSizer = wx.BoxSizer()
		self.SetSizer(mainSizer)
		
		# button for decreasing page number
		self.btnLeft = CustomButton(
			parent=self,
			value="<-",
			onClick=lambda evt : onChangePageButtonClick(self.currentPage-1)
		)
		mainSizer.Add(self.btnLeft, wx.SizerFlags(1).Centre())
		
		# centre sizer
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(self.sizer, wx.SizerFlags(10).Expand())
		
		# grid gets inserted here
		
		# display page number
		# a sizer is used to centre and get the width of the text element
		alignCentreSizer = wx.BoxSizer()
		self.sizer.Add(alignCentreSizer, wx.SizerFlags(1).Expand())
		alignCentreSizer.Add(0, 0, 1)
		self.txt = TextElement(parent=self)
		alignCentreSizer.Add(self.txt, wx.SizerFlags(1).Expand())
		alignCentreSizer.Add(0, 0, 1)
		
		# button for increasing page number
		self.btnRight = CustomButton(
			parent=self,
			value="->",
			onClick=lambda evt : onChangePageButtonClick(self.currentPage+1)
		)
		mainSizer.Add(self.btnRight, wx.SizerFlags(1).Centre())
	
	def render(self, numOfRows, numOfCols, numOfPages, currentPage, onIconButtonClick):
		# stored for changing page
		self.currentPage = currentPage
		
		# generate grid
		try:
			self.grid.Destroy()
		except:
			pass
		self.grid = Grid(
			parent=self,
			className=currentPage,
			numOfRows=numOfRows,
			numOfCols=numOfCols,
			onClick=onIconButtonClick
		)
		self.sizer.Insert(0, self.grid, wx.SizerFlags(30).Expand())
		self.sizer.Layout()
		
		# update text elements
		self.txt.render(str(currentPage)+"/"+str(numOfPages))