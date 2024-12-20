"""erpbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path, include  # Ensure `include` is imported # new

from rest_framework.schemas import get_schema_view

# Notes router
schema_view = get_schema_view(title='KEL ERP') 

urlpatterns = [
    path('admin_v2/', admin.site.urls),
    path('api/marketing/', include('marketing.urls')),
    path('schema/', schema_view),
    path('api/planning/',include('planning.urls')),
    path("", include("loginManager.urls")),
    path('api/notification/',include('notifications.urls')),
    path('api/materials/', include('materials.urls')),
]
