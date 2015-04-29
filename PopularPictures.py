from instagram.client import InstagramAPI
from Tkinter import *        
from PIL import ImageTk, Image
import urllib

api = InstagramAPI(client_id='7f674565db0d42ed9b4dd4f366db65be', client_secret='9a5f5c38eec74eff9f479e3659d4824f')
popular_media = api.media_popular(count=20)
i = 0
for media in popular_media:
    url =  media.images['standard_resolution'].url
    urllib.urlretrieve(url, "file"+ str(i) +".jpg")
    i += 1 


#Setting it up
img = ImageTk.PhotoImage(Image.open("file"+ str(0) +".jpg"))

#Displaying it
imglabel = Label(app_root, image=img).grid(row=1, column=1)        

app_root.mainloop()
