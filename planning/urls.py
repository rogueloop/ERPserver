from rest_framework import routers
from django.urls import include, path,re_path
from .views import *



urlpatterns=[
  path('Product_api/',Product_API_View.as_view(),name='Product_api'),
  path('Product_api/<str:pk>/',Product_API_View.as_view(),name='Product_get_by_id'),
  path('Material_api/<int:pk>/', Material_API.as_view(), name='Material_api'),
  path('Material_api/', Material_API.as_view(), name='Material_get_By_id'),
  path('Bom_api/v1/<str:pk>/',Bom_API_View.as_view(),name='Bom_api'),
  path('Bom_api/<str:product_id>', Bom_API_View.as_view(), name='Bom_api'),
  path('Stock_api/', AddStockAPI.as_view(), name='Stock_api'),
  path('notify_limit/',NotifyLimitAPI.as_view(), name='notify_limit'),
  path('get_bom_excel/v2/<str:pk>/',get_file),
  path('product_suggestions/',product_suggestions),
  path('pi_api/',Pr_Api.as_view()),
  path('pi_api/<int:pk>', Pr_Api.as_view()),
  path('stock_log/',Stock_log_Api.as_view()),
  path('status/<int:pk>', Status_Api.as_view()),
  path('material_suggestion',material_suggestion)


]