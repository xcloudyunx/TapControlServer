import wx

class SyncDialogBox(wx.ProgressDialog):
	def __init__(self, onSyncAll):
		super().__init__(
			title="Syncing...",
			message="Syncing...",
			style=wx.PD_APP_MODAL|wx.PD_SMOOTH
			)
		
		if not onSyncAll(self):
			self.Update(100, "No client detected.")