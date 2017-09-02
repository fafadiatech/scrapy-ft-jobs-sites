# -*- coding: utf-8 -*-
import os
from datetime import datetime
from bs4 import BeautifulSoup

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_ft_jobs_sites import settings

from .base import BaseFTSpider
from .parsers import IndeedParser


class IndeedSpider(BaseFTSpider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    base_url_pattern = "https://www.indeed.com/jobs?q="
    start_urls = ['http://indeed.co.in/']

    rules = (
        Rule(LinkExtractor(
            allow=(r'https\:\/\/www\.indeed\.com\/.+',)),
            callback='parse_item',
            follow=False),
    )


    def __init__(self, *args, **kwargs):
        super(IndeedSpider, self).__init__(*args, **kwargs)

        # Logic for start_urls creations
        self.start_urls = []

        for item in self.keywords:
            URL = self.base_url_pattern + item.replace(" ", "+")
            self.start_urls.append(URL)

            for pagination in range(10, 60, 10):
                URL = self.base_url_pattern + item.replace(" ", "+") + "&start=" + str(pagination)
                self.start_urls.append(URL)

    def parse_item(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        parser = IndeedParser(soup, "".join(self.allowed_domains))
        return parser.parse_response()