import wx

class SyncDialogBox(wx.ProgressDialog):
	def __init__(self):
		super().__init__(
			title="Syncing...",
			message="Syncing...",
			style=wx.PD_APP_MODAL|wx.PD_SMOOTH
			)