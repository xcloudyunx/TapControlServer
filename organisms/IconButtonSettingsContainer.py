import wx

from atoms.CustomButton import CustomButton
from atoms.TextElement import TextElement
from atoms.Heading import Heading
from organisms.IconButtonSettings import IconButtonSettings
from pages.RequiredDialogBox import RequiredDialogBox

class IconButtonSettingsContainer(wx.Panel):    
	def __init__(self, parent, className, id, numOfCols, onExitClick, onSaveIconButton, plugins, defaultValues):
		super().__init__(parent=parent)
		
		self.onSaveIconButton = onSaveIconButton
		
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
		self.iconButtonSettings = IconButtonSettings(
			parent=self,
			id=str(className)+"-"+str(id),
			plugins=plugins,
			defaultValues=defaultValues
		)
		sizerCentre.Add(self.iconButtonSettings, wx.SizerFlags(20).Expand())
		
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
			onClick=self.handleSaveButtonClick
		)
		sizerBottom.Add(saveButton, wx.SizerFlags(1))
		
		# spacer
		sizerBottom.Add(0, 0, 1)
		
		# spacer
		mainSizer.Add(0, 0, 1)
	
	def handleSaveButtonClick(self, evt):
		# retrieve values
		info = self.iconButtonSettings.retreiveInfo()
	
		# only save if all required fields have been filled
		if info:
			self.onSaveIconButton(info)
		else:
			# popup dialog saying to fill in all required fields
			RequiredDialogBox(self)