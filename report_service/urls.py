from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('infrastructure.django_app.reports.api.urls')),
    path('api/sesion/', include('infrastructure.django_app.sesion.urls'))
]
