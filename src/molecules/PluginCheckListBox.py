import wx

class PluginCheckListBox(wx.ListCtrl):
	def __init__(self, parent, plugins, onFocus):
		super().__init__(
			parent=parent,
			style=wx.LC_REPORT
		)
		
		self.EnableCheckBoxes()
		headerAttr = wx.ItemAttr()
		headerAttr.SetFont(headerAttr.GetFont().Bold())
		self.SetHeaderAttr(headerAttr)
		
		self.AppendColumn("Plugin")
		self.AppendColumn("Version")
		
		for pluginInfo in plugins:
			self.Append(pluginInfo)
			
		self.Bind(wx.EVT_LIST_ITEM_FOCUSED, onFocus)