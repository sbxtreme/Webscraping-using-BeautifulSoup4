'''Below is the code to download the images from a particular website.
Scope:

The code will not work for the websites which are secured or login required.
This needs to be handled in next release.

how to use:

In the command prompt type the below:
python image_scraping.py <name of website>
ex: python image_scraping.py http://www.nrigroupindia.com'''

# the below script is used to parse the website and download the images present on it.

import sys
import bs4 as bs
import urllib.request
import random as r

x=sys.argv
print('Parsing the website :',x[1])
try:
 url=x[1]
 sc = urllib.request.urlopen(url).read()
 soup= bs.BeautifulSoup(sc,'lxml')
 images=[]
 images=soup.findAll('img')
 for i in images:
  name=r.randrange(1,500)
  img_name=str(name)+'.jpg'
  img=''
  im=(i.get('src'))
  if im[:1]=='/':
   img=(url+im)
   urllib.request.urlretrieve(img,img_name)
  else:
   img=''
   img=im
   urllib.request.urlretrieve(img,img_name)
except:
 print('Error occured while downloading images')