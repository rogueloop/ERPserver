from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  
 
    re_path(r'create_order/',create_order),
    re_path(r'list_order/',list_order)
    
]