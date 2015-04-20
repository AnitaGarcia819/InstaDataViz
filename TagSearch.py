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
import requests


def tagSearch():
	access_token = "231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b"
	tag_here = raw_input("Enter First tag: ")
	file = request.get("https://api.instagram.com/v1/tags/" +tag_name + "/media/recent?access_token=" + access_token)
	data = file.json()
	#jasonfile = json.loads(file)


	for x in data['data']:
		if(data['location'] != None):
			variable = data['location']['latitude'] #to test
			print variable
			#csv.writerow([variable])
tagSearch()
