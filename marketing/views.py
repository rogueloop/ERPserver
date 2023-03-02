from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Marketing
from .serializers import MarketingSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = MarketingSerializer
    queryset = Marketing.objects.all()