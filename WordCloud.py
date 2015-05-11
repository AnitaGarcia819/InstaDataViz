#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# File name: WordCloud.py
# Authors: Anita & Gabriel Radinsky
# Created: 4/2015
# Description: This file will vizulaize Instagram tags on the west coast and the 
#              east coast. The word clouds generated will be displayed as a saved 
#              image. 
#              
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from instagram.client import InstagramAPI
import httplib2
import json
import urllib
from  urllib import urlopen
import time
import webbrowser


def getTags(lat, lng):  
    '''
    Returns the tags found in the location provided by the 'lat' and 'lng' 
    parameters being passed in. The 'lat' and 'lng' passed in will be used
    in the instagram API endpoint. 
    '''

    # Stores endpoint data in file 
    file = urlopen("https://api.instagram.com/v1/media/search?lat="+str(lat)+"&lng="+str(lng)+"&access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
    #Converts file into a JSON file
    data = json.loads(file)
    # Temperary array that holds tags 
    tagsTempArray = []
    # Adds the tags found in JSON file into the temporary array 
    # Note that a list of tags found will be stored into one single element. 
    for data in data["data"]:
        if data ['tags'] != '':
          	tag = data['tags']
          	tagsTempArray.append(tag)
    # Tags Array will hold one single tag in an element. 
    tagsArray = []
    # Adds each tag into a single element. 
    for element in tagsTempArray:
    	for tag in element:
    		tagsArray.append(tag)
    # Converts array into a string to be able to be 
    # Compatable with WordCloud library.
    string = ' '.join(tagsArray)
    return string


def openEastCoastCloud():
    '''
    Generates and displays East Coast word cloud. 
    '''

    #Stores tags from multiple cities into one text string. 
    TEXT = storesTags(40, 73) #New York City 
    TEXT += ' ' + storesTags(42.3744, 71.1169) #Harvard
    TEXT += ' ' + storesTags(42.3598, 71.0921)  #MIT
    TEXT = storesTags(38.9072, 77.0728) #GeorgeTown University 
    TEXT += ' ' + storesTags(42.3496, 71.0997) #Boston University
    #Draws Word Cloud 
    tags = make_tags(get_tag_counts(TEXT), maxsize=80)
    #Creates Word Cloud File 
    create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')
    #Opens Word Cloud File 
    webbrowser.open('cloud_large.png') # see results

def openWestCoastCloud():
    #Stores tags from multiple cities into one text string.
    TEXT = getTags(34,118) #Los Angeles
    TEXT += ' ' + getTags(37,122) # San Francisco 
    TEXT += ' ' + getTags(47,122) #Seattle 

    #Draws Word Cloud
    tags = make_tags(get_tag_counts(TEXT), maxsize=80)
    #Creates Word Cloud File 
    create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')
    #Opens Word Cloud File 
    webbrowser.open('cloud_large.png') # see results
    