import os

import src.App as App
from src.Server import Server

from src.atoms.Plugin import Plugin

def main():
	plugins = {}
	for file in os.listdir("./plugins"):
		plugin = Plugin(file)
		plugins[plugin.getName()] = plugin

	server = Server(plugins)
	server.start()
	App.startApp(
		plugins=plugins,
		commands=server.commands,
		state=server.state,
		onSyncState=server.handleSyncState,
		onSyncImage=server.handleSyncImage,
		onSyncAll=server.syncAll
	)

if __name__ == "__main__":
	main()