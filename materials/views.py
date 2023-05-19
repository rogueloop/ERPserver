from django.shortcuts import render

from rest_framework import generics

from .models import Po,Polog
from .serializers import Po_Serializer

# Create your views here.


class Po_api(generics.ListCreateAPIView):

    serializer_class = Po_Serializer

    queryset=Po.objects.all()