from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  path('Product_api/',Product_API_View.as_view(),name='Product_api'),
  path('Product_api/<str:pk>/',Product_API_View.as_view(),name='Product_get_by_id'),
  path('Material_api/<int:pk>/', Material_API.as_view(), name='Material_api'),
  path('Material_api/', Material_API.as_view(), name='Material_get_By_id'),
  path('Bom_api/<str:pk>/',Bom_API_View.as_view(),name='Bom_api'),
  path('Stock_api/', AddStockAPI.as_view(), name='Stock_api'),
  path('notify_limit/',NotifyLimitAPI.as_view(), name='notify_limit'),
  path('get_bom_excel/<str:pk>/',get_file)

]