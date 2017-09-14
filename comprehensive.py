from keras.models import load_model
import os
from PIL import Image
import numpy as np
import imghdr
from os import path

def preprocess_input(x):
	x /= 255
	x -= 0.5
	x *= 2
	return x

def comprehensive_censor(image_path):
	model_cigar = load_model('/home/zixuan/image_censor/models/cigar.h5')
	model_cigarette = load_model('/home/zixuan/image_censor/models/cigarette.h5')
	model_alcohol = load_model('/home/zixuan/image_censor/models/alcohol.h5')
	model_disaster = load_model('/home/zixuan/image_censor/models/disaster.h5')
	model_pill = load_model('/home/zixuan/image_censor/models/pill.h5')
	model_military = load_model('/home/zixuan/image_censor/models/military.h5')
	files = os.listdir(image_path)
	drug, alcohol, tobacco, military, disaster = [0, []], [0, []], [0, []], [0, []], [0, []]
	for f in files:
		file_path = path.join(image_path, f)
		if path.isdir(file_path):
			continue
		type_check = imghdr.what(file_path)
		if type_check != 'jpeg' and type_check != 'png':
			continue
		
		im = Image.open(file_path).resize((299, 299))
		nda = np.array(im)
		if nda.shape == (299, 299, 4):
			nda = nda[:,:,0:3]
		if nda.shape != (299, 299, 3):
			continue
		arr = np.expand_dims(nda, axis=0)
		y_pred = model_disaster.predict(preprocess_input(arr.astype('float32')))
		y_pred = y_pred.ravel()
		y_pred = list(y_pred)
		score = max(y_pred)
		idx = y_pred.index(score)
		# car_accident, earthquake, explosion, fire, flood, normal
		if idx != 5 and score > 0.95:
			disaster[0] += 1
			disaster[1].append(f)
		y_pred = model_pill.predict(preprocess_input(arr.astype('float32')))
		y_pred = y_pred.ravel()
                y_pred = list(y_pred)
                score = max(y_pred)
                idx = y_pred.index(score)
		# normal, pill
		if idx == 1 and score > 0.95:
			drug[0] += 1
			drug[1].append(f)
		y_pred = model_alcohol.predict(preprocess_input(arr.astype('float32')))
                y_pred = y_pred.ravel()
                y_pred = list(y_pred)
                score = max(y_pred)
                idx = y_pred.index(score)
		# alcohol, normal
		if idx == 0 and score > 0.95:
			alcohol[0] += 1
			alcohol[1].append(f)
		y_pred = model_cigar.predict(preprocess_input(arr.astype('float32')))
                y_pred = y_pred.ravel()
                y_pred = list(y_pred)
                score1 = max(y_pred)
                idx1 = y_pred.index(score1)
		# cigar, normal
		y_pred = model_cigarette.predict(preprocess_input(arr.astype('float32')))
                y_pred = y_pred.ravel()
                y_pred = list(y_pred)
                score2 = max(y_pred)
                idx2 = y_pred.index(score2)
		# cigarette, normal
		if (idx1 == 0 and score1 > 0.95) or (idx2 == 0 and score2 > 0.95):
			tobacco[0] += 1
			tobacco[1].append(f)
		y_pred = model_military.predict(preprocess_input(arr.astype('float32')))
                y_pred = y_pred.ravel()
                y_pred = list(y_pred)
                score = max(y_pred)
                idx = y_pred.index(score)
		# military, normal
		if idx == 0 and score > 0.95:
			military[0] += 1
			military[1].append(f)
	return drug[0], alcohol[0], tobacco[0], military[0], disaster[0], drug[1], alcohol[1], tobacco[1], military[1], disaster[1]
