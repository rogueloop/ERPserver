from django.shortcuts import render
from rest_framework.decorators import api_view
import psycopg2
from django.http import JsonResponse

from .serializer import BomSerializer
from .models import Bom
# Create your views here.
@api_view(['get'])
def list_bom(request):
    list_=Bom.objects.all();
    B=BomSerializer(list_,many=True).data
    return JsonResponse(str(B),safe=False)
