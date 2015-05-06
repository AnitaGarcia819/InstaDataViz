# File name: main.py
# Authors: Anita & Gabriel Radinsky
# Created: 4/2015
# Description: This program will run the
# InstaDataViz program. It will allow
# the user select which feature
# of the program the user would like to selecc
# through the GUI

import TagSearch
import PopularPictures
import WordCloud
import wx

class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):
    	# Creates buttons 
        self.button1 = wx.Button(self, id=-1, label='Tag Location Comparison',pos=(22, 8), size=(175, 28))
        self.button2 = wx.Button(self, id=-1, label='Popular Pictures',pos=(22, 38), size=(175, 28))
        self.button3 = wx.Button(self, id=-1, label='East Coast Word Cloud',pos=(22, 68), size=(175, 28))
        self.button4 = wx.Button(self, id=-1, label='West Coast Word Cloud', pos=(22, 98), size=(175,28))
   
        self.button9 = wx.Button(self, id=-1, label='Close' ,pos=(22, 228), size=(175,28))
        
        # Adds functionality to buttons
        self.button1.Bind(wx.EVT_BUTTON, self.locationComparison)
        self.button2.Bind(wx.EVT_BUTTON, self.PopularPictures)
        self.button3.Bind(wx.EVT_BUTTON, self.EastCoast)
        self.button4.Bind(wx.EVT_BUTTON, self.WestCoast)

    	self.button9.Bind(wx.EVT_BUTTON, self.OnQuitApp)

        # GUI Aesthetics 
        self.SetSize((220, 300))
        self.SetBackgroundColour("black")
        self.SetTitle("Instagram Data ")
        self.Center()
        self.Show(True)
    
    #Functions that are called when buttons are clicked on    
    def locationComparison(self, event):
    	TagSearch.showTagsonMap()
    def PopularPictures(self, event):
        PopularPictures.openWebPage()
    def EastCoast(self, event):
        WordCloud.openEastCoastCloud()
    def WestCoast(self, event):
        WordCloud.openWestCoastCloud()
    def OnQuitApp(self, event):
    	self.Close()

 
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main() 

