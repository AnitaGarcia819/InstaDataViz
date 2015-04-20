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


tag_here = raw_input("Enter Tag: ")
file = urlopen("https://api.instagram.com/v1/tags/"+ tag_here+"/media/recent?access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
data = json.loads(file)

latitude = []
longitude =[]

number_of_tags = latitude.amount()

for data in data["data"]:
	if(data['location'] != None):
		latitudePoint = data['location']['latitude']
		latitude.append(latitudePoint)
		longitudePoint = data['location']['longitude']
		longitude.append(longitudePoint)

def get_marker_color(number_of_tags):
    # Returns green for small earthquakes, yellow for moderate
    #  earthquakes, and red for significant earthquakes.
    if number_of_tags < 3.0:
        return ('go')
    elif number_of_tags < 5.0:
        return ('yo')
    else:
        return ('ro')

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
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = map(lon, lat)
    msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    map.plot(x, y, marker_string, markersize=msize)
    
title_string = "Earthquakes of Magnitude 1.0 or Greater\n"
title_string += "%s through %s" % (timestrings[-1][:10], timestrings[0][:10])
plt.title(title_string)
 
plt.show()

