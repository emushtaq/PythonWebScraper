#from urllib2 import urlopen
import requests
from BeautifulSoup import BeautifulSoup
import csv
url="https://en.wikipedia.org/wiki/2017_in_film"
#used to open a web page
	#urlopen(url)


#getting html
response=requests.get(url)
html=response.content

soup=BeautifulSoup(html)
#print (soup.prettify())
table=soup.find('table',attrs={'class':'sortable'})

for row in table.findAll('tr'):
    for column in row.findAll('td'):
    	print column.text

"""
outfile=open("./column_data.csv","wb")
writer=csv.writer()
"""