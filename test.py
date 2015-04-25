from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://losangeles.craigslist.org/search/cto"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//div[@class="content"]/p[@class="row"]')
        items = []
        for row in rows:
            item = CraigslistSampleItem()
            link = row.xpath('.//span[@class = "pl"]')
            item ["title"] = link.xpath("a/text()").extract()
            item ["time"] = link.xpath("time/text()").extract()
            item ["price"] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()
            items.append(item)
        return items
