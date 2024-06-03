from infrastructure.django_app.reports.models import Report
from .store_report import Store

class ReportStore(Store):
    def get_all_reports(self):
        return Report.objects.all()

    def get_report_by_id(self, id):
        return Report.objects.get(id=id)

    def create_report(self, data):
        return Report.objects.create(**data)

    def update_report(self, id, data):
        report = Report.get_by_id(id)
        for key, value in data.items():
            setattr(report, key, value)
        report.save()
        return report

    def delete_report(self, id):
        report = Report.get_by_id(id)
        report.delete()
        return report