# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from cmdparse import get_arguments
from data import spider_conf, dict_data
import urlparse


def init_options():
    args = get_arguments()
    if args.get('URL'):
        spider_conf.start_urls = args.get('URL')
    if args.get('-u'):
        spider_conf.start_urls = args.get('-u')
    if args.get('-f'):
        pass  # TODO
    load_dict_suffix()


def load_dict_suffix():
    with open('dic/suffix.txt') as f:  # TODO path!
        dict_data.url_suffix = f.read().split('\n')


def gen_urls(base_url):
    url = base_url.split('?')[0].rstrip('/')
    if not urlparse.urlparse(url).path:
        return []

    final_urls = []

    # index.php -> .index.php.swp
    url_piece = url.split('/')
    final_urls.append('/'.join(url_piece[:-1]) + '/.' + url_piece[-1].strip('.') + '.swp')

    for each in dict_data.url_suffix:
        final_urls.append(url + each)

    return final_urls
