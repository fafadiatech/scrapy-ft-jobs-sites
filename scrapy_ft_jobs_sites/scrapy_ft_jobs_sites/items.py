# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeadItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    source = scrapy.Field()
    source_url = scrapy.Field()
    tags = scrapy.Field()
    blurb = scrapy.Field()
