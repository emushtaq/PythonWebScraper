import subprocess
hashtag = raw_input("Enter the hashtag that you would like to scrap from Instagram: ")
number = raw_input("Enter the number of entries you would like to scrap: ")
subprocess.call(["scraper/bin/instagram-scraper", hashtag, "--tag", "-m", number, "-d", "./data/"+hashtag, "--media_metadata"])