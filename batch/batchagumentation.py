# -*- coding: utf-8 -*-
# !/usr/bin/env python

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
import shutil
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, default='')
parser.add_argument('--keyword', type=str, default='')
FLAGS = parser.parse_args()


datagen = ImageDataGenerator(rotation_range=50, width_shift_range=0.3, height_shift_range=0.3, shear_range=0.2,
                             zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')

folder = FLAGS.folder
keyword=FLAGS.keyword
files = os.listdir(folder)
file_number = sum([len(x) for _, _, x in os.walk(os.path.dirname(folder))])
count = math.floor(5000 / file_number)

for f in files:
    if os.path.isdir(os.path.join(folder, f)):
        shutil.rmtree(os.path.join(folder, f))
        continue
    img = load_img(os.path.join(folder, f))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir=folder, save_prefix=keyword, save_format='jpg'):
        i += 1
        if i > count:
            break

print('Augmentation finished!')

