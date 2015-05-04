from instagram.client import InstagramAPI
import urllib
import os
import platform

system = platform.system()

def createImageFiles():
	api = InstagramAPI(client_id='7f674565db0d42ed9b4dd4f366db65be', client_secret='9a5f5c38eec74eff9f479e3659d4824f')
	popular_media = api.media_popular(count=20)
	i = 0
	for media in popular_media:
		url =  media.images['standard_resolution'].url
    	urllib.urlretrieve(url, "file"+ str(i) +".jpg")
    	i += 1

def uploadPhotos():
	for x in range(20):
		os.system("scp file" + str(x) + ".jpg gradinsk@radinsky.me:/var/www/html/205/img/")

def openWebPage():
	if(system == "Darwin"):
		os.system("open http://radinsky.me/205")
	elif(system == "Linux"):
		os.system("xdg-open http://radinsky.me/205/ &")
