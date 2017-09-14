# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import shutil
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, default='')
parser.add_argument('--keyword', type=str, default='')
FLAGS = parser.parse_args()



#folder = '/data/datasets/imagedata' + name
folder = FLAGS.folder
keyword=FLAGS.keyword
train = '"'+'/data/datasets/imagedata/train/' + keyword+'"'
validation = '"'+'/data/datasets/imagedata/validation/' + keyword+'"'
test = '"'+'/data/datasets/imagedata/test/' + keyword+'"'


if os.path.exists(os.path.join(folder, '.ipynb_checkpoints')):
    shutil.rmtree(os.path.join(folder, '.ipynb_checkpoints'))

files = os.listdir(folder)
length = len(files)

train_number = int(length * 0.8)
validation_number = int(length * 0.95)

shuf = [i for i in range(length)]
random.shuffle(shuf)

for i in range(train_number):
    if not os.path.exists(train):
        os.mkdir(train)
    shutil.move(os.path.join(folder, files[shuf[i]]), os.path.join(train, files[shuf[i]]))
for i in range(train_number, validation_number):
    if not os.path.exists(validation):
        os.mkdir(validation)
    shutil.move(os.path.join(folder, files[shuf[i]]), os.path.join(validation, files[shuf[i]]))
for i in range(validation_number, length):
    if not os.path.exists(test):
        os.mkdir(test)
    shutil.move(os.path.join(folder, files[shuf[i]]), os.path.join(test, files[shuf[i]]))
