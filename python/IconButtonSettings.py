import wx

import colors

from IconButton import IconButton

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
		
		file = wx.FilePickerCtrl(
			parent=self#,
			#wildCard=
		)
		print(file.GetPath())
		#file.SetInitialDirectory() # asset directory from plugins?
		sizer.Add(file)
		
	
	def render(self):
		pass