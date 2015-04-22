# File name: main.py
# Authors: Anita & Gabriel Radinsky
# Created: 4/2015
# Description: This program will run the
# InstaDataViz program. It will allow
# the user select which feature
# of the program the user would like to select.
import TagSearch
import time

firstTag= raw_input("Enter Tag: ")
secondTag= raw_input("Enter Tag: ")

#Stores data for first tag
latitude_1= []
longitude_1= []

#Stores data for second tag
latitude_2= []
longitude_2= []


for x in range(1): #Testing with '1', change to 30 
	points = TagSearch.gatherLatitude(firstTag)
	latitude_1.append(points)
	longitude_1.append(TagSearch.gatherLongitude(firstTag))
	latitude_2.append(TagSearch.gatherLatitude(secondTag))
	longitude_2.append(TagSearch.gatherLongitude(secondTag))
	time.sleep(5)
    

number_of_tags1 = len(latitude_1)
number_of_tags2 = len(latitude_2)

print number_of_tags1
print number_of_tags1

