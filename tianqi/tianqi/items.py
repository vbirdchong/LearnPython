# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    day = scrapy.Field()
    week = scrapy.Field()
    air = scrapy.Field()
    temp = scrapy.Field()
    txt = scrapy.Field()
    up_to = scrapy.Field()
    
