from django.shortcuts import render
from rest_framework.decorators import api_view
import psycopg2
from django.http import JsonResponse

from .serializer import BomSerializer, MaterialSerializer, Product_Serializer
from .models import Bom, MaterialList, Product
# Create your views here.
@api_view(['get'])
def list_bom(request):
    list_=Bom.objects.all();
    B=BomSerializer(list_,many=True).data
    
    return JsonResponse(B,safe=False)

@api_view(['get'])
def list_product(request):
    list_=Product.objects.all();
    B=Product_Serializer(list_,many=True).data
    
    return JsonResponse(B,safe=False)

@api_view(['get'])
def list_materials(request):
    list_=MaterialList.objects.all();
    B=MaterialSerializer(list_,many=True).data
    
    return JsonResponse(B,safe=False)
