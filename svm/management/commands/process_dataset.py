import math
import numpy as np
import cPickle as pickle

from django.core.management.base import BaseCommand

from sklearn import preprocessing
from sklearn import svm
from sklearn import utils

class Command(BaseCommand):
    help = 'Preprocess the dataset by encoding and shuffling.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Retrieving and loading dataset...')
        data = open('nursery.dat', 'r')
        
        dataset = np.loadtxt(fname=data, delimiter=',', dtype=str, ndmin=2)
        self.stdout.write('Encoding dataset values...')
        encoders = []
        encoded = np.ndarray(shape=dataset.shape[::-1],dtype=np.int32)
        for i in range(0, len(dataset.T)):
            col = dataset.T[i]
            enc = preprocessing.LabelEncoder()
            col = enc.fit_transform(col)
            encoded[i] = col
            encoders.append(enc)
        self.stdout.write('Shuffling dataset...')
        dataset = utils.shuffle(encoded.T)
        self.stdout.write('Saving dataset and encoders...')
        pickle.dump(dataset, open('svm/pickles/dataset.pickle', 'w'))
        pickle.dump(encoders, open('svm/pickles/encoders.pickle', 'w'))
        self.stdout.write('dataset: \n%s' % dataset)
        self.stdout.write('Done.')


