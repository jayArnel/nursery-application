import os.path
from django.conf import settings
from django.core.management.base import BaseCommand

from _getch import getch

class Command(BaseCommand):
    help = 'Clear SVM'

    def handle(self, *args, **options):
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
