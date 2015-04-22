# File name: TagSearch.py
# Authors: Anita & Gabriel Radinsky
# Created: 4/2015
# Description: This file will extract two recent
# tags from instagram. This data will be given
# in a JSON format and then be visualized to compare
# the difference in usage.

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
        if data ['location'] != None:
            latitudePoint = data['location']['latitude']
            latitude.append(latitudePoint)
def gatherLongitude(tag):
    file = urlopen("https://api.instagram.com/v1/tags/"+ tag+"/media/recent?access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
    data = json.loads(file)

    longitude =[]

    for data in data["data"]:
        if(data['location'] != None):
            longitudePoint = data['location']['longitude']
            longitude.append(longitudePoint)
    return longitude



def get_marker_color(number_of_tags):
    # Returns green for smaller amounts of tags, yellow for moderate
    #  amounts of tags, and red for significant tags.
    if number_of_tags < 3.0:
        return ('go')
    elif number_of_tags < 5.0:
        return ('yo')
    else:
        return ('ro')
'''
map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
#map.fillcontinents(color = 'gray')
map.bluemarble()
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

min_marker_size = 2.25
for lon, lat in zip(longitude, latitude):
    x,y = map(lon, lat)
    msize = number_of_tags* min_marker_size
    marker_string = get_marker_color(number_of_tags)
    map.plot(x, y, marker_string, markersize=msize)

title_string = "#" + tag_here +" currently trending\n"
#title_string += "%s through %s" % (timestrings[-1][:10], timestrings[0][:10])
plt.title(title_string)

plt.show()

'''
