from rest_framework import serializers
from analytics.models import Membership, ActivitySession, Company, CompanyPerformance, Employee, QuarterlyPerformanceReport, AnnualSummary, RevenueBreakdown

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"

class ActivitySessionSerializer(serializers.ModelSerializer):
    membership = MembershipSerializer()
    location = serializers.StringRelatedField()
    activity_type = serializers.StringRelatedField()

    class Meta:
        model = ActivitySession
        fields = "__all__"

class CompanyPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPerformance
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Employee
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    performance = CompanyPerformanceSerializer(source="performances", many=True, read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

class QuarterlyPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyPerformanceReport
        fields = "__all__"

class RevenueBreakdownSerializer(serializers.ModelSerializer):
    activity_type = serializers.StringRelatedField()
    class Meta:
        model = RevenueBreakdown
        fields = "__all__"

class AnnualSummarySerializer(serializers.ModelSerializer):
    revenues = RevenueBreakdownSerializer(source="revenue_breakdowns", many=True, read_only=True)

    class Meta:
        model = AnnualSummary
        fields = "__all__"


