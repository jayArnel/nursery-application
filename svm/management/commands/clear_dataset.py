import os.path
from django.conf import settings
from django.core.management.base import BaseCommand

from _getch import getch

class Command(BaseCommand):
    help = 'Clear dataset'

    def handle(self, *args, **options):
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
