'''
Created on Apr 21, 2015

@author: christian
'''
from lxml import html
import json
import requests
page = requests.get('http://losangeles.craigslist.org/search/cta')
tree = html.fromstring(page.text)
vehicles = tree.xpath('//a[@class="hdrlnk"]/text()')
prices = tree.xpath('//span[@class="price"]/text()')
print 'Vehicle: ', vehicles
print 'Price: ', prices
with open('whatever', 'wb') as outfile:
    json.dump(vehicles, outfile)
    json.dump(prices, outfile)
    
