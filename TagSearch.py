# File name: TagSearch.py
# Authors: Anita & Gabriel Radinsky
# Created: 4/2015
# Description: This file will extract two recent
# tags from instagram. This data will be given
# in a JSON format and then be visualized to compare
# the difference in usage.
import TagSearch
import time
from instagram.client import InstagramAPI
import httplib2
import json
import urllib
from  urllib import urlopen
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


def gatherLatitude(tag):
    file = urlopen("https://api.instagram.com/v1/tags/"+ tag+"/media/recent?access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
    data = json.loads(file)
    latitude = []

    for data in data["data"]:
        if data['location'] != None:
                latitudePoint = data['location']['latitude']
                latitude.append(latitudePoint)

    return latitude
def gatherLongitude(tag):
    file = urlopen("https://api.instagram.com/v1/tags/"+ tag+"/media/recent?access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
    data = json.loads(file)

    longitude =[]

    for data in data["data"]:
        if data['location'] != None:
            longitudePoint = data['location']['longitude']
            longitude.append(longitudePoint)
    return longitude


def get_marker_color(tagColor):
    # Returns green for smaller amounts of tags, yellow for moderate
    #  amounts of tags, and red for significant tags.
    if tagColor == 1:
        return ('go') 
    else:
        return ('ro')

def plotMap(longitude1, latitude1, longitude2, latitude2, tag1, tag2):
    map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
    map.drawcoastlines()
    map.drawcountries()
    map.bluemarble()
    map.drawmapboundary()
    map.drawmeridians(np.arange(0, 360, 30))
    map.drawparallels(np.arange(-90, 90, 30))

    min_marker_size = 10
    #This will plot the latitudes and longitues for Tag1
    for lon, lat in zip(longitude1, latitude1):
        x,y = map(lon, lat)
        msize = min_marker_size
        marker_string = get_marker_color(1)
        map.plot(x, y, marker_string, markersize=msize)
    #This will plot latitudes and longitues for Tag2
    for lon, lat in zip(longitude2, latitude2):
        x,y = map(lon, lat)
        msize =  min_marker_size
        marker_string = get_marker_color(2)
        map.plot(x, y, marker_string, markersize=msize)

    title_string = "#" + tag1 +"(green) and #" + tag2 + "(red) currently trending\n"
    plt.title(title_string)
    plt.show()

def showTagsonMap():
    firstTag= raw_input("Enter Tag: ")
    secondTag= raw_input("Enter Tag: ")

    #Stores data for first tag
    latitude_1= []
    longitude_1= []

    #Stores data for second tag
    latitude_2= []
    longitude_2= []

    #Appends latitude into "latitude_1"

    for x in range(1): #Testing with '1', change to 30 
        points = gatherLatitude(firstTag)
        for data in points:
            latitude_1.append(data)

    for x in range(1): #Testing with '1', change to 30 
        points = gatherLongitude(firstTag)
        for data in points:
            longitude_1.append(data)

    for x in range(1): #Testing with '1', change to 30 
        points = gatherLatitude(secondTag)
        for data in points:
            latitude_2.append(data)

    for x in range(1): #Testing with '1', change to 30 
        points = gatherLongitude(secondTag)
        for data in points:
            longitude_2.append(data)
    if len(latitude_1) == 0:
        print "No data trending for first tag"
    if len(latitude_2) == 0:
        print "No data trending for second tag"

    plotMap(longitude_1, latitude_1, longitude_2, latitude_2, firstTag, secondTag)
   # plotMap(longitude_2, latitude_2, secondTag, 2)


