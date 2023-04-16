from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  path('list_bom',list_bom),
  path('list_product',list_product),
  path('Material_api/<int:pk>/', Material_API.as_view(), name='Material_api'),
  path('Material_api/', Material_API.as_view(), name='Material_get_By_id'),
  path('get_bom/<str:pk>',get_bom),
  path('get_status/<str:pk>',get_stat),
  path('add-stock-generic/', AddStockAPI.as_view(), name='add_stock_generic'),
  path('notify_limit/',NotifyLimitAPI.as_view(), name='notify_limit'),

]