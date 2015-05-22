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
    help = 'Load SVM and check parameters'

    def handle(self, *args, **options):
        if (os.path.isfile(settings.SVM_PATH)):
            svm = pickle.load(open(settings.SVM_PATH, 'r'))
            self.stdout.write(str(svm.get_params()))
        else:
            self.stdout.write(
                'No SVM is trained. Train SVM first? (Y/N): ', ending='')
            choice = getch()
            self.stdout.write(choice)
            if choice == 'Y':
                call_command('train_svm')
            elif choice == 'N':
                self.stdout.write('Aborting process.')
            else:
                raise CommandError('SVM loading cancelled')

