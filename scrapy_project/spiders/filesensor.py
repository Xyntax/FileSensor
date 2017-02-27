# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import scrapy
import urlparse
import re
from lib.data import spider_conf
from lib.common import gen_urls


class FileSensorSpider(scrapy.Spider):
    name = 'filesensor'
    handle_httpstatus_list = [301, 302, 204, 206, 403, 500]

    def __init__(self):
        super(FileSensorSpider, self).__init__()
        self.url = spider_conf.start_urls
        print('[START] ' + self.url)
        if not self.url.startswith('http://') and not self.url.startswith('https://'):
            self.url = 'http://%s/' % self.url
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse.urlparse(self.url).hostname)]

    def start_requests(self):
        return [scrapy.Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        print('[%s]%s' % (response.status, response.url))

        # generate new urls with /dict/suffix.txt
        for new_url in gen_urls(response.url):
            # avoid recursive loop
            yield scrapy.Request(new_url, callback=self.parse_end)

        extracted_url = []
        try:
            # TODO handle this <a href="/.htaccess">
            extracted_url.extend(response.xpath('//*/@href | //*/@src | //form/@action').extract())
        except:
            return

        for url in extracted_url:
            next_url = response.urljoin(url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_end(self, response):
        print('[Found!][%s]%s' % (response.status, response.url))
