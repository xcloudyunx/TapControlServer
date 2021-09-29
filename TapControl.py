import os

import App
from Server import Server

from atoms.Plugin import Plugin

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
		onSync=server.handleSync
	)

if __name__ == "__main__":
	main()