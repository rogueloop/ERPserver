from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Marketing,Item,addresss
from .serializers import MarketingSerializer,ItemSerializer,AddressSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = MarketingSerializer
    queryset = Marketing.objects.all()
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class=ItemSerializer
    queryset=Item.objects.all()

class AddresssViewset(viewsets.ModelViewSet):
    serializer_class=AddressSerializer
    queryset=addresss.objects.all()