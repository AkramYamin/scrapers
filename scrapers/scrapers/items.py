# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    arabic_title = scrapy.Field()
    english_title = scrapy.Field()
    urls = scrapy.Field()


class ProgramItem(scrapy.Item):
    name = scrapy.Field()
    version = scrapy.Field()
    bits = scrapy.Field()
    desc = scrapy.Field()
    logo = scrapy.Field()
    size = scrapy.Field()
    url_1 = scrapy.Field()
    url_2 = scrapy.Field()
    url_3 = scrapy.Field()
