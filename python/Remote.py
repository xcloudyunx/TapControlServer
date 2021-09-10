import threading

import App
import Server

def main():
	threading.Thread(target=Server.startServer, daemon=True).start()
	App.startApp()

if __name__ == "__main__":
	main()