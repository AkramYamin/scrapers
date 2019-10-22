import scrapy
from ..items import ScrapersItem


class MutazCatSpider(scrapy.Spider):

    name = 'mutaz_cat_spider'
    start_urls = ['https://www.mutaz.net/free-programs/']

    def parse(self, response):
        items = ScrapersItem()
        for category_div in response.css('div.category'):
            arabic_title = category_div.css('h1.category-title').xpath('@title').get()
            english_title = category_div.css('h1.category-title::text').get()
            urls = category_div.css('li.item a').xpath('@href').getall()

            # programs_descs = category_div.css('li.item').xpath('@data-dscrp').getall()
            # programs_names = category_div.css('li.item').xpath('@data-name').getall()
            # programs_sizes = category_div.css('li.item').xpath('@data-size').getall()
            # programs_logos = category_div.css('li.item').xpath('@data-img').getall()
            # programs_versions = category_div.css('li.item').xpath('@data-version').getall()
            # programs_bits = category_div.css('li.item').xpath('@data-bit').getall()

            urls = ['https://www.mutaz.net/free-programs/' + x for x in urls if not x.startswith("http")]
            items['arabic_title'] = arabic_title
            items['english_title'] = english_title
            items['urls'] = urls
            yield items
