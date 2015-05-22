import os.path
import math
import numpy as np
import cPickle as pickle

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from _getch import getch

from sklearn import svm
from sklearn import preprocessing
from sklearn import utils


class Command(BaseCommand):
    help = 'Preprocess the dataset by encoding and shuffling.'

    def handle(self, *args, **options):
        if (os.path.isfile(settings.DATASET_PATH)):
            self.stdout.write(
                'A processed dataset is already present. Do you want to '
                'overwrite existing dataset? (Y/N): ', ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                self.process()
            elif choice == 'N':
                self.stdout.write('Aborting process.')
            else:
                raise CommandError('Dataset processing cancelled')
        else:
            self.process()

    def process(self):
        self.stdout.write('Retrieving and loading dataset...')
        data = open('nursery.dat', 'r')
        dataset = np.loadtxt(fname=data, delimiter=',', dtype=str, ndmin=2)
        self.stdout.write('Encoding dataset values...')
        encoders = []
        encoded = np.ndarray(shape=dataset.shape[::-1], dtype=np.int32)
        for i in range(0, len(dataset.T)):
            col = dataset.T[i]
            enc = preprocessing.LabelEncoder()
            col = enc.fit_transform(col)
            encoded[i] = col
            encoders.append(enc)
        self.stdout.write('Shuffling dataset...')
        dataset = utils.shuffle(encoded.T)
        self.stdout.write('Saving dataset and encoders...')
        pickle.dump(dataset, open(settings.DATASET_PATH, 'w'))
        pickle.dump(encoders, open(settings.ENCODERS_PATH, 'w'))
        self.stdout.write('dataset: \n%s' % dataset)
        self.stdout.write('Done.')
