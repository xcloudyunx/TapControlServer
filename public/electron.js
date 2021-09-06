const path = require("path");

const { app, BrowserWindow, Tray, Menu } = require("electron");
const isDev = require("electron-is-dev");

function createWindow() {
	// Create the browser window.
	const win = new BrowserWindow({
		width: 600,
		height: 600,
		resizable: false,
		webPreferences: {
			nodeIntegration: true,
		},
	});

	// and load the index.html of the app.
	// win.loadFile("index.html");
	win.loadURL(
		isDev ? "http://localhost:3000" : "file://${path.join(__dirname, '../build/index.html')}"
	);
	// Open the DevTools.
	if (isDev) {
		win.webContents.openDevTools({ mode: "detach" });
	}
  
	let tray = null;

	win.on("minimize", function(event) {
		event.preventDefault();
		win.hide();
		tray = createTray();
	});

	win.on("restore", function(event) {
		win.show();
		tray.destroy();
	});
	
	return win;
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
	mainWindow = createWindow();
});

// Quit when all windows are closed, except on macOS. There, it"s common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on("window-all-closed", () => {
	if (process.platform !== "darwin") {
		app.quit();
	}
});

app.on("activate", () => {
	if (BrowserWindow.getAllWindows().length === 0) {
		createWindow();
	}
});

function createTray() {
	let appIcon = new Tray(path.join(__dirname, "./assets/favicon.png"));
	const contextMenu = Menu.buildFromTemplate([
		{
			label: "Show", click: function () {
				mainWindow.show();
			}
		},
		{
			label: "Exit", click: function () {
				app.isQuiting = true;
				app.quit();
			}
		}
	]);

	appIcon.on("double-click", function (event) {
		mainWindow.show();
	});
	appIcon.setToolTip("remote");
	appIcon.setContextMenu(contextMenu);
	return appIcon;
}