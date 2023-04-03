from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  path('list_bom',list_bom),
  path('list_product',list_product),
  path('list_materials',list_materials),
  path('get_bom/<str:pk>',get_bom),
  path('get_status/<str:pk>',get_stat)


 
  
    
]