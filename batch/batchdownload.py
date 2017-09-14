#!/usr/bin/env python
# -*- coding: utf-8 -*-

from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import os
import argparse
import imghdr
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--keyword', type=str, default='')
parser.add_argument('--number', type=int, default='700')
FLAGS = parser.parse_args()

number = FLAGS.number
key_word=FLAGS.keyword

dir='/data/datasets/imagedata'


google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': key_word})
google_crawler.crawl(keyword=key_word, offset=0, max_num=number, date_min=None, date_max=None, min_size=(200, 200),
                     max_size=None)

files = os.listdir(key_word)
for f in files:
    os.rename(os.path.join(key_word, f), os.path.join(key_word, 'google' + f))

bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': key_word})
bing_crawler.crawl(keyword=key_word, offset=0, max_num=number, min_size=None, max_size=None)

files = os.listdir(key_word)
for f in files:
    if f[0] != 'g':
        os.rename(os.path.join(key_word, f), os.path.join(key_word, 'bing' + f))


files = os.listdir(key_word)

for f in files:
    if os.path.isdir(os.path.join(key_word, f)):
        shutil.rmtree(os.path.join(key_word, f))
    elif imghdr.what(os.path.join(key_word, f)) != 'jpeg':
        os.remove(os.path.join(key_word, f))
