# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--number', type=int, default='700')
FLAGS = parser.parse_args()


table='mahjong casino gambling butcher knife gun ' \
      'firearm sword tank armour army bullet troop war soldier ' \
      'militia marines missile lightning thunder disaster fire explosion ' \
      'tornado flood fireman pollution smoke earthquake ' \
       'alocohol cocktail whisky liqueur wine ' \
       'death skull skeleton zombie darkness ' \
       'blood flesh organism grave ' \
       'accident smoking cigarette religion mythology slot weapon'

table1='traffic collision/tobacco products/alcoholic beverage/explosive material/military organization/military aircraft/cold weapon/slaughter house/destoryed city'

number = FLAGS.number
key_words = table.split()

dir='/data/datasets/imagedata'

for i in range(0, len(key_words)):
    output_dir = dir + '/' + key_words[i]
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
        os.system('python imagedownload --keywords key_word[i] --number number')    #download
        os.system('python imagedownload --keywords key_word[i]')                #filter
    else:
        os.system('python imagedownload --keywords key_word[i]')            #filter








