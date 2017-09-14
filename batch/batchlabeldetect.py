# -*- coding: utf-8 -*-
#!/usr/bin/env python
#pip install --upgrade google-cloud-vision
#export GOOGLE_APPLICATION_CREDENTIALS=/data/zixuan_google_api.json
from google.cloud import vision
import io
import os
from PIL import ImageFile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, default='')
parser.add_argument('--keyword', type=str, default='')
parser.add_argument('--score', type=str, default='')
FLAGS = parser.parse_args()

#os.system('export GOOGLE_APPLICATION_CREDENTIALS=/data/zixuan_google_api.json')
vision_client = vision.Client()

ImageFile.LOAD_TRUNCATED_IMAGES = True

folder = FLAGS.folder
files = os.listdir(folder)
length = len(files)
count = 0
for file_name in files:
	if file_name == '.DS_Store':
		continue
	file_path = os.path.join(folder, file_name)

	if os.stat(file_path).st_size > 4000000:
		os.remove(file_path)
		count += 1
		print('Deleted big image %s' % file_name)
		continue

	with io.open(file_path, 'rb') as image_file:
	    content = image_file.read()
	    image = vision_client.image(content=content)
	try:
		labels = image.detect_labels()
	except Exception as e:
		print('Deleted %s because failed to detect labels' % file_name)
		os.remove(file_path)
		count += 1
		continue
	descriptions = [label.description for label in labels]
	scores = [label.score for label in labels]
	keyword = FLAGS.keyword
	score=FLAGS.score

	if keyword in descriptions and scores[descriptions.index(keyword)] >= score:
		break
	else:
		os.remove(file_path)
		print('Deleted irrelevant image %s' % file_name)
		count += 1
	print('Kept good image %s' % file_name)
print('deleted %d images from %d total' % (count, length))
