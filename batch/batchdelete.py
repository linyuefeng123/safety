#!/usr/bin/env python
# -*- coding: utf-8 -*-

from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import os
import argparse
import imghdr


parser = argparse.ArgumentParser()
parser.add_argument('--keyword', type=str, default='')
FLAGS = parser.parse_args()

dir='/data/datasets/imagedata'


# delete non-jpeg
for i in range(0, len(key_words)):

    files = os.listdir(key_words[i])

    for f in files:
        if os.path.isdir(os.path.join(key_words[i], f)):
            shutil.rmtree(os.path.join(key_words[i], f))
        elif imghdr.what(os.path.join(key_words[i], f)) != 'jpeg':
            os.remove(os.path.join(key_words[i], f))

for i in range(0, len(dkey_words)):

    files = os.listdir(dkey_words[i])

    for f in files:
        if os.path.isdir(os.path.join(dkey_words[i], f)):
            shutil.rmtree(os.path.join(dkey_words[i], f))
        elif imghdr.what(os.path.join(dkey_words[i], f)) != 'jpeg':
            os.remove(os.path.join(dkey_words[i], f))