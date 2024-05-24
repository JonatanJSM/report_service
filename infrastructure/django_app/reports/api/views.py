from rest_framework import viewsets
from infrastructure.django_app.reports.models import Report
from infrastructure.django_app.reports.api.serializer import ReportSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ReportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
