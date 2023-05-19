from django.urls import path
from .views import Po_api

urlpatterns = [
    path('po_api/', Po_api.as_view()),
]