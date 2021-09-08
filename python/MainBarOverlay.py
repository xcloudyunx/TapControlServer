import wx, wx.adv

import colors

from CustomButton import CustomButton
from TextElement import TextElement
from MainBar import MainBar

class MainBarOverlay(wx.Panel):    
	def __init__(self, parent, onChangePageButtonClick):
		super().__init__(parent=parent)
		
		mainSizer = wx.BoxSizer()
		self.SetSizer(mainSizer)
		
		self.btnLeft = CustomButton(
			parent=self,
			value="<-",
			onClick=lambda evt : onChangePageButtonClick(self.currentPage-1)
		)
		mainSizer.Add(self.btnLeft, wx.SizerFlags(1).Centre())
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(sizer, wx.SizerFlags(10).Expand())
		
		self.mainBar = MainBar(
			parent=self
		)
		sizer.Add(self.mainBar, wx.SizerFlags(30).Expand())
		
		self.txt = TextElement(parent=self, width=3)
		sizer.Add(self.txt, wx.SizerFlags(1).Centre())
		
		
		self.btnRight = CustomButton(
			parent=self,
			value="->",
			onClick=lambda evt : onChangePageButtonClick(self.currentPage+1)
		)
		mainSizer.Add(self.btnRight, wx.SizerFlags(1).Centre())
	
	def render(self, numOfRows, numOfCols, numOfPages, currentPage, iconButtons, onIconButtonClick):
		self.mainBar.render(
			numOfRows=numOfRows,
			numOfCols=numOfCols,
			numOfPages=numOfPages,
			currentPage=currentPage,
			iconButtons=iconButtons,
			onIconButtonClick=onIconButtonClick
		)
	
		self.currentPage = currentPage
		
		# h = (self.parent.GetSize().height-self.btnLeft.GetSize().height)/2
		# self.btnLeft.SetPosition(wx.Point(0, h))
		# w = self.parent.GetSize().width-self.btnRight.GetSize().width
		# self.btnRight.SetPosition(wx.Point(w, h))
		
		self.txt.render(currentPage)
		# w = (self.parent.GetSize().width-self.txt.GetSize().width)/2
		# h = self.parent.GetSize().height-self.txt.GetSize().height
		# self.txt.SetPosition(wx.Point(w, h))
		