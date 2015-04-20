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
import csv

tag_here = raw_input("Enter Tag: ")
file = urlopen("https://api.instagram.com/v1/tags/"+ tag_here+"/media/recent?access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
data = json.loads(file)

for data in data["data"]:
	if(data['location'] != None):
		variable1 = data['location']['latitude']
		variable2 = data['location']['longitude']
		print variable1
		print "asdfasfas"
		print variable2
