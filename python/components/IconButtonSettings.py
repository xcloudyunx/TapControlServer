import wx
# change imports if change to sys.argv
import importlib
import pkgutil

import plugins

from config import colors

from components.IconButton import IconButton

class IconButtonSettings(wx.ScrolledWindow):    
	def __init__(self, parent, id, className):
		super().__init__(parent=parent)
		
		self.SetBackgroundColour(colors.secondary)
		
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
		self.plugins = {
			name: importlib.import_module(name)
			for finder, name, ispkg
			in pkgutil.iter_modules(plugins.__path__, plugins.__name__+".")
		}
		for finder, name, ispkg in pkgutil.iter_modules(plugins.__path__, plugins.__name__+"."):
			print(name)
		choices = [self.plugins[plugin].getName() for plugin in self.plugins]
		command = wx.Choice(
			parent=self,
			# choices=choices
		)
		sizer.Add(command, wx.SizerFlags(0))
		
	
	def render(self):
		pass