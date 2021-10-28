import wx

from src.atoms.IconButton import IconButton

class Row(wx.Panel):
	def __init__(self, parent, page, rowIndex, numOfCols, buttonDim, onClick):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		self.GetSizer().Add(0, 0, 1)
		for j in range(numOfCols):
			iconButton = IconButton(
				parent=self,
				page=page,
				rowIndex=rowIndex,
				colIndex=str(j),
				buttonDim=buttonDim,
				onClick=onClick
			)
			self.GetSizer().Add(iconButton, wx.SizerFlags(0).Centre())
			self.GetSizer().Add(0, 0, 1)