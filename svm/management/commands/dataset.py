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
    help = 'Dataset commands. Displays the dataset by default.'

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument('--clear',
                            action='store_true',
                            dest='clear',
                            default=False,
                            help='Clear SVM')
        
        parser.add_argument('--process',
                            action='store_true',
                            dest='process',
                            default=False,
                            help='Use SVM to predict')

    def handle(self, *args, **options):
        print options
        if options['clear']:
            self.clear()
        elif options['process']:
            self.process_handle()
        elif options:
            self.load()

    def load(self):
        if (os.path.isfile(settings.DATASET_PATH)):
            dataset = pickle.load(open(DATASET_PATH, 'r'))
            self.stdout.write("%s", dataset)
        else:
            self.stdout.write(
                'No dataset has been processed. Process dataset now? (Y/N): ',
                ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                call_command('dataset', '--process')
            elif choice == 'N':
                self.stdout.write('Aborting process.')
            else:
                raise CommandError('Dataset loading cancelled')

    def clear(self):
        if (os.path.isfile(settings.DATASET_PATH)):
            self.stdout.write(
                'Are you sure you want to clear the dataset? (Y/N): ',
                ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                os.remove(settings.DATASET_PATH)
                self.stdout.write('Dataset cleared.')
            elif choice == 'N':
                self.stdout.write('Dataset not cleared.')
        else:
            self.stdout.write('No dataset found. Nothing to clear.')

    def process_handle(self):
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
