from django.db import models

# models for csv data
class Membership(models.Model):
    membership_id = models.CharField(max_length=100, unique=True)
    membership_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.membership_id} - {self.membership_type}"
    
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class ActivityType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    
class ActivitySession(models.Model):
    date = models.DateField()
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.SET_NULL, null=True, blank=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.membership} - {self.activity_type}({self.duration_minutes} min)"
    

# models for json data

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    # this locations are different than the city locations that are in the activity csv data. Only 2 values, so no separate model
    location = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100) # too many roles. Simple charfield for now
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # "cashmoneh"
    hired_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class CompanyPerformance(models.Model):
    company = models.ForeignKey(Company, related_name='performances', on_delete=models.CASCADE)
    quarter = models.CharField(max_length=20)  # e.g., "2023_Q1"
    revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    profit_margin = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.company.name} - {self.quarter}"
    

# models for PDF data

class QuarterlyPerformanceReport(models.Model):
    report_type = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    quarter = models.CharField(max_length=2)  # e.g., "Q1", "Q2", etc.
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    memberships_sold = models.PositiveIntegerField()
    avg_duration = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.quarter}"
    
# models of pptx data

class AnnualSummary(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    total_memberships_sold = models.PositiveIntegerField()
    top_location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.company.name} {self.year} Annual Summary"


class RevenueBreakdown(models.Model):
    annual_summary = models.ForeignKey(AnnualSummary, related_name='revenue_breakdowns', on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    percentage = models.FloatField(help_text="Percentage of total revenue")
    
    def __str__(self):
        return f"{self.activity_type.name}: {self.percentage}%"