from rest_framework import routers
from django.urls import include, path
from .views import OrderViewSet,ItemViewSet,AddresssViewset

marketing_router = routers.SimpleRouter()

marketing_router.register(
    r'order',
    OrderViewSet,
    basename='order',
    
)
marketing_router.register(
    r'item',
    ItemViewSet,
    basename='item',
    
)
marketing_router.register(
    r'address',
    AddresssViewset,
    basename='address',
    
)

urlpatterns=[
    path('/',include(marketing_router.urls)),
 
    
    
]