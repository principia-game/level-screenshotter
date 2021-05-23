import screenshotter
import os
import urllib3
import json
from config import *
from ftplib import FTP
from pathlib import Path

def main():
	http = urllib3.PoolManager()
	data = json.loads(http.request('GET','%s/internal/levels_with_no_thumbs.php' % DOMAIN).data)

	os.system("principia &")
	print("vänta")
	input()

	print("ok")

	for level in data['levels_with_no_thumbs']:
		print("doing "+str(level))
		screenshotter.main(level)

	with FTP(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD) as ftp:
		ftp.set_pasv(False)
		ftp.cwd(FTP_THUMBDIR)
		for level in data['levels_with_no_thumbs']:
			with open("thumbs/%s.jpg" % level, 'rb') as fil:
				ftp.storbinary('STOR %s.jpg' % level, fil)


if __name__ == "__main__":
	main()