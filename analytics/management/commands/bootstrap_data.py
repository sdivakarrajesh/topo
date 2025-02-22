from django.core.management.base import BaseCommand
from analytics.parsers.csv_loader import CSVParser

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello!")
        CSVParser("data/dataset2.csv").run()