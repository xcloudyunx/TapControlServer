import wx

from src.atoms.Label import Label

class FileInput(wx.Panel):    
	def __init__(self, parent, title, wildcard, onChangeFile, default=None, required=False):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=("*" if required else "")+title+":"
		)
		sizer.Add(label, wx.SizerFlags(6).Expand())
		
		self.filePicker = wx.FilePickerCtrl(
			parent=self,
			wildcard=wildcard,
			size=wx.Size(1, 1)
		)
		# print(imageFilePicker.GetPath())
		#imageFilePicker.SetInitialDirectory() # asset directory from plugins?
		sizer.Add(self.filePicker, wx.SizerFlags(8).Expand())
		if default:
			self.filePicker.SetPath(default)
			onChangeFile(title, default, True)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		self.filePicker.Bind(wx.EVT_FILEPICKER_CHANGED, lambda evt : onChangeFile(title, self.filePicker.GetPath()))
	
	def reset(self):
		self.filePicker.SetPath("")