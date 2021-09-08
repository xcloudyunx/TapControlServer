import wx, wx.adv

import colors

from Row import Row

class Grid(wx.Panel):    
	def __init__(self, parent, className, numOfRows, numOfCols, page, onClick):
		super().__init__(parent=parent)
		
		self.className = className
		
		buttonDim = min(
			self.GetParent().GetSize().height/(numOfRows+1),
			self.GetParent().GetSize().width/(numOfCols+1)
		)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.GetSizer().Add(0, 0, 1)
		for i in range(numOfRows):
			row = Row(
				parent=self,
				id=i,
				numOfCols=numOfCols,
				buttonDim=buttonDim,
				row=page[i],
				onClick=lambda id : onClick(className, id)
			)
			self.GetSizer().Add(row, wx.SizerFlags(0).Expand())
			self.GetSizer().Add(0, 0, 1)