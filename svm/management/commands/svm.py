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
    help = 'SVM commands. Loads and displays SVM parameters by default.'

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument('--clear',
                            action='store_true',
                            dest='clear',
                            default=False,
                            help='Clear SVM')
        parser.add_argument('--train',
                            action='store_true',
                            dest='train',
                            default=False,
                            help='Train the SVM')

        parser.add_argument('--predict',
                            action='store_true',
                            dest='predict',
                            default=False,
                            help='Use SVM to predict')

    def handle(self, *args, **options):
        print options
        if options['clear']:
            self.clear()
        elif options['predict']:
            self.predict()
        elif options['train']:
            self.train_handle()
        elif options:
            self.load()

    def load(self):
        if (os.path.isfile(settings.SVM_PATH)):
            svm = pickle.load(open(settings.SVM_PATH, 'r'))
            self.stdout.write(str(svm.get_params()))
        else:
            self.stdout.write(
                'No SVM is trained. Train SVM first? (Y/N): ', ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                call_command('svm','--train')
            elif choice == 'N':
                self.stdout.write('Aborting process.')
            else:
                raise CommandError('SVM loading cancelled')

    def clear(self):
        if (os.path.isfile(settings.SVM_PATH)):
            self.stdout.write(
                'Are you sure you want to clear the SVM? (Y/N): ',
                ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                os.remove(settings.SVM_PATH)
                self.stdout.write('SVM cleared.')
            elif choice == 'N':
                self.stdout.write('SVM not cleared.')
        else:
            self.stdout.write('No SVM found. Nothing to clear.')

    def predict(self):
        self.stdout.write('Enter values:')
        X = []
        i = 0
        encoders = pickle.load(open(settings.ENCODERS_PATH, 'r'))
        self.stdout.write('Parent\'s occupation:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Child\'s nursery:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Form of the family:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Number of children:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Housing conditions:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Financial standing of the family:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Social conditions:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Health conditions:', ending='')
        le = encoders[i]
        for j in range(0, len(le.classes_)):
            self.stdout.write(
                '{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        svm = pickle.load(open(settings.SVM_PATH, 'r'))
        print X
        class_encoder = encoders[i]
        prediction = svm.predict(X)
        label = class_encoder.inverse_transform(prediction)
        self.stdout.write(label[0])

    def train_handle(self):
        if (os.path.isfile(settings.SVM_PATH)):
            self.stdout.write(
                'The SVM is already trained. Do you want to retrain and '
                'overwrite current SVM parameters? (Y/N): ', ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                pass
            elif choice == 'N':
                self.stdout.write('Aborting training.')
            else:
                raise CommandError('SVM training cancelled')

        if (os.path.isfile(settings.DATASET_PATH)):
            pass
        else:
            self.stdout.write(
                'No dataset has been processed. Processing dataset.')
            call_command('process_dataset')
        self.train()

    def train(self):
        self.stdout.write('Training SVM...')
        self.stdout.write('Loading dataset...')
        dataset = pickle.load(open(settings.DATASET_PATH, 'r'))
        self.stdout.write('dataset: \n%s' % dataset)
        self.stdout.write('Paritioning dataset...')
        instances = len(dataset)
        num_train = instances * .80
        num_train = math.modf(num_train)[1]
        num_test = instances - num_train
        X = dataset[:, :-1]
        Y = dataset[:, -1]
        X_train = X[:num_train]
        Y_train = Y[:num_train]
        X_test = X[-num_test:]
        Y_test = Y[-num_test:]
        gammaSteps = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]
        CSteps = [1, 3, 10, 30, 100, 300, 1000, 3000]
        maxScore = 0
        optC = 0
        optGamma = 0
        optClf = svm.SVC()
        self.stdout.write('Tuning parameters...')
        for tempC in CSteps:
            for tempGamma in gammaSteps:
                clf = svm.SVC(C=tempC, gamma=tempGamma)
                clf.fit(X_train, Y_train)
                score = clf.score(X_test, Y_test)
                self.stdout.write(
                    "C: {0}, gamma: {1}, score: {2}".format(
                        tempC, tempGamma, score))
                if score > maxScore:
                    optC = tempC
                    optClf = clf
                    optGamma = tempGamma
                    maxScore = score
        self.stdout.write(
            "optimum:\n C: {0}, gamma: {1}, score: {2}".format(
                optC, optGamma, maxScore))
        self.stdout.write('Saving SVM...')
        pickle.dump(optClf, open(settings.SVM_PATH, 'w'))
        self.stdout.write('Done.')
