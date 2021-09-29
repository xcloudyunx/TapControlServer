import wx

class RequiredDialogBox(wx.MessageDialog):
	def __init__(self, parent):
		super().__init__(
			parent=parent,
			message="Please fill in all required fields.",
			caption="Error"
			)
		
		self.ShowModal()