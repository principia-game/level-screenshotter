import screenshotter
import os
import urllib3
import json
import time
from config import *

def main():
	http = urllib3.PoolManager()
	data = json.loads(http.request('GET','%s/levels_with_no_thumbs' % DOMAIN).data)

	os.system("principia &")
	print("läumching principaa")
	#print("vänta")
	#input()
	time.sleep(6)

	print("ok")

	for level in data['levels_with_no_thumbs']:
		print("doing "+str(level))
		screenshotter.main(level)

	os.system("rsync -azP thumbs/* %s:%s/data/thumbs/" % (SERVER_SSH, SERVER_DIR))
	os.system("rsync -azP thumbs_low/* %s:%s/data/thumbs_low/" % (SERVER_SSH, SERVER_DIR))

if __name__ == "__main__":
	main()
