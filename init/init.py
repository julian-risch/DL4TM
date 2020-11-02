from keras.utils.data_utils import get_file
import numpy as np
import os

datasets_path = os.getcwd()+'/datasets/'

#print('> loading reuters data...')
#get_file(datasets_path + 'reuters.npz', 
#         origin='https://s3.amazonaws.com/text-datasets/reuters.npz')
#print('> loading reuters word index...')
#get_file(datasets_path + 'reuters_word_index.json', 
#         origin='https://s3.amazonaws.com/text-datasets/reuters_word_index.json')
#
#print('> loading IMDB data...')
#get_file(datasets_path + 'imdb.npz',
#         origin='https://s3.amazonaws.com/text-datasets/imdb.npz')
#print('> loading IMDB word index...')
#get_file(datasets_path + 'imdb_word_index.json', 
#         origin='https://s3.amazonaws.com/text-datasets/imdb_word_index.json')
#
#print('> loading boston housing data...')
#get_file(datasets_path + 'boston_housing.npz', 
#         origin='https://s3.amazonaws.com/keras-datasets/boston_housing.npz')

print('> testing tensorflow...')
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

print('> testing keras...')
from keras.backend import backend, epsilon
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras import __version__ as kv

print('Using Keras Version (Tutorial written with 2.0.5)', kv)
print('Keras is using backend (should print tensorflow): ' + backend())
print('Numeric precision:', epsilon())

model = Sequential()
model.add(Dense(units=2, input_dim=2))
model.add(Activation('relu'))
model.add(Dense(units=1))
model.add(Activation('softmax'))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
model.fit(np.array([[1,1],[1,2],[1,2],[1,1]]), np.array([0,1,1,0]), epochs=2, batch_size=1, verbose=0)

print('> testing sklearn')
import sklearn

print('Python setup done')


