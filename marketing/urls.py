from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('list_order/', views.list_order, name='list_order'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
    path('status/<str:pk>/', views.status, name='status'),
]