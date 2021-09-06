import wx, wx.adv

class MainFrame(wx.Frame):    
	def __init__(self):
		super().__init__(parent=None, title='Remote Server')
		
		self.Show()

def main():
	app = wx.App()
	frame = MainFrame()
	app.MainLoop()
			

if __name__ == "__main__":
	main()