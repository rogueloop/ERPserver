

from marketing.procedure import get_status
from rest_framework.decorators import api_view,APIView
import psycopg2
from django.http import JsonResponse
from rest_framework.response import Response

from .serializer import BomSerializer, MaterialSerializer, Product_Serializer
from .models import Bom, MaterialList, Product
# Create your views here.
@api_view(['get'])
def list_bom(request):
    list_=Bom.objects.all();
    B=BomSerializer(list_,many=True).data
    bom_list=[]
    result=dict()
    for each in B:
        
        bom_list.append(each)
    result.update({'Bom':bom_list})
        
        
    return JsonResponse(result,safe=False)

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
@api_view(['GET'])
def get_bom(request,pk):
    product=Product.objects.get(pk=pk)

    serialzer=Product_Serializer(product,many=False).data
    bp=str(serialzer['bpcode'])

    
    bom=BomSerializer(Bom.objects.filter(bpcode__exact=bp),many=True).data
    items=[]
    for each_item in bom:
        each=dict(each_item)
        material=MaterialSerializer(MaterialList.objects.get(pk=each_item['matcode']),many=False).data
        each_item.update({'title':material['title']})
        items.append(each_item)
        print(each)
    result={serialzer['productname']:items}
    
    
    return JsonResponse(result,safe=False)
@api_view(['GET'])
def get_stat(request,pk):
    a=get_status(pk=pk)
    
    return Response(a)
    