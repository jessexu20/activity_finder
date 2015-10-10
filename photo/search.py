import json
import requests
import os
#access_token="853851641394176|b09327fcb2c560c8fe211b5720bdf81c"
access_token="CAACEdEose0cBAOZArhltcUfywY8AkkwzuIMqlFqOjwWELehmZCWnnxpKqAcjW4kxh2ckuuXodgccBeZC4m0YmvSYrYSOAXTPi9bgHJt4gpEuKMalxfRFimFG5JJF8prQWjWB5SYKJEAHwf8NRgwOtp1euZAYAoB55hE12vsGowqMM2qy2mZBJxd3R8VhBiOlDvoF3Ggk4iZC7c4HRQKhYP"
search_word="raleigh"
fileW=open("event-id", "w")
def fb_event():
	url = "https://graph.facebook.com/search?q="+search_word+"&type=event&access_token="+access_token
	r = requests.get(url)
	if r.status_code == 200:
		for event in r.json()["data"]:
			#print event["id"]
			fileW.write(event["id"]+"\n")
#			print event
#	with open("json","w") as outfile:
#		json.dump(r.json(), outfile)
fb_event()
fileW.close()
