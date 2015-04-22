__author__ = 'Duran'

import requests
import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.urlopen('http://losangeles.craigslist.org/search/cta').read())


for row in soup('p', {'class': 'row'}):
    price = row.getText().split()[0]
    date = row.getText().split()[1] + " " + row.getText().split()[2]
    car = " "
    for i in range(3, 15):
        try:
            car += row.getText().split()[i] + " "
        except IndexError:
            print " "
    print "price: " + price
    print "date: " + date
    print "car: " + car
    print "-------------"

