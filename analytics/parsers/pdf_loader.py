from analytics.parsers.base import FileParser
import pdfplumber
from analytics.models import QuarterlyPerformanceReport

class PDFParser(FileParser):
    def __init__(self, file_path):
        self.file_path = file_path
        self.parsed_data = []

    def parse(self):
        print(f"Parsing {self.file_path}")
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                print(text)
                if text:
                    self.extract_quarterly_data(text)
        print(f"Finished parsing PDF. Extracted {len(self.parsed_data)} records.")

    def extract_quarterly_data(self, text):
        """
        Assumes the PDF contains a table with columns:
        Year | Quarter | Revenue ($) | Memberships Sold | Avg Duration (Minutes)
        """
        lines = text.split("\n")
        for line in lines:
            parts = line.split()
            if len(parts) == 5:  # Ensure it matches expected format
                try:
                    year = int(parts[0])
                    quarter = parts[1]
                    revenue = float(parts[2].replace(",", ""))
                    memberships_sold = int(parts[3])
                    avg_duration = int(parts[4])

                    report = QuarterlyPerformanceReport(
                        report_type="Sports and Leisure Quarterly Performance Report",
                        year=year,
                        quarter=quarter,
                        revenue=revenue,
                        memberships_sold=memberships_sold,
                        avg_duration=avg_duration
                    )
                    self.parsed_data.append(report)
                except ValueError as e:
                    print(f"Skipping invalid line: {line} | Error: {e}")
            else:
                print(f"Skipping invalid line: '{line}'")

    def load_db(self):
        print(f"Loading {self.file_path} data into the database")
        QuarterlyPerformanceReport.objects.bulk_create(self.parsed_data)
        print(f"Inserted {len(self.parsed_data)} records into the database.")

    def run(self):
        self.parse()
        self.load_db()
