from django.urls import path
from .views import *


urlpatterns = [
    path('status/',NotificationAPIView().as_view())
  

]
