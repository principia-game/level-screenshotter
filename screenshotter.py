from PIL import ImageGrab
import os
import sys
import time
from config import *
from pathlib import Path

def main(input_file, namespace = 'db'):
	Path("thumbs/low/").mkdir(parents=True, exist_ok=True)
	
	os.system("principia principia://play/lvl/%s/%s &" % (namespace, input_file))
	time.sleep(2)
	image = ImageGrab.grab(bbox=(
		(MONITOR_WIDTH - PRINCIPIA_WIDTH) / 2,
		(MONITOR_HEIGHT - PRINCIPIA_HEIGHT) / 2,
		(MONITOR_WIDTH - PRINCIPIA_WIDTH) / 2 + PRINCIPIA_WIDTH,
		(MONITOR_HEIGHT - PRINCIPIA_HEIGHT) / 2 + PRINCIPIA_HEIGHT))
	image.save("thumbs/%s.%s" % (input_file, IMAGEFORMAT))

	os.system("convert thumbs/%s.%s -resize 240 -unsharp 0x0.55+0.55+0.008 -quality 90 thumbs/low/%s.%s" % (input_file, IMAGEFORMAT, input_file, IMAGEFORMAT))

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("gimmie a level id uwu")
	else:
		if len(sys.argv) < 3:
			main(sys.argv[1], sys.argv[2])
		else:
			main(sys.argv[1])
