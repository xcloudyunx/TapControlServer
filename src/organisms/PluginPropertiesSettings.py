import wx
import wx.lib.scrolledpanel

from src.molecules.FileInput import FileInput
from src.molecules.ChoiceInput import ChoiceInput
from src.molecules.TextInput import TextInput

class PluginPropertiesSettings(wx.lib.scrolledpanel.ScrolledPanel):
	def __init__(self, parent, title, plugin, handleChangeProperty, defaultValues, default=None):
		super().__init__(parent=parent)
		
		self.SetWindowStyle(wx.BORDER_SIMPLE)
		
		# sizer to hold properties
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.sizer)
		
		# spacer
		self.sizer.Add(0, 5, 0)
		
		for property in plugin.getProperties():
			propertyType = plugin.getPropertyType(property)
			if propertyType == "choice":
				userInput = ChoiceInput()
			elif propertyType == "file":
				userInput = FileInput()
			elif propertyType == "text":
				userInput = TextInput()
			userInput.Create(
				parent=self,
				title=property,
				settings=plugin.getPropertySettings(property),
				onChange=handleChangeProperty,
				default=(defaultValues[property] if property in defaultValues else None) if default else None,
				required=plugin.isPropertyRequired(property)
			)
			self.sizer.Add(userInput, wx.SizerFlags().Expand())
						
			# spacer
			self.sizer.Add(0, 10, 0)
		
		self.SetupScrolling(scroll_x=False)
		
	def handleRemoveIconImage(self, evt):
		self.imageFilePicker.reset()
		self.icon.update(None)