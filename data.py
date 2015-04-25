__author__ = 'Duran'

import requests
import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.urlopen('http://losangeles.craigslist.org/search/cta').read())


for row in soup('p', {'class': 'row'}):
    data = row.getText().split()
    car = " "
    location = " "


    if "$" in data[0]:
        price = data[0]
        date = data[1] + " " + data[2]
    else:
        price = " "
        date = data[0] + " " + data[1]

    for i in range(3, 15):
        try:

            if "(" in data[i]:
                location = data[i]
                while ")" not in location:
                    location = location + " " + data[i+1]
                i = 15
                break
            else:
                car += data[i] + " "
        except IndexError:
            print ""

    print "price: " + price
    print "date: " + date
    print "car: " + car
    print "location: " + location
    print "-------------"

