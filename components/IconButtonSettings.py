import wx
import wx.lib.scrolledpanel

from config import colors

from components.IconButton import IconButton
from components.FileInput import FileInput
from components.ChoiceInput import ChoiceInput

class IconButtonSettings(wx.lib.scrolledpanel.ScrolledPanel):    
	def __init__(self, parent, id, className, plugins):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.secondary)
		
		self.plugins = plugins
		
		# main sizer
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(mainSizer)
		
		self.sizerTop = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(self.sizerTop, wx.SizerFlags(2).Expand())
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# preview icon image
		self.icon = IconButton(
			parent=self,
			id=id,
			className=className,
			buttonDim=100, #still need to decide on this size
			onClick=lambda className, id : None
		)
		self.sizerTop.Add(self.icon, wx.SizerFlags(0).Centre())
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# file picker for icon image
		imageFilePicker = FileInput(
			parent=self,
			title="Icon",
			wildcard="Images (*.png,*.jpg)|*.png;*.jpg"
		)
		self.sizerTop.Add(imageFilePicker, wx.SizerFlags(0).Expand())
		
		# spacer
		self.sizerTop.Add(0, 0, 1)
		
		# choose command
		self.command = ChoiceInput(
			parent=self,
			title="Command",
			choices=[plugin.getName() for plugin in self.plugins],
			onChangeChoice=self.handleChangeCommand
		)
		self.sizerTop.Add(self.command, wx.SizerFlags(0).Expand())
		
		# sizer to hold properties
		self.sizerBottom = wx.StaticBoxSizer(wx.VERTICAL, self)
		self.sizerBottom.GetStaticBox().Hide()
		mainSizer.Add(self.sizerBottom, wx.SizerFlags(1).Expand().ReserveSpaceEvenIfHidden())
		
		wx.CallAfter(self.afterInit)
		
	def afterInit(self):
		self.sizerTop.SetMinSize(wx.Size(self.sizerTop.GetMinSize().width, self.sizerTop.GetSize().height))
		self.GetSizer().GetItem(self.sizerTop).SetProportion(0)
		
	def handleChangeCommand(self, selection):
		self.sizerBottom.Clear(True)
	
		plugin = self.plugins[selection]
		
		# spacer
		self.sizerBottom.Add(0, 0, 1)
		
		for property in plugin.getProperties():
			propertyType = plugin.getPropertyType(property)
			if propertyType == "choice":
				userInput = ChoiceInput(
					parent=self,
					title=property,
					choices=plugin.getPropertySettings(property),
					onChangeChoice=None
				)
			elif propertyType == "file":
				userInput = FileInput(
					parent=self,
					title=property,
					wildcard=plugin.getPropertySettings(property)
				)
			self.sizerBottom.Add(userInput, wx.SizerFlags(0).Expand())
						
			# spacer
			self.sizerBottom.Add(0, 0, 1)
		
		self.sizerBottom.SetMinSize(wx.Size(self.sizerBottom.GetMinSize().width, self.sizerBottom.GetItem(1).GetSize().height*self.sizerBottom.GetItemCount()//2*1.5))
		self.sizerBottom.GetStaticBox().Show()
		self.GetSizer().Layout()
		self.SetupScrolling()