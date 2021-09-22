import wx

from components.CustomButton import CustomButton
from components.TextElement import TextElement
from components.Heading import Heading
from components.IconButtonSettings import IconButtonSettings

class IconButtonSettingsContainer(wx.Panel):    
	def __init__(self, parent, className, id, numOfCols, onExitClick, onSaveIconButton):
		super().__init__(parent=parent)
		
		# main sizer
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(mainSizer)
		
		# spacer
		mainSizer.Add(0, 0, 1)
		
		# sizer along the top bar
		sizerTop = wx.BoxSizer()
		mainSizer.Add(sizerTop, wx.SizerFlags(0).Expand())
		
		# spacer
		sizerTop.Add(0, 0, 1)
		
		# title
		title = Heading(
			parent=self,
			value="Page "+str(className)+", Row "+str(id//numOfCols+1)+", Col "+str(id%numOfCols+1),
		)
		sizerTop.Add(title, wx.SizerFlags(20).Expand())
		
		# exit button
		exitBtn = CustomButton(
			parent=self,
			value="X",
			onClick=lambda evt : onExitClick()
		)
		sizerTop.Add(exitBtn, wx.SizerFlags(0).Centre())
		
		# spacer
		sizerTop.Add(0, 0, 1)
		
		# spacer
		mainSizer.Add(0, 0, 1)
		
		# sizer for centre elements
		sizerCentre = wx.BoxSizer(wx.HORIZONTAL)
		mainSizer.Add(sizerCentre, wx.SizerFlags(20).Expand())
		
		# spacer
		sizerCentre.Add(0, 0, 1)
		
		# main element
		iconButtonSettings = IconButtonSettings(
			parent=self,
			id=id,
			className=className
		)
		sizerCentre.Add(iconButtonSettings, wx.SizerFlags(20).Expand())
		
		# spacer
		sizerCentre.Add(0, 0, 1)
		
		# spacer
		mainSizer.Add(0, 0, 1)
		
		# sizer along the bottom bar
		sizerBottom = wx.BoxSizer()
		mainSizer.Add(sizerBottom, wx.SizerFlags(0).Expand())
		
		# spacer
		sizerBottom.Add(0, 0, 1)
		
		# save button
		saveButton = CustomButton(
			parent=self,
			value="Save",
			onClick=lambda evt : onSaveIconButton()
		)
		sizerBottom.Add(saveButton, wx.SizerFlags(1))
		
		# spacer
		sizerBottom.Add(0, 0, 1)
		
		# spacer
		mainSizer.Add(0, 0, 1)
	
	def render(self):
		pass