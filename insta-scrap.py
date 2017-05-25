import subprocess
import csv

#number of images (must be a string)
number = "10"

keywords = []
with open('keywords.csv', 'r') as f:
    for line in f.readlines():
        keywords.extend(line.split(','))

print "Fetching data for :"
print keywords

for keyword in keywords:
	subprocess.call(["scraper/bin/instagram-scraper", keyword, "--tag", "-m", number, "-d", "./data/"+keyword, "--media_metadata"])

