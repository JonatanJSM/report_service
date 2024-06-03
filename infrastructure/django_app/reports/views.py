from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from infrastructure.django_app.reports.serializer import ReportSerializer
from infrastructure.stores.report_store import ReportStore
from core.usecases.report_usecase import ReportUseCase

class ReportViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    report_store = ReportStore()

    def list(self, request):
        usecase = ReportUseCase(self.report_store)
        reports = usecase.get_all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def create(self, request):
        usecase = ReportUseCase(self.report_store)
        report = usecase.create(request.data)
        serializer = ReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
