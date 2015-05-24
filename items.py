# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CraigslistSampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    owner_dealer = Field()
    title = Field()
    integer price = Field()
    time = Field()
    detailedTime = Field()
    area = Field()
    pass
