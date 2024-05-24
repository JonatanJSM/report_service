from rest_framework import serializers
from infrastructure.django_app.reports.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'