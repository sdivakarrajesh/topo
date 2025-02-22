from django.contrib import admin
from .models import Membership, Location, ActivityType, ActivitySession, Company, Employee, CompanyPerformance, QuarterlyPerformanceReport, AnnualSummary, RevenueBreakdown

# Register your models here.
class MembershipAdmin(admin.ModelAdmin):
    list_filter = ('membership_type',)
    search_fields = ('membership_id', 'membership_type')
    list_display = ('membership_id', 'membership_type')

class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class ActivityTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class ActivitySessionAdmin(admin.ModelAdmin):
    list_filter = (
        'membership__membership_type',
        'date', 
        'location', 
        'activity_type', 
    )

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name', 'industry')
    list_display = ('name', 'industry', 'revenue', 'location')
    list_filter = ('industry',)

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'role')
    list_filter = ('role',)
    list_display = ('name', 'role', 'salary', 'hired_date', 'company')

class CompanyPerformanceAdmin(admin.ModelAdmin):
    list_filter = ('quarter', 'company__name')
    list_display = ('company', 'quarter', 'revenue', 'profit_margin')

class QuarterlyPerformanceReportAdmin(admin.ModelAdmin):
    list_filter = ('year', 'quarter')
    list_display = ('report_type', 'year', 'quarter', 'revenue', 'memberships_sold', 'avg_duration')

class AnnualSummaryAdmin(admin.ModelAdmin):
    list_filter = ('year', 'company__name')
    list_display = ('year', 'company', 'total_revenue', 'total_memberships_sold', 'top_location')

class RevenueBreakdownAdmin(admin.ModelAdmin):
    list_filter = ('annual_summary__company__name', 'activity_type__name')
    list_display = ('annual_summary', 'activity_type', 'percentage')

admin.site.register(Membership, MembershipAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ActivityType, ActivityTypeAdmin)
admin.site.register(ActivitySession, ActivitySessionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CompanyPerformance, CompanyPerformanceAdmin)
admin.site.register(QuarterlyPerformanceReport, QuarterlyPerformanceReportAdmin)
admin.site.register(AnnualSummary, AnnualSummaryAdmin)
admin.site.register(RevenueBreakdown, RevenueBreakdownAdmin)

