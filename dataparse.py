import sys
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen

print("Please enter the URL:")

URL =  sys.stdin.readline()

# Testing URLs
#URL = "https://www.wired.com/2007/06/who-should-run-/"
#URL = "https://www.dataquest.io/blog/web-scraping-tutorial-python/"
#URL = "https://en.wikipedia.org/wiki/India"

# 
urlReader = urlopen(URL)
 
#soup = BeautifulSoup(r.content, 'html5lib')
htmlTree = BeautifulSoup(urlReader, 'html.parser')

#Find Content of the page
paragraphContent = htmlTree.findAll('p')

#Find H1 title of the page
headerContent = htmlTree.find('h1')


def getTextFromElm(element):
	return element.get_text()

pageHeader      = headerContent.get_text()
pageContentList = list(map(getTextFromElm, paragraphContent))

with open('pageContent.txt', 'w') as outfile:
    json.dump(dict(header =pageHeader, body = pageContentList), outfile)
