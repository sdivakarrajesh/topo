from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from analytics.models import ActivitySession, QuarterlyPerformanceReport, AnnualSummary, RevenueBreakdown, Company, Employee
from analytics.serializers import (
    ActivitySessionSerializer,
    QuarterlyPerformanceSerializer,
    AnnualSummarySerializer,
    RevenueBreakdownSerializer,
    CompanySerializer,
)

class AllDataView(APIView):
    """
    API to return the full unified dataset.
    """

    def get(self, request):
        sessions = ActivitySession.objects.all()
        quarterly_reports = QuarterlyPerformanceReport.objects.all()
        annual_summaries = AnnualSummary.objects.all()
        revenue_breakdowns = RevenueBreakdown.objects.all()
        companies = Company.objects.all()

        data = {
            "activity_sessions": ActivitySessionSerializer(sessions, many=True).data,
            "quarterly_reports": QuarterlyPerformanceSerializer(quarterly_reports, many=True).data,
            "annual_summaries": AnnualSummarySerializer(annual_summaries, many=True).data,
            "revenue_breakdowns": RevenueBreakdownSerializer(revenue_breakdowns, many=True).data,
            "companies": CompanySerializer(companies, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)


class DataByTypeView(APIView):
    """
    API to return data specific to a file type: csv, json, pdf, pptx.
    """

    def get(self, request, file_type):
        if file_type == "csv":
            sessions = ActivitySession.objects.all()
            response = {
                "activity_sessions": ActivitySessionSerializer(sessions, many=True).data,
            }
            return Response(response, status=status.HTTP_200_OK)

        elif file_type == "json":
            companies = Company.objects.all()
            response = {
                "companies": CompanySerializer(companies, many=True).data,
            }
            return Response(response, status=status.HTTP_200_OK)

        elif file_type == "pptx":
            annual_summaries = AnnualSummary.objects.filter()
            quarterly_reports = QuarterlyPerformanceReport.objects.filter(report_type="FitPro: Annual Summary 2023")

            data = {
                "annual_summaries": AnnualSummarySerializer(annual_summaries, many=True).data,
                "quarterly_reports": QuarterlyPerformanceSerializer(quarterly_reports, many=True).data,
            }
            return Response(data, status=status.HTTP_200_OK)

        elif file_type == "pdf":
            quarterly_reports = QuarterlyPerformanceReport.objects.filter(report_type="Sports and Leisure Quarterly Performance Report")
            response = {
                "quarterly_reports": QuarterlyPerformanceSerializer(quarterly_reports, many=True).data,
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({"error": "Invalid file type"}, status=status.HTTP_400_BAD_REQUEST)
