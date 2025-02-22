from django.contrib import admin
from .models import Membership, Location, ActivityType, ActivitySession, Company, Employee, CompanyPerformance

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
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass

class CompanyPerformanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Membership, MembershipAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ActivityType, ActivityTypeAdmin)
admin.site.register(ActivitySession, ActivitySessionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CompanyPerformance, CompanyPerformanceAdmin)
