from analytics.parsers.base import FileParser
import csv
from datetime import datetime
from analytics.models import Membership, Location, ActivityType, ActivitySession

class CSVParser(FileParser):
    def parse(self):
        print(f"Parsing {self.file_path}")
        with open(self.file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    date = datetime.strptime(row.get("Date"), "%Y-%m-%d").date()
                except Exception as e:
                    print(f"Error parsing date '{row.get('Date')}': {e}")
                    continue

                membership_id = row.get("Membership_ID")
                membership_type = row.get("Membership_Type")
                activity = row.get("Activity")

                try:
                    revenue = float(row.get("Revenue"))
                except Exception as e:
                    print(f"Error parsing revenue '{row.get('Revenue')}': {e}")
                    revenue = 0.0

                try:
                    duration = int(row.get("Duration (Minutes)"))
                except Exception as e:
                    print(f"Error parsing duration '{row.get('Duration (Minutes)')}': {e}")
                    duration = 0

                location = row.get("Location")

                parsed_row = {
                    "date": date,
                    "membership_id": membership_id,
                    "membership_type": membership_type,
                    "activity": activity,
                    "revenue": revenue,
                    "duration": duration,
                    "location": location,
                }
                self.parsed_data.append(parsed_row)
        print(f"Parsed CSV. Total rows parsed: {len(self.parsed_data)}")

    def load_db(self):
        print(f"Loading {self.file_path} data to the database")
        for row in self.parsed_data:
            membership, created = Membership.objects.get_or_create(
                membership_id=row["membership_id"],
            )
            membership.membership_type = row["membership_type"]
            membership.save()

            location, _ = Location.objects.get_or_create(name=row["location"])
            activity_type, _ = ActivityType.objects.get_or_create(name=row["activity"])

            activity_session = ActivitySession.objects.create(
                date=row["date"],
                membership=membership,
                activity_type=activity_type,
                revenue=row["revenue"],
                duration_minutes=row["duration"],
                location=location,
            )
            print(f"Created ActivitySession: {activity_session}")
        
    def run(self):
        self.parse()
        self.load_db()