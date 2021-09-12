import App
from Server import Server

def main():
	server = Server()
	server.start()
	App.startApp(onSync=server.handleSync)

if __name__ == "__main__":
	main()