
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from instagram.client import InstagramAPI
import httplib2
import json
import urllib
from  urllib import urlopen
import time



def getCityLatandLng(choice):
	if choice == 1: #LA
		lat = 33
		lng = 118

	elif choice == 2: #NYC
		lat = 40
		lng = 73

	elif choice == 3: #SF
		lat = 37
		lng = 122

	return lat, lng

def storesTags(lat, lng):  
    file = urlopen("https://api.instagram.com/v1/media/search?lat="+str(lat)+"&lng="+str(lng)+"&access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
    data = json.loads(file)

    tagsTempArray = []

    for data in data["data"]:
        if data ['tags'] != '':
          	tag = data['tags']
          	tagsTempArray.append(tag)
    
    tagsArray = []
    for element in tagsTempArray:
    	for tag in element:
    		tagsArray.append(tag)
    string = ' '.join(tagsArray)
    return string


def openEastCoastCloud():
    TEXT = storesTags(40, 73) #New York City 
    TEXT += ' ' + storesTags(42.3744, 71.1169) #Harvard
    TEXT += ' ' + storesTags(42.3598, 71.0921)  #MIT
    TEXT = storesTags(38.9072, 77.0728) #GeorgeTown University 
    TEXT += ' ' + storesTags(42.3496, 71.0997) #Boston University

    tags = make_tags(get_tag_counts(TEXT), maxsize=80)

    create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

    import webbrowser
    webbrowser.open('cloud_large.png') # see results

def openWestCoastCloud():
    TEXT = storesTags(34,118) #Los Angeles
    TEXT += ' ' + storesTags(37,122) # San Francisco 
    TEXT += ' ' + storesTags(47,122) #Seattle 

    tags = make_tags(get_tag_counts(TEXT), maxsize=80)
    create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

    import webbrowser
    webbrowser.open('cloud_large.png') # see results

def testCloud():
    TEXT = storesTags(34,118) #Los Angeles
    print "L.A.:" + TEXT
    TEXT += storesTags(37,122) # San Francisco 
    print "S.F: " + TEXT
    TEXT += ' ' + storesTags(47,122) #Seattle 
    print "Seattle: " + TEXT

    TEXT = storesTags(40, 73) #New York City 
    print "NYC: " + TEXT
    TEXT += ' ' + storesTags(25, 80) # Miami
    print "Chicago: " + TEXT
    TEXT += ' ' + storesTags(38, 77) #Washington D.C.
    print "Philadelphia: " + TEXT















