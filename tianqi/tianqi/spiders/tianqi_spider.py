import scrapy

from tianqi.items import TianqiItem

class TianqiSpider(scrapy.spiders.Spider):
    name = "Tianqi"
    allowed_domains = ["tianqi.com"]
    start_urls = [
        "http://tianqi.com/hangzhou/7"
    ]

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {'tianqi.middlewares.TianqiDownloaderMiddleware': 100,},
        'COOKIES_ENABLED' : False,
        'DEFAULT_REQUEST_HEADERS': {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
    } 

    def parse(self, response):
        item = TianqiItem()
        for sel in response.xpath('//dl[@class="table_day7 "]|//dl[@class="table_day7 tbg"]'):
            item['day'] = sel.xpath('dl/text()').extract()
            item['week'] = sel.xpath('dd[@class="week"]/text()').extract()
            item['air'] = sel.xpath('dd[@class="air"]/b/text()').extract()
            item['temp'] = sel.xpath('dd[@class="temp"]/text()').extract()
            item['txt'] = sel.xpath('dd[@class="txt"]/text()').extract()
            item['up_to'] = sel.xpath('dd[@class="txt"]/b/text()').extract()
            self.print_city_weather_info(item)

    def print_city_weather_info(self, item):
        info = item['day'][0]       + '  ' + \
                item['week'][0]     + '  ' + \
                item['air'][0]      + '  ' + \
                item['temp'][0]     + '  ' + \
                item['txt'][0]             + \
                item['up_to'][0]           + \
                item['txt'][1]      + '  ' + \
                item['txt'][2]
        print(info)

        