import string
import webbrowser
from bs4 import BeautifulSoup
import urllib2
import urllib
import json

def webScraper(artist):
    artist = artist.replace(' ', '_')
    ArtistPage = urllib2.urlopen("https://en.wikipedia.org/wiki/" + artist)
    ArtistSoup = BeautifulSoup(ArtistPage, 'html.parser')
    imgsrc = ''
    for link in ArtistSoup.find_all('table',attrs={"class":"infobox"}): #Finds the table at the right in the Wiki page
        #print link
        for link2 in link.find('a',attrs={"class":"image"}): # Gets the image in the table
            #print link2
            imgsrc = link2.get('src') # Gets the hyperlink of said image
    imgsrc = 'https:' + imgsrc
    return imgsrc

def saveimages(artist):
    artist = artist.replace(' ', '_') 
    urllib.urlretrieve(webScraper(artist), "/Lyrvana/"+artist+".jpg") # Save image to local disk.

#saveimages("Bob Marley")
docs = json.load(open('lyr2.json'))
artistList = []
for doc in docs:
    if doc['artist'] not in artistList:
        try:
            saveimages(doc['artist'])
            print 'Saved ' + doc['artist']
            artistList.append(doc['artist'])
        except:
            print doc['artist'] + " not saved"
            artistList.append(doc['artist'])
            continue
    else:
        continue

print "\n" + str(len(artistList)) + " artists saved."
