import math
import numpy as np
import cPickle as pickle
import sys

from django.core.management.base import BaseCommand

from sklearn import preprocessing

class Command(BaseCommand):
    help = 'Use the SVM for prediction'

    def handle(self, *args, **kwargs):
        self.stdout.write('Enter values:')
        X = []
        i = 0
        encoders = pickle.load(open('svm/pickles/encoders.pickle', 'r'))
        self.stdout.write('Parent\'s occupation:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Child\'s nursery:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Form of the family:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Number of children:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Housing conditions:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Financial standing of the family:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Social conditions:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        self.stdout.write('Health conditions:', ending='')
        le = encoders[i]
        for j in range(0,len(le.classes_)):
            self.stdout.write('{0}: {1}'.format(j, le.classes_[j]), ending='\t')
        X.append(raw_input())
        i += 1
        svm = pickle.load(open('svm/pickles/svm.pickle', 'r'))
        print X
        class_encoder = encoders[i]
        prediction = svm.predict(X)
        label = class_encoder.inverse_transform(prediction)
        self.stdout.write(label[0])


