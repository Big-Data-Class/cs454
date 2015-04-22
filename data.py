import requests
import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.urlopen('http://losangeles.craigslist.org/search/cta').read())

for info in soup('p', {'class': 'row'}):

    print info.getText()
