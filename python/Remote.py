import os

import App
from Server import Server

from components.Plugin import Plugin

def main():
	plugins = [
		Plugin(plugin)
		for plugin in os.listdir("./plugins")
	]

	server = Server()
	server.start()
	App.startApp(
		plugins=plugins,
		onSyncGrid=server.handleSyncGrid,
		onSyncImage=server.handleSyncImage
	)

if __name__ == "__main__":
	main()