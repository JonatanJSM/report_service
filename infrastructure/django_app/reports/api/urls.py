from rest_framework.routers import DefaultRouter
from infrastructure.django_app.reports.api.views import ReportViewSet

router = DefaultRouter()
router.register('reports', ReportViewSet, basename='report')
urlpatterns = router.urls