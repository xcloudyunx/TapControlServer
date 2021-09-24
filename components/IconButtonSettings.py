import wx

from config import colors

from components.IconButton import IconButton

class IconButtonSettings(wx.ScrolledWindow):    
	def __init__(self, parent, id, className, plugins):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.secondary)
		
		self.plugins = plugins
		
		# main sizer
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		self.icon = IconButton(
			parent=self,
			id=id,
			className=className,
			buttonDim=100, #still need to decide on this size
			onClick=lambda className, id : None
		)
		sizer.Add(self.icon, wx.SizerFlags(0))
		
		imageFilePicker = wx.FilePickerCtrl(
			parent=self,
			wildcard=("Images (*.png,*.jpg)|*.png;*.jpg")
		)
		# print(imageFilePicker.GetPath())
		#imageFilePicker.SetInitialDirectory() # asset directory from plugins?
		sizer.Add(imageFilePicker, wx.SizerFlags(0))
		
		# may change the below to sys.argv stuff for when its compiled
		choices = [plugin.getName() for plugin in self.plugins]
		self.command = wx.Choice(
			parent=self,
			choices=choices
		)
		sizer.Add(self.command, wx.SizerFlags(0))
		
		self.command.Bind(wx.EVT_CHOICE, self.changeCommand)
		
	def changeCommand(self, evt):
		plugin = self.plugins[self.command.GetSelection()]
		
		# something to do with plugins.getProperties()
		
		self.GetSizer().Layout()