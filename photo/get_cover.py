import json
import requests
import os, sys
import urllib
from PIL import Image
access_token="CAACEdEose0cBAA6w3tRDSWsr4Vd0VrZBu83niDh2ctsVfZAsT3xj3E5q2hQB73UtxyRgMoiSl75PnB7JVD9LF5VgyVRCPdOhYztAyvFWvkCUDkJBMshgnFdWJwWzK48bl1BswpbVnznau5Ta2hLegqRRAZBalUYEcipCTAjw3rJD3JXn6lfGOUMqEuOHVFmIvQBQe8LfZCc3qiVXrqEw"
fileR=open("event-id","r")
fileW=open("json", "w")
def get_cover():
    # param={
    #     "name": "",
    #     "id":"",
    #     "description":"",
    #     "start_time":"",
    #     "end_time":"",
    #     "longtitude":0,
    #     "latitude":0,
    #     "city":"",
    #     }
    # }
    count = 0
    for line in fileR:
        if count > 1:
            break;
        url = "https://graph.facebook.com/v2.5/"+line+"?fields=cover&access_token="+access_token#has cover
        r = requests.get(url)
        if r.status_code == 200:
            dic=r.json()
            if dic.has_key('cover'):
                dic2=dic['cover']
                if dic2.has_key('source'):
                    url2 = "https://graph.facebook.com/v2.5/"+line+"?&access_token="+access_token
                    r2=requests.get(url2)
                    if r2.status_code == 200:
                        eventjson=r2.json();
                        if eventjson.has_key('place')==False or eventjson.has_key('description')==False or eventjson.has_key('name')==False or eventjson.has_key('start_time')==False or eventjson.has_key('end_time')==False :
                            continue
                        placejson=eventjson['place']
                        if(placejson.has_key('location') and placejson['location'].has_key('longitude') and placejson['location'].has_key('latitude') and placejson['location'].has_key('city')):
                            download_cover(dic2['source'], str(count)+".jpg")
                            count = count + 1
                            param={}
                            param['name']=eventjson['name']
                            param['id']=str(count)
                            param['description']=eventjson['description']
                            param['start_time']=eventjson['start_time']
                            param['end_time']=eventjson['end_time']
                            param['longtitude']=placejson['location']['longitude']
                            param['latitude']=placejson['location']['latitude']
                            param['city']=placejson['location']['city']
                            # print param
                            json.dump(param, fileW,sort_keys=True);
def download_cover(url,name):
	image=urllib.URLopener()
	image.retrieve(url,"cover/"+name)
	im = Image.open("cover/"+name)
	im_resize = im.resize((650, 350), Image.ANTIALIAS)
	im_resize.save("cover/"+name)
get_cover()
fileR.close()
fileW.close()
with open('json') as data_file:    
    data = json.load(data_file)

print(data)
