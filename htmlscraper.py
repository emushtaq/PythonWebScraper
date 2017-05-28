import requests
from BeautifulSoup import BeautifulSoup
import csv
url="https://en.wikipedia.org/wiki/2017_in_film"

#getting html
response=requests.get(url)
html=response.content

soup=BeautifulSoup(html)
table=soup.find('table',attrs={'class':'sortable'})

datarows = []
for row in table.findAll('tr'):
    for column in row.findAll('td'):
    	#print column.text.encode('ascii', 'ignore')
    	datarows.append(column.text.encode('ascii', 'ignore'))

print datarows
outfile = open("./data.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(datarows)
