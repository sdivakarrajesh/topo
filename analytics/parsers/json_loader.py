from analytics.parsers.base import FileParser
import json
from datetime import datetime
from analytics.models import Company, Employee, CompanyPerformance

class JSONParser(FileParser):

    def parse(self):
        print(f"Parsing {self.file_path}")
        with open(self.file_path, 'r') as f:
            self.parsed_data = json.load(f)
        print("Finished parsing JSON.")

    def load_db(self):
        print(f"Loading {self.file_path} data to the database")
        companies = self.parsed_data.get("companies", [])
        for comp_data in companies:
            id = comp_data.get("id")
            name = comp_data.get("name")
            industry = comp_data.get("industry")
            revenue = comp_data.get("revenue")
            location = comp_data.get("location")
            
            company, created = Company.objects.get_or_create(id=id)
            company.name = name
            company.industry = industry
            company.revenue = revenue
            company.location = location
            company.save()

            for emp in comp_data.get("employees", []):
                emp_id = emp.get("id")
                emp_name = emp.get("name")
                role = emp.get("role")
                salary = emp.get("cashmoneh")
                hired_date_str = emp.get("hired_date")
                hired_date = None
                if hired_date_str:
                    try:
                        hired_date = datetime.strptime(hired_date_str, "%Y-%m-%d").date()
                    except Exception as e:
                        print(f"Error parsing hired_date for employee {emp_id}: {e}")
                Employee.objects.update_or_create(
                    employee_id=emp_id,
                    company=company,
                    defaults={
                        "name": emp_name,
                        "role": role,
                        "salary": salary,
                        "hired_date": hired_date,
                    }
                )

            performance = comp_data.get("performance", {})
            for quarter, metrics in performance.items():
                quarter_revenue = metrics.get("revenue")
                profit_margin = metrics.get("profit_margin")
                CompanyPerformance.objects.update_or_create(
                    company=company,
                    quarter=quarter,
                    defaults={
                        "revenue": quarter_revenue,
                        "profit_margin": profit_margin,
                    }
                )
        print("Finished loading JSON data into the database.")

    def run(self):
        self.parse()
        self.load_db()
