# -*- coding: utf-8 -*-
# !/usr/bin/env python
# usage: python batch.py --number 700
#export GOOGLE_APPLICATION_CREDENTIALS=/data/zixuan_google_api.json

import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, default='')
FLAGS = parser.parse_args()


table = 'mahjong casino gambling butcher knife gun ' \
        'firearm sword tank armour army bullet troop war soldier ' \
        'militia marines missile lightning earthquake thunder disaster fire explosion ' \
        'tornado flood fireman pollution smoke earthquake ' \
        'alcohol cocktail whisky liqueur wine ' \
        'death skull skeleton zombie darkness ' \
        'blood flesh organism grave ' \
        'accident smoking cigarette religion mythology slot weapon'


table1 = 'traffic collision/tobacco products/alcoholic beverage/explosive material/military organization/military aircraft/cold weapon/slaughter house/destroyed city'

key_words = table.split()
dkey_words = table1.split('/')

#key_words = key_words + dkey_words

score = FLAGS.score

dir = '/data/datasets/imagedata'

for i in range(0, len(key_words)):
    output_dir = dir + '/' + key_words[i]+ '/'
    command = 'python ' + 'batchagumentation.py ' + '--folder '+output_dir+' --keyword ' + key_words[i]
    print(command)
    subprocess.Popen(command, shell=True)

for i in range(0, len(dkey_words)):
    output_dir = dir + '/' + dkey_words[i]+ '/'
    command2 = 'python ' + 'batchagumentation.py ' + '--folder '+output_dir+' --keyword ' + '"'+dkey_words[i]+'"'
    print(command2)
    subprocess.Popen(command2, shell=True)


print('finish detecting, please start split script')





















