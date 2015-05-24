# -*- coding: utf-8 -*-

# Scrapy settings for craigslist_sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'craigslist_sample'

SPIDER_MODULES = ['craigslist_sample.spiders']
NEWSPIDER_MODULE = 'craigslist_sample.spiders'

FEED_EXPORTERS = {
 'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',
}
FEED_FORMAT = 'jsonlines'
FEED_URI = "items.json"
ITEM_PIPELINES = ['craigslist_sample.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "craigslist"
MONGODB_COLLECTION = "cars"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist_sample (+http://www.yourdomain.com)'
