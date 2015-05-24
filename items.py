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

    title = Field()
    date = Field()
    detailedTime = Field()
    model = Field()
    price = Field()
    odometer = Field()
    status = Field()
    area = Field()
    link = Field()
    pass
