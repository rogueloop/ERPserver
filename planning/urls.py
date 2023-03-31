from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  re_path(r'list_bom',list_bom),
  re_path(r'list_product',list_product),
  re_path(r'list_materials',list_materials)
 
  
    
]