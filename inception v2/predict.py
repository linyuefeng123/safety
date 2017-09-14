from keras.models import load_model
import os
from PIL import Image
import numpy as np
import inception_resnet_v2 as keras_irv2

model_path = '/data/keras-inception-resnet-v2/inception_resnet_bottleneck_drug.h5'
root = '/data/datasets/data_drug/test'
model = load_model(model_path)

folders = os.listdir(root)
folders.sort()
folders.pop(0)
for folder in folders:
    if os.path.isdir(os.path.join(root, folder)):
        idx = folders.index(folder)
        files = os.listdir(os.path.join(root, folder))
        length = len(files)
        count = 0
        wrong = []
        for f in files:
            im = Image.open(os.path.join(root, folder, f)).resize((299, 299))
            arr = np.expand_dims(np.array(im), axis=0)
            y_pred = model.predict(keras_irv2.preprocess_input(arr.astype('float32')))
            y_pred = y_pred.ravel()
            pred_idx = np.argmax(y_pred)
            pred_max = np.max(y_pred)
            if pred_idx == idx:
                count += 1
            else:
                wrong.append(pred_max)
        print(folder, count, length, float(count)/float(length))
        print(wrong)
