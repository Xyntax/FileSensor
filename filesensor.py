# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/FileSensor
# author = i@cdxy.me

from lib import envcheck # check environment at start
from lib.common import init_options, final_message
from scrapy_project.crawl import run_spider

init_options()
run_spider()
final_message()
