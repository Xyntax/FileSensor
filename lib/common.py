# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from cmdparse import get_arguments
from data import spider_conf


def init_options():
    args = get_arguments()
    if args.get('URL'):
        spider_conf.start_urls = args.get('URL')
    if args.get('-u'):
        spider_conf.start_urls = args.get('-u')
    if args.get('-f'):
        pass  # TODO
