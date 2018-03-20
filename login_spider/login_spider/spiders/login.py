# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request, FormRequest

class LoginSpider(scrapy.spiders.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = [
        'http://example.webscraping.com/user/profile'
    ]

    login_url = 'http://example.webscraping.com/places/default/user/login'

    def start_requests(self):
        print("In loging, start requests")
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        fd = {'email': 'liushuo@webscraping.com', 'password':'12345678'}
        yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)

    def parse_login(self, response):
        if 'Welcome Liu' in response.text:
            print('Yessssssssssssssssssssss')
            # python3 调用基类方法，继续抓取start_urls中的内容
            # yield from super().start_requests()
    
    def start_normal(self):
        print('start normal')
        super(LoginSpider, self).start_requests()

    def parse(self, response):
        keys = response.css('table label::text').re('(.+):')
        valus = response.css('table tb.w2p_fw::text').extract()
        print(keys)
        print(valus)
        yield dict(zip(keys, valus))
