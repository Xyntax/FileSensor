# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/FileSensor
# author = i@cdxy.me

import os
import hashlib
import random
import time
from urllib.parse import urlparse
from .cmdparse import get_arguments
from .data import spider_data, dict_data, paths, conf


def init_options():
    set_path()

    args = get_arguments()
    spider_data.start_urls = args.get('URL')
    spider_data.custom_404_regex = args.get('--404')
    spider_data.found = []
    spider_data.crawled = []
    conf.save_results = args.get('-o')

    load_dict_suffix()


def set_path():
    paths.root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    paths.dict_path = os.path.join(paths.root_path, 'dict')
    paths.default_suffix_dict = os.path.join(paths.dict_path, 'suffix.txt')
    paths.output_path = os.path.join(paths.root_path, 'output')

    if not all(os.path.exists(p) for p in paths.values()):
        exit('[CRITICAL]Some folders or files are missing, '
             'please download the project in https://github.com/Xyntax/FileSensor/')


def load_dict_suffix():
    with open(paths.default_suffix_dict) as f:
        dict_data.url_suffix = set(f.read().split('\n')) - {'', '#'}


def gen_urls(base_url):
    url = base_url.split('?')[0].rstrip('/')
    if not urlparse(url).path:
        return []

    final_urls = []

    # index.php -> .index.php.swp
    url_piece = url.split('/')
    final_urls.append('/'.join(url_piece[:-1]) + '/.' + url_piece[-1].strip('.') + '.swp')

    for each in dict_data.url_suffix:
        final_urls.append(url + each)

    return final_urls


def final_message():
    print('-' * 10)
    print('Crawled Page: %d' % len(spider_data.crawled))
    print('Sensitive File Found: %d' % len(spider_data.found))
    for each in spider_data.found:
        print(each)

    save_results()


def random_string():
    return hashlib.md5(str(random.uniform(1, 10)).encode('utf-8')).hexdigest()


def save_results():
    if not conf.save_results:
        return

    site = urlparse(spider_data.start_urls).netloc
    filepath = site if site else spider_data.start_urls.replace('/', '')
    filepath += time.strftime('-%Y%m%d-%H%M%S', time.localtime(time.time()))
    filepath = os.path.join(paths.output_path, filepath)

    try:
        with open(filepath, 'w') as f:
            f.write('\n'.join(spider_data.found))
    except Exception as e:
        exit(e)

    print('\nResults saved in %s' % filepath)
