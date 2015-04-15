from instagram.client import InstagramAPI
import httplib2
import json
import urllib
from  urllib import urlopen
import csv

tag_here = raw_input("Enter Tag: ")
file = urlopen("https://api.instagram.com/v1/tags/"+ tag_here+"/media/recent?access_token=231920771.7f67456.bfe24e8a256d4d5ca2e2131d56b7103b").read()
data = json.loads(file)
csv = csv.writer(open("test.csv", "wb"))

for data in data["data"]:
	if(data['location'] != None):
		variable = data['location'] #to test
		print variable
		csv.writerow([variable])
