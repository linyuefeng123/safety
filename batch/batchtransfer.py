# -*- coding: utf-8 -*-
# !/usr/bin/env python
# usage: python batchtransfer.py


import os
import subprocess



table = 'mahjong casino gambling butcher knife gun ' \
        'firearm sword tank armour army bullet troop war soldier ' \
        'militia marines missile lightning earthquake thunder disaster fire explosion ' \
        'tornado flood fireman pollution smoke ' \
        'alcohol cocktail whisky liqueur wine ' \
        'death skull skeleton zombie darkness ' \
        'blood flesh organism grave ' \
        'smoking cigarette religion mythology weapon ' \
        'abbess priest monk imam buddha data_drug data_representative_religious_objects data_religion_building chineseflag emblem'


table1 = 'traffic collision/tobacco products/alcoholic beverage/explosive material/military organization/military aircraft/cold weapon/slaughter house'

key_words = table.split()
dkey_words = table1.split('/')

'''
mv /data/datasets/imagedata/data_drug/train /data/datasets/imagedata/train/data_drug
mv /data/datasets/imagedata/data_drug/validation /data/datasets/imagedata/validation/data_drug
mv /data/datasets/imagedata/data_drug/test /data/datasets/imagedata/validation/test
'''



dir = '/data/datasets/imagedata/'



for i in range(0, len(key_words)):
    command1 = 'mv ' + dir +  key_words[i]+'/train '+dir+'train/' + key_words[i]
    command2 = 'mv ' + dir +  key_words[i]+'/validation '+dir+'validation/' + key_words[i]
    command3 = 'mv ' + dir +  key_words[i]+'/test '+dir+'test/' + key_words[i]
    print(command1, command2,command3)
    os.system(command1)
    os.system(command2)
    os.system(command3)

for i in range(0, len(dkey_words)):
    command1 = 'mv ' + dir +  dkey_words[i]+'/train '+dir+'train/' + '"'+dkey_words[i]+'"'
    command2 = 'mv ' + dir +  dkey_words[i]+'/validation '+dir+'validation/' + '"'+dkey_words[i]+'"'
    command3 = 'mv ' + dir +  dkey_words[i]+'/test '+dir+'test/' + '"'+dkey_words[i]+'"'
    print(command1, command2,command3)
    os.system(command1)
    os.system(command2)
    os.system(command3)























