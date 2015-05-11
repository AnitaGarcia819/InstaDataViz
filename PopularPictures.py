#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# File name: PopularPictures.py
# Authors: Anita Garcia & Gabriel Radinsky
# Created: 4/2015
# Description: This program queries the Instagram API to retrieve currently trending
#              pictures, store them in .jpg format, and then upload them to a web
#              server. After doing that, it opens the default browser to the webpage
#
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from instagram.client import InstagramAPI
import urllib
import os
import platform

system = platform.system()

#Queries the API to get the currently trending images
def createImageFiles():
	api = InstagramAPI(client_id='7f674565db0d42ed9b4dd4f366db65be', client_secret='9a5f5c38eec74eff9f479e3659d4824f')
	popular_media = api.media_popular(count=20)
	i = 0
	#Stores the pictures into .jpg format, in an easy to access order
	for media in popular_media:
		url =  media.images['standard_resolution'].url
		urllib.urlretrieve(url, "file"+ str(i) +".jpg")
		i += 1

#Uploads all pictures to a remote webhost and removes all previous pictures
def uploadPhotos():
	for x in range(20):
		os.system("scp file" + str(x) + ".jpg gradinsk@radinsky.me:/var/www/html/205/img/")

#Opens a a new tab in the default browser to display the webpage
def openWebPage():
	if(system == "Darwin"):
		os.system("open http://radinsky.me/205")
	elif(system == "Linux"):
		os.system("xdg-open http://radinsky.me/205/ &")
