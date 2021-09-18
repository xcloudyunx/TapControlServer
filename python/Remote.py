import App
from Server import Server

def main():
	server = Server()
	server.start()
	App.startApp(onSyncGrid=server.handleSyncGrid, onSyncImage=server.handleSyncImage)

if __name__ == "__main__":
	main()