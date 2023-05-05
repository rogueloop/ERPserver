from django.urls import path
from .views import (
    MarketingListCreateAPIView,
    MarketingRetrieveUpdateDestroyAPIView,
    ItemListCreateAPIView,
    ItemRetrieveUpdateDestroyAPIView,
    AddressListCreateAPIView,
    AddressRetrieveUpdateDestroyAPIView,
    StatusAPIView
)

urlpatterns = [
    path('order/', MarketingListCreateAPIView.as_view()),
    path('order/<int:pk>/', MarketingRetrieveUpdateDestroyAPIView.as_view()),
    path('item/', ItemListCreateAPIView.as_view()),
    path('item/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('addresss/', AddressListCreateAPIView.as_view()),
    path('addresss/<int:pk>/', AddressRetrieveUpdateDestroyAPIView.as_view()),
    path('status/<int:pk>/',StatusAPIView.as_view())
    
]
