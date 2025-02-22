from django.core.management.base import BaseCommand
from analytics.parsers.csv_loader import CSVParser
from analytics.parsers.json_loader import JSONParser
from analytics.parsers.pdf_loader import PDFParser

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello!")
        CSVParser("data/dataset2.csv").run()
        JSONParser("data/dataset1.json").run()
        PDFParser("data/dataset3.pdf").run()