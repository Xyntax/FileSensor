# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/FileSensor
# author = i@cdxy.me

import scrapy
import re
from urllib.parse import urlparse
from lib.data import spider_data
from lib.common import gen_urls


class FileSensorSpider(scrapy.Spider):
    name = 'filesensor'
    handle_httpstatus_list = [301, 302, 204, 206, 403, 500]

    def __init__(self):
        super(FileSensorSpider, self).__init__()
        self.url = spider_data.start_urls
        print('[START] ' + self.url)
        if not self.url.startswith('http://') and not self.url.startswith('https://'):
            self.url = 'http://%s/' % self.url
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse(self.url).hostname)]

    def start_requests(self):
        return [scrapy.Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        spider_data.crawled.append(response.url)
        print('[%s]%s' % (response.status, response.url))

        # generate new urls with /dict/suffix.txt
        for new_url in gen_urls(response.url):
            # avoid recursive loop
            yield scrapy.Request(new_url, callback=self.vul_found)

        extracted_url = []
        try:
            # TODO handle this <a href="/.htaccess">
            extracted_url.extend(response.xpath('//*/@href | //*/@src | //form/@action').extract())
        except:
            return

        # ignore links like <a href="#">
        extracted_url = set(extracted_url) - {'#', ''}

        # recursive crawling new links
        for url in extracted_url:
            next_url = response.urljoin(url)
            yield scrapy.Request(next_url, callback=self.parse)

    def vul_found(self, response):
        # filter custom 404 page(status_code=200) with [--404] option
        if spider_data.custom_404_regex and re.findall(spider_data.custom_404_regex, str(response.body)):
            return

        msg = '[%s]%s' % (response.status, response.url)
        spider_data.found.append(msg)
        print('[!]' + msg)
