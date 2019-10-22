import scrapy
from ..items import ProgramItem
import xml.etree.ElementTree as ET


class MutazProgSpider(scrapy.Spider):

    name = 'mutaz_prog_spider'

    tree = ET.parse('categories.xml')
    root = tree.getroot()
    start_urls = []
    for cat in root:
        for _url in cat[2]:
            start_urls.append(_url.text)
    print(start_urls)

    def parse(self, response):
        items = ProgramItem()
        name = response.css("span.long-txt-span::text").getall()[0]
        desc = response.css("span.long-txt-span::text").getall()[1]
        try:
            version = response.css("span.long-txt-span::text").getall()[2]
        except IndexError:
            version = None
        bits = response.css("span.long-txt-span::text").getall()[3]
        try:
            size = response.css("span.long-txt-span::text").getall()[4]
        except IndexError:
            size = bits
            bits = None
        logo = response.css("div.long-icon img").xpath('@src').get()
        url_1 = response.css('a.download').xpath('@href').getall()[0]
        try:
            url_2 = response.css('a.download').xpath('@href').getall()[1]
        except IndexError:
            url_2 = None
        try:
            url_3 = response.css('a.download').xpath('@href').getall()[2]
        except IndexError:
            url_3 = None
        items['name'] = name
        items['desc'] = desc
        items['version'] = version
        items['bits'] = bits
        items['size'] = size
        items['logo'] = logo
        items['url_1'] = url_1
        items['url_2'] = url_2
        items['url_3'] = url_3
        yield items
