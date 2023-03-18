from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  
 
    re_path(r'create_order/',create_order),
    re_path(r'list_order/',list_order),
    re_path(r'update_order/<int:pk>',update_order),
    re_path(r'delete_order/<int:pk>',delete_order),
    re_path(r'get_status/<int:pk>',status),
    
]