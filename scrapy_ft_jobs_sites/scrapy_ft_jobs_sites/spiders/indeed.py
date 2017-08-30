# -*- coding: utf-8 -*-
import os
from datetime import datetime
from bs4 import BeautifulSoup

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_ft_jobs_sites import settings
from scrapy_ft_jobs_sites.items import LeadItem

from .base import BaseFTSpider

class IndeedSpider(BaseFTSpider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    base_url_pattern = "https://www.indeed.com/jobs?q="
    start_urls = ['http://indeed.co.in/']
    html_stoarge_dir = 'indeed'

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
        item = LeadItem()

        postings = soup.find_all("div", {"itemtype": "http://schema.org/JobPosting"})

        category = soup.find("input", {"name": "q"})['value']

        for current in postings:
            item['title'] = current.h2.a["title"]
            item['source_url'] = "https://www.indeed.com" + current.h2.a["href"]
            item['source'] = "".join(self.allowed_domains)
            item['category'] = category

            try:
                item['company'] = current.find("span", {"itemprop": "name"}).a.text.strip()
            except:
                item['company'] = ""

            try:
                item['location'] = current.find("span", {"itemprop": "address"}).text.strip()
            except:
                item['location'] = ""

            try:
                item['blurb'] = current.find("span", {"itemprop": "description"}).text.strip()
            except:
                item['blurb'] = ""

        return item