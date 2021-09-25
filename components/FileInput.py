import wx

from config import colors

from components.Label import Label

class FileInput(wx.Panel):    
	def __init__(self, parent, title, wildcard):
		super().__init__(parent=parent)
		
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())
		
		label = Label(
			parent=self,
			value=title+":"
		)
		sizer.Add(label, wx.SizerFlags(6).Expand())
		
		filePicker = wx.FilePickerCtrl(
			parent=self,
			wildcard=wildcard,
			size=wx.Size(1, 1)
		)
		# print(imageFilePicker.GetPath())
		#imageFilePicker.SetInitialDirectory() # asset directory from plugins?
		sizer.Add(filePicker, wx.SizerFlags(8).Expand())
		
		sizer.Add(0, 0, wx.SizerFlags(1).Expand())