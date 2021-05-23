Xvfb :0 -screen 0 1280x720x24 &
DISPLAY=:0.0 wine /mnt/principia/principia.exe principia://play/lvl/local/$1 &
import -display :0 -window root image.jpg
