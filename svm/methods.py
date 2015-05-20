import math
import numpy as np

from sklearn import preprocessing
from sklearn import utils
from sklearn import svm

def get_dataset(filepath): 
    data = open(filepath, 'r')
    dataset = np.loadtxt(fname=data, delimiter=',', dtype=str, ndmin=2)
    return dataset

def encode(dataset):
    encoders = []
    encoded = np.ndarray(shape=dataset.shape[::-1])
    for i in range(0, len(dataset.T)):
        col = dataset.T[i]
        enc = preprocessing.LabelEncoder()
        col = enc.fit_transform(col)
        encoded[i] = col
        encoders.append(enc)
    return utils.shuffle(encoded.T), encoders

def partition(dataset):
    instances = len(dataset)
    num_train = instances * .80
    num_train = math.modf(num_train)[1]
    num_test = instances - num_train
    X = dataset[:,:-1]
    X = preprocessing.scale(X)
    Y = dataset[:,-1]
    X_train = X[:num_train]
    Y_train = Y[:num_train]
    X_test = X[-num_test:]
    Y_test = Y[-num_test:]
    return X_train, Y_train, X_test, Y_test

