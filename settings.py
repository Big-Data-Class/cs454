BOT_NAME = 'craigslist_sample'

SPIDER_MODULES = ['craigslist_sample.spiders']
NEWSPIDER_MODULE = 'craigslist_sample.spiders'

ITEM_PIPELINES = ['craigslist_sample.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "craigslist"
MONGODB_COLLECTION = "cars"
