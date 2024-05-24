from rest_framework import viewsets
from infrastructure.django_app.reports.models import Report
from infrastructure.django_app.reports.api.serializer import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer