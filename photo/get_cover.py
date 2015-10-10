import json
import requests
import os
import urllib
access_token="CAACEdEose0cBAOZArhltcUfywY8AkkwzuIMqlFqOjwWELehmZCWnnxpKqAcjW4kxh2ckuuXodgccBeZC4m0YmvSYrYSOAXTPi9bgHJt4gpEuKMalxfRFimFG5JJF8prQWjWB5SYKJEAHwf8NRgwOtp1euZAYAoB55hE12vsGowqMM2qy2mZBJxd3R8VhBiOlDvoF3Ggk4iZC7c4HRQKhYP"
fileR=open("event-id","r")
def get_cover():
	for line in fileR:
		url = "https://graph.facebook.com/v2.5/"+line+"?fields=cover&access_token="+access_token
		r = requests.get(url)
		if r.status_code == 200:
			dic=r.json()
			if dic.has_key('cover'):
				dic2=dic['cover']
			if dic2.has_key('source'):
				download_cover(dic2['source'], line+".jpg")

def download_cover(url,name):
	image=urllib.URLopener()
	image.retrieve(url,"cover/"+name)
get_cover()
fileR.close()
