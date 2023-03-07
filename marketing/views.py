from urllib import request
from django.http import JsonResponse
from django.shortcuts import HttpResponse


# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Marketing,Item,addresss
from .serializers import MarketingSerializer,ItemSerializer,AddressSerializer
from .deconstruct import Deconstruct
@api_view(['POST'])
def create_order(request):
    
    data=Deconstruct(request.data)
    
    marketing=MarketingSerializer(data.marketing())
    add_buyer=AddressSerializer(data.buyer_addr())
    add_consign=AddressSerializer(data.consign_address())
    items=data.item_deconstruct()
    
    
    if marketing.is_valid() and add_consign.is_valid() and add_buyer.is_valid():
        
        
        for i in items:
            item=ItemSerializer(dict(i))
            if item.is_valid():
                item.save()
            else:
                return HttpResponse("ERROR 503")

        
        marketing.save()
        add_buyer.save()
        add_consign.save()
        
        return HttpResponse("object is successfully added")
    
    return HttpResponse("ERROR 500")

@api_view(['GET'])
def list_order(request):
    marketing=Marketing.objects.all()
    addrs=addresss.objects.all()
    Items=Item.objects.all()
    result=marketing+addrs+Items
    return JsonResponse(result)
    
    
        
    
        
    
    
    
    
    
          