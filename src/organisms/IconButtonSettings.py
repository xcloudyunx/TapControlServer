import wx
import json

from config import colors

from src.atoms.CustomButton import CustomButton
from src.atoms.DummyIconButton import DummyIconButton
from src.molecules.FileInput import FileInput
from src.molecules.ChoiceInput import ChoiceInput
from src.organisms.PluginPropertiesSettings import PluginPropertiesSettings
   
class IconButtonSettings(wx.Panel):    
	def __init__(self, parent, id, plugins, defaultValues):
		super().__init__(parent=parent)
		
		self.info = {"id": id, "name": None}
		
		self.plugins = plugins
		
		self.pluginPropertiesSettings = None
		
		self.defaultValues = defaultValues[1] if defaultValues else None
		
		self.SetBackgroundColour(colors.secondary)
		
		# main sizer
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.mainSizer)
		
		self.sizerTop = wx.BoxSizer(wx.VERTICAL)
		self.mainSizer.Add(self.sizerTop, wx.SizerFlags(20).Expand())
		
		self.mainSizer.Add(0, 0, 1)
		
		self.mainSizer.Add(0, 0, 19)
		
		# sizerTop
		self.sizerTop.Add(0, 0, 1)
		
		# first row
		sizerRow = wx.BoxSizer()
		self.sizerTop.Add(sizerRow, wx.SizerFlags(0).Expand())
		
		# spacer
		sizerRow.Add(0, 0, 1)
		
		# preview icon image
		self.icon = DummyIconButton(
			parent=self,
			id=self.info["id"],
			buttonDim=100, #still need to decide on this size
		)
		sizerRow.Add(self.icon, wx.SizerFlags(0).Centre())
		
		# spacer
		sizerRow.Add(0, 0, 1)
		
		removeIconButton = CustomButton(
			parent=self,
			value="Remove Icon",
			onClick=self.handleRemoveIconImage
		)
		sizerRow.Add(removeIconButton, wx.SizerFlags(0).Centre())
		
		# spacer
		sizerRow.Add(0, 0, 1)
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# file picker for icon image
		self.imageFilePicker = FileInput(
			parent=self,
			title="Icon",
			settings="Images (*.png,*.jpg)|*.png;*.jpg",
			onChange=lambda _, path : self.icon.update(path)
		)
		self.sizerTop.Add(self.imageFilePicker, wx.SizerFlags(0).Expand())
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# choose command
		self.command = ChoiceInput(
			parent=self,
			title="Command",
			settings=[""]+[plugin for plugin in self.plugins],
			onChange=self.handleChangeCommand,
			default=defaultValues[0] if defaultValues else None
		)
		self.sizerTop.Add(self.command, wx.SizerFlags(0).Expand())
		
	def handleChangeCommand(self, title, pluginName, default=None):
		if self.info["name"] != pluginName:
			self.mainSizer.Remove(2)
			try:
				self.pluginPropertiesSettings.Destroy()
				self.pluginPropertiesSettings = None
			except:
				pass
			
			self.info["name"] = pluginName
			
			if pluginName:
				plugin = self.plugins[pluginName]
					
				self.pluginPropertiesSettings = PluginPropertiesSettings(
					parent=self,
					title=title,
					plugin=plugin,
					handleChangeProperty=self.handleChangeProperty,
					defaultValues=self.defaultValues,
					default=default
				)
				
				self.mainSizer.Add(self.pluginPropertiesSettings, wx.SizerFlags(19).Expand())
			else:
				self.mainSizer.Add(0, 0, 19)
			
			self.mainSizer.Layout()
		
	def handleChangeProperty(self, property, propertyValue, _=None):
		self.info[property] = propertyValue
		
	def handleRemoveIconImage(self, evt):
		self.imageFilePicker.reset()
		self.icon.update(None)
	
	def retreiveInfo(self):
		if self.checkRequired():
			self.icon.saveImage()
			return self.info
		else:
			return False
		
	def checkRequired(self):
		pluginName = self.info["name"]
		if pluginName:
			plugin = self.plugins[pluginName]
			for property in plugin.getProperties():
				if plugin.isPropertyRequired(property) and property not in self.info:
					return False
		return True