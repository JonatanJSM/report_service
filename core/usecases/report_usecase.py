from core.entities.report_entity import ReportEntity
from infrastructure.stores.report_store import ReportStore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ReportUseCase:
    def __init__(self, report_store: ReportStore):
        self.store = report_store

    def get_all(self):
        return self.store.get_all_reports()

    def get_by_id(self, id):
        return self.store.get_by_id(id)

    def create(self, data):
        user_instance = get_object_or_404(User, username=data['user'])
        return self.store.create_report({
            'user': user_instance,
            'title': data['title'],
            'description': data['description'],
            'location': data['location'],
            'rating': data['rating'],
            'photo': data['photo'],
        })

    def update(self, id, data):
        return self.store.update(id, data)

    def delete(self, id):
        return self.store.delete(id)

    def create_report_entity(self, data):
        return ReportEntity(**data)