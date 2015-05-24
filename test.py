from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem
import scrapy

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
            item ["date"] = link.xpath("time/text()").extract()
            item ["detailedTime"] = row.xpath(".//span/time/@datetime").extract()
            item ["price"] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').re("[0-9,]+")
            item ["area"] = row.xpath(".//span[@class='l2']/span[@class='pnr']/small/text()").extract()
            item ["link"] = row.xpath("a/@href").extract()
            
            fullLink = "http://losangeles.craigslist.org" + ' '.join(item["link"])
            request = scrapy.Request(fullLink, callback = self.parse_page)
            request.meta['item'] = item
            yield request
    
    def parse_page(self, response):
        item = response.meta["item"]
        attrGroup = response.xpath("//p[@class = 'attrgroup']")
        item ["model"] = attrGroup.xpath("span/b/text()")[0].extract()
        temp = attrGroup.xpath("span")[1].xpath("b/text()").extract()
        try:
            item ["odometer"] = attrGroup.xpath("span")[1].xpath("b/text()").extract()
        except:
            item ["odometer"] = None
        try:
            item ["status"] = attrGroup.xpath("span")[8].xpath("b/text()").extract()
        except:
            item ["status"] = None
        return item
        
