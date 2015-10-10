import json
import requests
import os
import urllib
access_token="CAACEdEose0cBAN2cZBDuWn7mOOUZCG2WuQbcO7peFZBQP0MFr3WkZCBBQqt6dDko4pWsXHm1whImBz2FkiZCBZCpd8mBPGgh2HSVGZCGX6wW2rZAL63I90HF4CsZASVk4PQM5qkPTla2xxJuZAYXXdRfOw7wFUjpyLOOZCBapGhsMzKPUNkgCJPhSZBmDPL3fZASf0S4SJHsVcaWZA73fTsfIlsy2r"
fileR=open("event-id","r")
fileW=open("json", "w")
def get_cover():
	count = 0
	for line in fileR:
		url = "https://graph.facebook.com/v2.5/"+line+"?fields=cover&access_token="+access_token
		r = requests.get(url)
		if r.status_code == 200:
			dic=r.json()
			if dic.has_key('cover'):
				dic2=dic['cover']
			if dic2.has_key('source'):
				download_cover(dic2['source'], str(count)+".jpg")
				count = count + 1
				url2 = "https://graph.facebook.com/v2.5/"+line+"?&access_token="+access_token
				r2=requests.get(url2)
				if r2.status_code == 200:
						json.dump(r2.json(), fileW);

def download_cover(url,name):
	image=urllib.URLopener()
	image.retrieve(url,"cover/"+name)
get_cover()
fileR.close()
fileW.close()
