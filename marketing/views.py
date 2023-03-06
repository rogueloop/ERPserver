from urllib import request
from django.shortcuts import HttpResponse

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Marketing,Item,addresss
from .serializers import MarketingSerializer,ItemSerializer,AddressSerializer

@api_view(['POST'])
def students_list(request):
    
    data=dict(request.data)
    cons_addresss=data["consignee_address"]
    ship_address=data["buyer_address"]
    items=data["item_details"]
    marketing=dict(data["woso"])
    marketing.update(data["additional_info"])

    
    mark=MarketingSerializer(data=marketing)
   
    Add=AddressSerializer(data=ship_address)
    print(Add.is_valid())
    
    a =mark.is_valid()
    print(a)

    if Add.is_valid():
        
        Add.save()
        
        return HttpResponse("added to the database")
    
        
    
    
    
    
    return HttpResponse("not working")
          