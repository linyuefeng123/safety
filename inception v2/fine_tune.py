import math, json, os, sys

import keras
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.models import Sequential
from keras import optimizers
from PIL import ImageFile
from inception_resnet_v2 import InceptionResNetV2
from keras import backend as K
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.grid_search import GridSearchCV


def recall(y_true, y_pred):
    """Recall metric.

    Only computes a batch-wise average of recall.

    Computes the recall, a metric for multi-label classification of
    how many relevant items are selected.
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

#custon loss function
#def my_koss(y_true,y_pred):
  #  return K.mean((y_pred-y_true),axis = -1)



DATA_DIR = '/data/datasets/data_drug'
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
VALID_DIR = os.path.join(DATA_DIR, 'validation')
SIZE = (299, 299)
#BATCH_SIZE = 32

if __name__ == "__main__":
    num_train_samples = sum([len(files) for r, d, files in os.walk(TRAIN_DIR)])
    num_valid_samples = sum([len(files) for r, d, files in os.walk(VALID_DIR)])

    num_train_steps = math.floor(num_train_samples/BATCH_SIZE)
    num_valid_steps = math.floor(num_valid_samples/BATCH_SIZE)

    gen = keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True, rotation_range=40, zoom_range=0.2, width_shift_range=0.2, height_shift_range=0.2)
    val_gen = keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True, rotation_range=40, zoom_range=0.2, width_shift_range=0.2, height_shift_range=0.2)

    batches = gen.flow_from_directory(TRAIN_DIR, target_size=SIZE, class_mode='categorical', shuffle=True, batch_size=BATCH_SIZE)
    val_batches = val_gen.flow_from_directory(VALID_DIR, target_size=SIZE, class_mode='categorical', shuffle=True, batch_size=BATCH_SIZE)
    classes = list(iter(batches.class_indices))
    for c in batches.class_indices:
        classes[batches.class_indices[c]] = c

    base_model = InceptionResNetV2(include_top=False, pooling='avg')
    for layer in base_model.layers:
        layer.trainable=False
    outputs = Dense(len(classes), activation='softmax')(base_model.output)


	# fix random seed for reproducibility
	seed = 7
	numpy.random.seed(seed)

	        #sklearn wrapper
	  def creat_model():
		    model = Model(base_model.input, outputs)
		    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
		    model.classes = classes
	  	return model

	model=KerasClassifier(build_fn=create_model, verbose=0)

	# define the grid search parameters
	BATCH_SIZE = [10, 20, 40, 60, 80, 100]
	epochs = [10, 50, 100]
	weight_constraint = [1, 2, 3, 4, 5]
	dropout_rate = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
	optimizer = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
	param_grid = dict(batch_size=BATCH_SIZE, nb_epoch=epochs,optimizer=optimizer,dropout_rate=dropout_rate, weight_constraint=weight_constraint)
	grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)
	grid_result = grid.fit(base_model, outputs)

	# summarize results
	print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
	for params, mean_score, scores in grid_result.grid_scores_:
	    print("%f (%f) with: %r" % (scores.mean(), scores.std(), params))

    


    early_stopping = EarlyStopping(patience=20)
    checkpointer = ModelCheckpoint('inception_resnet_bottleneck_drug_best.h5', verbose=1, save_best_only=True)

    ImageFile.LOAD_TRUNCATED_IMAGES = True

    model.fit_generator(batches, steps_per_epoch=num_train_steps, epochs=1000, callbacks=[early_stopping, checkpointer], validation_data=val_batches, validation_steps=num_valid_steps)
    model.save_weights('inception_resnet_bottleneck_drug_weights.h5')
    model.save('inception_resnet_bottleneck_drug.h5')

#     for layer in model.layers[-31:]:
#         layer.trainable=True
#     for layer in model.layers[:-31]:
#         layer.trainable=False

#     model.compile(loss='categorical_crossentropy', optimizer=optimizers.SGD(lr=1e-4, momentum=0.9), metrics=['accuracy'])

#     checkpointer = ModelCheckpoint('./resnet50_best_safety.h5', verbose=1, save_best_only=True)

#     model.fit_generator(batches, steps_per_epoch=num_train_steps, epochs=1000, callbacks=[early_stopping, checkpointer], validation_data=val_batches, validation_steps=num_valid_steps)
#     model.save('resnet50_safety.h5')
