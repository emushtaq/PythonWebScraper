#from urllib2 import urlopen
import requests
from BeautifulSoup import BeautifulSoup
url="https://en.wikipedia.org/wiki/2017_in_film"
#used to open a web page
	#urlopen(url)


#getting html
response=requests.get(url)
html=response.content

soup=BeautifulSoup(html)
print (soup.prettify())