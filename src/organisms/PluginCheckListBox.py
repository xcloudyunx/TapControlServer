import wx

from config import colors

class PluginCheckListBox(wx.ListCtrl):
	def __init__(self, parent, plugins):
		super().__init__(
			parent=parent,
			style=wx.LC_REPORT
		)
		
		#idx = self.FindItem(start=-1, str="searching for this string", partial=True) for searching
		# need to trigger above for each character press and then do 
		#self.Focus(idx) to highlight item
		
		self.EnableCheckBoxes()
		headerAttr = wx.ItemAttr()
		headerAttr.SetFont(headerAttr.GetFont().Bold())
		self.SetHeaderAttr(headerAttr)
		
		self.AppendColumn("Plugin")
		self.AppendColumn("Version")
		
		for plugin in plugins:
			self.Append([plugin, "Insert Version Number Here"])
		
		self.Hide()