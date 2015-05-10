from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = []
    for i in range(0, 25):
        if(i == 0):
            url = "http://losangeles.craigslist.org/search/cta"
            start_urls.append(url)
        else:
            url = "http://losangeles.craigslist.org/search/cta/?s=" + str(i*100)
            start_urls.append(url)
            
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
