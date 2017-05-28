# PythonWebScrapper
A python wrapper to scrap instagram images and metadata with hastags

## Create a virtual environment with virtualenv and install the dependencies there
`virtualenv <ENV_NAME>`
`source ENV_NAME/bin/activate`
`pip install -r requirements.txt`

## To run the HTML scrapper: 
`python htmlscraper.py`

### To Change URLs and scraper context, alter the file : htmlscraper.py

## To run the instagram scraper for hashtags: 
`python insta-scrap.py`

### Alter keywords.csv to change to hashtags, insta-scrap.py to change the number of images to scrap.

USES instagram-scraper (see requirements.txt)

The result will be stored in the data folder. It will also contain a JSON metadata file