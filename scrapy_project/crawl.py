# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/FileSensor
# author = i@cdxy.me

import os
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings


def run_spider():
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapy_project.settings'
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    d = runner.crawl('filesensor')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
