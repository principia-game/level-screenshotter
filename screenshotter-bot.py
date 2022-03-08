import screenshotter
import os
import urllib3
import json
import time
from config import *

def main():
	http = urllib3.PoolManager()
	data = json.loads(http.request('GET','%s/internal/levels_with_no_thumbs.php' % DOMAIN).data)

	os.system("principia &")
	print("läumching principaa")
	#print("vänta")
	#input()
	time.sleep(6)

	print("ok")

	for level in data['levels_with_no_thumbs']:
		print("doing "+str(level))
		screenshotter.main(level)

	os.system("scp thumbs/%s.jpg %s:%s/levels/thumbs/" % (level, SERVER_SSH, SERVER_DIR))
	os.system("scp thumbs/low/%s.jpg %s:%s/levels/thumbs/low/" % (level, SERVER_SSH, SERVER_DIR))

if __name__ == "__main__":
	main()
