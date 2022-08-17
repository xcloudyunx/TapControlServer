import wx

from src.molecules.PluginCheckListBox import PluginCheckListBox

class PluginManagerNotebookPanel(wx.Panel):
	def __init__(self, parent, plugins, onFocus):
		super().__init__(
			parent=parent
		)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)
		
		#idx = self.FindItem(start=-1, str="searching for this string", partial=True) for searching
		# need to trigger above for each character press and then do 
		#self.Focus(idx) to highlight item
		
		self.checkListBox = PluginCheckListBox(
			parent=self,
			plugins=plugins,
			onFocus=onFocus
		)
		sizer.Add(self.checkListBox, wx.SizerFlags(1).Expand())