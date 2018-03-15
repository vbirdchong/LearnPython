import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    # def start_requests(self):
    #     meta_proxy = "http://10.144.1.10:8080"
    #     for url in self.start_urls:
    #         print("url = " + url)
    #         yield scrapy.Request(url = url, callback=self.parse, meta={'proxy':meta_proxy})

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
        # filename = response.url.split("/")[-2]
        # with open(filename, "wb") as f:
        #     f.write(response.body)