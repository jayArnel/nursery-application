import math
import numpy as np
import cPickle as pickle

from django.core.management.base import BaseCommand

from sklearn import svm
from sklearn import preprocessing
from sklearn import utils

class Command(BaseCommand):
    help = 'Train the Support Vector Machine using the given dataset'

    def handle(self, *args, **kwargs):
        self.stdout.write('Training SVM...')
        self.stdout.write('Loading dataset...')
        dataset = pickle.load(open('svm/pickles/dataset.pickle', 'r'))
        self.stdout.write('dataset: \n%s' % dataset)
        self.stdout.write('Paritioning dataset...')
        instances = len(dataset)
        num_train = instances * .80
        num_train = math.modf(num_train)[1]
        num_test = instances - num_train
        X = dataset[:,:-1]
        self.stdout.write('Normalizing features...')
        X = preprocessing.scale(X)
        Y = dataset[:,-1]
        X_train = X[:num_train]
        Y_train = Y[:num_train]
        X_test = X[-num_test:]
        Y_test = Y[-num_test:]
        gammaSteps = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]
        CSteps = [1, 3, 10, 30, 100, 300, 1000, 3000];
        maxScore = 0
        optC = 0
        optGamma = 0
        self.stdout.write('Tuning parameters...')
        for tempC in CSteps:
            for tempGamma in gammaSteps:
                clf = svm.SVC(C=tempC, gamma=tempGamma)
                clf.fit(X_train, Y_train)
                score = clf.score(X_test, Y_test)
                self.stdout.write("C: {0}, gamma: {1}, score: {2}".format(tempC, tempGamma, score))
                if score > maxScore:
                    optC = tempC
                    optGamma = tempGamma
                    maxScore = score
        self.stdout.write("optimum:\n C: {0}, gamma: {1}, score: {2}".format(optC, optGamma, maxScore))
        clf = svm.SVC(C=optC, gamma=optGamma)
        self.stdout.write('Saving SVM...')
        pickle.dump(clf, open('svm/pickles/svm.pickle', 'w'))
        self.stdout.write('Done.')



