# File name: main.py
# Authors: Anita & Gabriel Radinsky
# Created: 4/2015
# Description: This program will run the
# InstaDataViz program. It will allow
# the user select which feature
# of the program the user would like to select.
import TagSearch
import time

tag_here = raw_input("Enter Tag: ")
for x in range(30):
    TagSearch.gatherData(tag_here)
    time.sleep(5)
