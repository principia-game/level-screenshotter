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

	os.system("rsync -azP thumbs/* %s:%s/levels/thumbs/" % (SERVER_SSH, SERVER_DIR))

if __name__ == "__main__":
	main()
