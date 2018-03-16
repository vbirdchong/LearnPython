# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from toscrape_book.items import ToscrapeBookItem


class BooksSpider(scrapy.spiders.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    custom_settings = {
        'FEED_EXPORT_FIELDS' : ['upc', 'name', 'price', 'stock', 'review_rating', 'review_num']
    }

    def parse(self, response):
        # get each book's url then parse the detail info
        le = LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)

        # after parse the book info, we get the next page's url then continue to parse others books info
        le = LinkExtractor(restrict_css='li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            # get next url then call the self.parse
            yield scrapy.Request(next_url, callback=self.parse)     

    def parse_book(self, response):
        book = ToscrapeBookItem()
        sel = response.css('div.product_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')

        sel = response.css('table.table.table-striped')
        book['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first()
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()

        yield book


