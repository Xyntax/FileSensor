# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import scrapy
import requests
import urlparse
import re
from lib.data import spider_conf


class FileSensorSpider(scrapy.Spider):
    name = 'filesensor'

    def __init__(self, **kw):
        super(FileSensorSpider, self).__init__(**kw)
        self.url = spider_conf.start_urls
        print(self.url)
        if not self.url.startswith('http://') and not self.url.startswith('https://'):
            self.url = 'http://%s/' % self.url
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse.urlparse(self.url).hostname)]

    def start_requests(self):
        return [scrapy.Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        print('[%s]%s' % (response.status, response.url))
        self.check(response.url)

        extracted_url = []
        extracted_url.extend(response.xpath('//*/@href | //*/@src | //form/@action').extract())

        for url in extracted_url:
            next_url = response.urljoin(url)
            yield scrapy.Request(next_url, callback=self.parse)

    def check(self, url):
        url = url.split('?')[0]
        url_piece = url.split('/')
        if '.' not in url_piece[-1]:
            return
        if not urlparse.urlparse(url).path:
            return

        new_urls = []
        new_urls.append(url + '~')  # index.php~
        new_urls.append('/'.join(url_piece[:-1]) + '/.' + url_piece[-1] + '.swp')  # .index.php.swp

        for url in new_urls:
            r = requests.get(url)
            if r.status_code != 404:
                print('[%s]%s' % (r.status_code, url))
