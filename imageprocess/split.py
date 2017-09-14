import os
import shutil
import random

folder = '/data/random15000/random_image'
files = os.listdir(folder)
length = len(files)

train_number = int(5000 * 0.8)
validation_number = int(5000 * 0.95)

shuf = [i for i in range(length)]
random.shuffle(shuf)

for i in range(train_number):
    shutil.copyfile(os.path.join(folder, files[shuf[i]]), os.path.join('notdrugTrain', files[shuf[i]]))
for i in range(train_number, validation_number):
    shutil.copyfile(os.path.join(folder, files[shuf[i]]), os.path.join('notdrugValidation', files[shuf[i]]))
for i in range(validation_number, 5000):
    shutil.copyfile(os.path.join(folder, files[shuf[i]]), os.path.join('notdrugTest', files[shuf[i]]))
