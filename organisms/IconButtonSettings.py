import wx
import wx.lib.scrolledpanel

from config import colors

from atoms.CustomButton import CustomButton
from atoms.DummyIconButton import DummyIconButton
from molecules.FileInput import FileInput
from molecules.ChoiceInput import ChoiceInput

class IconButtonSettings(wx.lib.scrolledpanel.ScrolledPanel):    
	def __init__(self, parent, id, className, plugins, defaultValues):
		super().__init__(parent=parent)
		
		self.info = {"page": className, "id": id, "name": None}
		
		self.plugins = plugins
		
		self.defaultValues = defaultValues[1] if defaultValues else None
		
		self.SetBackgroundColour(colors.secondary)
		
		# main sizer
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(mainSizer)
		
		self.sizerTop = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(self.sizerTop, wx.SizerFlags(2).Expand())
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# first row
		sizerRow = wx.BoxSizer()
		self.sizerTop.Add(sizerRow, wx.SizerFlags(0).Expand())
		
		# spacer
		sizerRow.Add(0, 0, 1)
		
		# preview icon image
		self.icon = DummyIconButton(
			parent=self,
			id=id,
			className=className,
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
			wildcard="Images (*.png,*.jpg)|*.png;*.jpg",
			onChangeFile=lambda _, path : self.icon.update(path)
		)
		self.sizerTop.Add(self.imageFilePicker, wx.SizerFlags(0).Expand())
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# sizer to hold properties
		self.sizerBottom = wx.StaticBoxSizer(wx.VERTICAL, self)
		self.sizerBottom.GetStaticBox().Hide()
		mainSizer.Add(self.sizerBottom, wx.SizerFlags(1).Expand().ReserveSpaceEvenIfHidden())
		
		# choose command
		self.command = ChoiceInput(
			parent=self,
			title="Command",
			choices=[""]+[plugin for plugin in self.plugins],
			onChangeChoice=self.handleChangeCommand,
			default=defaultValues[0] if defaultValues else None
		)
		self.sizerTop.Add(self.command, wx.SizerFlags(0).Expand())
		
		wx.CallAfter(self.afterInit)
		
	def afterInit(self):
		self.sizerTop.SetMinSize(wx.Size(self.sizerTop.GetMinSize().width, self.sizerTop.GetSize().height))
		self.GetSizer().GetItem(self.sizerTop).SetProportion(0)
		# self.GetSizer().GetItem(self.sizerBottom).SetProportion(0)
		
	def handleChangeCommand(self, title, pluginName, default=None):
		if self.info["name"] != pluginName:
			self.sizerBottom.Clear(True)
			
			self.info["name"] = pluginName
			
			if pluginName:
				plugin = self.plugins[pluginName]
				
				# spacer
				self.sizerBottom.Add(0, 0, 1)
				
				for property in plugin.getProperties():
					propertyType = plugin.getPropertyType(property)
					if propertyType == "choice":
						userInput = ChoiceInput(
							parent=self,
							title=property,
							choices=plugin.getPropertySettings(property),
							onChangeChoice=self.handleChangeProperty,
							default=(self.defaultValues[property] if property in self.defaultValues else None) if default else None,
							required=plugin.isPropertyRequired(property)
						)
					elif propertyType == "file":
						userInput = FileInput(
							parent=self,
							title=property,
							wildcard=plugin.getPropertySettings(property),
							onChangeFile=self.handleChangeProperty,
							default=(self.defaultValues[property] if property in self.defaultValues else None) if default else None,
							required=plugin.isPropertyRequired(property)
						)
					self.sizerBottom.Add(userInput, wx.SizerFlags(0).Expand())
								
					# spacer
					self.sizerBottom.Add(0, 0, 1)
				
				self.sizerBottom.SetMinSize(wx.Size(self.sizerBottom.GetMinSize().width, self.sizerBottom.GetItem(1).GetSize().height*self.sizerBottom.GetItemCount()//2*1.5))
				self.sizerBottom.GetStaticBox().Show()
				self.GetSizer().Layout()
				self.SetupScrolling()
			else:
				self.sizerBottom.GetStaticBox().Hide()
				self.GetSizer().Layout()
		
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