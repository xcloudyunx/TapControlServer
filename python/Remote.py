# change imports if change to sys.argv
import importlib
import pkgutil

import plugins

import App
from Server import Server

def main():
	pluginList = [
		importlib.import_module(name)
		for finder, name, ispkg
		in pkgutil.iter_modules(plugins.__path__, plugins.__name__+".")
	]

	server = Server()
	server.start()
	App.startApp(
		pluginList=pluginList,
		onSyncGrid=server.handleSyncGrid,
		onSyncImage=server.handleSyncImage
	)

if __name__ == "__main__":
	main()