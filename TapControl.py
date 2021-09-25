import os

import App
from Server import Server

from components.Plugin import Plugin

def main():
	plugins = {}
	for file in os.listdir("./plugins"):
		plugin = Plugin(file)
		plugins[plugin.getName()] = plugin

	server = Server()
	server.start()
	App.startApp(
		plugins=plugins,
		onSyncGrid=server.handleSyncGrid,
		onSyncImage=server.handleSyncImage
	)

if __name__ == "__main__":
	main()