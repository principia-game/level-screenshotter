from config import *
from pathlib import Path
import json
import os
import requests
import time
import urllib3

headers = {'User-Agent': 'ohmygoshcuddles'}

def screenshot(id):
	Path("thumbs/").mkdir(exist_ok=True)
	Path("thumbs_low/").mkdir(exist_ok=True)
	Path("screenshots/").mkdir(exist_ok=True)

	data = requests.get(f"https://principia-web.se/internal/get_level?i={id}", headers=headers)

	if data.status_code == 200:
		with open(f".p/storage/lvl/db/{id}.plvl", 'wb') as file:
			file.write(data.content)
	else:
		print("wah >.<")
		return

	os.system(f"./.p/principia principia://principia-web.se/play/lvl/db/{id}")

	statefile = Path(".p/principia.state")
	while True:
		time.sleep(0.25)
		if not statefile.is_file():
			break

	raw_screenshot = f".p/ss-0.png"
	screenshot = f"screenshots/{id}.png"

	os.system(f"mv {raw_screenshot} {screenshot}")

	os.system(f"convert {screenshot} -quality 85 thumbs/{id}.jpg")

	os.system(f"convert {screenshot} -resize 240 -unsharp 0x0.55+0.55+0.008 -quality 92 thumbs_low/{id}.jpg")

def main():
	http = urllib3.PoolManager()
	data = json.loads(http.request('GET','https://principia-web.se/internal/levels_with_no_thumbs').data)

	for level in data['levels_with_no_thumbs']:
		print("doing "+str(level))
		screenshot(level)

	os.system(f"rsync -azP thumbs/* {RSYNC_REMOTE}/data/thumbs/")
	os.system(f"rsync -azP thumbs_low/* {RSYNC_REMOTE}/data/thumbs_low/")

if __name__ == "__main__":
	main()
