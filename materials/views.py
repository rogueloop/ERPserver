from django.shortcuts import render

from rest_framework import generics

from .models import Po,Polog
from .serializers import Po_Serializer,Polog_Serializer
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.


class Po_api(generics.ListCreateAPIView):
    
    serializer_class = Po_Serializer

    queryset=Po.objects.all()

    def post(request,self,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logSerializer = Polog_Serializer(data=request.data)
        if logSerializer.is_valid():
            logSerializer.save()
        return Response({"successfully po created and logged":serializer.data},status=status.HTTP_201_CREATED)