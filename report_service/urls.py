from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('infrastructure.django_app.reports.api.urls')),
    path('login', views.login),
    path('register', views.register),
    path('profile', views.profile),
]
