# level-screenshotter
This repository contains the screenshotting scripts I use for making level thumbnails on principia-web.

These scripts are rather lazily done and has various hardcoded values and functionality intended for my setup (System install of Principia on Linux, containing Reshade), which might need to be changed.

## Python version
The Python version is currently the one that is being used for making level thumbnails, and the one that would work the best.

Despite various hardcoded goodness, there is a config file. Here's the required values, along with some sane defaults.
```python
DOMAIN = "http://principia-web.uwu"

MONITOR_WIDTH = 1920
MONITOR_HEIGHT = 1080

PRINCIPIA_WIDTH = 1280
PRINCIPIA_HEIGHT = 720

IMAGEFORMAT = "jpg"

FTP_SERVER   = "[ftp server]"
FTP_USERNAME = "[username]"
FTP_PASSWORD = "[password]"
FTP_THUMBDIR = "/srv/http/principia-web/levels/thumbs/"
```
Paste the code into a file called `config.py`.

Beyond being able to automatically take screenshots of new community levels, screenshotter.py can act as a standalone level screenshotter that can take any level you put in. Simply put the level ID and then namespace like `python screenshotter.py <level id> <namespace>`. Namespace can be `local` for local levels saved in your Principia home folder, `db` for levels on the current community site that the game is connected to, and `main` for built in levels.

There's also a `toggle-gui.py` file that can quickly disable or enable the GUI of Principia. **It needs to be closed first or else it'll override the changed settings!**

## Xvfb version
The Xvfb version is a simple shell script called `screenshotter.sh` that was written to take screenshots headlessly and automatically with no user interaction, initially intended to be run on the principia-web server. It was put on hold and replaced with the Python version as the server currently isn't able to run Principia, but is being included here for completedness.