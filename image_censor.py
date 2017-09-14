# -*- coding: utf-8 -*-  
import os
import argparse
from PIL import Image
from os import path
from os import listdir
# from irv2 import Safety
from comprehensive import comprehensive_censor
from adult import image_adult
from terrorism import image_terrorism
from politician import image_politician
# from google.cloud import vision
# from politician import add_politician 
# Uncomment the above IMPORT line if more politicians need to be added. 
# Usage: add_politician(image_path, person_id, person_name, group_ids = ['politician'], data_type = 0)(data_type = 1 means URL, 0 means local file)

def censor(image_path):
	# Use Google cloud vision to calibrate results (optional)
	# os.system('export GOOGLE_APPLICATION_CREDENTIALS=/home/zixuan/image_censor/zixuan_google_api.json')
	# vision_client = vision.Client()

	# Filter out small images
	files = listdir(image_path)
	total_image_number = len(files)
	lower_thre = 400
	percent_thre = 0.5
	resolutions = []
	for f in files:
		im = Image.open(path.join(image_path, f))
		width, height = im.size
		resolution = width * height
		resolutions.append((resolution, f))
	resolutions.sort(key = lambda x : x[0], reverse = True)
	if not resolutions:
		print('No images in the folder')
		return
	elif resolutions[0][0] < lower_thre:
		print('All images are too small')
		return
	remain = int(len(resolutions) * percent_thre)
	files = [resolutions[i][1] for i in range(remain)]

	# print(files)

	# Porn censor
	porn_count = 0
	porns = []
	for f in files:
		res = image_adult(path.join(image_path, f))
		if res[0] == 'error':
			res = image_adult(path.join(image_path, f))
		if res[0] == 'error':
			continue
		if res[0] == 'porn':
			porn_count += 1	
			porns.append(f)	

	# Politician censor (Party and Government leader in China)
	politician_count = 0
	politicians = []
	for f in files:
		res = image_politician(path.join(image_path, f))
		if res == 'Error or There is no person face in image':
			res = image_politician(path.join(image_path, f))
		if res == 'Error or There is no person face in image':
			continue
		if res != 'Not a Chinese Zhongnanhai Politician':
			politician_count += 1	
			politicians.append(f)	

	terrorism_count = 0
	terrorisms = []
	for f in files:
		res = image_terrorism(path.join(image_path, f))
		if res[0] != 'other' and res[1] > 95:
			terrorism_count += 1
			terrorisms.append(f) 
	
	# Terrorism censor (terrorists, knife, guns, blood, fire, flag, crowd, other)
	# terrorism_count, terrorisms = image_terrorism(image_path)

	# Others censor (drug, alcohol, tobacco, religion, gambling, military, disaster)
	# safety = Safety(image_path)
	# drug, alcohol, tobacco, military, disaster, drugs, alcohols, tobaccos, militarys, disasters = safety.censor()
	
	drug, alcohol, tobacco, military, disaster, drugs, alcohols, tobaccos, militarys, disasters = comprehensive_censor(image_path)

	return total_image_number, porn_count, politician_count, terrorism_count, drug, alcohol, tobacco, military, disaster, porns, politicians, terrorisms, drugs, alcohols, tobaccos, militarys, disasters

	#if porn_count > 0 or politician_count > 0 or float(terrorism_count)/total_image_number >= 0.1 or float(drug)/total_image_number >= 0.1 or float(alcohol)/total_image_number >= 0.1 or float(tobacco)/total_image_number >= 0.1 or float(religion)/total_image_number or float(military)/total_image_number >= 0.1 or float(disaster)/total_image_number >= 0.1:
	#	print(1)
	#else:
	#	print(0)

	#print('Total image number: %d' % total_image_number)
	#print('Unsafe Image Count')
	#print('Porn: %d' % porn_count)
	#print('Politician: %d' % politician_count)
	#print('Terrorism: %d' % terrorism_count)
	#print('Drug: %d' % drug)
	#print('Alcohol: %d' % alcohol)
	#print('Tobacco: %d' % tobacco)
	#print('Religion: %d' % religion)
	#print('Gambling: %d' % gambling)
	#print('Military: %d' % military)
	#print('Disaster: %d' % disaster)
